==========
Change Log
==========

This document records all notable changes to `stellar-model <https://github.com/StellarCN/stellar-model/>`_.

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