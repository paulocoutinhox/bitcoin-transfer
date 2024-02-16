import argparse
import os

from bip38 import bip38_decrypt
from bit import PrivateKey
from pygemstones.util import log as l

# Argument parser
parser = argparse.ArgumentParser(description="Bitcoin Transfer")

parser.add_argument(
    "--to",
    type=str,
    help="Destination Wallet Address",
    required=True,
)

parser.add_argument(
    "--amount",
    type=float,
    help="Bitcoin Amount (ex: 0.00001000)",
    required=True,
)

parser.add_argument(
    "--draft",
    help="Draft Run Without Transaction",
    required=False,
    action="store_true",
)

args = parser.parse_args()

# Setup key
l.d("Setup key...")
my_priv_key = os.environ["BTC_WALLET_PRIV"]
my_priv_pass = os.environ.get("BTC_WALLET_PRIV_PASS")

if my_priv_pass:
    key_wif = bip38_decrypt(my_priv_key, my_priv_pass)
else:
    key_wif = my_priv_key

key = PrivateKey(key_wif)

# Checking balance
l.d("Checking balance...")
my_balance = key.get_balance("btc")
my_balance_usd = key.get_balance("usd")
my_balance_brl = key.get_balance("brl")

l.i(f"Your balance in BTC: {my_balance}")
l.i(f"Your balance in USD: {my_balance_usd}")
l.i(f"Your balance in BRL: {my_balance_brl}")

# Check if the balance is sufficient
if float(my_balance) >= args.amount:
    if args.draft:
        l.i(f"Transaction not performed (draft mode)")
    else:
        # Perform the transaction
        l.d("Performing transaction...")
        try:
            tx_hash = key.send([(args.to, args.amount, "btc")])

            l.i(f"Transaction ID: {tx_hash}")
            l.s(f"Transaction successful!")
        except Exception as e:
            l.e(f"An error occurred during the transaction: {e}")
else:
    l.e("Insufficient balance for this transaction.")
