#!/usr/bin/env python
import os
import sys
from boil import Boil

from clerk import Clerk
from asset import Asset
from app import App
from account import Account
from empty import EmptyModule

def main_help():
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

def check_flags(flag):
    if flag == 'v':
        print("version 0.0.1")
    elif flag == 'h':
        main_help()

def check_full_flags(flag):
    if flag == "version":
        print("version 0.0.1")
    elif flag == "help":
        main_help()
    else:
        print(f"Error: unknown flag: --{flag}\n")
        print("Usage:")
        print("  boil [flags]")
        print("  boil [module]\n")
        main_help()

def main():
    if len(sys.argv) <= 1:
        main_help()
    else:
        choice = sys.argv[1]

        if   choice == "clerk":     module = Clerk(sys.argv[2:])
        elif choice == "asset":     module = Asset(sys.argv[2:])
        elif choice == "app":       module = App(sys.argv[2:])
        elif choice == "account":   module = Account(sys.argv[2:])

        elif choice.startswith('-') and len(choice) == 2:
            check_flags(choice[1])
            return

        elif choice.startswith('--'):
            flag = choice[2:]
            check_full_flags(flag)
            return

        else:                       module = EmptyModule(sys.argv[2:])

        boil = Boil(module)

main()
