import datetime
import unittest

from stellar_model.model.horizon.transaction import Transaction
from tests.model.horizon import load_horizon_file


class TestTransaction(unittest.TestCase):
    def test_transaction_valid(self):
        raw_data = load_horizon_file("transaction.json")
        parsed_data = Transaction.model_validate(raw_data)
        self.assertEqual(
            parsed_data.id,
            "5ebd5c0af4385500b53dd63b0ef5f6e8feef1a7e1c86989be3cdcce825f3c0cc",
        )
        self.assertEqual(parsed_data.paging_token, "120103542047408128")
        self.assertEqual(parsed_data.successful, True)
        self.assertEqual(
            parsed_data.hash,
            "5ebd5c0af4385500b53dd63b0ef5f6e8feef1a7e1c86989be3cdcce825f3c0cc",
        )
        self.assertEqual(parsed_data.ledger, 27963785)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2020, 1, 28, 10, 3, 33, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.source_account,
            "GDI5EK4HNMBHJJQGP3GUXQJIIOHU2CJO3LABPWD6WYSPJZP5NP67TMNN",
        )
        self.assertEqual(parsed_data.source_account_sequence, 65046128646685383)
        self.assertEqual(
            parsed_data.fee_account,
            "GDI5EK4HNMBHJJQGP3GUXQJIIOHU2CJO3LABPWD6WYSPJZP5NP67TMNN",
        )
        self.assertEqual(parsed_data.fee_charged, 100)
        self.assertEqual(parsed_data.max_fee, 100)
        self.assertEqual(parsed_data.operation_count, 1)
        self.assertEqual(
            parsed_data.envelope_xdr,
            "AAAAANHSK4drAnSmBn7NS8EoQ49NCS7awBfYfrYk9OX9a/35AAAAZADnFxwAAALHAAAAAAAAAAAAAAABAAAAAQAAAADR0iuHawJ0pgZ+zUvBKEOPTQku2sAX2H62JPTl/Wv9+QAAAAEAAAAA+qpaPAsU/CGcSeS4KnvqE9y+Bcjhyr1l6jiwixRsvu8AAAABTkdOVAAAAAAs4YIuYne69wMuNtfiZ64gb7E3qnTR7A4yD4jZDSS8AQAAAdGpSiAAAAAAAAAAAAH9a/35AAAAQM5LSBiFRQKtFYRPpNabwVuvIhZSVRDaajf0KzYaqJmgaXAlFaTOYyYc11YuxUM1Fzl1VT4UEbI22BvO/8HzUgQ=",
        )
        self.assertEqual(
            parsed_data.result_xdr, "AAAAAAAAAGQAAAAAAAAAAQAAAAAAAAABAAAAAAAAAAA="
        )
        self.assertEqual(
            parsed_data.result_meta_xdr,
            "AAAAAgAAAAIAAAADAaqxiQAAAAAAAAAA0dIrh2sCdKYGfs1LwShDj00JLtrAF9h+tiT05f1r/fkAAAAAAhWQlADnFxwAAALGAAAAAQAAAAEAAAAAhD8BLsZFQEF33rKS6YopQUT3b6iLBG4nspe68/DBNBYAAAAAAAAAAAEAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBqrGJAAAAAAAAAADR0iuHawJ0pgZ+zUvBKEOPTQku2sAX2H62JPTl/Wv9+QAAAAACFZCUAOcXHAAAAscAAAABAAAAAQAAAACEPwEuxkVAQXfespLpiilBRPdvqIsEbieyl7rz8ME0FgAAAAAAAAAAAQAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAQAAAADAan62gAAAAEAAAAA+qpaPAsU/CGcSeS4KnvqE9y+Bcjhyr1l6jiwixRsvu8AAAABTkdOVAAAAAAs4YIuYne69wMuNtfiZ64gb7E3qnTR7A4yD4jZDSS8AQAAAAAAAAALf/////////8AAAABAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEBqrGJAAAAAQAAAAD6qlo8CxT8IZxJ5Lgqe+oT3L4FyOHKvWXqOLCLFGy+7wAAAAFOR05UAAAAACzhgi5id7r3Ay421+JnriBvsTeqdNHsDjIPiNkNJLwBAAAB0alKIAt//////////wAAAAEAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwGp+6EAAAABAAAAANHSK4drAnSmBn7NS8EoQ49NCS7awBfYfrYk9OX9a/35AAAAAU5HTlQAAAAALOGCLmJ3uvcDLjbX4meuIG+xN6p00ewOMg+I2Q0kvAEAAAkQQwRXzX//////////AAAAAQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAaqxiQAAAAEAAAAA0dIrh2sCdKYGfs1LwShDj00JLtrAF9h+tiT05f1r/fkAAAABTkdOVAAAAAAs4YIuYne69wMuNtfiZ64gb7E3qnTR7A4yD4jZDSS8AQAABz6ZujfNf/////////8AAAABAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        )
        self.assertEqual(
            parsed_data.fee_meta_xdr,
            "AAAAAgAAAAMBqfuhAAAAAAAAAADR0iuHawJ0pgZ+zUvBKEOPTQku2sAX2H62JPTl/Wv9+QAAAAACFZD4AOcXHAAAAsYAAAABAAAAAQAAAACEPwEuxkVAQXfespLpiilBRPdvqIsEbieyl7rz8ME0FgAAAAAAAAAAAQAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGqsYkAAAAAAAAAANHSK4drAnSmBn7NS8EoQ49NCS7awBfYfrYk9OX9a/35AAAAAAIVkJQA5xccAAACxgAAAAEAAAABAAAAAIQ/AS7GRUBBd96ykumKKUFE92+oiwRuJ7KXuvPwwTQWAAAAAAAAAAABAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=",
        )
        self.assertEqual(parsed_data.memo_type, "none")
        self.assertEqual(parsed_data.memo_bytes, None)
        self.assertEqual(parsed_data.memo, None)
        self.assertEqual(len(parsed_data.signatures), 1)
        self.assertEqual(
            parsed_data.signatures[0],
            "zktIGIVFAq0VhE+k1pvBW68iFlJVENpqN/QrNhqomaBpcCUVpM5jJhzXVi7FQzUXOXVVPhQRsjbYG87/wfNSBA==",
        )
        self.assertEqual(
            parsed_data.valid_after,
            datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.valid_before,
            datetime.datetime(2022, 5, 6, 5, 29, 45, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.preconditions.timebounds.min_time,
            datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.preconditions.timebounds.max_time,
            datetime.datetime(2022, 5, 6, 5, 29, 45, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.preconditions.ledgerbounds.min_ledger, 1)
        self.assertEqual(parsed_data.preconditions.ledgerbounds.max_ledger, 10000)
        self.assertEqual(parsed_data.preconditions.min_account_sequence, 123)
        self.assertEqual(parsed_data.preconditions.min_account_sequence_age, 300)
        self.assertEqual(parsed_data.preconditions.min_account_sequence_ledger_gap, 120)
        self.assertEqual(len(parsed_data.preconditions.extra_signers), 2)
        self.assertEqual(
            parsed_data.preconditions.extra_signers[0],
            "GCT4SSY2KZLMKE4SNX4CHNBDFU5RBEDQV3AZG3XDGP6X2ASNAONW5OVR",
        )
        self.assertEqual(
            parsed_data.preconditions.extra_signers[1],
            "PAJFT5XMURWA3ZYIWGVB7YLKTIZQVJDPIC44XMVYCF4TV6QGISUWEAAAAACXIZLTOQYQAAAA2JNQ",
        )
        self.assertEqual(parsed_data.fee_bump_transaction, None)
        self.assertEqual(parsed_data.inner_transaction, None)
        self.assertEqual(parsed_data.account_muxed, None)
        self.assertEqual(parsed_data.account_muxed_id, None)
        self.assertEqual(parsed_data.fee_account_muxed, None)
        self.assertEqual(parsed_data.fee_account_muxed_id, None)

    def test_transaction_fee_bump_valid(self):
        raw_data = load_horizon_file("transaction_fee_bump.json")
        parsed_data = Transaction.model_validate(raw_data)
        self.assertEqual(
            parsed_data.id,
            "ac8cf91a1c0559091ba26573c0966191ae81466d5df4931af302f135d99c0d72",
        )
        self.assertEqual(parsed_data.paging_token, "2661015707721728")
        self.assertEqual(parsed_data.successful, True)
        self.assertEqual(
            parsed_data.hash,
            "ac8cf91a1c0559091ba26573c0966191ae81466d5df4931af302f135d99c0d72",
        )
        self.assertEqual(parsed_data.ledger, 619566)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 1, 53, 2, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.source_account,
            "GBZXN7PIRZGNMHGA7MUUUF4GWPY5AYPV6LY4UV2GL6VJGIQRXFDNMADI",
        )
        self.assertEqual(parsed_data.source_account_sequence, 2660813844250626)
        self.assertEqual(
            parsed_data.fee_account,
            "GBB2UWEFNJIKGYBIOJ3BFTNLJFLTXQ6WGCI2XMS7E5USPD2OSNI5WITS",
        )
        self.assertEqual(parsed_data.fee_charged, 200)
        self.assertEqual(parsed_data.max_fee, 400)
        self.assertEqual(parsed_data.operation_count, 1)
        self.assertEqual(
            parsed_data.envelope_xdr,
            "AAAABQAAAABDqliFalCjYChydhLNq0lXO8PWMJGrsl8naSePTpNR2wAAAAAAAAGQAAAAAgAAAABzdv3ojkzWHMD7KUoXhrPx0GH18vHKV0ZfqpMiEblG1gAAADIACXP/AAAAAgAAAAEAAAAAYIN5+QAAAABgg3sgAAAAAQAAAA9IZWxsbywgU3RlbGxhciEAAAAAAQAAAAAAAAABAAAAAGqka26GRAaOmdSR+9P28gWFYn/iQ3GPQsRGAuT5bF4JAAAAAAAAAAA7msoAAAAAAAAAAAERuUbWAAAAQFj+NkGTRSlLcPXcwkH8VOBN3rk+B09f1Xx57nqdHb/1tNyaDnm2seYnx9BRVD8LhgdD46aTdcF3qUkNGm0PSQkAAAAAAAAAAU6TUdsAAABAKbfbHT6jbk7gCOyyKZ+cyGQPnNoTAHy3lZgGqbrPkNWE8ekJSnicNScamUQYzngXkyd2ekTdmQxTaPkEHleTBQ==",
        )
        self.assertEqual(
            parsed_data.result_xdr,
            "AAAAAAAAAMgAAAABk+eiw4WhAiOttZ1mTY+zfrXh1B+wx+3B5aR+sYKR7REAAAAAAAAAMgAAAAAAAAABAAAAAAAAAAEAAAAAAAAAAAAAAAA=",
        )
        self.assertEqual(
            parsed_data.result_meta_xdr,
            "AAAAAgAAAAQAAAADAAl0LgAAAAAAAAAAQ6pYhWpQo2AocnYSzatJVzvD1jCRq7JfJ2knj06TUdsAAAAXSHbmcAAJc/0AAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAABAAl0LgAAAAAAAAAAQ6pYhWpQo2AocnYSzatJVzvD1jCRq7JfJ2knj06TUdsAAAAXSHbmcAAJc/0AAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAADAAl0EQAAAAAAAAAAc3b96I5M1hzA+ylKF4az8dBh9fLxyldGX6qTIhG5RtYAAAAXDNweAAAJc/8AAAABAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAABAAl0LgAAAAAAAAAAc3b96I5M1hzA+ylKF4az8dBh9fLxyldGX6qTIhG5RtYAAAAXDNweAAAJc/8AAAACAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAABAAAABAAAAAMACXQRAAAAAAAAAABqpGtuhkQGjpnUkfvT9vIFhWJ/4kNxj0LERgLk+WxeCQAAABeEEbIAAAl0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAEACXQuAAAAAAAAAABqpGtuhkQGjpnUkfvT9vIFhWJ/4kNxj0LERgLk+WxeCQAAABe/rHwAAAl0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAMACXQuAAAAAAAAAABzdv3ojkzWHMD7KUoXhrPx0GH18vHKV0ZfqpMiEblG1gAAABcM3B4AAAlz/wAAAAIAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAEACXQuAAAAAAAAAABzdv3ojkzWHMD7KUoXhrPx0GH18vHKV0ZfqpMiEblG1gAAABbRQVQAAAlz/wAAAAIAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAA=",
        )
        self.assertEqual(
            parsed_data.fee_meta_xdr,
            "AAAAAgAAAAMACXQRAAAAAAAAAABDqliFalCjYChydhLNq0lXO8PWMJGrsl8naSePTpNR2wAAABdIduc4AAlz/QAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAEACXQuAAAAAAAAAABDqliFalCjYChydhLNq0lXO8PWMJGrsl8naSePTpNR2wAAABdIduZwAAlz/QAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAA==",
        )
        self.assertEqual(parsed_data.memo_type, "text")
        self.assertEqual(parsed_data.memo_bytes, b"Hello, Stellar!")
        self.assertEqual(parsed_data.memo, "Hello, Stellar!")
        self.assertEqual(len(parsed_data.signatures), 1)
        self.assertEqual(
            parsed_data.signatures[0],
            "KbfbHT6jbk7gCOyyKZ+cyGQPnNoTAHy3lZgGqbrPkNWE8ekJSnicNScamUQYzngXkyd2ekTdmQxTaPkEHleTBQ==",
        )
        self.assertEqual(
            parsed_data.valid_after,
            datetime.datetime(2021, 4, 24, 1, 52, 57, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.valid_before,
            datetime.datetime(2021, 4, 24, 1, 57, 52, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.fee_bump_transaction.hash,
            "ac8cf91a1c0559091ba26573c0966191ae81466d5df4931af302f135d99c0d72",
        )
        self.assertEqual(len(parsed_data.fee_bump_transaction.signatures), 1)
        self.assertEqual(
            parsed_data.fee_bump_transaction.signatures[0],
            "KbfbHT6jbk7gCOyyKZ+cyGQPnNoTAHy3lZgGqbrPkNWE8ekJSnicNScamUQYzngXkyd2ekTdmQxTaPkEHleTBQ==",
        )
        self.assertEqual(
            parsed_data.inner_transaction.hash,
            "93e7a2c385a10223adb59d664d8fb37eb5e1d41fb0c7edc1e5a47eb18291ed11",
        )
        self.assertEqual(parsed_data.inner_transaction.max_fee, 50)
        self.assertEqual(len(parsed_data.inner_transaction.signatures), 1)
        self.assertEqual(
            parsed_data.inner_transaction.signatures[0],
            "WP42QZNFKUtw9dzCQfxU4E3euT4HT1/VfHnuep0dv/W03JoOebax5ifH0FFUPwuGB0PjppN1wXepSQ0abQ9JCQ==",
        )
        self.assertEqual(parsed_data.account_muxed, None)
        self.assertEqual(parsed_data.account_muxed_id, None)
        self.assertEqual(parsed_data.fee_account_muxed, None)
        self.assertEqual(parsed_data.fee_account_muxed_id, None)

    def test_transaction_muxed_account_valid(self):
        raw_data = load_horizon_file("transaction_muxed_account.json")
        parsed_data = Transaction.model_validate(raw_data)
        self.assertEqual(
            parsed_data.account_muxed,
            "MDSPXRRA5D4WD4LCR6NNZEHQJHHZ74UCPHXJT4SC7HCFWJFOFOLUUAAAAAAAAAAAPMRCO",
        )
        self.assertEqual(parsed_data.account_muxed_id, 123)
        self.assertEqual(
            parsed_data.fee_account_muxed,
            "MDSPXRRA5D4WD4LCR6NNZEHQJHHZ74UCPHXJT4SC7HCFWJFOFOLUUAAAAAAAAAAAPMRCO",
        )
        self.assertEqual(parsed_data.fee_account_muxed_id, 123)


if __name__ == "__main__":
    unittest.main()
