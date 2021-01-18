import csv
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider('wss://ropsten.infura.io/ws/v3/aedfdb9bade24481a2b829f32220850c'))
block=w3.eth.getBlock(9447422)
val = block.number

address = "0x0433d7DF46bC3328620948CfbdbEA54eDAa2A876"

if block != None and block.transactions != None:
    print("Difficulty -",block.difficulty)
    print()
  
for txHash in block.transactions:
    tx = w3.eth.getTransaction(txHash)
    send = (tx['from'])
    receiver = (tx['to'])
    ether = tx['value']
    if(receiver == address):
        print("Transaction is Found on Block -",val)
        print("Block Hash -",block.hash.hex())
        print("Transaction hash -",tx['hash'].hex())
        print("Timstamp -",block.timestamp)
        print("From: "+send+" To: "+receiver)
        print("Ether Value -",w3.fromWei(ether, "ether"))

        with open('Transactions.csv', mode='w') as csv_file:
            fieldnames = ['Block', 'Block_Hash','Transaction_Hash', 'Timestamp','From','To','Ether']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Block': val , 'Block_Hash':block.hash.hex() , 'Transaction_Hash':tx['hash'].hex() , 'Timestamp':block.timestamp , 'From':send , 'To':receiver ,'Ether':w3.fromWei(ether, "ether")})
        