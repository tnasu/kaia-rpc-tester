import unittest
import random
from utils import Utils
from common import eth as eth_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceTransactionRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_sendTransaction_error_no_param1(self):
        method = f"{self.ns}_sendTransaction"
        params = None
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_sendTransaction_error_no_param2(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_eth_sendTransaction_error_no_param3(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"gasPrice": txGasPrice, "value": txValue}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ContractCreationWithoutData", error)

    def test_eth_sendTransaction_error_no_param4(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"to": txTo, "gas": txGas, "gasPrice": txGasPrice, "value": txValue}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "UnknownAccount", error)

    def test_eth_sendTransaction_success_no_param1(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom, "to": txTo}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendTransaction_success_no_param2(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendTransaction_success_no_param3(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas, "gasPrice": txGasPrice}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendTransaction_success_no_param4(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom, "to": txTo, "value": txValue}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendTransaction_success_no_param5(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [{"from": txFrom, "to": txTo, "gas": txGas, "value": txValue}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendTransaction_error_wrong_type_param1(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": 1234,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsFromAddress", error) # Error messages in the data structure part are differen

    def test_eth_sendTransaction_error_wrong_type_param2(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsToAddress", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_type_param3(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": 1234,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsGasUint", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_type_param4(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": 1234,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsGaspriceBig", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_type_param5(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": 1234,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsValueBig", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_value_param1(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom + "1",
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsFromAddress", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_value_param2(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo + "1",
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsToAddress", error) # Error messages in the data structure part are different

    def test_eth_sendTransaction_error_wrong_value_param3(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasTooLow", error)

    def test_eth_sendTransaction_error_wrong_value_param4(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = hex(25)
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InvalidGasPrice", error)

    def test_eth_sendTransaction_error_wrong_value_param5(self):
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [txFrom, "latest"]
        result, error = Utils.call_rpc(self.endpoint, f"{self.ns}_getBalance", params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_sendTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": result,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InsufficientFundsFrom", error)

    def test_eth_sendTransaction_success(self):
        method = f"{self.ns}_sendTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(Utils.to_kei(1.5))

        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_fillTransaction_error_no_param(self):
        method = f"{self.ns}_fillTransaction"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_fillTransaction_success(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_fillTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_signTransaction_error_no_param1(self):
        method = f"{self.ns}_signTransaction"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_signTransaction_error_no_param2(self):
        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [
            {
                "from": txFrom,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasNotSpecified", error)

    def test_eth_signTransaction_error_no_param3(self):
        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [
            {
                "to": txTo,
                "value": txValue,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasNotSpecified", error)

    def test_eth_signTransaction_error_no_param4(self):
        method = f"{self.ns}_signTransaction"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [{"from": txFrom, "to": txTo}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasNotSpecified", error)

    def test_eth_signTransaction_error_wrong_type_param1(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": 1234,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsFromAddress", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_type_param2(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsToAddress", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_type_param3(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": "txGas",
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsGasUint", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_type_param4(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": "txGasPrice",
                "value": txValue,
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsGaspriceBig", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_type_param5(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": "txValue",
                "nonce": nonce,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsValueBig", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_type_param6(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": "nonce",
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsNonceUint", error) # Error messages in the data structure part are different

    def test_eth_signTransaction_error_wrong_value_param(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        # Tx with Envelop
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
                "typeInt": 30800,
            }
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "UndefinedTxType", error)

    def test_eth_signTransaction_success(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result["tx"]["gasPrice"], txGasPrice)

    def test_eth_createAccessList_success(self):
        method = f"{self.ns}_createAccessList"
        txFrom = test_data_set["account"]["sender"]["address"]
        txTo = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        params = {
            "from": txFrom,
            "to": txTo,
            "data": code,
        }

        result, error = Utils.call_rpc(self.endpoint, method, [params], self.log_path)
        self.assertIsNone(error)
        self.assertIsNotNone(result)
        self.assertEqual(len(result["accessList"]), 1)
        self.assertEqual(result["accessList"][0]["address"], txTo)
        self.assertEqual(len(result["accessList"][0]["storageKeys"]), 2)
        self.assertEqual(result["gasUsed"], '0x5551')

    def test_eth_sendRawTransaction_error_no_param(self):
        method = f"{self.ns}_sendRawTransaction"
        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_sendRawTransaction_error_wrong_type_param(self):
        method = f"{self.ns}_sendRawTransaction"
        params = ["abcd"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToBytes", error)

    def test_eth_sendRawTransaction_success(self):
        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]
        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441406250)

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_signTransaction"
        params = [
            {
                "from": txFrom,
                "to": txTo,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "nonce": nonce,
            }
        ]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        method = f"{self.ns}_sendRawTransaction"
        params = [rawData]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendRawTransaction_AccessList_error_wrong_prefix(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "gasPrice": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30721,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        rawTxWithoutHexPrefix = rawData[4:]

        testSize = 300
        for i in range(0, testSize):
            randomPrefix = hex(random.randint(3, 256))
            if len(randomPrefix) % 2 == 1:
                randomPrefix = f"0x0{randomPrefix[2:]}"
            rawTx = randomPrefix + rawTxWithoutHexPrefix
            method = f"{self.ns}_sendRawTransaction"
            params = [rawTx]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNotNone(error)
            self.assertTrue("undefined tx type" in error["message"] or "rlp:" in error["message"])

    def test_eth_sendRawTransaction_AccessList_success(self):
        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "gasPrice": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30721,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_sendRawTransaction"
        rawData = result["raw"]
        params = [rawData]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendRawTransaction_DynamicFee_error_wrong_prefix(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30722,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        rawTxWithoutHexPrefix = rawData[4:]

        testSize = 300
        for i in range(0, testSize):
            randomPrefix = hex(random.randint(3, 256))
            if len(randomPrefix) % 2 == 1:
                randomPrefix = f"0x0{randomPrefix[2:]}"
            rawTx = randomPrefix + rawTxWithoutHexPrefix
            method = f"{self.ns}_sendRawTransaction"
            params = [rawTx]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNotNone(error)
            self.assertTrue("undefined tx type" in error["message"] or "rlp:" in error["message"])

    def test_eth_sendRawTransaction_DynamicFee_success(self):
        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        storageKeys = [
            "0x0000000000000000000000000000000000000000000000000000000000000003",
            "0x0000000000000000000000000000000000000000000000000000000000000007",
        ]
        accessList = [{"address": txFrom, "storageKeys": storageKeys}]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "typeInt": 30722,
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        method = f"{self.ns}_sendRawTransaction"
        params = [rawData]
        txHash, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_sendRawTransaction_SetCode_error_wrong_prefix(self):
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        accessList = []
        authrizetions = [{
                        "chainId": "0x0",
                        "address": "0x000000000000000000000000000000000000aaaa",
                        "nonce": "0x0",
                        "yParity": "0x1",
                        "r": "0x79eae4cbf85eae84eac1311d7384f4f3bca88078cde0dbf0203248b074b7c36d",
                        "s": "0x8ea1adf9dded4d8223bd6784a6bf711211b381f04a34e9bea39e3ea81213d32",
        },]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "authorizationList": authrizetions,
            "typeInt": 30724, # SetCodeTxType
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        rawTxWithoutHexPrefix = rawData[6:]

        testSize = 300
        for i in range(0, testSize):
            randomPrefix = hex(random.randint(81, 30720))
            if len(randomPrefix) % 2 == 1:
                randomPrefix = f"0x0{randomPrefix[2:]}"
            rawTx = randomPrefix + rawTxWithoutHexPrefix
            method = f"{self.ns}_sendRawTransaction"
            params = [rawTx]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNotNone(error)
            self.assertTrue("undefined tx type" in error["message"] or "rlp:" in error["message"])

    def test_eth_sendRawTransaction_SetCode_success(self):
        Utils.waiting_count("Waiting for", 5, "seconds until writing a block.")
        method = f"{self.ns}_getTransactionCount"
        tag = "latest"
        txFrom = test_data_set["account"]["sender"]["address"]

        params = [txFrom, tag]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        method = f"{self.ns}_chainId"
        params = []
        chainId, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        password = test_data_set["account"]["sender"]["password"]
        txTo = test_data_set["account"]["sender"]["address"]
        txGas = hex(60400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(2441)
        accessList = []
        authrizetions = [{
                        "chainId": "0x0",
                        "address": "0x000000000000000000000000000000000000aaaa",
                        "nonce": "0x0",
                        "yParity": "0x1",
                        "r": "0x79eae4cbf85eae84eac1311d7384f4f3bca88078cde0dbf0203248b074b7c36d",
                        "s": "0x8ea1adf9dded4d8223bd6784a6bf711211b381f04a34e9bea39e3ea81213d32",
        },]
        transaction = {
            "from": txFrom,
            "to": txTo,
            "gas": txGas,
            "maxPriorityFeePerGas": txGasPrice,
            "maxFeePerGas": txGasPrice,
            "value": txValue,
            "nonce": nonce,
            "accessList": accessList,
            "chainId": chainId,
            "authorizationList": authrizetions,
            "typeInt": 30724, # SetCodeTxType
        }

        method = f"{self.ns}_signTransaction"
        params = [transaction]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        rawData = result["raw"]
        method = f"{self.ns}_sendRawTransaction"
        params = [rawData]
        txHash, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getTransactionByBlockHashAndIndex_error_no_param(self):
        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = []
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)
        self.assertIsNone(nonce)

    def test_eth_getTransactionByBlockHashAndIndex_error_wrong_type_param(self):
        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = ["txhash", "0x0"]
        nonce, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)
        self.assertIsNone(nonce)

    def test_eth_getTransactionByBlockHashAndIndex_error_wrong_value_param(self):
        method = f"{self.ns}_getTransactionByBlockHashAndIndex"

        params = [
            "0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
            "0x0",
        ]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "BlockNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getTransactionByBlockHashAndIndex_success(self):
        method = f"{self.ns}_getTransactionByBlockHashAndIndex"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["blockHash"], tx["result"]["index"]]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            eth_common.checkGasPriceField(self, result)
            eth_common.checkAuthorizationListField(self, result)

    def test_eth_getTransactionByBlockNumberAndIndex_error_no_param(self):
        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)
        self.assertIsNone(result)

    def test_eth_getTransactionByBlockNumberAndIndex_error_wrong_value_param(self):
        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        params = ["0xffffffff", "0x0"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        # Utils.check_error(self, "BlockNotExist", error)
        self.assertIsNone(result)
        self.assertIsNone(error)

    def test_eth_getTransactionByBlockNumberAndIndex_success(self):
        method = f"{self.ns}_getTransactionByBlockNumberAndIndex"

        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["blockNumber"], tx["result"]["index"]]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            eth_common.checkGasPriceField(self, result)
            eth_common.checkAuthorizationListField(self, result)

    def test_eth_getRawTransactionByBlockNumberAndIndex_error_no_param(self):
        method = f"{self.ns}_getRawTransactionByBlockNumberAndIndex"

        params = []
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)
        self.assertIsNone(result)

    def test_eth_getRawTransactionByBlockNumberAndIndex_success(self):
        method = f"{self.ns}_getRawTransactionByBlockNumberAndIndex"

        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["blockNumber"], tx["result"]["index"]]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            eth_common.checkGasPriceField(self, result)
            eth_common.checkAuthorizationListField(self, result)

    def test_eth_getRawTransactionByBlockNumberAndIndex_success_empty_slice_result(self):
        method = f"{self.ns}_getRawTransactionByBlockNumberAndIndex"

        params = ["0xffffffff", "0x0"]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        # The empty slice marshals as "0x" and no error even if the transaction does not exist
        # https://github.com/kaiachain/kaia/blob/91b2f0bbfbfbd63732f54dc66944ef099a5ea10c/common/hexutil/json.go#L44-L54
        self.assertEqual(result, "0x")
        self.assertIsNone(error)

    def test_eth_getTransactionReceipt_error_no_param(self):
        method = f"{self.ns}_getTransactionReceipt"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getTransactionReceipt_error_wrong_type_param(self):
        method = f"{self.ns}_getTransactionReceipt"
        params = ["abcd"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToHash", error)

    def test_eth_getTransactionReceipt_success_wrong_value_param(self):
        method = f"{self.ns}_getTransactionReceipt"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getTransactionReceipt_success(self):
        method = f"{self.ns}_getTransactionReceipt"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["hash"]]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            self.assertIsNotNone(result["effectiveGasPrice"])
            eth_common.checkGasPriceField(self, result)
            eth_common.checkAuthorizationListField(self, result)

    def test_eth_getTransactionByHash_error_no_param(self):
        method = f"{self.ns}_getTransactionByHash"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getTransactionByHash_error_wrong_type_param(self):
        method = f"{self.ns}_getTransactionByHash"
        params = [1234]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToHash", error)

    def test_eth_getTransactionByHash_success_wrong_value_param(self):
        method = f"{self.ns}_getTransactionByHash"
        params = ["0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getTransactionByHash_success(self):
        method = f"{self.ns}_getTransactionByHash"
        txData = test_data_set["txData"]
        for tx in txData:
            params = [tx["result"]["hash"]]
            result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
            self.assertIsNone(error)
            self.assertIsNotNone(result)
            eth_common.checkGasPriceField(self, result)
            eth_common.checkAuthorizationListField(self, result)

    def test_eth_pendingTransactions_success(self):
        method = f"{self.ns}_pendingTransactions"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_call_error_no_param1(self):
        method = f"{self.ns}_call"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_call_error_no_param2(self):
        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        params = [{"to": contract}, "latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_eth_call_error_no_param3(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"data": code}, "latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "VMErrorOccurs", error)

    def test_eth_call_error_wrong_type_param1(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": 1234,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsFromAddress", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param2(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": 1234,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsToAddress", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param3(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": "txGas",
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsGasUint", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param4(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": "txGasPrice",
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsGaspriceBig", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param5(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": "txValue",
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsValueBig", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param6(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": 1234,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NonstringToEthTransactionArgsDataBytes", error) # Error messages in the data structure part are different

    def test_eth_call_error_wrong_type_param7(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "abcd",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_eth_call_error_wrong_value_param1(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(100000000000000000000000000000000000000000)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_eth_call_error_evm_revert_message(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        ownerContract = test_data_set["contracts"]["unknown"]["address"][0]
        notOwner = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        changeOwnerAbi = "0xa6f9dae10000000000000000000000003e2ac308cd78ac2fe162f9522deb2b56d9da9499"
        params = [
            {"from": notOwner, "to": ownerContract, "data": changeOwnerAbi},
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_eth_call_error_intrinsic_gas(self):
        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x99",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasTooLow", error)

    def test_eth_call_success1(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [{"to": contract, "data": code}, "latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_call_success2(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [{"from": address, "to": contract, "data": code}, "latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_call_success3(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_call_success4(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_call_success_insufficient_balance_sender(self):
        method = f"{self.ns}_call"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGasPrice = test_data_set["unitGasPrice"]
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x99999",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        #Utils.check_error(self, "InsufficientBalanceFeePayer", error) # Call doesn't depend on the balance of the sender
        self.assertIsNone(error)
        self.assertIsNotNone(result)

    def test_eth_call_success_state_override_balance_and_code(self):
        method = f"{self.ns}_call"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        # Although the balance was insufficient, stateOverrides is overwritten as if the balance were large, so that the call can be performed normally.
        stateOverrides = {address: {"balance": hex(int(txGas, base=16) * int(txGasPrice, base=16))}}
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
            stateOverrides,
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_estimateGas_error_no_param(self):
        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_estimateGas_error_wrong_type_param1(self):
        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = "abcd"
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToEthTransactionArgsToAddressWithoutPrefix", error) # Error messages in the data structure part are different

    def test_eth_estimateGas_error_wrong_type_param2(self):
        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = "abcd"
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0StringToEthTransactionArgsDataBytes", error) # Error messages in the data structure part are different

    def test_eth_estimateGas_error_insufficient_balance(self):
        method = f"{self.ns}_estimateGas"
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        txValue = hex(1)
        params = [
            {
                "from": zeroBalanceAddr,
                "to": zeroBalanceAddr,
                "value": txValue,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InsufficientBalance", error)

    def test_eth_estimateGas_error_insufficient_funds(self):
        method = f"{self.ns}_estimateGas"
        zeroBalanceAddr = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": zeroBalanceAddr,
                "to": contract,
                "data": code,
                "gas": "0x999",
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "InsufficientFunds", error)

    def test_eth_estimateGas_error_exceeds_allowance(self):
        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["1pebHolder"]["address"]
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": address,
                "value": txValue,
                "gasPrice": txGasPrice,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "GasRequiredExceedsAllowance", error)

    def test_eth_estimateGas_error_evm_revert_message(self):
        method = f"{self.ns}_estimateGas"
        ownerContract = test_data_set["contracts"]["unknown"]["address"][0]
        notOwner = "0x15318f21f3dee6b2c64d2a633cb8c1194877c882"
        changeOwnerAbi = "0xa6f9dae10000000000000000000000003e2ac308cd78ac2fe162f9522deb2b56d9da9499" # changeOwner("0x3e2ac308cd78ac2fe162f9522deb2b56d9da9499")
        params = [
            {"from": notOwner, "to": ownerContract, "data": changeOwnerAbi},
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_eth_estimateGas_error_revert(self):
        method = f"{self.ns}_estimateGas"
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        params = [{"to": contract}, "latest"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "ExecutionReverted", error)

    def test_eth_estimateGas_success(self):
        method = f"{self.ns}_estimateGas"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [{"from": address, "to": contract, "value": txValue, "data": code}]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_estimateComputationCost_success(self):
        method = f"{self.ns}_estimateComputationCost"
        address = test_data_set["account"]["sender"]["address"]
        contract = test_data_set["contracts"]["unknown"]["address"][0]
        code = test_data_set["contracts"]["unknown"]["input"]
        txGas = hex(30400)
        txGasPrice = test_data_set["unitGasPrice"]
        txValue = hex(0)
        params = [
            {
                "from": address,
                "to": contract,
                "gas": txGas,
                "gasPrice": txGasPrice,
                "value": txValue,
                "data": code,
            },
            "latest",
        ]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)


    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_no_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_no_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_no_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_no_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success_no_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success_no_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success_no_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success_no_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success_no_param5"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_type_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_type_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_type_param5"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_value_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_value_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_value_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_value_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_error_wrong_value_param5"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendTransaction_success"))

        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_fillTransaction_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_fillTransaction_success"))

        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_no_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_no_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_no_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_no_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param5"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_type_param6"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_signTransaction_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_createAccessList_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_AccessList_error_wrong_prefix"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_AccessList_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_DynamicFee_error_wrong_prefix"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_DynamicFee_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_SetCode_error_wrong_prefix"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_sendRawTransaction_SetCode_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockHashAndIndex_error_no_param"))
        suite.addTest(
            TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockHashAndIndex_error_wrong_type_param")
        )
        suite.addTest(
            TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockHashAndIndex_error_wrong_value_param")
        )
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockHashAndIndex_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockNumberAndIndex_error_no_param"))
        suite.addTest(
            TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockNumberAndIndex_error_wrong_value_param")
        )
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByBlockNumberAndIndex_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByHash_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByHash_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByHash_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionByHash_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getRawTransactionByBlockNumberAndIndex_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getRawTransactionByBlockNumberAndIndex_success"))
        suite.addTest(
            TestEthNamespaceTransactionRPC("test_eth_getRawTransactionByBlockNumberAndIndex_success_empty_slice_result")
        )
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionReceipt_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionReceipt_error_wrong_type_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionReceipt_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_getTransactionReceipt_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_pendingTransactions_success"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_no_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_no_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_no_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param5"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param6"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_type_param7"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_wrong_value_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_evm_revert_message"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_error_intrinsic_gas"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success3"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success4"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success_insufficient_balance_sender"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_call_success_state_override_balance_and_code"))
        
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_no_param"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_insufficient_balance"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_insufficient_funds"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_exceeds_allowance"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_evm_revert_message"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_error_revert"))
        suite.addTest(TestEthNamespaceTransactionRPC("test_eth_estimateGas_success"))














        return suite
