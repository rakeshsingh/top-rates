from typing import Optional, Annotated, List
from sqlmodel import Field, Session, SQLModel, create_engine, select
from pydantic import BaseModel, Field as PydanticField, HttpUrl, field_validator
from datetime import datetime, date
from enum import Enum
from decimal import Decimal


class ProductType(str, Enum):
    """Types of bank accounts"""
    SAVINGS = "savings"
    CHECKING = "checking"
    MONEY_MARKET = "money_market"
    CD = "certificate_of_deposit"
    HIGH_YIELD_SAVINGS = "high_yield_savings"
    STUDENT_SAVINGS = "student_savings"
    BUSINESS_SAVINGS = "business_savings"
    BUSINESS_CHECKING = "business_checking"
    INTEREST_CHECKING = "interest_checking"


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
    __table_name__ = "banks"
    id: str = Field(primary_key=True, description="Unique identifier for the bank")
    name: str = Field(..., description="Official name of the bank")
    old_name: str = Field(
        None,
        description="Previous name of the bank, if it has changed") 
    rss_id: Optional[str] = Field(
        None,
        description="RSS feed identifier for the bank")
    uninum: Optional[str] = Field(
        None,
        description="UNINUM identifier for the bank"
    )
    type: str = Field(
        None,
        description="Classification of the bank (e.g., national, regional, credit union)"
    )
    routing_number: Optional[str] = Field(
        None,
        description="9-digit ABA routing number"
    )
    website: Optional[str] = Field(
        None,
        description="Official website URL of the bank"
    )
    zipcode: Optional[str] = Field(
        None,
        description="Zipcode of the bank headquarters")
    # bank_address: str = Field(..., description="Street address of the bank headquarters")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this bank record was created"
    )
    last_updated: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this bank's data was last updated"
    )


class FinancialProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    bank_id: str = Field(..., description="Unique identifier for the bank")
    bank_name: Optional[str] = Field(..., description="Name of the bank offering this product")
    bank_website: Optional[str] = Field(..., description="Website of the bank offering this interest rate")
    
    product_type: ProductType = Field(..., description="Type of financial product")
    product_name: str = Field(..., description="Name of the financial product")
    apy: Decimal = Field(..., description="Annual Percentage Yield (APY) as a decimal")
    rate_start_date: date = Field(..., description="Date when the rate became effective")
    rate_end_date: Optional[date] = Field(None, description="Date when the rate expires, if applicable")
    compounding_frequency: InterestCompoundingFrequency = Field(..., description="How often interest is compounded")
    cd_term: Optional[CDTerm] = Field(None,
        description="Term length for Certificate of Deposit (CD) accounts"
    )
    minimum_balance: Optional[Decimal] = Field(
        None,
        description="Minimum balance required to earn this interest rate"
    )
    maximum_balance: Optional[Decimal] = Field(
        None,
        description="Maximum balance for which this interest rate applies"
    )
    additional_details: Optional[str] = Field(
        None,
        description="Additional details about this product interest rate"
    )
    last_updated: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this interest rate was last updated"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When this interest rate record was created"
    )