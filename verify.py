import web3
from web3 import Web3
import eth_account
from eth_account.messages import encode_defunct
from web3.middleware import ExtraDataToPOAMiddleware
import random, os, secrets

# def claim_nft():
#     RPC_FUJI = "https://api.avax-test.network/ext/bc/C/rpc"
#     CONTRACT_ADDRESS = web3.Web3.to_checksum_address("0x85ac2e065d4526FBeE6a2253389669a12318A412")
#
#     ABI = open("NFT.abi").read()
#
#     private_key = "0x6608bee2f462fa92b53bf52acb0ebfab6e8597ac618059d028f07b4f08023c16"
#     account = eth_account.Account.from_key(private_key)
#     address = account.address
#
#     # connect to the network
#     w3 = web3.Web3(web3.Web3.HTTPProvider(RPC_FUJI))
#     w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
#
#     #test if connected
#     assert w3.is_connected(), "NOT CONNECTED!!!"
#
#     contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
#
#     # helper fx, to create random nonce
#     def rand_nonce():
#         return secrets.token_bytes(32)
#
#     def do_transaction(nonce_bytes: bytes, address: str, w3: web3.Web3, contract: web3.contract.Contract):
#         return contract.functions.claim(address, nonce_bytes).build_transaction({
#             'from': address,
#             'nonce': w3.eth.get_transaction_count(address),
#             'maxFeePerGas': w3.to_wei('50', 'gwei'),
#             'maxPriorityFeePerGas': w3.to_wei('2', 'gwei'),
#             'chainId': w3.eth.chain_id,
#         })
#
#     while True:
#         nonce = rand_nonce()
#         txn = do_transaction(nonce, address, w3, contract)
#         signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
#         tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
#         receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#         print(f"Transaction receipt: {receipt}")
#
#         # Check if the transaction was successful and if a tokenID was minted
#         if receipt.status == 1:
#             logs = contract.events.Transfer().process_receipt(receipt)
#             if logs:
#                 token_id = logs[0]['args']['tokenId']
#                 print(f"Successfully claimed NFT with tokenID: {token_id}")
#                 break
#             else:
#                 print("No NFT minted, trying again...")
#         else:
#             print("Transaction failed, trying again...")
#
# #brute force until we get a valid tokenID




def sign_challenge( challenge ):

    w3 = Web3()

    """ To actually claim the NFT you need to write code in your own file, or use another claiming method
    Once you have claimed an NFT you can come back to this file, update the "sk" and submit to codio to 
    prove that you have claimed your NFT.
    
    This is the only line you need to modify in this file before you submit """
    sk = "0x6608bee2f462fa92b53bf52acb0ebfab6e8597ac618059d028f07b4f08023c16"

    acct = w3.eth.account.from_key(sk)

    signed_message = w3.eth.account.sign_message( challenge, private_key = acct.key )

    return acct.address, signed_message.signature


def verify_sig():
    """
        This is essentially the code that the autograder will use to test signChallenge
        We've added it here for testing 
    """
    
    challenge_bytes = random.randbytes(32)

    challenge = encode_defunct(challenge_bytes)
    address, sig = sign_challenge( challenge )

    w3 = Web3()

    return w3.eth.account.recover_message( challenge , signature=sig ) == address


if __name__ == '__main__':
    """
        Test your function
    """
    # claim_nft()
    if verify_sig():
        print( f"You passed the challenge!" )
    else:
        print( f"You failed the challenge!" )
