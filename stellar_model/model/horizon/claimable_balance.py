from datetime import datetime
from decimal import Decimal
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


__all__ = ["ClaimableBalance"]


class Links(BaseModel):
    self: Link
    transactions: Link
    operations: Link


class ClaimPredicate(BaseModel):
    """
    Represents a claimant predicate.
    """

    # TODO: add type in the future.
    unconditional: Optional[bool] = Field(
        description="If **True** it means this clause of the condition "
        "is always satisfied."
    )
    # https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
    and_predicates: Optional[List["ClaimPredicate"]] = Field(
        alias="and",
        description="The array will always contain "
        "two elements which also are "
        "predicates. This clause of the "
        "condition is satisfied if both "
        "of the two elements in the array "
        "are satisfied.",
    )
    or_predicates: Optional[List["ClaimPredicate"]] = Field(
        alias="or",
        description="The array will always contain two "
        "elements which also are "
        "predicates. This clause of the "
        "condition is satisfied if at "
        "least one of the two elements "
        "in the array are satisfied.",
    )
    not_predicate: Optional["ClaimPredicate"] = Field(
        alias="not",
        description="The value is also a predicate. This "
        "clause of the condition is satisfied "
        "if the value is not satisfied.",
    )
    abs_before: Optional[datetime] = Field(
        description="The datetime representing a deadline for when the claimable "
        "balance can be claimed. If the balance is claimed before the "
        "date then this clause of the condition is satisfied."
    )
    abs_before_epoch: Optional[int] = Field(
        "The Unix Epoch value represented by the same custom extended "
        "ISO date value in the abs_before field."
    )
    rel_before: Optional[int] = Field(
        description="A relative deadline for when the claimable balance can be "
        "claimed. The value represents the number of seconds since the "
        "close time of the ledger which created the claimable balance."
    )


class Claimant(BaseModel):
    """
    Represents a claimable balance claimant.
    """

    destination: str = Field(description="The account ID who can claim the balance.")
    predicate: ClaimPredicate = Field(
        description="The condition which must be satisfied so **destination** can claim the balance."
    )


class ClaimableBalanceFlags(BaseModel):
    """
    Represents the state of a claimable balance's flags.
    """

    clawback_enabled: bool


class ClaimableBalance(BaseModel):
    """
    Represents a claimable balance.
    """

    id: str = Field(description="A unique identifier for this claimable balance.")
    asset: str = Field(
        description="The asset available to be claimed in the "
        "**SEP-11 form asset_code:issuing_address** or **native** (for XLM)"
    )
    amount: Decimal = Field(description="The amount of **asset** that can be claimed.")
    sponsor: Optional[str] = Field(
        description="The account id of the sponsor who is paying the reserves for this claimable balance."
    )
    last_modified_ledger: int = Field(
        description="The sequence number of the last ledger in which this claimable balance was modified."
    )
    last_modified_time: Optional[datetime] = Field(
        description="The datetime of last modification time."
    )
    claimants: List[Claimant] = Field(
        description="The list of entries which could claim the claimable balance."
    )
    flags: ClaimableBalanceFlags
    paging_token: str = Field(description="A cursor value for use in pagination.")
    links: Links = Field(alias="_links")


ClaimPredicate.update_forward_refs()
