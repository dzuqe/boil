import os

import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic

from utils import wait_for_confirmation
from node import Node

class Clerk():
    def __init__(self, account, client):
        self.account = account
        self.client = client

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

        client.send_transactions([signed_txn])

        wait_for_confirmation(client, tx_id)
        transaction_response = client.pending_transaction_info(tx_id)
        print(transaction_response)

    def sign(self):
        pass
    def inspect(self):
        pass
    def rawsend(self):
        pass
