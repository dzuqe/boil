#!/usr/bin/env python
import os
import sys

from src.clerk import Clerk
from src.asset import Asset
from src.app import App
from src.account import Account
from src.empty import EmptyModule
from src.module import Module
from src.node import Node

class Boil(Module):
    def __init__(self, argv):
        self.argv = argv
        self.node = Node(os.environ['PURESTAKE_API_KEY'], 'testnet')

    def help(self):
        print("""boil is the alternative cli for interacting with Algorand \
public nodes.

Usage:
  boil [flags]
  boil [command]

Available modules:
  clerk         provides tools to perform transactions
  account       control and manage algorand accounts
  asset         manage assets
  app           manage applications

Flags:
  -v, --version     display version information
  -h, --help        help for boil
""")

    def check_flags(self, flag):
        if flag == 'v':
            print("version 0.0.1")
        elif flag == 'h':
            self.help()

    def check_full_flags(self, flag):
        if flag == "version":
            print("version 0.0.1")
        elif flag == "help":
            self.help()
        else:
            print(f"Error: unknown flag: --{flag}\n")
            print("Usage:")
            print("  boil [flags]")
            print("  boil [module]\n")
            self.help()

    def exec(self):
        if len(self.argv) <= 1:
            self.help()
        else:
            choice = self.argv[1]

            if   choice == "clerk":     module = Clerk(self.argv[2:])
            elif choice == "asset":     module = Asset(self.argv[2:])
            elif choice == "app":       module = App(self.argv[2:])
            elif choice == "account":   module = Account(os.environ['MARC'], self.argv[2:])

            elif choice.startswith('-') and len(choice) == 2:
                self.check_flags(choice[1])
                return

            elif choice.startswith('--'):
                flag = choice[2:]
                self.check_full_flags(flag)
                return

            else:                       module = EmptyModule(self.argv[2:])

            module.set_client(self.node.client)
            module.exec()

boil = Boil(sys.argv)
boil.exec()
