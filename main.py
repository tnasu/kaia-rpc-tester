import unittest
import json
import argparse
import types
from functools import wraps
from HtmlTestRunner import HTMLTestRunner
from utils import Utils
from common import personal as personal_common
from common import kaia as kaia_common
from admin import admin_rpc
from admin import admin_ws
from admin.admin_rpc import TestAdminNamespaceRPC
from admin.admin_ws import TestAdminNamespaceWS
from debug import debug_rpc
from debug import debug_ws
from debug.debug_rpc import TestDebugNamespaceRPC
from debug.debug_ws import TestDebugNamespaceWS
from net import net_rpc
from net import net_ws
from net.net_rpc import TestNetNamespaceRPC
from net.net_ws import TestNetNamespaceWS
from personal import personal_rpc
from personal import personal_ws
from personal.personal_rpc import TestPersonalNamespaceRPC
from personal.personal_ws import TestPersonalNamespaceWS
from txpool import txpool_rpc
from txpool import txpool_ws
from txpool.txpool_rpc import TestTxpoolNamespaceRPC
from txpool.txpool_ws import TestTxpoolNamespaceWS
from kaia.account import kaia_account_rpc
from kaia.account import kaia_account_ws
from kaia.account.kaia_account_rpc import TestKaiaNamespaceAccountRPC
from kaia.account.kaia_account_ws import TestKaiaNamespaceAccountWS
from kaia.block import kaia_block_rpc
from kaia.block import kaia_block_ws
from kaia.block.kaia_block_rpc import TestKaiaNamespaceBlockRPC
from kaia.block.kaia_block_ws import TestKaiaNamespaceBlockWS
from kaia.configuration import kaia_configuration_rpc
from kaia.configuration import kaia_configuration_ws
from kaia.configuration.kaia_configuration_rpc import TestKaiaNamespaceConfigurationRPC
from kaia.configuration.kaia_configuration_ws import TestKaiaNamespaceConfigurationWS
from kaia.miscellaneous import kaia_miscellaneous_rpc
from kaia.miscellaneous import kaia_miscellaneous_ws
from kaia.miscellaneous.kaia_miscellaneous_rpc import TestKaiaNamespaceMiscellaneousRPC
from kaia.miscellaneous.kaia_miscellaneous_ws import TestKaiaNamespaceMiscellaneousWS
from kaia.transaction import kaia_transaction_rpc
from kaia.transaction import kaia_transaction_ws
from kaia.transaction.kaia_transaction_rpc import TestKaiaNamespaceTransactionRPC
from kaia.transaction.kaia_transaction_ws import TestKaiaNamespaceTransactionWS
from kaia.filter import kaia_filter_rpc
from kaia.filter import kaia_filter_ws
from kaia.filter.kaia_filter_rpc import TestKaiaNamespaceFilterRPC
from kaia.filter.kaia_filter_ws import TestKaiaNamespaceFilterWS
from eth.account import eth_account_rpc
from eth.account import eth_account_ws
from eth.account.eth_account_rpc import TestEthNamespaceAccountRPC
from eth.account.eth_account_ws import TestEthNamespaceAccountWS
from eth.block import eth_block_rpc
from eth.block import eth_block_ws
from eth.block.eth_block_rpc import TestEthNamespaceBlockRPC
from eth.block.eth_block_ws import TestEthNamespaceBlockWS
from eth.configuration import eth_configuration_rpc
from eth.configuration import eth_configuration_ws
from eth.configuration.eth_configuration_rpc import TestEthNamespaceConfigurationRPC
from eth.configuration.eth_configuration_ws import TestEthNamespaceConfigurationWS
from eth.miscellaneous import eth_miscellaneous_rpc
from eth.miscellaneous import eth_miscellaneous_ws
from eth.miscellaneous.eth_miscellaneous_rpc import TestEthNamespaceMiscellaneousRPC
from eth.miscellaneous.eth_miscellaneous_ws import TestEthNamespaceMiscellaneousWS
from eth.transaction import eth_transaction_rpc
from eth.transaction import eth_transaction_ws
from eth.transaction.eth_transaction_rpc import TestEthNamespaceTransactionRPC
from eth.transaction.eth_transaction_ws import TestEthNamespaceTransactionWS
from eth.filter import eth_filter_rpc
from eth.filter import eth_filter_ws
from eth.filter.eth_filter_rpc import TestEthNamespaceFilterRPC
from eth.filter.eth_filter_ws import TestEthNamespaceFilterWS
from eth.gas import eth_gas_rpc
from eth.gas import eth_gas_ws
from eth.gas.eth_gas_rpc import TestEthNamespaceGasRPC
from eth.gas.eth_gas_ws import TestEthNamespaceGasWS
from kaia.gas import kaia_gas_rpc
from kaia.gas import kaia_gas_ws
from kaia.gas.kaia_gas_rpc import TestKaiaNamespaceGasRPC
from kaia.gas.kaia_gas_ws import TestKaiaNamespaceGasWS


test_data_set = None
config = None
rpc_test_suites = None
ws_test_suites = None
_, _, log_path = Utils.get_log_filename_with_path()


def decorate_all_functions(module, decorator):
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, types.FunctionType):
            setattr(module, name, decorator(obj))


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "test" in f.__name__:
            Utils.write_head_or_tail_log(
                log_path,
                Utils.TestingStatus.START,
                f.__name__,
            )
            try:
                res = f(*args, **kwargs)
            finally:
                Utils.write_head_or_tail_log(
                    log_path,
                    Utils.TestingStatus.FINISHED,
                    f.__name__,
                )
        else:
            res = f(*args, **kwargs)
        return res

    return wrapper


decorate_all_functions(TestAdminNamespaceRPC, my_decorator)
decorate_all_functions(TestAdminNamespaceWS, my_decorator)
decorate_all_functions(TestDebugNamespaceRPC, my_decorator)
decorate_all_functions(TestDebugNamespaceWS, my_decorator)
decorate_all_functions(TestNetNamespaceRPC, my_decorator)
decorate_all_functions(TestNetNamespaceWS, my_decorator)
decorate_all_functions(TestPersonalNamespaceRPC, my_decorator)
decorate_all_functions(TestPersonalNamespaceWS, my_decorator)
decorate_all_functions(TestTxpoolNamespaceRPC, my_decorator)
decorate_all_functions(TestTxpoolNamespaceWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceAccountRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceAccountWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceBlockRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceBlockWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceConfigurationRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceConfigurationWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceMiscellaneousRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceMiscellaneousWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceTransactionRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceTransactionWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceFilterRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceFilterWS, my_decorator)
decorate_all_functions(TestEthNamespaceAccountRPC, my_decorator)
decorate_all_functions(TestEthNamespaceAccountWS, my_decorator)
decorate_all_functions(TestEthNamespaceBlockRPC, my_decorator)
decorate_all_functions(TestEthNamespaceBlockWS, my_decorator)
decorate_all_functions(TestEthNamespaceConfigurationRPC, my_decorator)
decorate_all_functions(TestEthNamespaceConfigurationWS, my_decorator)
decorate_all_functions(TestEthNamespaceMiscellaneousRPC, my_decorator)
decorate_all_functions(TestEthNamespaceMiscellaneousWS, my_decorator)
decorate_all_functions(TestEthNamespaceTransactionRPC, my_decorator)
decorate_all_functions(TestEthNamespaceTransactionWS, my_decorator)
decorate_all_functions(TestEthNamespaceFilterRPC, my_decorator)
decorate_all_functions(TestEthNamespaceFilterWS, my_decorator)
decorate_all_functions(TestEthNamespaceGasRPC, my_decorator)
decorate_all_functions(TestEthNamespaceGasWS, my_decorator)
decorate_all_functions(TestKaiaNamespaceGasRPC, my_decorator)
decorate_all_functions(TestKaiaNamespaceGasWS, my_decorator)


def parse_arguments():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog="rpc-tester",
        usage="python main.py --protocol <rpc_or_ws>",
        description="Run tests using RPC or WebSocket",
        add_help=True,
    )
    parser.add_argument(
        "--protocol",
        help="Protocol when used during tests: rpc or ws",
    )
    args = parser.parse_args()
    return args.protocol


def load_test_data():
    """
    Load test data and create global test_data_set which will be used by many TCs commonly.
    """
    test_data_json = """
    {
        "account": {
            "sender": {
                "address": "",
                "password": "",
                "privateKey": ""
            },
            "1pebHolder": {
                "address": ""
            },
            "feePayer": {
                "address": "",
                "password": "",
                "privateKey": ""
            },
            "eoaWithCode": {
                "address": "",
                "password": "",
                "privateKey": ""
            },
            "receiver": {
                "address": ""
            },
            "import": {
                "address": "",
                "password": "",
                "privateKey": ""
            }
        },
        "contracts": {
            "unknown": {
                "address": [""],
                "data": "0x608060405234801561001057600080fd5b506040516020806102fb8339810180604052602081101561003057600080fd5b810190808051906020019092919050505033600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550600160026000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600001819055508060ff166003816100fd919061010c565b50600f6000819055505061015f565b815481835581811115610133578183600052602060002091820191016101329190610138565b5b505050565b61015c91905b80821115610158576000808201600090555060010161013e565b5090565b90565b61018d8061016e6000396000f3fe60806040526004361061003b576000357c010000000000000000000000000000000000000000000000000000000090048063b3f98adc14610040575b600080fd5b34801561004c57600080fd5b5061007c6004803603602081101561006357600080fd5b81019080803560ff16906020019092919050505061007e565b005b6000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002090508060010160009054906101000a900460ff16806100e657506003805490508260ff1610155b156100f1575061015e565b60018160010160006101000a81548160ff021916908315150217905550818160010160016101000a81548160ff021916908360ff160217905550806000015460038360ff1681548110151561014257fe5b9060005260206000200160000160008282540192505081905550505b5056fea165627a7a72305820dad6d3e144a160eb6e34d8d99084ed29d207271e201aaac513007f652a26e2200029",
                "dataDescription": "Please add description for bytecode",
                "input": "0xb3f98adc0000000000000000000000000000000000000000000000000000000000000001",
                "description": "Please add description for contract source code and input"
            },
            "ownerContract": {
                "address": [""],
                "data": "0x608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16600073ffffffffffffffffffffffffffffffffffffffff167f342827c97908e5e2f71151c08502a66d44b6f758e3ac2f1de95f02eb95f0a73560405160405180910390a3610356806100db6000396000f3fe608060405234801561001057600080fd5b50600436106100365760003560e01c8063893d20e81461003b578063a6f9dae114610059575b600080fd5b610043610075565b604051610050919061025d565b60405180910390f35b610073600480360381019061006e91906101fe565b61009e565b005b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461012c576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040161012390610278565b60405180910390fd5b8073ffffffffffffffffffffffffffffffffffffffff1660008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f342827c97908e5e2f71151c08502a66d44b6f758e3ac2f1de95f02eb95f0a73560405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b6000813590506101f881610309565b92915050565b600060208284031215610214576102136102db565b5b6000610222848285016101e9565b91505092915050565b610234816102a9565b82525050565b6000610247601383610298565b9150610252826102e0565b602082019050919050565b6000602082019050610272600083018461022b565b92915050565b600060208201905081810360008301526102918161023a565b9050919050565b600082825260208201905092915050565b60006102b4826102bb565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600080fd5b7f43616c6c6572206973206e6f74206f776e657200000000000000000000000000600082015250565b610312816102a9565b811461031d57600080fd5b5056fea2646970667358221220d8b1ba73854235865084cd146d56b584ad91a0dd55cf8fe3ca277e04896bf95c64736f6c63430008070033",
                "dataDescription": "compiled bytecode of contracts/Owner.sol",
                "input": "0xa6f9dae10000000000000000000000003e2ac308cd78ac2fe162f9522deb2b56d9da9499",
                "inputDescription": "call changeOwner('0x3e2ac308cd78ac2fe162f9522deb2b56d9da9499') of contracts/Owner.sol"
            }
        },
        "info": {
            "kni": "kni://6219a5b7f741a237ffdb9f59832c68fc942b1f8b3f964fca5af54fcaa76a3c51bfa58b8cf5bd256da7fd8de30ec69425b8fba040bb46cf72404b921d633d49a4@13.125.209.116:32323"
        },
        "test": {
            "knis": [
                "kni://71534185c62a4404c516fbc5dd0252c6578c1955b94bab55c363d5a1a86fac0e6562e584e4e8d046bb9b197962d3b350417af49f0bf08b4368cb4916232b50c3@10.10.0.129:32323",
                "kni://ff7303e607caa04a2b81c638c3b2e689a659eea4d4561b8d9766dc1017ba294c49f4198556b7433f39cf39d06f41bf8e19edc9342bea35c24cdc2a3d7be15257@10.10.0.101:32323",
                "kni://444444444444447303e607caa04a2b81c638c3b259eea4d4561b8d9766dc1017ba294c49f4198556b7433f39cf39d06f41bf8e19edc934c24cdc2a3d7be15257@10.10.0.101:32323"
            ]
        }
    }
            """

    global test_data_set
    test_data_set = json.loads(test_data_json)
    test_data_set["account"]["sender"]["address"] = config["faucetAddress"]
    test_data_set["account"]["sender"]["password"] = config.get("faucetPassword", "")
    test_data_set["account"]["sender"]["privateKey"] = "0x" + config["faucetPrivateKey"]
    # Set a fee payer account. If config.json does not have fee payer fields, use sender.
    test_data_set["account"]["feePayer"]["address"] = config.get("feePayerAddress", config["faucetAddress"])
    test_data_set["account"]["feePayer"]["password"] = config.get("feePayerPassword", config.get("faucetPassword", ""))
    test_data_set["account"]["feePayer"]["privateKey"] = "0x" + config.get(
        "feePayerPrivateKey", config["faucetPrivateKey"]
    )
    # Set a eoa with code account. If config.json does not have eoa with code fields.
    test_data_set["account"]["eoaWithCode"]["address"] = config["eoaWithCodeAddress"]
    test_data_set["account"]["eoaWithCode"]["password"] = config.get("eoaWithCodePassword", "")
    test_data_set["account"]["eoaWithCode"]["privateKey"] = "0x" + config["eoaWithCodePrivateKey"]

    test_data_set["account"]["receiver"]["address"] = "0x44711E89b0c23845b5B2ed9D3716BA42b8a3e075"
    # 1pebHolder is for estimateGas test case
    test_data_set["account"]["1pebHolder"]["address"] = "0x1111111111111111111111111111111111111111"
    gas_price, error = Utils.call_rpc("", "kaia_gasPrice", [], log_path)
    assert error is None
    test_data_set["unitGasPrice"] = gas_price


def makeTxData():
    global test_data_set
    txFrom = test_data_set["account"]["sender"]["address"]
    txFeePayer = test_data_set["account"]["sender"]["address"]
    txTo = test_data_set["account"]["sender"]["address"]
    txData = test_data_set["contracts"]["unknown"]["data"]
    txValueZero = "0x0"
    txValueOne = "0x1"
    txMemo = "0xb3f98adc0000000000000000000000000000000000000000000000000000000000000001"
    txKey = "0x01c0"
    txGas = hex(3040000000)
    txGasPrice = test_data_set["unitGasPrice"]
    txContractAddress = test_data_set["contracts"]["unknown"]["address"][0]
    txContractExecutionData = test_data_set["contracts"]["unknown"]["input"]
    txFeeRatio = 30
    txCodeFormat = 0
    txHumanReadable = False

    txs = [
        {
            "type": "TxTypeLegacyTransaction",
            "tx": {
                "from": txFrom,
                "to": test_data_set["account"]["1pebHolder"]["address"],
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeLegacyTransaction",
            "tx": {
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "data": txData,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeValueTransfer",
            "tx": {
                "typeInt": 8,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedValueTransfer",
            "tx": {
                "typeInt": 9,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedValueTransferWithRatio",
            "tx": {
                "typeInt": 10,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeValueTransferMemo",
            "tx": {
                "typeInt": 16,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
                "input": txMemo,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedValueTransferMemo",
            "tx": {
                "typeInt": 17,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
                "input": txMemo,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedValueTransferMemoWithRatio",
            "tx": {
                "typeInt": 18,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueOne,
                "input": txMemo,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeAccountUpdate",
            "tx": {
                "typeInt": 32,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "key": txKey,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedAccountUpdate",
            "tx": {
                "typeInt": 33,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "key": txKey,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedAccountUpdateWithRatio",
            "tx": {
                "typeInt": 34,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "key": txKey,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeSmartContractDeploy",
            "tx": {
                "typeInt": 40,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txData,
                "codeFormat": txCodeFormat,
                "humanReadable": txHumanReadable,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedSmartContractDeploy",
            "tx": {
                "typeInt": 41,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txData,
                "codeFormat": txCodeFormat,
                "humanReadable": txHumanReadable,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedSmartContractDeployWithRatio",
            "tx": {
                "typeInt": 42,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txData,
                "codeFormat": txCodeFormat,
                "humanReadable": txHumanReadable,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeSmartContractExecution",
            "tx": {
                "typeInt": 48,
                "from": txFrom,
                "to": txContractAddress,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txContractExecutionData,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedSmartContractExecution",
            "tx": {
                "typeInt": 49,
                "from": txFrom,
                "to": txContractAddress,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txContractExecutionData,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedSmartContractExecutionWithRatio",
            "tx": {
                "typeInt": 50,
                "from": txFrom,
                "to": txContractAddress,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValueZero,
                "input": txContractExecutionData,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeCancel",
            "tx": {"typeInt": 56, "from": txFrom, "gas": txGas, "gasPrice": txGasPrice},
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedCancel",
            "tx": {
                "typeInt": 57,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedCancelWithRatio",
            "tx": {
                "typeInt": 58,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        # To test TxTypeChainDataAnchoring, end point node should accept local anchorTx by `--txpool.allow-local-anchortx` flag.
        {
            "type": "TxTypeChainDataAnchoring",
            "tx": {
                "typeInt": 72,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "input": txMemo,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedChainDataAnchoring",
            "tx": {
                "typeInt": 73,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "input": txMemo,
                "feePayer": txFeePayer,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeFeeDelegatedChainDataAnchoringWithRatio",
            "tx": {
                "typeInt": 74,
                "from": txFrom,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "input": txMemo,
                "feePayer": txFeePayer,
                "feeRatio": txFeeRatio,
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeEthereumDynamicFee",
            "tx": {
                "typeInt": 30722,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "value": txValueOne,
                "maxFeePerGas": txGasPrice,
                "maxPriorityFeePerGas": txGasPrice,
                "accessList": [
                    {
                        "address": txFrom,
                        "storageKeys": [
                            "0x0000000000000000000000000000000000000000000000000000000000000003",
                            "0x0000000000000000000000000000000000000000000000000000000000000007",
                        ],
                    },
                ],
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
        {
            "type": "TxTypeEthereumSetCode",
            "tx": {
                "typeInt": 30724,
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "value": txValueOne,
                "maxFeePerGas": txGasPrice,
                "maxPriorityFeePerGas": txGasPrice,
                "accessList": [],
                "authorizationList": [
                    {
                        "chainId": "0x0",
                        "address": "0x000000000000000000000000000000000000aaaa",
                        "nonce": "0x0",
                        "yParity": "0x1",
                        "r": "0x79eae4cbf85eae84eac1311d7384f4f3bca88078cde0dbf0203248b074b7c36d",
                        "s": "0x8ea1adf9dded4d8223bd6784a6bf711211b381f04a34e9bea39e3ea81213d32",
                    },
                ],
            },
            "result": {"hash": "", "blockHash": "", "blockNumber": "", "index": ""},
        },
    ]
    for tx in txs:
        if "FeeDelegated" in tx["type"]:
            # Sign the transaction as a sender before signing as a fee payer
            method = "kaia_signTransaction"
            params = [tx["tx"]]
            result, error = Utils.call_rpc("", method, params, log_path)
            assert error is None
            tx["tx"]["signatures"] = result["tx"]["signatures"]
            tx["tx"]["nonce"] = result["tx"]["nonce"]

            # After signing the tx as a sender, send tx to the Node as a fee payer
            method = "kaia_sendTransactionAsFeePayer"
            params = [tx["tx"]]
            result, error = Utils.call_rpc("", method, params, log_path)
            assert error is None
            tx["result"]["hash"] = result

        else:
            method = "kaia_sendTransaction"
            params = [tx["tx"]]
            result, error = Utils.call_rpc("", method, params, log_path)
            assert error is None
            tx["result"]["hash"] = result

    Utils.waiting_count("Waiting for", 5, "seconds to transaction is finalized.")

    for tx in txs:
        result, error = kaia_common.get_transaction_receipt(config.get("endpoint"), [tx["result"]["hash"]])
        tx["result"]["blockHash"] = result["blockHash"]
        tx["result"]["blockNumber"] = result["blockNumber"]
        tx["result"]["index"] = result["transactionIndex"]
        tx["result"]["status"] = result["status"]

    test_data_set["txData"] = txs


def prepare():
    """
    Prepare some pre-required jobs to do tests.
    """
    # Import and unlock sender's account
    sender_private_key = test_data_set["account"]["sender"]["privateKey"][2:]
    sender_password = test_data_set["account"]["sender"]["password"]
    personal_common.import_rawkey(config.get("endpoint"), [sender_private_key, sender_password])

    sender = test_data_set["account"]["sender"]["address"]
    duration = 10000000
    personal_common.unlock_account(config.get("endpoint"), [sender, sender_password, duration])

    fee_payer = test_data_set["account"]["feePayer"]["address"]
    # Import and unlock feePayer's account if it is existed in config.json
    if fee_payer != sender:
        fee_payer_private_key = test_data_set["account"]["feePayer"]["privateKey"][2:]
        fee_payer_password = test_data_set["account"]["feePayer"]["password"]
        personal_common.import_rawkey(config.get("endpoint"), [fee_payer_private_key, fee_payer_password])
        personal_common.unlock_account(config.get("endpoint"), [fee_payer, fee_payer_password, duration])

    contracts = test_data_set["contracts"]
    for contract in contracts:
        tx_args = {
            "from": sender,
            "gas": hex(30400000),
            "gasPrice": test_data_set["unitGasPrice"],
            "value": "0x0",
            "data": contracts[contract]["data"],
        }
        transaction_hash, error = kaia_common.send_transaction(config.get("endpoint"), [tx_args])
        assert error is None
        Utils.waiting_count("Waiting for", 5, "seconds to transaction is finalized.")

        receipt, error = kaia_common.get_transaction_receipt(config.get("endpoint"), [transaction_hash])
        assert error is None
        test_data_set["contracts"][contract]["address"][0] = receipt["contractAddress"]


def make_multisig_account():
    method = "kaia_sendRawTransaction"
    params = [
        "0x20f8db808604bab82720008366926694a2a8854b1802d8cd5de631e690817c253d6a9153b86f05f86ca302a103f26489914098c5da51f0f646e3000da4d6197217df082b4f7ce1530f0a0cbf2aa302a10263021199702b9fefca617bdcb2a9ed4a810dfa8d270d4e804a1e778450e63ec3a302a103dc9dccbd788c00fa98f7f4082f2f714e799bc0c29d63f04d48b54fe6250453cdf847f845820fe9a05a718af76dfc82143975058065acb99c4d66bac99c3d226e7dde31d6b954de14a03b17300eb773d4a2a20b71b92eae33f1411dc74bb80e0c2316572345908539e7"
    ]
    result, error = Utils.call_rpc("", method, params, log_path)
    #assert error is None


def inject_test_data_to_testcases():
    """
    Inject prepared test_data_set to each test files.
    Initialization process should works 1 time during whole tests.
    """
    admin_rpc.test_data_set = test_data_set
    admin_ws.test_data_set = test_data_set
    debug_rpc.test_data_set = test_data_set
    debug_ws.test_data_set = test_data_set
    net_rpc.test_data_set = test_data_set
    net_ws.test_data_set = test_data_set
    personal_rpc.test_data_set = test_data_set
    personal_ws.test_data_set = test_data_set
    txpool_rpc.test_data_set = test_data_set
    txpool_ws.test_data_set = test_data_set
    kaia_account_rpc.test_data_set = test_data_set
    kaia_account_ws.test_data_set = test_data_set
    kaia_block_rpc.test_data_set = test_data_set
    kaia_block_ws.test_data_set = test_data_set
    kaia_configuration_rpc.test_data_set = test_data_set
    kaia_configuration_ws.test_data_set = test_data_set
    kaia_miscellaneous_rpc.test_data_set = test_data_set
    kaia_miscellaneous_ws.test_data_set = test_data_set
    kaia_transaction_rpc.test_data_set = test_data_set
    kaia_transaction_ws.test_data_set = test_data_set
    kaia_filter_rpc.test_data_set = test_data_set
    kaia_filter_ws.test_data_set = test_data_set
    eth_account_rpc.test_data_set = test_data_set
    eth_account_ws.test_data_set = test_data_set
    eth_block_rpc.test_data_set = test_data_set
    eth_block_ws.test_data_set = test_data_set
    eth_configuration_rpc.test_data_set = test_data_set
    eth_configuration_ws.test_data_set = test_data_set
    eth_miscellaneous_rpc.test_data_set = test_data_set
    eth_miscellaneous_ws.test_data_set = test_data_set
    eth_transaction_rpc.test_data_set = test_data_set
    eth_transaction_ws.test_data_set = test_data_set
    eth_filter_rpc.test_data_set = test_data_set
    eth_filter_ws.test_data_set = test_data_set
    eth_gas_rpc.test_data_set = test_data_set
    eth_gas_ws.test_data_set = test_data_set
    kaia_gas_rpc.test_data_set = test_data_set
    kaia_gas_ws.test_data_set = test_data_set


def load_test_suites():
    """
    Load all test suites defined in rpc-tester.
    """
    global rpc_test_suites
    global ws_test_suites
    rpc_test_suites = list()
    ws_test_suites = list()

    namespaces = config.get("namespaces", "admin,debug,eth,governance,kaia,net,personal,txpool")
    namespaces = namespaces.split(",")

    if "admin" in namespaces:
        rpc_test_suites.append(TestAdminNamespaceRPC.suite())
        ws_test_suites.append(TestAdminNamespaceWS.suite())

    if "debug" in namespaces:
        rpc_test_suites.append(TestDebugNamespaceRPC.suite())
        ws_test_suites.append(TestDebugNamespaceWS.suite())

    if "net" in namespaces:
        rpc_test_suites.append(TestNetNamespaceRPC.suite())
        ws_test_suites.append(TestNetNamespaceWS.suite())

    if "personal" in namespaces:
        rpc_test_suites.append(TestPersonalNamespaceRPC.suite())
        ws_test_suites.append(TestPersonalNamespaceWS.suite())

    if "txpool" in namespaces:
        rpc_test_suites.append(TestTxpoolNamespaceRPC.suite())
        ws_test_suites.append(TestTxpoolNamespaceWS.suite())

    if "kaia" in namespaces:
        rpc_test_suites.append(TestKaiaNamespaceAccountRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceAccountWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceBlockRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceBlockWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceConfigurationRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceConfigurationWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceMiscellaneousRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceMiscellaneousWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceTransactionRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceTransactionWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceFilterRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceFilterWS.suite())
        rpc_test_suites.append(TestKaiaNamespaceGasRPC.suite())
        ws_test_suites.append(TestKaiaNamespaceGasWS.suite())

    if "eth" in namespaces:
        rpc_test_suites.append(TestEthNamespaceAccountRPC.suite())
        ws_test_suites.append(TestEthNamespaceAccountWS.suite())
        rpc_test_suites.append(TestEthNamespaceBlockRPC.suite())
        ws_test_suites.append(TestEthNamespaceBlockWS.suite())
        rpc_test_suites.append(TestEthNamespaceConfigurationRPC.suite())
        ws_test_suites.append(TestEthNamespaceConfigurationWS.suite())
        rpc_test_suites.append(TestEthNamespaceMiscellaneousRPC.suite())
        ws_test_suites.append(TestEthNamespaceMiscellaneousWS.suite())
        rpc_test_suites.append(TestEthNamespaceTransactionRPC.suite())
        ws_test_suites.append(TestEthNamespaceTransactionWS.suite())
        rpc_test_suites.append(TestEthNamespaceFilterRPC.suite())
        ws_test_suites.append(TestEthNamespaceFilterWS.suite())
        rpc_test_suites.append(TestEthNamespaceGasRPC.suite())
        ws_test_suites.append(TestEthNamespaceGasWS.suite())

def initialize():
    global config
    config = Utils.get_config()
    load_test_data()
    prepare()
    makeTxData()
    inject_test_data_to_testcases()
    make_multisig_account()
    load_test_suites()


if __name__ == "__main__":
    protocol = parse_arguments()

    initialize()
    runner = HTMLTestRunner(
        output="testReport",
        report_title="KaiaTestReport",
        report_name="KaiaTestReport",
        combine_reports=True,
    )

    suites = list()
    if protocol == "rpc":
        suites = rpc_test_suites
    elif protocol == "ws":
        suites = ws_test_suites
    else:
        suites.extend(rpc_test_suites)
        suites.extend(ws_test_suites)

    all_test_suite = unittest.TestSuite(suites)

    result = runner.run(all_test_suite)

    if not result.wasSuccessful():
        exit(1)
