import os

import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic

from utils import wait_for_confirmation
from user import User
from node import Node

class Clerk(User):
    def __init__(self, mnemonic):
        User.__init__(self, mnemonic)

    def send(self, to, amount, client):
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

    def sign(self):
        pass
    def inspect(self):
        pass
    def rawsend(self):
        pass
