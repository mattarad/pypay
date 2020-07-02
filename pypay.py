# import Json
from web3 import Web3


# infura_url = ""
# infura_url_mainnet = ""

# web3 = Web3(Web3.HTTPProvider(infura_url))

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("")
print(web3.fromWei(balance, "ether"))

# my_account = web3.eth.account.create('')
# print(my_account._address)
# ''
# print(my_account._private_key)
# HexBytes('')

tx_sender = input('enter wallet that will send the funds:')
priv_key = input('enter the sending wallets private key:')
tx_recieve = input('enter wallet that will recieve the funds:')
tx_amount = input('enter the amount you wish to send: ')

nonce = web3.eth.getTransactionCount(tx_sender)

tx = {
    'nonce': nonce,
    'to': tx_recieve,
    'value': web3.toWei(tx_amount, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, priv_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
