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
            "from": {
                "value": "",
                "required": False,
                "error": False,
            },
            "amount": {
                "value": -1,
                "required": True,
                "error": False,
            },
            "to": {
                "value": "",
                "required": True,
                "error": False,
            },
        }

        i = 0
        while i < len(args):
            if args[i] == "-f" \
                    and (i + 1) < len(args):
                self.data["from"]["value"] = args[i + 1]
            elif args[i] == "-a" \
                    and (i + 1) < len(args):
                self.data["amount"]["value"] = int(args[i + 1])
            elif args[i] == "-t" \
                    and (i + 1) < len(args):
                self.data["to"]["value"] = args[i + 1]
            i += 1

        self.account = Account(os.environ["MARC"], args)

    def exec(self):
        if self.data['command'] == 'send':
            # interrogate data struct
            error = False
            if self.data['to']['value'] == '':
                self.data['to']['error'] = True
                error = True
            if self.data['amount']['value'] == -1:
                self.data['amount']['error'] = True
                error = True

            if error is False:
                self.send(self.data['to']['value'], self.data['amount']['value'])
            else:
                print(f"Error: arguements {self.stripErrors()} missing")

        else:
            print(f"Unknown command: {self.data['command']}\n")
            self.help()

    def stripErrors(self):
        stripped = ""
        i = 0
        args = ['from','to','amount']
        for label in args:
            item = self.data[label]
            if item['required'] is True:
                stripped += "{" + label + "}"
                if i < len(args) - 1:
                    stripped += ", "
            i += 1
        return stripped

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
