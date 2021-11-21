import os
from node import Node
from clerk import Clerk

print("hi")
node = Node(os.environ["PURESTAKE_API_KEY"], 'https://mainnet-algorand.api.purestake.io/ps2')
choice="clerk"

if choice == "clerk":
    clerk = Clerk(os.environ['MARC'])
    print(clerk)
    #clerk.transfer(binance_acc, amount, node.client)
else:
    print("help")
