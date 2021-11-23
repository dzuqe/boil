from node import Node
import os

class Boil():
    def __init__(self, module):
        self.node = Node(os.environ['PURESTAKE_API_KEY'], 'https://mainnet-algorand.api.purestake.io/ps2')
        self.module = module
        self.module.set_client(self.node.client)

