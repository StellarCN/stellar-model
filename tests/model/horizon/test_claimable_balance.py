import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.claimable_balance import ClaimableBalance
from tests.model.horizon import load_horizon_file


class TestClaimableBalance(unittest.TestCase):
    def test_unconditional_valid(self):
        raw_data = load_horizon_file("claimable_balance_unconditional.json")
        parsed_data = ClaimableBalance.parse_obj(raw_data)
        self.assertEqual(
            parsed_data.id,
            "0000000035950db8eb2f303c37b67890aff15a26b5c16693aba4b40dcd31b54162e60456",
        )
        self.assertEqual(
            parsed_data.asset,
            "USDS:GBK4AYTOYIAYT4UJECSQGMACUWLKYOOM4VCAUUZ3Y3FG5XD2LYK3FGK2",
        )
        self.assertEqual(parsed_data.amount, Decimal("0.1000000"))
        self.assertEqual(
            parsed_data.sponsor,
            "GDDGK5C7UQWC7AEFZZVO7KXRXZVP2BBQJ2IQFAIROKME2O3XQR2CMVC7",
        )
        self.assertEqual(parsed_data.last_modified_ledger, 35068305)
        self.assertEqual(
            parsed_data.last_modified_time,
            datetime.datetime(2021, 4, 23, 14, 40, 19, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(len(parsed_data.claimants), 1)
        self.assertEqual(
            parsed_data.claimants[0].destination,
            "GANVXZ2DQ2FFLVCBSVMBBNVWSXS6YVEDP247EN4C3CM3I32XR4U3OU2I",
        )
        self.assertEqual(parsed_data.claimants[0].predicate.unconditional, True)
        self.assertEqual(parsed_data.flags.clawback_enabled, False)
        self.assertEqual(
            parsed_data.paging_token,
            "35068305-0000000035950db8eb2f303c37b67890aff15a26b5c16693aba4b40dcd31b54162e60456",
        )

    def test_conditional_valid(self):
        raw_data = load_horizon_file("claimable_balance_conditional.json")
        parsed_data = ClaimableBalance.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.claimants), 2)
        self.assertEqual(
            parsed_data.claimants[0].destination,
            "GCYTED6QWSGDNLQ2RBXDVYSKCOUB2BC6DLKGAU5QPNONMVN47ABUN6WE",
        )
        self.assertEqual(
            parsed_data.claimants[0].predicate.abs_before,
            datetime.datetime(2021, 4, 21, 19, 3, 6, tzinfo=datetime.timezone.utc),
        )

        self.assertEqual(
            parsed_data.claimants[1].destination,
            "GDDAESY7RTZAZNWZLZD5RIKP2TWEAVISKQJZ43ZZ2YTMCNICRVW7OJP3",
        )
        self.assertEqual(
            parsed_data.claimants[1].predicate.not_predicate.abs_before,
            datetime.datetime(2021, 4, 21, 19, 3, 1, tzinfo=datetime.timezone.utc),
        )
