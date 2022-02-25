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
from src.nodeModule import NodeModule

class Boil(Module):
    def __init__(self, argv):
        self.argv = argv

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
        net = 'testnet'
        provider = 'ps'
        token = os.environ['PURESTAKE_API_KEY']

        if 'BOIL_NET' in os.environ.keys() and os.environ['BOIL_NET'] == '':
            print('Warning: BOIL_NET environment variable not set. Defaulting to "testnet"')
        else:
            net = os,environ['BOIL_NET']

        if 'BOIL_PROV' not in os.environ.keys() or ('BOIL_PROV' in os.environ.keys() and os.environ['BOIL_PROV'] == ''):
            print('Warning: BOIL_PROV environment variable not set. Defaulting to Pure Stake [ps]')
            if os.environ['PURESTAKE_API_KEY'] == '':
                print("Error: PURESTAKE_API_KEY environment variable not set.")
                return
        elif 'BOIL_PROV' in os.environ.keys():    
            provider = os.environ['BOIL_PROV']
            if provider == 'ps':
                if os.environ['PURESTAKE_API_KEY'] == '':
                    print("Error: PURESTAKE_API_KEY environment variable not set.")
                    return

        print()
        self.node = Node(token, net, provider)

        if len(self.argv) <= 1:
            self.help()
        else:
            choice = self.argv[1]

            if   choice == "clerk":     module = Clerk(self.argv[2:])
            elif choice == "asset":     module = Asset(self.argv[2:])
            elif choice == "app":       module = App(self.argv[2:])
            elif choice == "account":   module = Account(os.environ['MARC'], self.argv[2:])

            elif choice == "node":
                module = NodeModule(self.argv[2:], self.node)

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
