<img width="250" src="extras/images/bitcoin-logo.png" alt="Bitcoin Logo">

# Bitcoin Transfer

A simple application that transfer Bitcoin from one wallet to other wallet.

It is configured to use BIP38 wallet address if you pass wallet password.

[![Build](https://github.com/paulocoutinhox/bitcoin-transfer/actions/workflows/build.yml/badge.svg)](https://github.com/paulocoutinhox/bitcoin-transfer/actions/workflows/build.yml)

## How to use

1 - Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

2 - Set your wallet private data:

```bash
export BTC_WALLET_PRIV='YOUR-PRIVATE-ADDRESS'
```

or if you use BIP38 wallet with password:

```bash
export BTC_WALLET_PRIV='YOUR-PRIVATE-ADDRESS'
export BTC_WALLET_PRIV_PASS='YOUR-PRIVATE-ADDRESS-PASSWORD'
```

3 - Transfer Bitcoins

```bash
python3 transfer.py --to 1Em2mh42vmqDxHLuaMM2u6KQPJWFDP8Jy8 --amount 0.00001000
```

or if you only want a draft execution, without perform transaction, execute:

```bash
python3 transfer.py --to 1Em2mh42vmqDxHLuaMM2u6KQPJWFDP8Jy8 --amount 0.00001000 --draft
```

## Troubleshooting

1. If you have problems with macOS when install `bip38` about `openssl` headers not found, execute the following command and install dependencies again:

```bash
brew install openssl
export CFLAGS="-I$(brew --prefix openssl)/include"
export LDFLAGS="-L$(brew --prefix openssl)/lib"
```

## Buy me a coffee

<a href='https://ko-fi.com/paulocoutinho' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi1.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2024, Paulo Coutinho
