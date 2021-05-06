# TODO

## Test

### operations

| type_i |               type               | tested |
| :----: | :------------------------------: | :----: |
|    0   |          create_account          |   yes  |
|    1   |              payment             |   yes  |
|    2   |    path_payment_strict_receive   |   yes  |
|    3   |         manage_sell_offer        |   yes  |
|    4   |     create_passive_sell_offer    |   yes  |
|    5   |            set_options           |   yes  |
|    6   |           change_trust           |   yes  |
|    7   |            allow_trust           |   yes  |
|    8   |           account_merge          |   yes  |
|    9   |             inflation            |   yes  |
|   10   |            manage_data           |   yes  |
|   11   |           bump_sequence          |   yes  |
|   12   |         manage_buy_offer         |   yes  |
|   13   |     path_payment_strict_send     |   yes  |
|   14   |     create_claimable_balance     |   yes  |
|   15   |      claim_claimable_balance     |   yes  |
|   16   | begin_sponsoring_future_reserves |   yes  |
|   17   |  end_sponsoring_future_reserves  |   yes  |
|   18   |        revoke_sponsorship        |   yes  |
|   19   |             clawback             |   yes  |
|   20   |    clawback_claimable_balance    |   yes  |
|   21   |       set_trust_line_flags       |   yes  |

### effects

| type_i |                     type                     | tested |
| :----: | :------------------------------------------: | :----: |
|    0   |                account_created               |   yes  |
|    1   |                account_removed               |   yes  |
|    2   |               account_credited               |   yes  |
|    3   |                account_debited               |   yes  |
|    4   |          account_thresholds_updated          |   yes  |
|    5   |          account_home_domain_updated         |   yes  |
|    6   |             account_flags_updated            |   yes  |
|    7   |     account_inflation_destination_updated    |   yes  |
|   10   |                signer_created                |   yes  |
|   11   |                signer_removed                |   yes  |
|   12   |                signer_updated                |   yes  |
|   20   |               trustline_created              |   yes  |
|   21   |               trustline_removed              |   yes  |
|   22   |               trustline_updated              |   yes  |
|   23   |             trustline_authorized             |   yes  |
|   24   |            trustline_deauthorized            |   yes  |
|   25   | trustline_authorized_to_maintain_liabilities |   yes  |
|   26   |            trustline_flags_updated           |   yes  |
|   30   |                 offer_created                |   no   |
|   31   |                 offer_removed                |   no   |
|   32   |                 offer_updated                |   no   |
|   33   |                     trade                    |   yes  |
|   40   |                 data_created                 |   yes  |
|   41   |                 data_removed                 |   yes  |
|   42   |                 data_updated                 |   yes  |
|   43   |                sequence_bumped               |   yes  |
|   50   |           claimable_balance_created          |   yes  |
|   51   |      claimable_balance_claimant_created      |   yes  |
|   52   |           claimable_balance_claimed          |   yes  |
|   60   |          account_sponsorship_created         |   yes  |
|   61   |          account_sponsorship_updated         |   no   |
|   62   |          account_sponsorship_removed         |   yes  |
|   63   |         trustline_sponsorship_created        |   yes  |
|   64   |         trustline_sponsorship_updated        |   no   |
|   65   |         trustline_sponsorship_removed        |   yes  |
|   66   |           data_sponsorship_created           |   yes  |
|   67   |           data_sponsorship_updated           |   no   |
|   68   |           data_sponsorship_removed           |   yes  |
|   69   |     claimable_balance_sponsorship_created    |   yes  |
|   70   |     claimable_balance_sponsorship_updated    |   no   |
|   71   |     claimable_balance_sponsorship_removed    |   yes  |
|   72   |          signer_sponsorship_created          |   yes  |
|   73   |          signer_sponsorship_updated          |   no   |
|   74   |          signer_sponsorship_removed          |   yes  |
|   80   |         claimable_balance_clawed_back        |   yes  |