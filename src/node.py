import algosdk

class Node():
    def __init__(self, token, node):
        self.token = token
        self.node = node
        self.client = self.get_purestake_client()

    def get_purestake_client(self):
        headers = { 'X-API-Key': self.token }

        return algosdk.v2client.algod.AlgodClient(
            self.token, 
            self.provider(self.node, 'ps2'), 
            headers
        )

    def provider(self, net, type):
        return f"https://{net}-algorand.api.purestake.io/{type}"

    """
    Switch node

    @param node - new node
    """
    def switchNode(self, node):
        if node in ['mainnet', 'betanet', 'testnet']:
            self.node = node
        else:
            print(f"Error: unidentified node: {node}")
