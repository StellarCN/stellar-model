import datetime
import unittest
from decimal import Decimal

from stellar_model.model.horizon.effects import *
from tests.model.horizon import load_horizon_file

"""
        raw_data = load_horizon_file("effects/")
        parsed_data = AccountCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "")
        self.assertEqual(parsed_data.paging_token, "")
        self.assertEqual(parsed_data.account, "")
        self.assertEqual(parsed_data.type, "")
        self.assertEqual(parsed_data.type_i, 0)
        self.assertEqual(parsed_data.created_at, None)
"""


class TestEffects(unittest.TestCase):
    def test_valid_account_created(self):
        raw_data = load_horizon_file("effects/account_created.json")
        parsed_data = AccountCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661856401629185-0000000001")
        self.assertEqual(parsed_data.paging_token, "150661856401629185-1")
        self.assertEqual(
            parsed_data.account,
            "GCQPKZEC6VNFPDJMK73ET7JKKMN65BWYHCWF3Z65ZZPAL4E7DPWHP3YY",
        )
        self.assertEqual(parsed_data.type, "account_created")
        self.assertEqual(parsed_data.type_i, 0)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 18, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.starting_balance, Decimal("15.8675013"))

    def test_valid_account_removed(self):
        raw_data = load_horizon_file("effects/account_removed.json")
        parsed_data = AccountRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661749027127297-0000000003")
        self.assertEqual(parsed_data.paging_token, "150661749027127297-3")
        self.assertEqual(
            parsed_data.account,
            "GBDORGZMFCIY4J2SOUTXJJXX7NRPG7J3ZBEXYEP7OCUFKQCJGD3EH673",
        )
        self.assertEqual(parsed_data.type, "account_removed")
        self.assertEqual(parsed_data.type_i, 1)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 15, 44, tzinfo=datetime.timezone.utc),
        )

    def test_valid_account_credited(self):
        raw_data = load_horizon_file("effects/account_credited.json")
        parsed_data = AccountCreditedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661749027127297-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661749027127297-2")
        self.assertEqual(
            parsed_data.account,
            "GDYG6NVTFCY6HPBRQ3SQNKTDZUR7SS6WAWNEAKAFJW5EMKDGQLPG523C",
        )
        self.assertEqual(parsed_data.type, "account_credited")
        self.assertEqual(parsed_data.type_i, 2)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 15, 44, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "native")
        self.assertEqual(parsed_data.asset_code, None)
        self.assertEqual(parsed_data.asset_issuer, None)
        self.assertEqual(parsed_data.amount, Decimal("3.9999700"))

    def test_valid_account_debited(self):
        raw_data = load_horizon_file("effects/account_debited.json")
        parsed_data = AccountDebitedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661856401629185-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661856401629185-2")
        self.assertEqual(
            parsed_data.account,
            "GAY4G3PY3TPOVOSHDD2PZ4PIKA533VBBKEEJ5ASTOMPZOHAVKEWZ3ADS",
        )
        self.assertEqual(parsed_data.type, "account_debited")
        self.assertEqual(parsed_data.type_i, 3)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 18, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "native")
        self.assertEqual(parsed_data.asset_code, None)
        self.assertEqual(parsed_data.asset_issuer, None)
        self.assertEqual(parsed_data.amount, Decimal("15.8675013"))

    def test_valid_account_thresholds_updated(self):
        raw_data = load_horizon_file("effects/account_thresholds_updated.json")
        parsed_data = AccountThresholdsUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660954458435585-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660954458435585-1")
        self.assertEqual(
            parsed_data.account,
            "GC52GNOWS6DHRDVNA3ZZ7J6S52FZAQR3V5GIKVJPNMD6MOSQINEP672L",
        )
        self.assertEqual(parsed_data.type, "account_thresholds_updated")
        self.assertEqual(parsed_data.type_i, 4)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 59, 3, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.low_threshold, 20)
        self.assertEqual(parsed_data.med_threshold, 20)
        self.assertEqual(parsed_data.high_threshold, 20)

    def test_valid_account_home_domain_updated(self):
        raw_data = load_horizon_file("effects/account_home_domain_updated.json")
        parsed_data = AccountHomeDomainUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150665691807358978-0000000001")
        self.assertEqual(parsed_data.paging_token, "150665691807358978-1")
        self.assertEqual(
            parsed_data.account,
            "GBTNTMWPIGH3JCJQNMO3FG36YB6XHSL2TSXX74KXTRWXBRWHDMEWN6NB",
        )
        self.assertEqual(parsed_data.type, "account_home_domain_updated")
        self.assertEqual(parsed_data.type_i, 5)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 7, 38, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.home_domain, "lobstr.co")

    def test_valid_account_flags_updated(self):
        raw_data = load_horizon_file("effects/account_flags_updated.json")
        parsed_data = AccountFlagsUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150740432828043265-0000000001")
        self.assertEqual(parsed_data.paging_token, "150740432828043265-1")
        self.assertEqual(
            parsed_data.account,
            "GAZKVM2K3G3EICVODZHRW3CGEVIQOAMWJV6K77DFM246PIVBDYWNIHHW",
        )
        self.assertEqual(parsed_data.type, "account_flags_updated")
        self.assertEqual(parsed_data.type_i, 6)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 25, 9, 46, 54, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.auth_required_flag, True)
        self.assertEqual(parsed_data.auth_revokable_flag, None)

    def test_valid_account_inflation_destination_updated(self):
        raw_data = load_horizon_file(
            "effects/account_inflation_destination_updated.json"
        )
        parsed_data = AccountInflationDestinationUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660920098471939-0000000002")
        self.assertEqual(parsed_data.paging_token, "150660920098471939-2")
        self.assertEqual(
            parsed_data.account,
            "GB4KWEW6EQNV7S7DRAWDMNQJB64JKLH4YHXNVMIOFVAMZBHQ5IJCJ43R",
        )
        self.assertEqual(parsed_data.type, "account_inflation_destination_updated")
        self.assertEqual(parsed_data.type_i, 7)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 58, 20, tzinfo=datetime.timezone.utc),
        )

    def test_valid_signer_created(self):
        raw_data = load_horizon_file("effects/signer_created.json")
        parsed_data = SignerCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661856401629185-0000000003")
        self.assertEqual(parsed_data.paging_token, "150661856401629185-3")
        self.assertEqual(
            parsed_data.account,
            "GCQPKZEC6VNFPDJMK73ET7JKKMN65BWYHCWF3Z65ZZPAL4E7DPWHP3YY",
        )
        self.assertEqual(parsed_data.type, "signer_created")
        self.assertEqual(parsed_data.type_i, 10)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 18, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.weight, 1)
        self.assertEqual(
            parsed_data.public_key,
            "GCQPKZEC6VNFPDJMK73ET7JKKMN65BWYHCWF3Z65ZZPAL4E7DPWHP3YY",
        )
        self.assertEqual(parsed_data.key, "")

    def test_valid_signer_removed(self):
        raw_data = load_horizon_file("effects/signer_removed.json")
        parsed_data = SignerRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661134846902279-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661134846902279-2")
        self.assertEqual(
            parsed_data.account,
            "GDUQFAHWHQ6AUP6Q5MDAHILRG222CRF35HPUVRI66L7HXKHFJAQGHICR",
        )
        self.assertEqual(parsed_data.type, "signer_removed")
        self.assertEqual(parsed_data.type_i, 11)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 2, 51, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.weight, 0)
        self.assertEqual(
            parsed_data.public_key,
            "GDUQFAHWHQ6AUP6Q5MDAHILRG222CRF35HPUVRI66L7HXKHFJAQGHICR",
        )
        self.assertEqual(parsed_data.key, "")

    def test_valid_signer_updated(self):
        raw_data = load_horizon_file("effects/signer_updated.json")
        parsed_data = SignerUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660954458435585-0000000002")
        self.assertEqual(parsed_data.paging_token, "150660954458435585-2")
        self.assertEqual(
            parsed_data.account,
            "GC52GNOWS6DHRDVNA3ZZ7J6S52FZAQR3V5GIKVJPNMD6MOSQINEP672L",
        )
        self.assertEqual(parsed_data.type, "signer_updated")
        self.assertEqual(parsed_data.type_i, 12)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 59, 3, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.weight, 10)
        self.assertEqual(
            parsed_data.public_key,
            "GC52GNOWS6DHRDVNA3ZZ7J6S52FZAQR3V5GIKVJPNMD6MOSQINEP672L",
        )
        self.assertEqual(parsed_data.key, "")

    def test_valid_trustline_created(self):
        raw_data = load_horizon_file("effects/trustline_created.json")
        parsed_data = TrustlineCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660636630859777-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660636630859777-1")
        self.assertEqual(
            parsed_data.account,
            "GCAD67WM4IFVEEJ2Q3IPHUFKVORXLD7MOHUBLYNSCU3ERKOJQD52YZ7J",
        )
        self.assertEqual(parsed_data.type, "trustline_created")
        self.assertEqual(parsed_data.type_i, 20)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 52, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.asset_code, "DOGET")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GDOEVDDBU6OBWKL7VHDAOKD77UP4DKHQYKOKJJT5PR3WRDBTX35HUEUX",
        )
        self.assertEqual(parsed_data.limit, Decimal("922337203685.4775807"))

    def test_valid_trustline_removed(self):
        raw_data = load_horizon_file("effects/trustline_removed.json")
        parsed_data = TrustlineRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660924393627649-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660924393627649-1")
        self.assertEqual(
            parsed_data.account,
            "GDG2HNHRFG72XDZ64GPKUZOJJAG7PMJTV7BV22AH7ZCV44O4AOAHJNOH",
        )
        self.assertEqual(parsed_data.type, "trustline_removed")
        self.assertEqual(parsed_data.type_i, 21)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 58, 26, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "TERN")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GDGQDVO6XPFSY4NMX75A7AOVYCF5JYGW2SHCJJNWCQWIDGOZB53DGP6C",
        )
        self.assertEqual(parsed_data.limit, Decimal("0"))

    def test_valid_trustline_updated(self):
        raw_data = load_horizon_file("effects/trustline_updated.json")
        parsed_data = TrustlineUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660975933218817-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660975933218817-1")
        self.assertEqual(
            parsed_data.account,
            "GBDJ2WBVME6CRBZSDUSG3IYWK3MEY2XWSLX2AUSTOLQ75ONRW53DYV3C",
        )
        self.assertEqual(parsed_data.type, "trustline_updated")
        self.assertEqual(parsed_data.type_i, 22)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 59, 30, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.asset_code, "DOGET")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GDOEVDDBU6OBWKL7VHDAOKD77UP4DKHQYKOKJJT5PR3WRDBTX35HUEUX",
        )
        self.assertEqual(parsed_data.limit, Decimal("922337203685.4775807"))

    def test_valid_trustline_authorized(self):
        raw_data = load_horizon_file("effects/trustline_authorized.json")
        parsed_data = TrustlineAuthorizedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660791249526785-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660791249526785-1")
        self.assertEqual(
            parsed_data.account,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(parsed_data.type, "trustline_authorized")
        self.assertEqual(parsed_data.type_i, 23)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 55, 41, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.trustor,
            "GBL73HAKZGDGPSLOHI543CSK7FVJSMLHSIRUZRBH7SV43GM7IQWS7QET",
        )
        self.assertEqual(parsed_data.asset_code, "MSCIW")
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")

    def test_valid_trustline_deauthorized(self):
        raw_data = load_horizon_file("effects/trustline_deauthorized.json")
        parsed_data = TrustlineDeauthorizedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150662573661081605-0000000001")
        self.assertEqual(parsed_data.paging_token, "150662573661081605-1")
        self.assertEqual(
            parsed_data.account,
            "GBGYVMLI5EHUYQLXKQHD5CPBF35VLCR7IKBNUUQQQNVTT5M6HRWFZOVO",
        )
        self.assertEqual(parsed_data.type, "trustline_deauthorized")
        self.assertEqual(parsed_data.type_i, 24)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 33, 8, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.trustor,
            "GCLF6MCQFP2XJ7M46JUCO3CFZDNVXXC6NNKGFSPQXED6OVMUOUZ3HLNE",
        )
        self.assertEqual(parsed_data.asset_code, "LPTK")
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")

    def test_valid_trustline_authorized_to_maintain_liabilities(self):
        raw_data = load_horizon_file(
            "effects/trustline_authorized_to_maintain_liabilities.json"
        )
        parsed_data = TrustlineAuthorizedToMaintainLiabilitiesEffect.model_validate(
            raw_data
        )
        self.assertEqual(parsed_data.id, "0150660791249526794-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660791249526794-1")
        self.assertEqual(
            parsed_data.account,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(
            parsed_data.type, "trustline_authorized_to_maintain_liabilities"
        )
        self.assertEqual(parsed_data.type_i, 25)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 55, 41, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.trustor,
            "GBL73HAKZGDGPSLOHI543CSK7FVJSMLHSIRUZRBH7SV43GM7IQWS7QET",
        )
        self.assertEqual(parsed_data.asset_code, "MSCIW")
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")

    def test_valid_trustline_flags_updated(self):
        raw_data = load_horizon_file("effects/trustline_flags_updated.json")
        parsed_data = TrustlineFlagsUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660791249526785-0000000002")
        self.assertEqual(parsed_data.paging_token, "150660791249526785-2")
        self.assertEqual(
            parsed_data.account,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(parsed_data.type, "trustline_flags_updated")
        self.assertEqual(parsed_data.type_i, 26)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 55, 41, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.asset_code, "MSCIW")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(
            parsed_data.trustor,
            "GBL73HAKZGDGPSLOHI543CSK7FVJSMLHSIRUZRBH7SV43GM7IQWS7QET",
        )
        self.assertEqual(parsed_data.authorized_flag, True)
        self.assertEqual(parsed_data.authorized_to_maintain_liabilites_flag, None)
        self.assertEqual(parsed_data.clawback_enabled_flag, None)

    def test_valid_offer_created(self):
        pass

    def test_valid_offer_removed(self):
        pass

    def test_valid_offer_updated(self):
        pass

    def test_valid_trade(self):
        raw_data = load_horizon_file("effects/trade.json")
        parsed_data = TradeEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660580796153857-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660580796153857-1")
        self.assertEqual(
            parsed_data.account,
            "GBRFGFQF2JAJ5C4HHYLBA3S342ASPXVJRUK2DVEQH67733M2OJMTBM5E",
        )
        self.assertEqual(parsed_data.type, "trade")
        self.assertEqual(parsed_data.type_i, 33)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 51, 16, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.seller,
            "GCMYQPCR2FZ44ARPCWDX65TEYIQFXPOWTMHZCXAT4MDDEOBPI5S5EBX2",
        )
        self.assertEqual(parsed_data.offer_id, "545489795")
        self.assertEqual(parsed_data.sold_amount, Decimal("1.9295894"))
        self.assertEqual(parsed_data.sold_asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.sold_asset_code, "BUSD1")
        self.assertEqual(
            parsed_data.sold_asset_issuer,
            "GCIEGKAZ4ZUM4PEBTDXUMG6N4ZXOTCCK3UMSJCJ33QE5SVMCTTBKCVNY",
        )
        self.assertEqual(parsed_data.bought_amount, Decimal("4.3525833"))
        self.assertEqual(parsed_data.bought_asset_type, "native")
        self.assertEqual(parsed_data.bought_asset_code, None)
        self.assertEqual(parsed_data.bought_asset_issuer, None)

    def test_valid_data_created(self):
        raw_data = load_horizon_file("effects/data_created.json")
        parsed_data = DataCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660636630765571-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660636630765571-1")
        self.assertEqual(
            parsed_data.account,
            "GBLZGNXYDTZN3Q2FP4WWEKFO5DZJ2ED43S6YMUFD7ZO6B6LNIEOKWUPX",
        )
        self.assertEqual(parsed_data.type, "data_created")
        self.assertEqual(parsed_data.type_i, 40)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 52, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.name, "MESSAGE_DATA_0")
        self.assertEqual(
            parsed_data.value,
            "UW1mNkhpemtkRTRWdDdrTmFDRzhiUnJ4WnlvamtQd2ZIcHdUUE1WQzlzZTNHbw==",
        )

    def test_valid_data_removed(self):
        raw_data = load_horizon_file("effects/data_removed.json")
        parsed_data = DataRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150660636630765572-0000000001")
        self.assertEqual(parsed_data.paging_token, "150660636630765572-1")
        self.assertEqual(
            parsed_data.account,
            "GBLZGNXYDTZN3Q2FP4WWEKFO5DZJ2ED43S6YMUFD7ZO6B6LNIEOKWUPX",
        )
        self.assertEqual(parsed_data.type, "data_removed")
        self.assertEqual(parsed_data.type_i, 41)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 52, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.name, "MESSAGE_DATA_0")

    def test_valid_data_updated(self):
        raw_data = load_horizon_file("effects/data_updated.json")
        parsed_data = DataUpdatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661027472793603-0000000001")
        self.assertEqual(parsed_data.paging_token, "150661027472793603-1")
        self.assertEqual(
            parsed_data.account,
            "GCPNXP5WSNEXM2QNJYBOSWB6NGB6G37ZF2ODHYE7D4P5BCTBSYSO4E2R",
        )
        self.assertEqual(parsed_data.type, "data_updated")
        self.assertEqual(parsed_data.type_i, 42)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 0, 34, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.name, "MESSAGE_DATA_0")
        self.assertEqual(
            parsed_data.value,
            "UW1VNnU3UWZZcG9iZkRUTGt6N0VYTmpxZ1o5bkYza2lMTllQWHl1VzE0YTNGcw==",
        )

    def test_valid_sequence_bumped(self):
        raw_data = load_horizon_file("effects/sequence_bumped.json")
        parsed_data = SequenceBumpedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0151249850311778305-0000000001")
        self.assertEqual(parsed_data.paging_token, "151249850311778305-1")
        self.assertEqual(
            parsed_data.account,
            "GALG2O3DFETG4MKQGB52GRSASJWDSF62NZQTE25WG3CU7UTXP4GSWMWD",
        )
        self.assertEqual(parsed_data.type, "sequence_bumped")
        self.assertEqual(parsed_data.type_i, 43)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 2, 18, 42, 31, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.new_seq, 108136397361122527)

    def test_valid_claimable_balance_created(self):
        raw_data = load_horizon_file("effects/claimable_balance_created.json")
        parsed_data = ClaimableBalanceCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150684654087864322-0000000001")
        self.assertEqual(parsed_data.paging_token, "150684654087864322-1")
        self.assertEqual(
            parsed_data.account,
            "GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_created")
        self.assertEqual(parsed_data.type_i, 50)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 14, 16, 59, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.asset,
            "USDPEND:GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(
            parsed_data.balance_id,
            "0000000048a70acdec712be9547d19f7e58adc22e35e0f5bcf3897a0353ab5dd4c5d61f4",
        )
        self.assertEqual(parsed_data.amount, Decimal("900.0000000"))

    def test_valid_claimable_balance_claimant_created(self):
        raw_data = load_horizon_file("effects/claimable_balance_claimant_created.json")
        parsed_data = ClaimableBalanceClaimantCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150684654087864322-0000000003")
        self.assertEqual(parsed_data.paging_token, "150684654087864322-3")
        self.assertEqual(
            parsed_data.account,
            "GCBMP2WKIAX7KVDRCSFXJWFM5P7HDCGTCC76U5XR52OYII6AOWS7G3DT",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_claimant_created")
        self.assertEqual(parsed_data.type_i, 51)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 14, 16, 59, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.asset,
            "USDPEND:GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(
            parsed_data.balance_id,
            "0000000048a70acdec712be9547d19f7e58adc22e35e0f5bcf3897a0353ab5dd4c5d61f4",
        )
        self.assertEqual(parsed_data.amount, Decimal("900.0000000"))
        self.assertEqual(
            parsed_data.predicate.not_predicate.abs_before,
            datetime.datetime(2021, 4, 26, 4, 0, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.predicate.not_predicate.abs_before_epoch, 1619409600
        )

    def test_valid_claimable_balance_claimed(self):
        raw_data = load_horizon_file("effects/claimable_balance_claimed.json")
        parsed_data = ClaimableBalanceClaimedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150803053451329538-0000000001")
        self.assertEqual(parsed_data.paging_token, "150803053451329538-1")
        self.assertEqual(
            parsed_data.account,
            "GANVXZ2DQ2FFLVCBSVMBBNVWSXS6YVEDP247EN4C3CM3I32XR4U3OU2I",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_claimed")
        self.assertEqual(parsed_data.type_i, 52)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 26, 7, 35, 19, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.asset,
            "USDC:GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
        )
        self.assertEqual(
            parsed_data.balance_id,
            "0000000016cbeff27945d389e9123231ec916f7bb848c0579ceca12e2bfab5c34ce0da24",
        )
        self.assertEqual(parsed_data.amount, Decimal("1"))

    def test_valid_account_sponsorship_created(self):
        raw_data = load_horizon_file("effects/account_sponsorship_created.json")
        parsed_data = AccountSponsorshipCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661134846902274-0000000004")
        self.assertEqual(parsed_data.paging_token, "150661134846902274-4")
        self.assertEqual(
            parsed_data.account,
            "GDUQFAHWHQ6AUP6Q5MDAHILRG222CRF35HPUVRI66L7HXKHFJAQGHICR",
        )
        self.assertEqual(parsed_data.type, "account_sponsorship_created")
        self.assertEqual(parsed_data.type_i, 60)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 2, 51, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.sponsor,
            "GCZGSFPITKVJPJERJIVLCQK5YIHYTDXCY45ZHU3IRCUC53SXSCAL44JV",
        )

    def test_valid_account_sponsorship_updated(self):
        pass

    def test_valid_account_sponsorship_removed(self):
        raw_data = load_horizon_file("effects/account_sponsorship_removed.json")
        parsed_data = AccountSponsorshipRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0151324471070908417-0000000004")
        self.assertEqual(parsed_data.paging_token, "151324471070908417-4")
        self.assertEqual(
            parsed_data.account,
            "GAHM22VLSTZHTY7RP64UYKG4VR7DDFGDGKJ4GVRRS77D7M6EMXG5XTNS",
        )
        self.assertEqual(parsed_data.type, "account_sponsorship_removed")
        self.assertEqual(parsed_data.type_i, 62)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 3, 20, 29, 17, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.former_sponsor,
            "GA7PT6IPFVC4FGG273ZHGCNGG2O52F3B6CLVSI4SNIYOXLUNIOSFCK4F",
        )

    def test_valid_trustline_sponsorship_created(self):
        raw_data = load_horizon_file("effects/trustline_sponsorship_created.json")
        parsed_data = TrustlineSponsorshipCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661134846902276-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661134846902276-2")
        self.assertEqual(
            parsed_data.account,
            "GDUQFAHWHQ6AUP6Q5MDAHILRG222CRF35HPUVRI66L7HXKHFJAQGHICR",
        )
        self.assertEqual(parsed_data.type, "trustline_sponsorship_created")
        self.assertEqual(parsed_data.type_i, 63)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 2, 51, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.asset,
            "USDC:GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
        )
        self.assertEqual(
            parsed_data.sponsor,
            "GCZGSFPITKVJPJERJIVLCQK5YIHYTDXCY45ZHU3IRCUC53SXSCAL44JV",
        )

    def test_valid_trustline_sponsorship_updated(self):
        pass

    def test_valid_trustline_sponsorship_removed(self):
        raw_data = load_horizon_file("effects/trustline_sponsorship_removed.json")
        parsed_data = TrustlineSponsorshipRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150671008977530881-0000000002")
        self.assertEqual(parsed_data.paging_token, "150671008977530881-2")
        self.assertEqual(
            parsed_data.account,
            "GB6JGOVUP3UXRPA2BUAUF6YGGZSRWQUMPTHVRSRATVYGFOYUYRPWJACK",
        )
        self.assertEqual(parsed_data.type, "trustline_sponsorship_removed")
        self.assertEqual(parsed_data.type_i, 65)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 9, 29, 50, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.asset,
            "SQ0202:GCZODXV5HXRHHOZHWE57LMWIELKAXPKC64SOEBGTK7BV4GMRMOKYDIQQ",
        )
        self.assertEqual(
            parsed_data.former_sponsor,
            "GA7PT6IPFVC4FGG273ZHGCNGG2O52F3B6CLVSI4SNIYOXLUNIOSFCK4F",
        )

    def test_valid_data_sponsorship_created(self):
        raw_data = load_horizon_file("effects/data_sponsorship_created.json")
        parsed_data = DataSponsorshipCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0003520460138483714-0000000002")
        self.assertEqual(parsed_data.paging_token, "3520460138483714-2")
        self.assertEqual(
            parsed_data.account,
            "GAJADTBH23KY25XZPBZDS5NKV5ZXTIMDGORKSQCHE4DVVLEHSXSV2EQK",
        )
        self.assertEqual(parsed_data.type, "data_sponsorship_created")
        self.assertEqual(parsed_data.type_i, 66)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 6, 1, 13, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.data_name, "hello")
        self.assertEqual(
            parsed_data.sponsor,
            "GDDQTK5V3E3JFGLZZTJTKURTVY7QJPNQLTR5QS5HIWZWY5XPYIO5YELN",
        )

    def test_valid_data_sponsorship_updated(self):
        pass

    def test_valid_data_sponsorship_removed(self):
        raw_data = load_horizon_file("effects/data_sponsorship_removed.json")
        parsed_data = DataSponsorshipRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0003520511678095361-0000000001")
        self.assertEqual(parsed_data.paging_token, "3520511678095361-1")
        self.assertEqual(
            parsed_data.account,
            "GDDQTK5V3E3JFGLZZTJTKURTVY7QJPNQLTR5QS5HIWZWY5XPYIO5YELN",
        )
        self.assertEqual(parsed_data.type, "data_sponsorship_removed")
        self.assertEqual(parsed_data.type_i, 68)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 6, 2, 18, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.data_name, "hello")
        self.assertEqual(
            parsed_data.former_sponsor,
            "GDDQTK5V3E3JFGLZZTJTKURTVY7QJPNQLTR5QS5HIWZWY5XPYIO5YELN",
        )

    def test_valid_claimable_balance_sponsorship_created(self):
        raw_data = load_horizon_file(
            "effects/claimable_balance_sponsorship_created.json"
        )
        parsed_data = ClaimableBalanceSponsorshipCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150684654087864322-0000000005")
        self.assertEqual(parsed_data.paging_token, "150684654087864322-5")
        self.assertEqual(
            parsed_data.account,
            "GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_sponsorship_created")
        self.assertEqual(parsed_data.type_i, 69)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 14, 16, 59, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.balance_id,
            "0000000048a70acdec712be9547d19f7e58adc22e35e0f5bcf3897a0353ab5dd4c5d61f4",
        )
        self.assertEqual(
            parsed_data.sponsor,
            "GBGJB2WEIQCCUZYISUKAFRPR46LQ62O7W6CDKN52NVROG44LLL3L73X2",
        )

    def test_valid_claimable_balance_sponsorship_updated(self):
        pass

    def test_valid_claimable_balance_sponsorship_removed(self):
        raw_data = load_horizon_file(
            "effects/claimable_balance_sponsorship_removed.json"
        )
        parsed_data = ClaimableBalanceSponsorshipRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150803053451329538-0000000003")
        self.assertEqual(parsed_data.paging_token, "150803053451329538-3")
        self.assertEqual(
            parsed_data.account,
            "GANVXZ2DQ2FFLVCBSVMBBNVWSXS6YVEDP247EN4C3CM3I32XR4U3OU2I",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_sponsorship_removed")
        self.assertEqual(parsed_data.type_i, 71)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 26, 7, 35, 19, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.balance_id,
            "0000000016cbeff27945d389e9123231ec916f7bb848c0579ceca12e2bfab5c34ce0da24",
        )
        self.assertEqual(
            parsed_data.former_sponsor,
            "GDDGK5C7UQWC7AEFZZVO7KXRXZVP2BBQJ2IQFAIROKME2O3XQR2CMVC7",
        )

    def test_valid_signer_sponsorship_created(self):
        raw_data = load_horizon_file("effects/signer_sponsorship_created.json")
        parsed_data = SignerSponsorshipCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661134846902275-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661134846902275-2")
        self.assertEqual(
            parsed_data.account,
            "GDUQFAHWHQ6AUP6Q5MDAHILRG222CRF35HPUVRI66L7HXKHFJAQGHICR",
        )
        self.assertEqual(parsed_data.type, "signer_sponsorship_created")
        self.assertEqual(parsed_data.type_i, 72)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 2, 51, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.signer,
            "GD6632TYLXUKGVFNQYSC2AC752YZWR7VFNJZ5X7HYPKBLZKK5YVWQ54S",
        )
        self.assertEqual(
            parsed_data.sponsor,
            "GCZGSFPITKVJPJERJIVLCQK5YIHYTDXCY45ZHU3IRCUC53SXSCAL44JV",
        )

    def test_valid_signer_sponsorship_updated(self):
        pass

    def test_valid_signer_sponsorship_removed(self):
        raw_data = load_horizon_file("effects/signer_sponsorship_removed.json")
        parsed_data = SignerSponsorshipRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0150661624473337857-0000000002")
        self.assertEqual(parsed_data.paging_token, "150661624473337857-2")
        self.assertEqual(
            parsed_data.account,
            "GA26UJZUXR5Q2VMTJHAFS2DV6DKFRWBIN7JKDALGYFEXTRNGX5K6DEAZ",
        )
        self.assertEqual(parsed_data.type, "signer_sponsorship_removed")
        self.assertEqual(parsed_data.type_i, 74)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 13, 9, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.signer,
            "GBIQ43HRJ3HKDRR3AYV25VYWQAQHZ7RWFBNUOU755FNY2O5UIFQD5TRD",
        )
        self.assertEqual(
            parsed_data.former_sponsor,
            "GCZGSFPITKVJPJERJIVLCQK5YIHYTDXCY45ZHU3IRCUC53SXSCAL44JV",
        )

    def test_valid_claimable_balance_clawed_back(self):
        raw_data = load_horizon_file("effects/claimable_balance_clawed_back.json")
        parsed_data = ClaimableBalanceClawedBackEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0003513936083165185-0000000001")
        self.assertEqual(parsed_data.paging_token, "3513936083165185-1")
        self.assertEqual(
            parsed_data.account,
            "GD5YHBKE7FSUUZIOSL4ED6UKMM2HZAYBYGZI7KRCTMFDTOO6SGZCQB4Z",
        )
        self.assertEqual(parsed_data.type, "claimable_balance_clawed_back")
        self.assertEqual(parsed_data.type_i, 80)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 3, 48, 5, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.balance_id,
            "000000001fe36f3ce6ab6a6423b18b5947ce8890157ae77bb17faeb765814ad040b74ce1",
        )

    def test_liquidity_pool_deposited(self):
        raw_data = load_horizon_file("effects/liquidity_pool_deposited.json")
        parsed_data = LiquidityPoolDepositedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0001579044726386689-0000000001")
        self.assertEqual(parsed_data.paging_token, "1579044726386689-1")
        self.assertEqual(
            parsed_data.account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(
            parsed_data.account_muxed_id,
            1278881,
        )
        self.assertEqual(parsed_data.type, "liquidity_pool_deposited")
        self.assertEqual(parsed_data.type_i, 90)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 6, 32, tzinfo=datetime.timezone.utc),
        )

        self.assertEqual(
            parsed_data.liquidity_pool.id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.liquidity_pool.fee_bp, 30)
        self.assertEqual(parsed_data.liquidity_pool.type, "constant_product")
        self.assertEqual(parsed_data.liquidity_pool.total_trustlines, 1)
        self.assertEqual(
            parsed_data.liquidity_pool.total_shares, Decimal("250.0000000")
        )
        self.assertEqual(len(parsed_data.liquidity_pool.reserves), 2)
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_code, "COOL"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.liquidity_pool.reserves[0].amount, Decimal("250"))
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_code, "SONESO"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.liquidity_pool.reserves[1].amount, Decimal("250"))

        self.assertEqual(len(parsed_data.liquidity_pool.reserves), 2)
        self.assertEqual(
            parsed_data.reserves_deposited[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_deposited[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_deposited[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.reserves_deposited[0].amount, Decimal("250"))
        self.assertEqual(
            parsed_data.reserves_deposited[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_deposited[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_deposited[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.reserves_deposited[1].amount, Decimal("250"))

        self.assertEqual(parsed_data.shares_received, Decimal("250.0000000"))

    def test_liquidity_pool_withdrew(self):
        raw_data = load_horizon_file("effects/liquidity_pool_withdrew.json")
        parsed_data = LiquidityPoolWithdrewEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0001579096265998337-0000000001")
        self.assertEqual(parsed_data.paging_token, "1579096265998337-1")
        self.assertEqual(
            parsed_data.account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(
            parsed_data.account_muxed_id,
            1278881,
        )
        self.assertEqual(parsed_data.type, "liquidity_pool_withdrew")
        self.assertEqual(parsed_data.type_i, 91)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 7, 37, tzinfo=datetime.timezone.utc),
        )

        self.assertEqual(
            parsed_data.liquidity_pool.id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.liquidity_pool.fee_bp, 30)
        self.assertEqual(parsed_data.liquidity_pool.type, "constant_product")
        self.assertEqual(parsed_data.liquidity_pool.total_trustlines, 1)
        self.assertEqual(
            parsed_data.liquidity_pool.total_shares, Decimal("400.0000000")
        )
        self.assertEqual(len(parsed_data.liquidity_pool.reserves), 2)
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_code, "COOL"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.liquidity_pool.reserves[0].amount, Decimal("400"))
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_code, "SONESO"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.liquidity_pool.reserves[1].amount, Decimal("400"))

        self.assertEqual(len(parsed_data.liquidity_pool.reserves), 2)
        self.assertEqual(
            parsed_data.reserves_received[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_received[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_received[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.reserves_received[0].amount, Decimal("100"))
        self.assertEqual(
            parsed_data.reserves_received[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_received[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_received[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.reserves_received[1].amount, Decimal("100"))

        self.assertEqual(parsed_data.shares_redeemed, Decimal("100.0000000"))

    def test_liquidity_pool_trade(self):
        raw_data = load_horizon_file("effects/liquidity_pool_trade.json")
        parsed_data = LiquidityPoolTradeEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0001579418388553729-0000000003")
        self.assertEqual(parsed_data.paging_token, "1579418388553729-3")
        self.assertEqual(
            parsed_data.account,
            "GARIJI33DZEOA2HT7H5Q3E7W6KY2KBOYA6ZSUHKNNWNQR75JSQMU3SRJ",
        )
        self.assertEqual(
            parsed_data.account_muxed,
            None,
        )
        self.assertEqual(
            parsed_data.account_muxed_id,
            None,
        )
        self.assertEqual(parsed_data.type, "liquidity_pool_trade")
        self.assertEqual(parsed_data.type_i, 92)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 14, 6, tzinfo=datetime.timezone.utc),
        )

        self.assertEqual(
            parsed_data.liquidity_pool.id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.liquidity_pool.fee_bp, 30)
        self.assertEqual(parsed_data.liquidity_pool.type, "constant_product")
        self.assertEqual(parsed_data.liquidity_pool.total_trustlines, 1)
        self.assertEqual(
            parsed_data.liquidity_pool.total_shares, Decimal("400.0000000")
        )
        self.assertEqual(len(parsed_data.liquidity_pool.reserves), 2)
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_code, "COOL"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[0].amount, Decimal("381.0068105")
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_code, "SONESO"
        )
        self.assertEqual(
            parsed_data.liquidity_pool.reserves[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.liquidity_pool.reserves[1].amount, Decimal("420"))

        self.assertEqual(parsed_data.sold.asset.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.sold.asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.sold.asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.sold.amount, Decimal("18.9931895"))
        self.assertEqual(parsed_data.bought.asset.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.bought.asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.bought.asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.bought.amount, Decimal("20"))

    def test_liquidity_pool_created(self):
        raw_data = load_horizon_file("effects/liquidity_pool_created.json")
        parsed_data = LiquidityPoolCreatedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0001578868632723457-0000000002")
        self.assertEqual(parsed_data.paging_token, "1578868632723457-2")
        self.assertEqual(
            parsed_data.account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(
            parsed_data.account_muxed_id,
            1278881,
        )
        self.assertEqual(parsed_data.type, "liquidity_pool_created")
        self.assertEqual(parsed_data.type_i, 93)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 2, 57, tzinfo=datetime.timezone.utc),
        )

        self.assertEqual(
            parsed_data.liquidity_pool.id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )

    def test_liquidity_pool_removed(self):
        raw_data = load_horizon_file("effects/liquidity_pool_removed.json")
        parsed_data = LiquidityPoolRemovedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0179972298072752130-0000000002")
        self.assertEqual(parsed_data.paging_token, "179972298072752130-2")
        self.assertEqual(
            parsed_data.liquidity_pool_id,
            "89c11017d16552c152536092d7440a2cd4cf4bf7df2c7e7552b56e6bcac98d95",
        )

    def test_liquidity_pool_revoked(self):
        pass

    def test_contract_credited(self):
        raw_data = load_horizon_file("effects/contract_credited.json")
        parsed_data = EffectContractCreditedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0000021517786157057-0000000002")
        self.assertEqual(parsed_data.paging_token, "21517786157057-2")
        self.assertEqual(parsed_data.account, "GDAT5HWTGIU4TSSZ4752OUC4SABDLTLZFRPZUJ3D6LKBNEPA7V2CIG54")
        self.assertEqual(parsed_data.type, "contract_credited")
        self.assertEqual(parsed_data.type_i, 96)
        self.assertEqual(parsed_data.created_at,
                         datetime.datetime(2023, 9, 19, 5, 43, 12, tzinfo=datetime.timezone.utc))
        self.assertEqual(parsed_data.asset_type, "native")
        self.assertEqual(parsed_data.asset_code, None)
        self.assertEqual(parsed_data.asset_issuer, None)
        self.assertEqual(parsed_data.amount, Decimal("100"))

    def test_contract_debited(self):
        raw_data = load_horizon_file("effects/contract_debited.json")
        parsed_data = EffectContractCreditedEffect.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "0000021517786157057-0000000002")
        self.assertEqual(parsed_data.paging_token, "21517786157057-2")
        self.assertEqual(parsed_data.account, "GDAT5HWTGIU4TSSZ4752OUC4SABDLTLZFRPZUJ3D6LKBNEPA7V2CIG54")
        self.assertEqual(parsed_data.type, "contract_debited")
        self.assertEqual(parsed_data.type_i, 97)
        self.assertEqual(parsed_data.created_at,
                         datetime.datetime(2023, 9, 19, 5, 43, 12, tzinfo=datetime.timezone.utc))
        self.assertEqual(parsed_data.asset_type, "native")
        self.assertEqual(parsed_data.asset_code, None)
        self.assertEqual(parsed_data.asset_issuer, None)
        self.assertEqual(parsed_data.amount, Decimal("100"))
