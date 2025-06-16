import unittest

from utils import Utils
from common import eth as eth_common

# test_data_set is injected by rpc-tester/main.py
global test_data_set


class TestEthNamespaceAccountRPC(unittest.TestCase):
    config = Utils.get_config()
    _, _, log_path = Utils.get_log_filename_with_path()
    endpoint = config.get("endpoint")
    rpc_port = config.get("rpcPort")
    ws_port = config.get("wsPort")
    ns = "eth"
    waiting_count = 2

    def test_eth_accounts_success_wrong_value_param(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_accounts"
        _, error = Utils.call_rpc(self.endpoint, method, ["abcd"], self.log_path)
        self.assertIsNone(error)

    def test_eth_accounts_success(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_accounts"
        result, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        self.assertIsNone(error)
        # See the config.json
        self.assertEqual(result, [
            "0xf77e71cf745e14129a344bcfb7e28240a5351beb", # faucetAddress
            "0x4b2c736fd05c2e2da3ccbd001a395a444f16a861" # feePayerAddress
        ])
        self.assertNotIn("0x71562b71999873DB5b286dF957af199Ec94617F7", result) # eoaWithCodeAddress

    def test_eth_getBalance_error_no_param(self):
        method = f"{self.ns}_getBalance"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = []
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getBalance_error_wrong_type_param1(self):
        method = f"{self.ns}_getBalance"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = ["address", tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_eth_getBalance_error_wrong_type_param2(self):
        method = f"{self.ns}_getBalance"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, "tag"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_eth_getBalance_error_wrong_value_param(self):
        method = f"{self.ns}_getBalance"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, "0xffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "HeaderNotExist", error)

    def test_eth_getBalance_success(self):
        method = f"{self.ns}_getBalance"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getTransactionCount_error_no_param(self):
        method = f"{self.ns}_getTransactionCount"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = None
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getTransactionCount_error_wrong_type_param1(self):
        method = f"{self.ns}_getTransactionCount"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = ["address", tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_eth_getTransactionCount_error_wrong_type_param2(self):
        method = f"{self.ns}_getTransactionCount"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, "tag"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_eth_getTransactionCount_error_wrong_value_param(self):
        method = f"{self.ns}_getTransactionCount"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, "0xffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "HeaderNotExist", error)

    def test_eth_getTransactionCount_success(self):
        method = f"{self.ns}_getTransactionCount"
        address = test_data_set["account"]["sender"]["address"]
        tag = "latest"
        params = [address, tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

    def test_eth_getCode_error_no_param(self):
        method = f"{self.ns}_getCode"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_getCode_error_wrong_tag(self):
        method = f"{self.ns}_getCode"
        tag = "latest2"
        address = test_data_set["contracts"]["unknown"]["address"][0]
        params = [address, tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_eth_getCode_error_wrong_type_param1(self):
        method = f"{self.ns}_getCode"
        tag = "latest"
        params = ["contractAddress", tag]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_eth_getCode_error_wrong_type_param2(self):
        method = f"{self.ns}_getCode"
        tag = "latest"
        address = test_data_set["contracts"]["unknown"]["address"][0]
        params = [address, "tag"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexWithoutPrefix", error)

    def test_eth_getCode_error_wrong_value_param(self):
        method = f"{self.ns}_getCode"
        tag = "latest"
        address = test_data_set["contracts"]["unknown"]["address"][0]
        params = [address, "0xffffffff"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "HeaderNotExist", error)

    def test_eth_getCode_success(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_getCode"
        tag = "latest"
        address = test_data_set["account"]["sender"]["address"]
        params = [address, tag]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, "0x")

    def test_eth_getCode_success_eoa_with_code(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_getCode"
        tag = "latest"
        address = test_data_set["account"]["eoaWithCode"]["address"]
        params = [address, tag]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, "0xef0100000000000000000000000000000000000000aaaa") # Expected value for delegation

    def test_eth_getCode_success_sca(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_getCode"
        tag = "latest"
        address = test_data_set["contracts"]["unknown"]["address"][0]
        params = [address, tag]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        self.assertEqual(result, "0x60806040526004361061003b576000357c010000000000000000000000000000000000000000000000000000000090048063b3f98adc14610040575b600080fd5b34801561004c57600080fd5b5061007c6004803603602081101561006357600080fd5b81019080803560ff16906020019092919050505061007e565b005b6000600260003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002090508060010160009054906101000a900460ff16806100e657506003805490508260ff1610155b156100f1575061015e565b60018160010160006101000a81548160ff021916908315150217905550818160010160016101000a81548160ff021916908360ff160217905550806000015460038360ff1681548110151561014257fe5b9060005260206000200160000160008282540192505081905550505b5056fea165627a7a72305820dad6d3e144a160eb6e34d8d99084ed29d207271e201aaac513007f652a26e2200029")

    def test_eth_sign_error_no_param(self):
        method = f"{self.ns}_sign"
        _, error = Utils.call_rpc(self.endpoint, method, [], self.log_path)
        Utils.check_error(self, "arg0NoParams", error)

    def test_eth_sign_error_wrong_type_param1(self):
        method = f"{self.ns}_sign"
        message = Utils.convert_to_hex("Hi Utils!")
        params = ["address", message]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg0HexToAddress", error)

    def test_eth_sign_error_wrong_type_param2(self):
        method = f"{self.ns}_sign"
        message = Utils.convert_to_hex("Hi Utils!")
        address = test_data_set["account"]["sender"]["address"]
        params = [address, "message"]
        _, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        Utils.check_error(self, "arg1HexToBytes", error)

    def test_eth_sign_success(self):
        block_number = eth_common.get_block_number(self.endpoint)
        self.assertIsNotNone(block_number)

        method = f"{self.ns}_sign"
        message = Utils.convert_to_hex("Hi Utils!")
        address = test_data_set["account"]["sender"]["address"]
        params = [address, message]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)

        signature = result

        method = "personal_ecRecover"
        message = Utils.convert_to_hex("Hi Utils!")
        params = [message, signature]
        result, error = Utils.call_rpc(self.endpoint, method, params, self.log_path)
        self.assertIsNone(error)
        validAddress = result

        self.assertEqual(address.lower(), validAddress.lower())

    @staticmethod
    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_accounts_success_wrong_value_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_accounts_success"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getBalance_error_no_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getBalance_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getBalance_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getBalance_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getBalance_success"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getTransactionCount_error_no_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getTransactionCount_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getTransactionCount_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getTransactionCount_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getTransactionCount_success"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_error_no_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_error_wrong_tag"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_error_wrong_value_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_success"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_success_eoa_with_code"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_getCode_success_sca"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_sign_error_no_param"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_sign_error_wrong_type_param1"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_sign_error_wrong_type_param2"))
        suite.addTest(TestEthNamespaceAccountRPC("test_eth_sign_success"))

        return suite
