# INTRODUCTORY BLOCKCHAIN CONCEPTS

## What is Blockchain?

A blockchain, is a growing list of records, called blocks, that are linked using cryptography. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. (Wikipedia)

### Key terms

  - __Block__: A block is an individual transaction or piece of data that is being stored within the blockchain.

  - __Blockchain__: A blockchain is a continuously growing list (“chain”) of records (“block”), called blocks, which are linked chronologically and secured using cryptography.

  - __Blockchain Network__: The blockchain network and blockchain are terms used interchangeably. They represent the entire blockchain from the structure itself to the network that it is a part of.

  - __Decentralization__: The concept in which participants work together to validate transactions without relying on a central authority.

  - __Participant__: A client that owns a copy of the blockchain and verifies transactions across the network.

## What are Blocks?

Blocks are the building blocks of a blockchain. A block contains transaction data and other important details related to the creation of that block, such as the time when it was created and other unique information.

### Properties of Block:

  - __Timestamp__: The time the block is created determines the location of it on the blockchain.

  - __Transaction Data__: The information to be securely stored in the block.

  - __Hash__: A unique code produced by combining all the contents within the block itself — also known as a digital fingerprint.

  - __Previous Hash__: Each block has a reference to the block prior to its hash. This is what makes the blockchain unique because this link will be broken if a block is tampered with.

### Hashing

Hashing is an application of cryptography that is fundamental to the design of the blockchain. It is a way to generate a seemingly random, but calculated string of letters and numbers from any input. This is accomplished by the use of a hash function.  Blockchain uses a cryptographic hash function, meaning that the output is random but deterministic.

### Key terms

  - __Deterministic__: The same input will always produce the same output, but that output cannot produce the original input.

  - __Hash__: A calculated string of letters and numbers produced from a specific input.

  - __Hash Function__: A function that takes in an input of a random size, performs hashing on the input, and generates a seemingly random output of a fixed size, also known as the hash.

###  Genesis Block

The genesis block is the first block on the blockchain and it is typically hard-coded into the blockchain structure. Being the first block on the blockchain, it does not have a link to a previous hash.
