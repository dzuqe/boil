#!/usr/bin/env python
import os
import sys
from boil import Boil

from clerk import Clerk
from asset import Asset
from app import App
from account import Account
from empty import EmptyModule

class Lexer():
    def lex(self, argv):
        for arg in argv:
            print(arg)

if len(sys.argv) <= 1:
    print("""boil is the alternative cli for interacting with Algorand public nodes. 

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

else:
    choice = sys.argv[1]
    if   choice == "clerk":     module = Clerk(sys.argv[2:])
    elif choice == "asset":     module = Asset(sys.argv[2:])
    elif choice == "app":       module = App(sys.argv[2:])
    elif choice == "account":   module = Account(sys.argv[2:])
    else:                       module = EmptyModule(sys.argv[2:])

    boil = Boil(module)

