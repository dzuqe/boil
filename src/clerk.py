import os

import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic

from src.module import Module
from src.account import Account

class Clerk(Module):
    def __init__(self, args):
        command = ""
        if len(args) > 0:
            command = args[0]
        self.data = {
            "command": command,
            "from": "",
            "amount": -1,
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

        self.account = Account(os.environ["MARC"], args)

    def exec(self):
        if self.data['command'] == 'send':
            # interrogate data struct
            if self.data['to'] == '':
                print('Error: To arguement missing.')
                self.help()
                return
            elif self.data['amount'] == -1:
                print('Error: Invalid amount value')
                self.help()
                return

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

        try:
            signed_txn = txn.sign(self.account.private_key)
            tx_id = signed_txn.transaction.get_txid()
            self.client.send_transactions([signed_txn])
            print("tx:", tx_id, "\n")

        except algosdk.error.WrongKeyLengthError:
            print("Error: Invalid 'to' address (Wrong Key Length):", self.data['to'],"\n")
            self.help()

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
