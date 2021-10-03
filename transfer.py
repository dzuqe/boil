import base64
import datetime
import os

#from algosdk import v2client
import algosdk
#from contract import approval, clear
from pyteal import *
from algosdk.future import transaction
from algosdk import account, mnemonic

def get_private_key_from_mnemonic(mn):
    private_key = mnemonic.to_private_key(mn)
    return private_key

# helper function to compile program source
def compile_program(client, source_code):
    compile_response = client.compile(source_code)
    return base64.b64decode(compile_response["result"])

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
    headers,
)

# get node suggested parameters
params = client.suggested_params()
# comment out the next two (2) lines to use suggested fees
params.flat_fee = True
params.fee = 1000

admin = os.environ['ALGO_MNEMONIC']

acc_pk = algosdk.mnemonic.to_private_key(admin)
acc_public = algosdk.mnemonic.to_public_key(admin)
binance_acc = 'LMOMTWMBXYCFVJMSSFNYZOEXNL6CLI66KT46GJ2DBXSNUQOXJUYTLMTB4I'

amount = 250000

# create unsigned transaction
txn = algosdk.future.transaction.PaymentTxn(
    acc_public, # sender
    params,     # sp
    binance_acc,# receiver
    amount,     # amount to send
)

print(acc_pk)

signed_txn = txn.sign(acc_pk)
tx_id = signed_txn.transaction.get_txid()

client.send_transactions([signed_txn])

wait_for_confirmation(client, tx_id)
transaction_response = client.pending_transaction_info(tx_id)
app_id = transaction_response["application-index"]
print(app_id)
