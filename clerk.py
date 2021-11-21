import os

# sdk 
import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic
#from pyteal import *

from utils import wait_for_confirmation
from user import User
from node import Node

class Clerk(User):
    def __init__(self, mnemonic):
        User.__init__(self, mnemonic)

    def transfer(self, to, amount, client):
        params = client.suggested_params()
        params.flat_fee = True
        params.fee = 1000

        txn = algosdk.future.transaction.PaymentTxn(
            self.public_key, # sender
            params,     # sp
            to,         # receiver
            amount,     # amount to send
        )

        signed_txn = txn.sign(self.private_key)
        tx_id = signed_txn.transaction.get_txid()

        client.send_transactions([signed_txn])

        wait_for_confirmation(client, tx_id)
        transaction_response = client.pending_transaction_info(tx_id)
        print(transaction_response)

node = Node(os.environ["PURESTAKE_API_KEY"], 'https://mainnet-algorand.api.purestake.io/ps2')

binance_acc = 'LMOMTWMBXYCFVJMSSFNYZOEXNL6CLI66KT46GJ2DBXSNUQOXJUYTLMTB4I'
amount = 1000

clerk = Clerk(os.environ['MARC'])
#clerk.transfer(binance_acc, amount, node.client)
