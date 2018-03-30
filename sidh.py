from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import simplejson
import os

w3 = Web3(HTTPProvider('https://ropsten.infura.io/R0JC6u2n5GHifC4NLX8y'))
file_path = os.path.join(path,'trust.json')
with open("trust.json") as f:
    filecontents = simplejson.load(f)
bytes1 = w3.toBytes(text='abc')

contract = w3.eth.contract('0x5Aa1Da862C66B342E2946560b18C13a61C52e98D',abi = filecontents, ContractFactoryClass = ConciseContract)
contract = w3.eth.contract('0x6c8B815c51D8B84324804167DD6A1a5623407a3F', abi = filecontents)

txn = contract.addAttribute("Sid",True,bytes1,"abc","abc",buildTransaction = {'chainId':3,'gas':300000, 'gasPrice':w3.toWei('4', 'gwei'),'nonce' : nonce})
nonce = w3.eth.getTransactionCount('0x6c8B815c51D8B84324804167DD6A1a5623407a3F')

private_key = ""
signed = w3.eth.account.signTransaction(txn, private_key=private_key)

w3.eth.sendRawTransaction(signed.rawTransaction)
                                   
                                   
                                
