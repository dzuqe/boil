import base64
import datetime
import os

#from algosdk import v2client
import algosdk
from pyteal import *
from algosdk.future import transaction
from algosdk import account, mnemonic

def get_private_key_from_mnemonic(mn):
    private_key = mnemonic.to_private_key(mn)
    return private_key

# helper function that waits for a given txid to be confirmed by the network
def wait_for_confirmation(client, txid):
    last_round = client.status().get("last-round")
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get("confirmed-round") and txinfo.get("confirmed-round") > 0):
        print("Waiting for confirmation...")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print(
        "Transaction {} confirmed in round {}.".format(
            txid, txinfo.get("confirmed-round")
        )
    )
    return txinfo

def wait_for_round(client, round):
    last_round = client.status().get("last-round")
    print(f"Waiting for round {round}")
    while last_round < round:
        last_round += 1
        client.status_after_block(last_round)
        print(f"Round {last_round}")


token = os.environ["PURESTAKE_API_KEY"]
headers = {
    'X-API-Key': token
}

client = algosdk.v2client.algod.AlgodClient(
    token,
    'https://mainnet-algorand.api.purestake.io/ps2', 
    headers
)

# get node suggested parameters
params = client.suggested_params()
# comment out the next two (2) lines to use suggested fees
params.flat_fee = True
params.fee = 1000

admin = os.environ['TOKEN_CONTROLLER']

acc_pk = algosdk.mnemonic.to_private_key(admin)
acc_public = algosdk.mnemonic.to_public_key(admin)

# asset create transaction
txn = algosdk.future.transaction.AssetCreateTxn(
    sender=acc_public,
    sp=params,
    total=10000000,
    decimals=0,
    default_frozen=False,
    manager=acc_public,
    reserve=acc_public,
    freeze=acc_public,
    clawback=acc_public,
    unit_name="ABRNZ",
    asset_name="ABronze",
    url="https://shorturl.at/imFNZ",
    note="bronze merchant",
)

# sign tx
signed_txn = txn.sign(acc_pk)
tx_id = signed_txn.transaction.get_txid()

# send tx
client.send_transactions([signed_txn])
wait_for_confirmation(client, tx_id)
transaction_response = client.pending_transaction_info(tx_id)

# print results
print(transaction_response)
