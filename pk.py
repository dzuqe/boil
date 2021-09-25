import algosdk

token = os.environ['PURESTAKE_API_KEY']
headers = {
    'X-API-Key': token
}

client = algosdk.v2client.algod.AlgodClient(
    token,
    'https://mainnet-algorand.api.purestake.io/ps2', 
    headers
)

sender_pk, sender_addr = algosdk.account.generate_account()
receiver_pk, receiver_addr = algosdk.account.generate_account()

params = client.suggested_params()
params.flat_fee = True
params.fee = 1000

admin = os.environ['ALGO_MNEMONIC']

sender_pk = algosdk.mnemonic.to_private_key(admin)

txn = algosdk.future.transaction.PaymentTxn(sender_addr, params, receiver_addr, 10000)
