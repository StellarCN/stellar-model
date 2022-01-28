import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.operations import *
from tests.model.horizon import load_horizon_file


"""
        raw_data = load_horizon_file("operations/")
        parsed_data = CreateAccountOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "")
        self.assertEqual(parsed_data.paging_token, "")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(parsed_data.source_account, "")
        self.assertEqual(parsed_data.type, "")
        self.assertEqual(parsed_data.type_i, 0)
        self.assertEqual(parsed_data.created_at, None)
        self.assertEqual(parsed_data.transaction_hash, "")
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
"""


class TestOperations(unittest.TestCase):
    def test_valid_create_account_operation(self):
        raw_data = load_horizon_file("operations/create_account.json")
        parsed_data = CreateAccountOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661852106629126")
        self.assertEqual(parsed_data.paging_token, "150661852106629126")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GDYG6NVTFCY6HPBRQ3SQNKTDZUR7SS6WAWNEAKAFJW5EMKDGQLPG523C",
        )
        self.assertEqual(parsed_data.type, "create_account")
        self.assertEqual(parsed_data.type_i, 0)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 17, 55, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "2d634bd0b1f5006a11555309fc812ff0ae21020c534697954631fd17b042eb06",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.account,
            "GCYXLFYRSJWRPQ7JYSPHDNFRNXQ377BNUHF3TDZCPCQMVJS2QKMXCT2E",
        )
        self.assertEqual(
            parsed_data.funder,
            "GDYG6NVTFCY6HPBRQ3SQNKTDZUR7SS6WAWNEAKAFJW5EMKDGQLPG523C",
        )
        self.assertEqual(parsed_data.starting_balance, Decimal("4.0000000"))

    def test_valid_payment_operation(self):
        raw_data = load_horizon_file("operations/payment.json")
        parsed_data = PaymentOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661113372200961")
        self.assertEqual(parsed_data.paging_token, "150661113372200961")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GA6PS2RUKTEEEDNG463HAJWSMNCMG2Z7Q4ALYFQOHIKS47POTBVAU4QV",
        )
        self.assertEqual(parsed_data.type, "payment")
        self.assertEqual(parsed_data.type_i, 1)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 2, 24, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "77d866660693f5c1550b1b5a8bb6583ded550e1c9687c68c83282443c8c91341",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.from_,
            "GA6PS2RUKTEEEDNG463HAJWSMNCMG2Z7Q4ALYFQOHIKS47POTBVAU4QV",
        )
        self.assertEqual(
            parsed_data.to, "GDLE7PMXCPKNALUQP6VLZTDUD2O5SJJ4GKKYXUME6KWHCPEAVGIWY6G6"
        )
        self.assertEqual(parsed_data.amount, Decimal("67.7492240"))

    def test_valid_path_payment_strict_receive_operation(self):
        raw_data = load_horizon_file("operations/path_payment_strict_receive.json")
        parsed_data = PathPaymentStrictReceiveOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661572933464065")
        self.assertEqual(parsed_data.paging_token, "150661572933464065")
        self.assertEqual(parsed_data.transaction_successful, False)
        self.assertEqual(
            parsed_data.source_account,
            "GDQLBBDNG5L3TZLR5RPVQFT4CUORSTHWX3GJBHCCADXBJV55ZHW6CL5B",
        )
        self.assertEqual(parsed_data.type, "path_payment_strict_receive")
        self.assertEqual(parsed_data.type_i, 2)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 12, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "999119fca29afe1d994fb744e80afbb76efc9a4abb56e6ed8209b1248c0f629e",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "native")
        self.assertEqual(parsed_data.asset_code, None)
        self.assertEqual(parsed_data.asset_issuer, None)
        self.assertEqual(
            parsed_data.from_,
            "GDQLBBDNG5L3TZLR5RPVQFT4CUORSTHWX3GJBHCCADXBJV55ZHW6CL5B",
        )
        self.assertEqual(
            parsed_data.to, "GDQLBBDNG5L3TZLR5RPVQFT4CUORSTHWX3GJBHCCADXBJV55ZHW6CL5B"
        )
        self.assertEqual(parsed_data.amount, Decimal("2386.8885355"))
        self.assertEqual(parsed_data.source_amount, Decimal("0"))
        self.assertEqual(parsed_data.source_max, Decimal("2386.8885355"))
        self.assertEqual(parsed_data.source_asset_type, "native")
        self.assertEqual(parsed_data.source_asset_code, None)
        self.assertEqual(parsed_data.source_asset_issuer, None)
        self.assertEqual(len(parsed_data.path), 2)
        self.assertEqual(parsed_data.path[0].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.path[0].asset_code, "USDC")
        self.assertEqual(
            parsed_data.path[0].asset_issuer,
            "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
        )
        self.assertEqual(parsed_data.path[1].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.path[1].asset_code, "SLT")
        self.assertEqual(
            parsed_data.path[1].asset_issuer,
            "GCKA6K5PCQ6PNF5RQBF7PQDJWRHO6UOGFMRLK3DYHDOI244V47XKQ4GP",
        )

    def test_valid_manage_sell_offer_operation(self):
        raw_data = load_horizon_file("operations/manage_sell_offer.json")
        parsed_data = ManageSellOfferOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661572935458818")
        self.assertEqual(parsed_data.paging_token, "150661572935458818")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GBLKRATZODTSJNU7XTB5HY5VAAN63CPRT77UYZT2VLCNXE7F3YHSW22M",
        )
        self.assertEqual(parsed_data.type, "manage_sell_offer")
        self.assertEqual(parsed_data.type_i, 3)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 12, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "559fa74a4c492e2bc8402b77b1aec28725bf094825e3b78d571f2160501d0f56",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.amount, Decimal("478.6351404"))
        self.assertEqual(parsed_data.price, Decimal("32.6639943"))
        self.assertEqual(parsed_data.price_r.n, 326639943)
        self.assertEqual(parsed_data.price_r.d, 10000000)
        self.assertEqual(parsed_data.buying_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.buying_asset_code, "RMT")
        self.assertEqual(
            parsed_data.buying_asset_issuer,
            "GDEGOXPCHXWFYY234D2YZSPEJ24BX42ESJNVHY5H7TWWQSYRN5ZKZE3N",
        )
        self.assertEqual(parsed_data.selling_asset_type, "native")
        self.assertEqual(parsed_data.selling_asset_code, None)
        self.assertEqual(parsed_data.selling_asset_issuer, None)

    def test_valid_create_passive_sell_offer_operation(self):
        raw_data = load_horizon_file("operations/create_passive_sell_offer.json")
        parsed_data = CreatePassiveSellOfferOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150701833957081089")
        self.assertEqual(parsed_data.paging_token, "150701833957081089")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GCQPF34D4NP66RYULISYRSBS52M5FFZ2JVJ4LMQTQXDI2XGP6UDSE3IB",
        )
        self.assertEqual(parsed_data.type, "create_passive_sell_offer")
        self.assertEqual(parsed_data.type_i, 4)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 20, 17, 32, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "b18f88e11353f60532eabbef17d76ed25eebc31f9448e765cf1cfdbbf4451e54",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.amount, Decimal("0.0001000"))
        self.assertEqual(parsed_data.price, Decimal("1.0000000"))
        self.assertEqual(parsed_data.price_r.n, 1)
        self.assertEqual(parsed_data.price_r.d, 1)
        self.assertEqual(parsed_data.buying_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.buying_asset_code, "USA")
        self.assertEqual(
            parsed_data.buying_asset_issuer,
            "GCQPF34D4NP66RYULISYRSBS52M5FFZ2JVJ4LMQTQXDI2XGP6UDSE3IB",
        )
        self.assertEqual(parsed_data.selling_asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.selling_asset_code, "MONEY")
        self.assertEqual(
            parsed_data.selling_asset_issuer,
            "GA2KQTETIRREL66P64GV6KCVICPULLDVHWJDZSIJKDLIAGBXUCIZ6P6E",
        )

    def test_valid_set_options_operation(self):
        raw_data = load_horizon_file("operations/set_options.json")
        parsed_data = SetOptionsOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "2696453482881025")
        self.assertEqual(parsed_data.paging_token, "2696453482881025")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GASM5Q5QTMV7K45AWLFY7CAJGSPXVRH3MUNN7N3P7X4JHAFSB6RXHWCC",
        )
        self.assertEqual(parsed_data.type, "set_options")
        self.assertEqual(parsed_data.type_i, 5)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 13, 55, 29, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "125c35e68b82b2a77970f1ccfa737e3a2e7b12e6c6bc683f9d415ed77a98f54e",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(len(parsed_data.set_flags), 1)
        self.assertEqual(parsed_data.set_flags[0], 1)
        self.assertEqual(len(parsed_data.set_flags_s), 1)
        self.assertEqual(parsed_data.set_flags_s[0], "auth_required")
        self.assertEqual(len(parsed_data.clear_flags), 1)
        self.assertEqual(parsed_data.clear_flags[0], 2)
        self.assertEqual(len(parsed_data.clear_flags_s), 1)
        self.assertEqual(parsed_data.clear_flags_s[0], "auth_revocable")
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.home_domain, "example.com")
        self.assertEqual(
            parsed_data.inflation_dest,
            "GDLSZ37Q6AJN6UNQPXIWNRAB3LETWAASA2H3OWNHRUWMG2LVU3A45S6D",
        )
        self.assertEqual(parsed_data.master_key_weight, 10)
        self.assertEqual(
            parsed_data.signer_key,
            "GDLSZ37Q6AJN6UNQPXIWNRAB3LETWAASA2H3OWNHRUWMG2LVU3A45S6D",
        )
        self.assertEqual(parsed_data.signer_weight, 10)
        self.assertEqual(parsed_data.low_threshold, 1)
        self.assertEqual(parsed_data.med_threshold, 10)
        self.assertEqual(parsed_data.high_threshold, 20)

    def test_valid_change_trust_operation_asset(self):
        raw_data = load_horizon_file("operations/change_trust_asset.json")
        parsed_data = ChangeTrustOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661512804089860")
        self.assertEqual(parsed_data.paging_token, "150661512804089860")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GA26UJZUXR5Q2VMTJHAFS2DV6DKFRWBIN7JKDALGYFEXTRNGX5K6DEAZ",
        )
        self.assertEqual(parsed_data.type, "change_trust")
        self.assertEqual(parsed_data.type_i, 6)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 10, 44, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "c96337fca2de58731dbfd7a70e90e1078af796e8c5b8f621584c4565311be4c1",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(
            parsed_data.sponsor,
            "GCZGSFPITKVJPJERJIVLCQK5YIHYTDXCY45ZHU3IRCUC53SXSCAL44JV",
        )
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "USDC")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
        )
        self.assertEqual(parsed_data.limit, Decimal("922337203685.4775807"))
        self.assertEqual(
            parsed_data.trustee,
            "GA5ZSEJYB37JRC5AVCIA5MOP4RHTM335X2KGX3IHOJAPP5RE34K4KZVN",
        )
        self.assertEqual(
            parsed_data.trustor,
            "GA26UJZUXR5Q2VMTJHAFS2DV6DKFRWBIN7JKDALGYFEXTRNGX5K6DEAZ",
        )

    def test_valid_change_trust_operation_liquidity_pool_id(self):
        raw_data = load_horizon_file("operations/change_trust_liquidity_pool_id.json")
        parsed_data = ChangeTrustOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "1578868632723457")
        self.assertEqual(parsed_data.paging_token, "1578868632723457")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.source_account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(parsed_data.source_account_muxed_id, 1278881)
        self.assertEqual(parsed_data.type, "change_trust")
        self.assertEqual(parsed_data.type_i, 6)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 2, 57, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "4ebd36d6ae43622d606a0b7c59fd28d1c0b07d96bae7deb5c86e7b93a9c1c5c3",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "liquidity_pool_shares")
        self.assertEqual(
            parsed_data.liquidity_pool_id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.limit, Decimal("922337203685.4775807"))
        self.assertEqual(
            parsed_data.trustee,
            None,
        )
        self.assertEqual(
            parsed_data.trustor,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.trustor_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(
            parsed_data.trustor_muxed_id,
            1278881,
        )

    def test_valid_allow_trust_operation(self):
        raw_data = load_horizon_file("operations/allow_trust.json")
        parsed_data = AllowTrustOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150662449110290439")
        self.assertEqual(parsed_data.paging_token, "150662449110290439")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(parsed_data.type, "allow_trust")
        self.assertEqual(parsed_data.type_i, 7)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 30, 21, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "918370699c6c59c2ab2b59657f6a9d968197a5b90fa87734f805b0c3954d6010",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "4GLD")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(
            parsed_data.trustee,
            "GBRDHSZL4ZKOI2PTUMM53N3NICZXC5OX3KPCD4WD4NG4XGCBC2ZA3KAG",
        )
        self.assertEqual(
            parsed_data.trustor,
            "GDJ4X5NVRMIB3ZYO2PQ7U2QKZ5C42YKV7ZH3LJYXZWQOP4K5CUBSNGVS",
        )
        self.assertEqual(parsed_data.authorize_to_maintain_liabilities, True)

    def test_valid_account_merge_operation(self):
        raw_data = load_horizon_file("operations/account_merge.json")
        parsed_data = AccountMergeOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661877876133889")
        self.assertEqual(parsed_data.paging_token, "150661877876133889")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GBMZ7GUHNHT6TG4ITOBG46TKA5YMNH7ZKHHJSQRU6PNYBSAELLXNOFDE",
        )
        self.assertEqual(parsed_data.type, "account_merge")
        self.assertEqual(parsed_data.type_i, 8)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 18, 26, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "f86aaf456dc000e565ac89bd0b21abcedad4d3ab497bdb9fefa782c9e6ce8c98",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.account,
            "GBMZ7GUHNHT6TG4ITOBG46TKA5YMNH7ZKHHJSQRU6PNYBSAELLXNOFDE",
        )
        self.assertEqual(
            parsed_data.into, "GDYG6NVTFCY6HPBRQ3SQNKTDZUR7SS6WAWNEAKAFJW5EMKDGQLPG523C"
        )

    def test_valid_inflation_operation(self):
        raw_data = load_horizon_file("operations/inflation.json")
        parsed_data = InflationOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "85376614040350721")
        self.assertEqual(parsed_data.paging_token, "85376614040350721")
        self.assertEqual(parsed_data.transaction_successful, False)
        self.assertEqual(
            parsed_data.source_account,
            "GDC2XPNEM4YAH22FK2TW7FSVGWQRGZGXLA3DAJLHNJ7YL5L5RSIXXXXX",
        )
        self.assertEqual(parsed_data.type, "inflation")
        self.assertEqual(parsed_data.type_i, 9)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2018, 9, 8, 5, 0, 7, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "25fca20b8d726ecced601b5ec230c3ef02852bbdc3aa082e9f6131a0ccf50ece",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)

    def test_valid_manage_data_operation(self):
        raw_data = load_horizon_file("operations/manage_data.json")
        parsed_data = ManageDataOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150660585091022850")
        self.assertEqual(parsed_data.paging_token, "150660585091022850")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GDPNHOQWJG6EFYCSSBJTNZH6L7YVQKIAQOKQDH6HDDV2OTDVTFVAF5GN",
        )
        self.assertEqual(parsed_data.type, "manage_data")
        self.assertEqual(parsed_data.type_i, 10)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 51, 21, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "d050b7036b96b8eeb1735b9ed78b5d514b7f54126e519d8980c14b988ae6d479",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.name, "MESSAGE_DATA_0")
        self.assertEqual(
            parsed_data.value,
            "UW1kaDJ5d2hmclJmWmQ2elFrcnpSdDdTM1dCOUFLQnJ3dHBIQ0RGUm5OWmhTcA==",
        )

    def test_valid_bump_sequence_operation(self):
        raw_data = load_horizon_file("operations/bump_sequence.json")
        parsed_data = BumpSequenceOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150675003296243713")
        self.assertEqual(parsed_data.paging_token, "150675003296243713")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GC37FPMWRUEMIEIMMR7L32NMIJLZJ6W3UYKEAN2M5YKX4TPZMQ4HZWWQ",
        )
        self.assertEqual(parsed_data.type, "bump_sequence")
        self.assertEqual(parsed_data.type_i, 11)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 10, 54, 19, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "7cf9775c27cf2f386a25fd871cd951fe715eca16e28ff45495cb7c3add389f6d",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.bump_to, 136025045943191412)

    def test_valid_manage_buy_offer_operation(self):
        raw_data = load_horizon_file("operations/manage_buy_offer.json")
        parsed_data = ManageBuyOfferOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150661598703333378")
        self.assertEqual(parsed_data.paging_token, "150661598703333378")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GBYUYEAO52BYHZEUMLHMHM5SWENBB2RHKAGDVAKBUHZLJTSSRMR6SZYL",
        )
        self.assertEqual(parsed_data.type, "manage_buy_offer")
        self.assertEqual(parsed_data.type_i, 12)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 6, 12, 36, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "0c52b9b2136bc32ca636f30cd44c72f4d532d50759c09d9ec103ffa749d0e501",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.amount, Decimal("389.4340658"))
        self.assertEqual(parsed_data.price, Decimal("2.3058668"))
        self.assertEqual(parsed_data.price_r.d, 2500000)
        self.assertEqual(parsed_data.price_r.n, 5764667)
        self.assertEqual(parsed_data.buying_asset_type, "native")
        self.assertEqual(parsed_data.buying_asset_code, None)
        self.assertEqual(parsed_data.buying_asset_issuer, None)
        self.assertEqual(parsed_data.selling_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.selling_asset_code, "XXA")
        self.assertEqual(
            parsed_data.selling_asset_issuer,
            "GC4HS4CQCZULIOTGLLPGRAAMSBDLFRR6Y7HCUQG66LNQDISXKIXXADIM",
        )
        self.assertEqual(parsed_data.offer_id, "0")

    def test_valid_path_payment_strict_send_operation(self):
        raw_data = load_horizon_file("operations/path_payment_strict_send.json")
        parsed_data = PathPaymentStrictSendOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150660589386170369")
        self.assertEqual(parsed_data.paging_token, "150660589386170369")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GDBKRQWEUJGRWWCAGK75L4PZXM2S3DQQIG6S43Y2GMN3IUFZWCLSRA46",
        )
        self.assertEqual(parsed_data.type, "path_payment_strict_send")
        self.assertEqual(parsed_data.type_i, 13)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 51, 27, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "add2a945914c8090a8f889e6fe6177c58fea0fe2c361893612462d0601f2eb31",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "BTC")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GAUTUYY2THLF7SGITDFMXJVYH3LHDSMGEAKSBU267M2K7A3W543CKUEF",
        )
        self.assertEqual(
            parsed_data.from_,
            "GDBKRQWEUJGRWWCAGK75L4PZXM2S3DQQIG6S43Y2GMN3IUFZWCLSRA46",
        )
        self.assertEqual(
            parsed_data.to, "GDBKRQWEUJGRWWCAGK75L4PZXM2S3DQQIG6S43Y2GMN3IUFZWCLSRA46"
        )
        self.assertEqual(parsed_data.amount, Decimal("0.0005045"))
        self.assertEqual(len(parsed_data.path), 2)
        self.assertEqual(parsed_data.path[0].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.path[0].asset_code, "ETH")
        self.assertEqual(
            parsed_data.path[0].asset_issuer,
            "GBDEVU63Y6NTHJQQZIKVTC23NWLQVP3WJ2RI2OTSJTNYOIGICST6DUXR",
        )
        self.assertEqual(parsed_data.path[1].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.path[1].asset_code, "USDT")
        self.assertEqual(
            parsed_data.path[1].asset_issuer,
            "GCQTGZQQ5G4PTM2GL7CDIFKUBIPEC52BROAQIAPW53XBRJVN6ZJVTG6V",
        )
        self.assertEqual(parsed_data.source_amount, Decimal("57.4988800"))
        self.assertEqual(parsed_data.destination_min, Decimal("0.0004995"))
        self.assertEqual(parsed_data.source_asset_type, "native")
        self.assertEqual(parsed_data.source_asset_code, None)
        self.assertEqual(parsed_data.source_asset_issuer, None)

    def test_valid_create_claimable_balance_operation(self):
        raw_data = load_horizon_file("operations/create_claimable_balance.json")
        parsed_data = CreateClaimableBalanceOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150684654087864322")
        self.assertEqual(parsed_data.paging_token, "150684654087864322")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(parsed_data.type, "create_claimable_balance")
        self.assertEqual(parsed_data.type_i, 14)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 14, 16, 59, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "bc00281659b1b3d25674fd078c294036476dbbde37403e70ab66b651fd829c18",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(
            parsed_data.sponsor,
            "GBGJB2WEIQCCUZYISUKAFRPR46LQ62O7W6CDKN52NVROG44LLL3L73X2",
        )
        self.assertEqual(
            parsed_data.asset,
            "USDPEND:GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(parsed_data.amount, Decimal("900"))
        self.assertEqual(len(parsed_data.claimants), 2)
        self.assertEqual(
            parsed_data.claimants[0].destination,
            "GBHNGLLIE3KWGKCHIKMHJ5HVZHYIK7WTBE4QF5PLAKL4CJGSEU7HZIW5",
        )
        self.assertEqual(parsed_data.claimants[0].predicate.unconditional, True)
        self.assertEqual(
            parsed_data.claimants[1].destination,
            "GCBMP2WKIAX7KVDRCSFXJWFM5P7HDCGTCC76U5XR52OYII6AOWS7G3DT",
        )
        self.assertEqual(
            parsed_data.claimants[1].predicate.not_predicate.abs_before,
            datetime.datetime(2021, 4, 26, 4, 0, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.claimants[1].predicate.not_predicate.abs_before_epoch,
            1619409600,
        )

    def test_valid_claim_claimable_balance_operation(self):
        raw_data = load_horizon_file("operations/claim_claimable_balance.json")
        parsed_data = ClaimClaimableBalanceOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "2730894825627649")
        self.assertEqual(parsed_data.paging_token, "2730894825627649")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GAEY7JFLBBDD6PAUPVRVKMBNSL5W6GYMUOGJKNGHGFSFGJU6CT2IUARS",
        )
        self.assertEqual(parsed_data.type, "claim_claimable_balance")
        self.assertEqual(parsed_data.type_i, 15)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 25, 1, 37, 30, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "ebf78969b439f9b6c0777695c76a668e5baabe747696fbef7fc7d40b5cbe9a6d",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.balance_id,
            "00000000a5c8c85c12a32ec1b30fc1792a542ca38702afd78eb4fe524d028887cf6b6952",
        )
        self.assertEqual(
            parsed_data.claimant,
            "GAEY7JFLBBDD6PAUPVRVKMBNSL5W6GYMUOGJKNGHGFSFGJU6CT2IUARS",
        )

    def test_valid_begin_sponsoring_future_reserves_operation(self):
        raw_data = load_horizon_file("operations/begin_sponsoring_future_reserves.json")
        parsed_data = BeginSponsoringFutureReservesOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150660619450806273")
        self.assertEqual(parsed_data.paging_token, "150660619450806273")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GDDUVW72OCNRAVL752HXYJQTXEJQRYHDWU76YKGDEWZ5HCATZBSKJM7Y",
        )
        self.assertEqual(parsed_data.type, "begin_sponsoring_future_reserves")
        self.assertEqual(parsed_data.type_i, 16)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 52, 6, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "41d80b1509a355d45271e0058c7ceac8ee616c2b5215bdb664ec55e50d2bad6c",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.sponsored_id,
            "GDS6ULV46WVSO2USGIVTIUDYBL3ROBPQEEANE3AY6XZION25DCNFIE2R",
        )

    def test_valid_end_sponsoring_future_reserves_operation(self):
        raw_data = load_horizon_file("operations/end_sponsoring_future_reserves.json")
        parsed_data = EndSponsoringFutureReservesOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150660606565855256")
        self.assertEqual(parsed_data.paging_token, "150660606565855256")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GD6XEQ7YNR2EQIDWFX6AISIPKKVBC5GXBV4X5GL73QUUZK5GMWJIN3LW",
        )
        self.assertEqual(parsed_data.type, "end_sponsoring_future_reserves")
        self.assertEqual(parsed_data.type_i, 17)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 24, 5, 51, 49, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "4e4e2cc4ed2e31091db53762d74340f3689431b88321acc1c0935bbced6aa252",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.begin_sponsor,
            "GDDUVW72OCNRAVL752HXYJQTXEJQRYHDWU76YKGDEWZ5HCATZBSKJM7Y",
        )

    def test_valid_revoke_sponsorship_operation(self):
        raw_data = load_horizon_file("operations/revoke_sponsorship.json")
        parsed_data = RevokeSponsorshipOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "2731345797189633")
        self.assertEqual(parsed_data.paging_token, "2731345797189633")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GDD6DIT7PDSB6PZ5B5SBUKQBIHZDWWBZN4LCFDEHYIYI4DNTC4WXL4ZO",
        )
        self.assertEqual(parsed_data.type, "revoke_sponsorship")
        self.assertEqual(parsed_data.type_i, 18)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 4, 25, 1, 46, 45, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "8a9cb28209126c9ac3691eca753f492606318268a0c3d27359e28ccd9bad0588",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.account_id,
            "GBAG5JOFNNE7B2FXLZGLV56U5NR2ZFHRS6FALKCX3W5CND27W4DM7TBX",
        )

    def test_valid_clawback_operation(self):
        raw_data = load_horizon_file("operations/clawback.json")
        parsed_data = ClawbackOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "3510036252856321")
        self.assertEqual(parsed_data.paging_token, "3510036252856321")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GCHYD6AWPR2PN66JFFDR63OEFO5RMOUGFL7D3BBUEMTJDMUFHPLNX2SC",
        )
        self.assertEqual(parsed_data.type, "clawback")
        self.assertEqual(parsed_data.type_i, 19)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 2, 28, 28, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "7c4b7f6ef383afba397b20628b1f2556d72eb092dc8b875093e9b92cde1b4889",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.asset_code, "Hello")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GCHYD6AWPR2PN66JFFDR63OEFO5RMOUGFL7D3BBUEMTJDMUFHPLNX2SC",
        )
        self.assertEqual(
            parsed_data.from_,
            "GCDG7N63GJMJDI4627LY3XKNZARQNX3QFY6HAWON3JDAS3SCGINGQHEQ",
        )
        self.assertEqual(parsed_data.amount, Decimal("1234"))

    def test_valid_clawback_claimable_balance_operation(self):
        raw_data = load_horizon_file("operations/clawback_claimable_balance.json")
        parsed_data = ClawbackClaimableBalanceOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "3513936083165185")
        self.assertEqual(parsed_data.paging_token, "3513936083165185")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GD5YHBKE7FSUUZIOSL4ED6UKMM2HZAYBYGZI7KRCTMFDTOO6SGZCQB4Z",
        )
        self.assertEqual(parsed_data.type, "clawback_claimable_balance")
        self.assertEqual(parsed_data.type_i, 20)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 3, 48, 5, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "8820306ee424f47fd1c16b28ab034a3bdab0147fc16c65b145ba1df5f338c8a2",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.balance_id,
            "000000001fe36f3ce6ab6a6423b18b5947ce8890157ae77bb17faeb765814ad040b74ce1",
        )

    def test_valid_set_trust_line_flags_operation(self):
        raw_data = load_horizon_file("operations/set_trust_line_flags.json")
        parsed_data = SetTrustLineFlagsOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "3513373442449409")
        self.assertEqual(parsed_data.paging_token, "3513373442449409")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GD5YHBKE7FSUUZIOSL4ED6UKMM2HZAYBYGZI7KRCTMFDTOO6SGZCQB4Z",
        )
        self.assertEqual(parsed_data.type, "set_trust_line_flags")
        self.assertEqual(parsed_data.type_i, 21)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 5, 6, 3, 36, 35, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "b1e3090a209925e38cee64ce451a85e0a15cff311963b7548f1931dc3af5b7fb",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.asset_code, "Hello")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GD5YHBKE7FSUUZIOSL4ED6UKMM2HZAYBYGZI7KRCTMFDTOO6SGZCQB4Z",
        )
        self.assertEqual(
            parsed_data.trustor,
            "GAYWF2KJ4RVFBACNI7W2YVSLEQOUHEMPGJIZCDXHCF2BFR2V7O55UWBB",
        )
        self.assertEqual(parsed_data.set_flags, [1])
        self.assertEqual(parsed_data.set_flags_s, ["authorized"])
        self.assertEqual(parsed_data.clear_flags, [4])
        self.assertEqual(parsed_data.clear_flags_s, ["clawback_enabled"])

    def test_valid_liquidity_pool_deposit_operation(self):
        raw_data = load_horizon_file("operations/liquidity_pool_deposit.json")
        parsed_data = LiquidityPoolDepositOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "1579044726386689")
        self.assertEqual(parsed_data.paging_token, "1579044726386689")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.source_account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(parsed_data.source_account_muxed_id, 1278881)
        self.assertEqual(parsed_data.type, "liquidity_pool_deposit")
        self.assertEqual(parsed_data.type_i, 22)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 6, 32, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "81e9fb3781ece5031b304d0ced21b5f673cfc4581861de99b7751f2f4c905b50",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.liquidity_pool_id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.min_price, Decimal("1.0000000"))
        self.assertEqual(parsed_data.min_price_r.n, 1)
        self.assertEqual(parsed_data.min_price_r.d, 1)

        self.assertEqual(len(parsed_data.reserves_max), 2)
        self.assertEqual(
            parsed_data.reserves_max[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_max[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_max[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.reserves_max[0].amount, Decimal("250.0000000"))
        self.assertEqual(
            parsed_data.reserves_max[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_max[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_max[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.reserves_max[1].amount, Decimal("250.0000000"))
        self.assertEqual(parsed_data.max_price, Decimal("2.0000000"))
        self.assertEqual(parsed_data.max_price_r.n, 2)
        self.assertEqual(parsed_data.max_price_r.d, 1)
        self.assertEqual(len(parsed_data.reserves_deposited), 2)
        self.assertEqual(
            parsed_data.reserves_deposited[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_deposited[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_deposited[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(
            parsed_data.reserves_deposited[0].amount, Decimal("250.0000000")
        )
        self.assertEqual(
            parsed_data.reserves_deposited[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_deposited[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_deposited[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.reserves_max[1].amount, Decimal("250.0000000"))
        self.assertEqual(parsed_data.shares_received, Decimal("250.0000000"))

    def test_valid_liquidity_pool_withdraw_operation(self):
        raw_data = load_horizon_file("operations/liquidity_pool_withdraw.json")
        parsed_data = LiquidityPoolWithdrawOperation.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "1579096265998337")
        self.assertEqual(parsed_data.paging_token, "1579096265998337")
        self.assertEqual(parsed_data.transaction_successful, True)
        self.assertEqual(
            parsed_data.source_account,
            "GAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2V2K",
        )
        self.assertEqual(
            parsed_data.source_account_muxed,
            "MAQXAWHCM4A7SQCT3BOSVEGRI2OOB7LO2CMFOYFF6YRXU4VQSB5V2AAAAAAAAE4DUGF2O",
        )
        self.assertEqual(parsed_data.source_account_muxed_id, 1278881)
        self.assertEqual(parsed_data.type, "liquidity_pool_withdraw")
        self.assertEqual(parsed_data.type_i, 23)
        self.assertEqual(
            parsed_data.created_at,
            datetime.datetime(2021, 10, 7, 18, 7, 37, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(
            parsed_data.transaction_hash,
            "c37a86a8b4291a1afceca7ffea12e65c0d32c875ebf53820bb009a15831ea23e",
        )
        self.assertEqual(parsed_data.transaction, None)
        self.assertEqual(parsed_data.sponsor, None)
        self.assertEqual(
            parsed_data.liquidity_pool_id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )

        self.assertEqual(len(parsed_data.reserves_min), 2)
        self.assertEqual(
            parsed_data.reserves_min[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_min[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_min[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.reserves_min[0].amount, Decimal("100.0000000"))
        self.assertEqual(
            parsed_data.reserves_min[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_min[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_min[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(parsed_data.reserves_min[1].amount, Decimal("100.0000000"))
        self.assertEqual(parsed_data.shares, Decimal("100.0000000"))
        self.assertEqual(len(parsed_data.reserves_received), 2)
        self.assertEqual(
            parsed_data.reserves_received[0].asset.asset_type, "credit_alphanum4"
        )
        self.assertEqual(parsed_data.reserves_received[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves_received[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(
            parsed_data.reserves_received[0].amount, Decimal("100.0000000")
        )
        self.assertEqual(
            parsed_data.reserves_received[1].asset.asset_type, "credit_alphanum12"
        )
        self.assertEqual(parsed_data.reserves_received[1].asset.asset_code, "SONESO")
        self.assertEqual(
            parsed_data.reserves_received[1].asset.asset_issuer,
            "GAOF7ARG3ZAVUA63GCLXG5JQTMBAH3ZFYHGLGJLDXGDSXQRHD72LLGOB",
        )
        self.assertEqual(
            parsed_data.reserves_received[1].amount, Decimal("100.0000000")
        )
