import os

import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic

from utils import wait_for_confirmation
from node import Node
from module import Module
from account import Account

class Clerk(Module):
    def __init__(self, args):
        command = ""
        if len(args) > 0:
            command = args[0]
        self.data = {
            "command": command,
            "from": "",
            "amount": 0,
            "to": "",
        }

        i = 0
        while i < len(args):
            if args[i] == "-f" \
                    and (i + 1) < len(args):
                self.data["from"] = args[i + 1]
            elif args[i] == "-a" \
                    and (i + 1) < len(args):
                self.data["amount"] = int(args[i + 1])
            elif args[i] == "-t" \
                    and (i + 1) < len(args):
                self.data["to"] = args[i + 1]
            i += 1

        self.account = Account(os.environ["MARC"])

    def exec(self):
        if self.data['command'] == 'send':
            # interrogate data struct
            self.send(self.data['to'], self.data['amount'])

        else:
            print(f"Unknown command: {self.data['command']}\n")
            self.help()

    def send(self, to, amount):
        params = self.client.suggested_params()
        params.flat_fee = True
        params.fee = 1000

        txn = algosdk.future.transaction.PaymentTxn(
            self.account.public_key, # sender
            params,     # sp
            to,         # receiver
            amount,     # amount to send
        )

        signed_txn = txn.sign(self.account.private_key)
        tx_id = signed_txn.transaction.get_txid()

        self.client.send_transactions([signed_txn])

        wait_for_confirmation(self.client, tx_id)
        transaction_response = self.client.pending_transaction_info(tx_id)
        print(transaction_response)

    def sign(self):
        pass

    def inspect(self):
        pass

    def help(self):
        print("Usage: ")
        print("  boil clerk [command] [flags]\n")
        print("Avaialble commands:")
        print("  send       send money to an address")
        print("  inspect    print a transaction file")
        print("  sign       sign a transaction file")
