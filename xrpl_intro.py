"""
In this code we 
    1. Connect to the XRPL
    2. Create an account on the XRPL
    3. Query Data about the newly created account
    4. Send a payment to another account
"""

# Import to - Connect to Ripple test server
from xrpl.clients import JsonRpcClient
# Import to - Create wallet
from xrpl.wallet import generate_faucet_wallet
# Import to - Look up info about your account
from xrpl.models.requests.account_info import AccountInfo
# Import to - Make payment transactions
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
# Import to - Sign and submit the transaction
from xrpl.transaction import submit_and_wait
import json

# Connect to ripple test server
JSON_RPC_URL = 'https://s.altnet.rippletest.net:51234/'
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html
test_wallet = generate_faucet_wallet(client, debug=True)

print('Wallet Created: ', test_wallet)
test_account = test_wallet.address

print('===================================================')

# Query legder for info on acc
acct_info = AccountInfo(
    account=test_account,
    ledger_index="validated",
    strict=True,
)
response = client.request(acct_info)
result = response.result
print("response.status: ", response.status)
print(json.dumps(response.result, indent=4, sort_keys=True))

print('===================================================')

# Create a transaction
my_tx_payment = Payment(
    account=test_account,
    amount=xrp_to_drops(22),
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
)

print('Transaction Created: ', my_tx_payment)

print('===================================================')

# submitting the transaction
tx_response = submit_and_wait(my_tx_payment, client, test_wallet)
print('Transaction response ', tx_response)
