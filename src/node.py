import algosdk

class Node():
    def __init__(self, token, node):
        self.token = token
        self.node = node
        self.client = self.get_purestake_client()

    def get_purestake_client(self):
        headers = { 'X-API-Key': self.token }
        return algosdk.v2client.algod.AlgodClient(self.token, self.node, headers)

