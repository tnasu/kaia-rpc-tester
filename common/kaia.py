from utils import Utils

_, _, log_path = Utils.get_log_filename_with_path()


def send_transaction(endpoint, params):
    transaction_hash, error = Utils.call_rpc(endpoint, "kaia_sendTransaction", params, log_path)
    return transaction_hash, error


def get_transaction(endpoint, params):
    transaction, error = Utils.call_rpc(endpoint, "kaia_getTransactionByHash", params, log_path)
    return transaction, error


def get_transaction_receipt(endpoint, params):
    receipt, error = Utils.call_rpc(endpoint, "kaia_getTransactionReceipt", params, log_path)
    return receipt, error


def get_latest_block_by_number(endpoint):
    method = "kaia_getBlockByNumber"
    latest_block, _ = Utils.call_rpc(endpoint, method, ["latest", True], log_path)
    return latest_block


def get_block_number(endpoint):
    method = "kaia_blockNumber"
    block_number, _ = Utils.call_rpc(endpoint, method, ["latest", True], log_path)
    return block_number

def get_chain_config(endpoint):
    method = "kaia_getChainConfig"
    chain_config, _ = Utils.call_rpc(endpoint, method, [], log_path)
    return chain_config

def checkBaseFeePerGasFieldAndValue(self, result, value=""):
    self.assertIsNotNone(result)
    self.assertIsNotNone(result["baseFeePerGas"])

    if value != "":
        isMagma = get_chain_config(self.endpoint)['magmaCompatibleBlock'] <= int(get_block_number(self.endpoint), 16)
        if isMagma:
                value = "0x5d21dba00"
        else:
            value = "0x0"
        self.assertEqual(result["baseFeePerGas"], value)

def checkGasPriceField(self, result):
    self.assertIsNotNone(result["gasPrice"])
    if result["typeInt"] == 30722 or result["typeInt"] == 30724:  # TxTypeEthereumDynamicFee, TxTypeEthereumSetCode
        self.assertIsNotNone(result["maxFeePerGas"])
        self.assertIsNotNone(result["maxPriorityFeePerGas"])

def checkAuthorizationListField(self, result):
    if result["typeInt"] == 30724:  # TxTypeEthereumSetCode
        self.assertIsNotNone(result["authorizationList"])

# In KIP228, EOA now returns storageRoot, codeHash, codeFormat, and vmVersion when gettingAccount.
# This function checks to make sure they are not None.
def checkIfEoaFollowKIP228(self, result):
    self.assertIsNotNone(result["account"]["storageRoot"])
    self.assertIsNotNone(result["account"]["codeHash"])
    self.assertIsNotNone(result["account"]["codeFormat"])
    self.assertIsNotNone(result["account"]["vmVersion"])
