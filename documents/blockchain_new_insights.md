
# Blockchain New Insights
_Some further research into Bitcoin, and starting my own node on AWS has given me some new insights that I did not have prior to the blockchain discussion on 06/02._

----
## 1 Transaction Fees are voluntary

The transaction fees that are lost when transferring bitcoin are an **incentive** to the miner to publish your transactions in their next block. Each block can only contain 750kb of transaction data - miners will typically only record transactions for the highest transaction fees except for during times of low transaction volumes. Bitcoin Core automatically decides what your transaction fees are - but you can actually set it manually.

Bitcoin NODES are used for verification and do not currently get any of the transaction fee - although this is something many people want to change.

## 2 Wallets are not addresses

Wallets are just a collection of addresses. The addresses are abstracted out into a wallet by Bitcoin Core. Wallets are not actually a part of the true bitcoin specification - they are a software construct... which leads to the next thing I realized...

## 3 Bitcoin is pure mathematics
Bitcoin Core is the software implementation of bitcoin. Bitcoin itself is just the cryptographic transaction system, block mining, and blockchain specification. Bitcoin Core and Blockchain are just an 'instance' of Bitcoin as envisioned by the Satoshi Paper. Technically, we could start a second blockchain with it's own network of nodes that is completely unrelated to the existing one.  

## 4 Address versus Public Key
It took me forever to figure out why the redundant address/public key thing was going on.

Your address is a simple one-way hash of your public key. You can receive money using either one. The reason they chose to use an address is to protect against a scenario where SHA256 is broken (E.G. quantum computers). If your public key is still hidden, then your bitcoins are still safe AS LONG AS you have never revealed the public key by spending the bitcoins from that address. (Would be safe but frozen until a new encryption protocol is put in place)

Typically a new address should be made every time you receive money.

# Fun Facts

## Bitcoin Nodes

![nodes][

2,163 nodes in the USA (+1 including Tyler's new AWS node!)

All the hashing algorithms for bitcoin in order that they are performed.
http://gobittest.appspot.com/Address

Probably the best developer resource on using the blockchain. Written in
c though... difficult to understand for us pythonistas. It's geared towards more of a Ryan background.
http://davidederosa.com/basic-blockchain-programming/
