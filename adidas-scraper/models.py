from pydantic import BaseModel
from typing import List, Optional

class SearchProduct(BaseModel):
    productId: str
    modelId: str
    title: str
    subTitle: str
    url: str
    image: str
    priceData: dict
    rating: Optional[float] = None

class ProductAvailability(BaseModel):
    id: str
    availability_status: str
    quantity: int
    variation_list: List[dict]

class SearchResponse(BaseModel):
    count: int
    startIndex: int
    searchTerm: str
    items: List[SearchProduct]
