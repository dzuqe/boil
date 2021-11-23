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

    def exec(self):
        pass

    def create(self):
        pass

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



                                                    #ints #bytes
#global_schema = algosdk.future.transaction.StateSchema(8,3)
#local_schema = algosdk.future.transaction.StateSchema(3,0)
#
#app_args = [
#    '226UJQ6F4M2MFO54PPLBI6HCLZXZG34JVTBOG3LLE2PP4IXDLMAGRNMIX4', #algo reserve
#]
#
## compile teal with pyteal
#approval_prog_teal = compileTeal(approval(), mode=Mode.Application, version=2)
#clear_prog_teal = compileTeal(clear(), mode=Mode.Application, version=2)
#
#approval_prog = compile_program(client, approval_prog_teal)
#clear_prog = compile_program(client, clear_prog_teal)
#
## get node suggested parameters
#params = client.suggested_params()
## comment out the next two (2) lines to use suggested fees
#params.flat_fee = True
#params.fee = 1000
#
#admin = os.environ['ALGO_MNEMONIC']
#
#acc_pk = algosdk.mnemonic.to_private_key(admin)
#acc_public = algosdk.mnemonic.to_public_key(admin)
#
## create unsigned transaction
#txn = algosdk.future.transaction.ApplicationCreateTxn(
#    acc_public,
#    params,
#    algosdk.future.transaction.OnComplete.NoOpOC.real,
#    approval_prog,
#    clear_prog,
#    global_schema,
#    local_schema,
#    app_args,
#)
#
#print(acc_pk)
#
#signed_txn = txn.sign(acc_pk)
#tx_id = signed_txn.transaction.get_txid()
#
#client.send_transactions([signed_txn])
#
#wait_for_confirmation(client, tx_id)
#transaction_response = client.pending_transaction_info(tx_id)
#app_id = transaction_response["application-index"]
#print(app_id)
