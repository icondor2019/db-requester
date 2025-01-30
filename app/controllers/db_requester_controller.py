from fastapi import APIRouter, HTTPException, Header
from app.responses.product_response import AvailableRecordsResponse, ActiveProductResponse, MarketSummaryResponse
from app.repositories.product_repository import ProductRepository


api = APIRouter()


__product_repository = ProductRepository()


@api.get(path="/v1/seller/{seller_uuid}/availability")
def get_available_products(seller_uuid: str) -> AvailableRecordsResponse:
    records = __product_repository.get_all_active_seller_products(seller_uuid=seller_uuid)
    if records == 'error':
        raise HTTPException(status_code=404, detail='Error consulting availabilities')

    record_dict = [
        ActiveProductResponse(
            raw_description=i[0],
            stock=i[1],
            price=i[2]
        ) for i in records
    ]

    output = AvailableRecordsResponse(error=False, data=record_dict)
    return output

@api.get(path="/v1/market/summary")
def get_market_summary() -> AvailableRecordsResponse:
    records = __product_repository.get_market_summary()
    if records == 'error':
        raise HTTPException(status_code=404, detail='Error consulting availabilities')

    record_dict = [
        MarketSummaryResponse(
            product_uuid=i[0],
            name=i[1],
            color=i[2],
            size=i[3],
            stems=i[4],
            total_sellers=i[5],
            market_stock=i[6],
            avg_seller_stock=i[7],
            avg_price=i[8],
            median_price=i[9],
            max_price=i[10],
            min_price=i[11]
        ) for i in records
    ]

    output = AvailableRecordsResponse(error=False, data=record_dict)
    return output
