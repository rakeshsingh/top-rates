from typing import Optional, Annotated, List
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Field as PydanticField, HttpUrl, field_validator
from datetime import datetime, date
from enum import Enum
from decimal import Decimal


class ProductType(str, Enum):
    """Types of bank accounts"""

    SAVINGS = "Savings"
    # CHECKING = "Checking"
    MONEY_MARKET = "Money Market"
    CD = "Certificate of Deposit"
    HIGH_YIELD_SAVINGS = "High-Yield Savings"
    # STUDENT_SAVINGS = "student_savings"
    # BUSINESS_SAVINGS = "business_savings"
    # BUSINESS_CHECKING = "business_checking"
    # INTEREST_CHECKING = "interest_checking"


class BankType(str, Enum):
    """Classification of banks"""

    NATIONAL = "national"
    REGIONAL = "regional"
    COMMUNITY = "community"
    CREDIT_UNION = "credit_union"
    ONLINE = "online"


class CDTerm(str, Enum):
    """CD term lengths"""

    THREE_MONTHS = "3_months"
    SIX_MONTHS = "6_months"
    NINE_MONTHS = "9_months"
    ONE_YEAR = "1_year"
    EIGHTEEN_MONTHS = "18_months"
    TWO_YEARS = "2_years"
    THREE_YEARS = "3_years"
    FIVE_YEARS = "5_years"
    TEN_YEARS = "10_years"


class InterestCompoundingFrequency(str, Enum):
    """How often interest is compounded"""

    DAILY = "daily"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    ANNUALLY = "annually"


class Bank(SQLModel, table=True):
    """Bank or financial institution"""

    __tablename__: str = "banks"
    id: str = Field(primary_key=True, description="Unique identifier for the bank")
    name: str = Field(..., description="Official name of the bank")
    old_name: str = Field(
        None, description="Previous name of the bank, if it has changed"
    )
    rss_id: Optional[str] = Field(None, description="RSS feed identifier for the bank")
    uninum: Optional[str] = Field(None, description="UNINUM identifier for the bank")
    type: str = Field(
        None,
        description="Classification of the bank (e.g., national, regional, credit union)",
    )
    routing_number: Optional[str] = Field(
        None, description="9-digit ABA routing number"
    )
    website: Optional[str] = Field(None, description="Official website URL of the bank")
    zipcode: Optional[str] = Field(None, description="Zipcode of the bank headquarters")
    # bank_address: str = Field(..., description="Street address of the bank headquarters")
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="When this bank record was created"
    )
    last_updated: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this bank's data was last updated",
    )


class BankProduct(SQLModel, table=True):
    """Products offered by a Bank or a Financial Institution"""

    __tablename__: str = "bank_products"
    id: Optional[int] = Field(default=None, primary_key=True)
    bank_id: str = Field(..., description="Unique identifier for the bank")
    bank_name: Optional[str] = Field(
        ..., description="Name of the bank offering this product"
    )
    bank_url: Optional[str] = Field(
        ..., description="Website of the bank offering this interest rate"
    )
    bank_logo_url: Optional[str] = Field(
        ..., description="Website of the bank offering this interest rate"
    )
    name: str = Field(..., description="Name of the financial product")
    type: ProductType = Field(..., description="Type of financial product")
    description: Optional[str] = Field(
        None, description="Description of the financial product"
    )
    product_url: Optional[str] = Field(None, description="URL to the product")
    apy: Decimal = Field(..., description="Annual Percentage Yield (APY) as a decimal")
    min_deposit: Optional[Decimal] = Field(
        None, description="Minimum balance required to earn this interest rate"
    )
    min_balance: Optional[Decimal] = Field(
        None, description="Maximum balance for which this interest rate applies"
    )
    compounding_frequency: InterestCompoundingFrequency = Field(
        ..., description="How often interest is compounded"
    )
    interest_payment_frequency: Optional[InterestCompoundingFrequency] = Field(
        None, description="How often interest is paid out to the account holder"
    )
    additional_info: Optional[str] = Field(
        None, description="Additional details about this product interest rate"
    )
    start_date: date = Field(..., description="Date when the rate became effective")
    end_date: Optional[date] = Field(
        None, description="Date when the rate expires, if applicable"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this interest rate record was created",
    )
    last_updated: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this interest rate was last updated",
    )

