import algosdk
from module import Module

class Account(Module):
    def __init__(self, mnemonic, args):
        self.private_key = algosdk.mnemonic.to_private_key(mnemonic)
        self.public_key = algosdk.mnemonic.to_public_key(mnemonic)

        command = ""
        if len(args) > 0:
            command = args[0]

        self.data ={
            "command": command,
            "address": "",
        }

        i = 0
        while i < len(args):
            if args[i] == '-a' and (i+1)<len(args):
                self.data['address'] = args[i+1]
                i += 1
            i += 1

    def exec(self):
        if self.data['command'] == 'balance':
            self.balance()
        elif self.data['command'] == 'rewards':
            self.rewards()
        else:
            print(f"Error: Unknown command: {self.data['command']}")
            self.help()

    def balance(self):
        if self.data['address'] == '':
            print("Error: Address arguement missing.\n")
            self.help()
            return
        account = self.client.account_info(self.data['address'])
        amount = algosdk.util.microalgos_to_algos(account['amount'])
        print(f"Balance: {amount}")

    def delete(self):
        pass

    def rewards(self):
        if self.data['address'] == '':
            print("Error: Address arguement missing.\n")
            self.help()
            return
        account = self.client.account_info(self.data['address'])
        amount = algosdk.util.microalgos_to_algos(account['rewards'])
        print(f"Rewards: {amount}")

    def help(self):
        print("Usage:")
        print("boil account [command]\n")
        print("Available commands:")
        print("  balance    display account balance in algos")
        print("  rewards    display account rewards in algos")

