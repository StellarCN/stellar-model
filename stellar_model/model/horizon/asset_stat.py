from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from stellar_model.model.horizon.account import AccountFlags
from stellar_model.model.horizon.link import Link

__all__ = ["AssetStat"]


class Links(BaseModel):
    toml: Link


class AssetStatBalances(BaseModel):
    """
    Represents the summarized balances for a single Asset.
    """

    # TODO: add description
    authorized: Decimal
    authorized_to_maintain_liabilities: Decimal
    unauthorized: Decimal


class AssetStatAccounts(BaseModel):
    """
    Represents the summarized account numbers for a single Asset.
    """

    # TODO: add description
    authorized: int
    authorized_to_maintain_liabilities: int
    unauthorized: int


class AssetStat(BaseModel):
    asset_type: str = Field(
        description="This asset's type. Either **credit_alphanum4** or **credit_alphanum12**."
    )
    asset_code: str = Field(description="This asset's code")
    asset_issuer: str = Field(description="The Stellar address of this asset's issuer.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    contract_id: Optional[str] = Field(description="The contract ID of this asset.")
    num_claimable_balances: int = Field(
        description="The current number of claimable_balances for this asset."
    )
    num_liquidity_pools: int = Field(
        description="The current number of liquidity_pools for this asset."
    )
    num_contracts: int
    accounts: AssetStatAccounts = Field(
        description="The number of accounts grouped by each trustline flag state."
    )
    claimable_balances_amount: Decimal = Field(
        description="The number of units in claimable balances for this asset."
    )
    liquidity_pools_amount: Decimal = Field(
        description="The number of units in liquidity pools for this asset."
    )
    contracts_amount: Decimal
    balances: AssetStatBalances = Field(
        description="The number of units issued for this asset grouped by each trustline flag state."
    )
    flags: AccountFlags = Field(
        description="Flags denote the enabling/disabling of certain asset issuer privileges."
    )
    links: Links = Field(alias="_links")
