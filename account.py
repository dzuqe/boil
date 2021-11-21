import algosdk

class Account():
    def __init__(self, mnemonic):
        self.private_key = algosdk.mnemonic.to_private_key(mnemonic)
        self.public_key = algosdk.mnemonic.to_public_key(mnemonic)

    def balance(self):
        pass
    def delete(self):
        pass
    def rewards(self):
        pass
