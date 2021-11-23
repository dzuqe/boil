import base64
import datetime
import os

#from algosdk import v2client
import algosdk
from pyteal import *
from algosdk.future import transaction
from algosdk import account, mnemonic

from utils import wait_for_confirmation
from module import Module

#token = os.environ["PURESTAKE_API_KEY"]
#headers = {
#    'X-API-Key': token
#}
#
#client = algosdk.v2client.algod.AlgodClient(
#    token,
#    'https://mainnet-algorand.api.purestake.io/ps2', 
#    headers
#)
#
#params = client.suggested_params()
#params.flat_fee = True
#params.fee = 1000
#
#admin = os.environ['TOKEN_CONTROLLER']
#
#acc_pk = algosdk.mnemonic.to_private_key(admin)
#acc_public = algosdk.mnemonic.to_public_key(admin)
#
## asset create transaction
#txn = algosdk.future.transaction.AssetCreateTxn(
#    sender=acc_public,
#    sp=params,
#    total=10000000,
#    decimals=0,
#    default_frozen=False,
#    manager=acc_public,
#    reserve=acc_public,
#    freeze=acc_public,
#    clawback=acc_public,
#    unit_name="ABRNZ",
#    asset_name="ABronze",
#    url="https://shorturl.at/imFNZ",
#    note="bronze merchant",
#)
#
## sign tx
#signed_txn = txn.sign(acc_pk)
#tx_id = signed_txn.transaction.get_txid()
#
## send tx
#client.send_transactions([signed_txn])
#wait_for_confirmation(client, tx_id)
#transaction_response = client.pending_transaction_info(tx_id)
#
## print results
#print(transaction_response)


class Asset(Module):
    def __init__(self, args):
        Module.__init__(self, args)
