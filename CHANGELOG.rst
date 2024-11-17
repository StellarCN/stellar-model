==========
Change Log
==========

This document records all notable changes to `stellar-model <https://github.com/StellarCN/stellar-model/>`_.

0.6.0
----------------------------
* feat: add support for Horizon v22.0.0. (`#62 <https://github.com/StellarCN/stellar-model/pull/62/>`_)

0.5.4
----------------------------
* feat: add support for Horizon v2.27.0. (`#59 <https://github.com/StellarCN/stellar-model/pull/59/>`_)

0.5.3
----------------------------
* deps: bump pydantic to v2. (`#48 <https://github.com/StellarCN/stellar-model/pull/48/>`_)
* fix: bug fixes.

0.5.2
----------------------------
* fix: fix model for `LiquidityPoolRemovedEffect`. (`#43 <https://github.com/StellarCN/stellar-model/pull/43/>`_)

0.5.1
----------------------------
* feat: add `EffectResponse` to parse single effect. (`#36 <https://github.com/StellarCN/stellar-model/pull/36/>`_)

0.5.0
----------------------------
* feat: add support for Horizon `v2.17.0 <https://github.com/stellar/go/releases/tag/horizon-v2.17.0>`_. (`#31 <https://github.com/StellarCN/stellar-model/pull/31/>`_)

0.4.1b0
----------------------------
* feat: add support for order book endpoint.

0.4.0b0
----------------------------
* feat: add support for horizon-v2.13.0

0.3.1b0
----------------------------
* fix: ClaimPredicate.rel_before, Optional[datetime] -> Optional[int]

0.3.0b0
----------------------------
This release contains breaking updates.

You can check the `release log of horizon-v2.9.0-rc1 <https://github.com/stellar/go/releases/tag/horizon-v2.9.0rc1>`_ and `Horizon Liquidity Pool API Docs <https://docs.google.com/document/d/1pXL8kr1a2vfYSap9T67R-g72B_WWbaE1YsLMa04OgoU/edit#heading=h.bexstdt2tlbj>`_. (`Download Horizon Liquidity Pool API.pdf <https://github.com/StellarCN/stellar-model/files/7315193/Horizon.Liquidity.Pool.API.pdf>`_)

* feat: add support for horizon-v2.9.0~rc1 (`#21 <https://github.com/StellarCN/stellar-model/pull/21/>`_)

0.2.2b0
------------------------
* fix: make `ClaimableBalance.last_modified_time` and `Offer.last_modified_time` optional.

0.2.1b0
------------------------
* fix: make `Account.last_modified_time` optional. (`#19 <https://github.com/StellarCN/stellar-model/pull/19/>`_)

0.2.0b0
------------------------
* feat: add support for muxed account.

0.1.0b1
------------------------
* Bug fix.

0.1.0b0
------------------------
* First beta release.