from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    uuid: str = Field(...)
    seller_uuid: str = Field(...)
    product_uuid: str = Field(...)
    raw_description: str = Field(default=None)
    stock: int = Field(...)
    price: float = Field(...)
    status: str = Field(default='active')

    class Config:
        from_attributes = True


class ActiveProductResponse(BaseModel):
    raw_description: str = Field(default=None)
    stock: int = Field(...)
    price: float = Field(...)

class MarketSummaryResponse(BaseModel):
    product_uuid: str
    name: str
    color: str
    size: int
    stems: int
    total_sellers: int
    market_stock: int
    avg_seller_stock: float
    avg_price: float
    median_price: float
    max_price: float
    min_price: float

class AvailableRecordsResponse(BaseModel):
    error: bool
    data: list
