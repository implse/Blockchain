from block import Block
from blockchain import Blockchain


# Instantiate class
local_blockchain = Blockchain()

# Genesis block
local_blockchain.print_blocks()

# Transactions
block_one_transactions = {"sender":"Keanu", "receiver": "Charly", "amount":"50"}
block_two_transactions = {"sender": "Betito", "receiver":"Gin", "amount":"25"}
block_three_transactions = {"sender":"Rosalie", "receiver":"Baboon", "amount":"35"}

# Fake Transactions
fake_transactions = {"sender": "Caramel", "receiver":"Myrtilles, Alice", "amount":"25"}

# Add Block
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

local_blockchain.print_blocks()

# Add fake Block
local_blockchain.chain[2].transactions = fake_transactions

# Validate chain
local_blockchain.validate_chain()
