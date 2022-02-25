import algosdk

class Node():
    def __init__(self, token, node='testnet', prov='ps'):
        self.token = token
        self.node = node
        self.prov = prov
        self.client = self.get_purestake_client()

    def __str__(self):
        text = f"Node:\t\t{self.node}\nToken:\t\t{self.token}\nProvider:\t{self.provider_name()}"
        return text

    def get_purestake_client(self):
        headers = { 'X-API-Key': self.token }

        return algosdk.v2client.algod.AlgodClient(
            self.token, 
            self.ps_provider(), 
            headers
        )

    def provider(self):
        if self.prov == 'ps':
            return self.ps_provider()
        else:
            return 'no other provider available'

    def ps_provider(self):
        return f"https://{self.node}-algorand.api.purestake.io/ps2"

    def provider_name(self):
        if self.prov == 'ps':
            return 'Pure Stake'
        else:
            return 'Unknown provider'
