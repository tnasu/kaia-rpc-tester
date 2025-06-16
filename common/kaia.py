from typing import Final
from utils import Utils

_, _, log_path = Utils.get_log_filename_with_path()

EMPTY_STORAGE_ROOT: Final = "0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421"
EMPTY_CODE_HASH: Final = "xdJGAYb3IzySfn2y3McDwOUAtlPKgic7e/rYBF2FpHA="
EMPTY_CODE_FORMAT: Final = 0
EMPTY_VM_VERSION: Final = 0

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

# SCA has specific values of storageRoot, codeHash, codeFormat, and vmVersion when getting Account.
# In KIP228, EOA with code also returns them. See https://kips.kaia.io/KIPs/kip-228
# This function checks to ensure they are or are not.
def checkIfAccountHasSpecificValues(self, result, isNotEqual=True):
    if isNotEqual:
        self.assertNotEqual(result["account"]["vmVersion"], EMPTY_VM_VERSION)
        self.assertNotEqual(result["account"]["codeHash"], EMPTY_CODE_HASH)
        self.assertEqual(result["account"]["codeFormat"], EMPTY_CODE_FORMAT) # The prepared test data is not updated
        if result["accType"] == 1: # EOA (In this case, this is EOA with code)
            self.assertEqual(result["account"]["storageRoot"], EMPTY_STORAGE_ROOT) # The prepared test data is not updated
        elif result["accType"] == 2: # SCA
            self.assertNotEqual(result["account"]["storageRoot"], EMPTY_STORAGE_ROOT)
    else:
        self.assertEqual(result["account"]["vmVersion"], EMPTY_VM_VERSION)
        self.assertEqual(result["account"]["codeHash"], EMPTY_CODE_HASH)
        self.assertEqual(result["account"]["codeFormat"], EMPTY_CODE_FORMAT)
        self.assertEqual(result["account"]["storageRoot"], EMPTY_STORAGE_ROOT)
