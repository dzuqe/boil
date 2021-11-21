#!/usr/bin/env python
import os
import sys
from boil import Boil

if len(sys.argv) <= 1:
    print("help")
else:
    choice = sys.argv[1]
    boil = Boil()

    if choice == "clerk":
        print("clerk")
        print(boil.clerk)

    elif choice == "asset":
        print("asset")
        print(boil.asset)

    elif choice == "app":
        print("app")
        print(boil.app)

    elif choice == "account":
        print("account")
        print(boil.account)

    else:
        print("Error: Unknown option")
