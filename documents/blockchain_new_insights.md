
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

In fact, there is a second 'test' blockchain that is used by bitcoin developers to test implementations using bitcoin core

## 4 Address versus Public Key
It took me forever to figure out why the redundant address/public key thing was going on.

Your address is a simple one-way hash of your public key. You can receive money using either one. The reason they chose to use an address is to protect against a scenario where SHA256 is broken (E.G. quantum computers). If your public key is still hidden, then your bitcoins are still safe AS LONG AS you have never revealed the public key by spending the bitcoins from that address. (Would be safe but practically frozen until a new encryption protocol is put in place)

Typically a new address should be made every time you send money, to store the remainder of money that you want to keep. This means only momentarily exposing your public key until the money has already left the address when the next block is written.

## 5 Nodes form a CONSENSUS
A block cannot be written to the blockchain until all nodes have formed a consensus that the block and transactions follow all of the rules.

I am not certain how a malicious node would be removed if it simply vetoed every block.

## 6 Skilled bitcoin developers are in huge demand
Computer scientists with cryptography skills can demand 200-300k to work as crypto developers. It's a really hot field with almost no MOOC or internet resources to draw masses of people into it. I had a hard time finding good documentation simply on the bitcoin core client - it's a really strong protected niche.

I noticed this because I started get job ads popping up at me after googles search engine figured out I was looking at bitcoin development stuff.

## 7 Transactions must distribute ALL of a previous payment

 * Addresses can never be reused after they are output

![sample](https://raw.githubusercontent.com/tylerc-atx/blockchain_network/master/documents/images/sample_transaction.png)

A new transaction must distribute ALL of the previous transaction's coins. The above transaction distributes a payment to somebody, stores the extra money in a new address (presumably owned by the sender), and loses a little bit of money as a fee to the miner who will post the transaction in his block.

## 8 There is no transaction link going forward up the blockchain

Each 'output point' is simply a transaction output that has a 'script signature' that only one person can use to seize the transaction output and create a new transaction. This often results in multiple inputs to a single transaction.

One issue is that the entire blockchain needs to be parsed to find an old output that has never been spent.

# Fun Facts

## Bitcoin Nodes

![nodes](https://raw.githubusercontent.com/tylerc-atx/blockchain_network/master/documents/images/nodecount.png)

2,168 nodes in the USA (+1 including Tyler's new AWS node!)

## Bitcoin key derivation flowchart

![keys](https://raw.githubusercontent.com/tylerc-atx/blockchain_network/master/documents/images/bitcoinkeys-s588.png)

2,168 nodes in the USA (+1 including Tyler's new AWS node!)

# Some cool sites

All the hashing algorithms for bitcoin in order that they are performed.
http://gobittest.appspot.com/Address

Python-based intro on bitcoin development
http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html

Probably the best developer resource on using the blockchain. Written in
c though... difficult to understand for us pythonistas. It's geared towards more of a Ryan background.
http://davidederosa.com/basic-blockchain-programming/

Two of the best textbooks on bitcoin stored on my github
https://github.com/tylerc-atx/textbook_resources/btc
