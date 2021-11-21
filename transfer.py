import os

# sdk 
import algosdk
from algosdk.future import transaction
from algosdk import account, mnemonic
#from pyteal import *

from utils import wait_for_confirmation

node = 'https://mainnet-algorand.api.purestake.io/ps2'
token = os.environ["PURESTAKE_API_KEY"]

headers = {
    'X-API-Key': token
}

client = algosdk.v2client.algod.AlgodClient(token, node, headers)

params = client.suggested_params()

params.flat_fee = True
params.fee = 1000

admin = os.environ['MARC']

acc_pk = algosdk.mnemonic.to_private_key(admin)
acc_public = algosdk.mnemonic.to_public_key(admin)
binance_acc = 'LMOMTWMBXYCFVJMSSFNYZOEXNL6CLI66KT46GJ2DBXSNUQOXJUYTLMTB4I'

amount = 1000000

txn = algosdk.future.transaction.PaymentTxn(
    acc_public, # sender
    params,     # sp
    binance_acc,# receiver
    amount,     # amount to send
)

signed_txn = txn.sign(acc_pk)
tx_id = signed_txn.transaction.get_txid()

client.send_transactions([signed_txn])

wait_for_confirmation(client, tx_id)
transaction_response = client.pending_transaction_info(tx_id)
print(transaction_response)
