import os

import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic

from src.module import Module
from src.account import Account

class NodeModule(Module):
    def __init__(self, args, node):
        self.node = node

        self.command = ""
        if len(args) > 0:
            self.command = args[0]

    def exec(self):
        if self.command == 'show':
            print(self.node)
        else:
            print(f"Unknown command: {self.data['command']}\n")
            self.help()

    def help(self):
        print("Usage: ")
        print("  boil node [command]\n")
        print("Avaialble commands:")
        print("  show          show node properties")
