from account import Account
from node import Node
from clerk import Clerk
from asset import Asset
from app import App
import os

class Boil():
    def __init__(self):
        self.node = Node(os.environ['PURESTAKE_API_KEY'], 'https://mainnet-algorand.api.purestake.io/ps2')
        self.account = Account(os.environ['MARC'])
        self.clerk = Clerk(self.account, self.node.client)
        self.asset = Asset()
        self.app = App()
