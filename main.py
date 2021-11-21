#!/usr/bin/env python
import os
import sys
from boil import Boil

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
    lexer = Lexer()
    lexer.lex(sys.argv[1:])
    choice = sys.argv[1]
    boil = Boil()

#    if choice == "clerk":
#        print("clerk")
#        if 
#        cli = sys.argv[2]
#        print(cli)
#        print(boil.clerk)
#
#    elif choice == "asset":
#        print("asset")
#        print(boil.asset)
#
#    elif choice == "app":
#        print("app")
#        print(boil.app)
#
#    elif choice == "account":
#        print("account")
#        print(boil.account)
#
#    else:
#        print("Error: Unknown option")


