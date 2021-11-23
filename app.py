import base64
import datetime
import os

#from algosdk import v2client
import algosdk
from pyteal import *
from algosdk.future import transaction
from algosdk import account, mnemonic

from utils import wait_for_confirmation
from node import Node
from account import Account
from asset import Asset
from module import Module

class App(Module):
    def __init__(self, args):
        Module.__init__(self, args)
        self.account = Account(os.environ['ALGO_MNEMONIC'])
        command = ""
        if len(args) > 0:
            command = args[0]

        self.data = {
            "command": command,
        }

    def exec(self):
        if self.data['command'] == 'create':
            print('create asset')
        else:
            print(f"Error: Unknown command: {self.data['command']}")
            self.help()

    def create(self):
                                                    #ints #bytes
        global_schema = algosdk.future.transaction.StateSchema(8,3)
        local_schema = algosdk.future.transaction.StateSchema(3,0)

        app_args = [
            '226UJQ6F4M2MFO54PPLBI6HCLZXZG34JVTBOG3LLE2PP4IXDLMAGRNMIX4', #algo reserve
        ]

        # compile teal with pyteal
        approval_prog_teal = compileTeal(approval(), mode=Mode.Application, version=2)
        clear_prog_teal = compileTeal(clear(), mode=Mode.Application, version=2)

        approval_prog = ""#compile_program(client, approval_prog_teal)
        clear_prog = ""#compile_program(client, clear_prog_teal)

        params = self.client.suggested_params()
        params.flat_fee = True
        params.fee = 1000

        # create unsigned transaction
        txn = algosdk.future.transaction.ApplicationCreateTxn(
            self.account.public_key,
            params,
            algosdk.future.transaction.OnComplete.NoOpOC.real,
            approval_prog,
            clear_prog,
            global_schema,
            local_schema,
            app_args,
        )

        signed_txn = txn.sign(self.account.private_key)
        tx_id = signed_txn.transaction.get_txid()

        client.send_transactions([signed_txn])

        wait_for_confirmation(client, tx_id)
        transaction_response = client.pending_transaction_info(tx_id)
        app_id = transaction_response["application-index"]
        print(app_id)

    def call(self):
        pass

    def clear(self):
        pass

    def closeout(self):
        pass

    def optin(self):
        pass

    def delete(self):
        pass

    def info(self):
        pass

    def interact(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def help(self):
        print("asset help")


