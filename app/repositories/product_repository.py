from loguru import logger
from sqlalchemy import text
from app.configuration.database import db
from sqlalchemy.exc import SQLAlchemyError
from app.responses.product_response import ProductResponse
from app.repositories.queries.product_query import (
    CREATE_SELLER_PRODUCT_QUERY,
    DEACTIVATE_SELLER_PRODUCTS_QUERY,
    GET_ALL_SELLER_ACTIVE_PRODUCTS_QUERY,
    GET_MARKET_SUMMARY_QUERY
)


class ProductRepository:
    """Manage Catalogue records & embeddings"""

    def add_new_seller_product(self, product_record: ProductResponse):
        try:
            params = product_record.model_copy().model_dump()
            db.execute(text(CREATE_SELLER_PRODUCT_QUERY), params)
            db.commit()
            logger.debug(f"New product created. uuid: {params['uuid']}")
        except SQLAlchemyError as ex:
            db.rollback()
            logger.error(f"Error saving product. uuid {params['uuid']}. Error: {ex}")
    
    def deactivate_seller_products(self, seller_uuid: str):
        result = None
        try:
            params = {'seller_uuid': seller_uuid}
            db.execute(text(DEACTIVATE_SELLER_PRODUCTS_QUERY), params)
            logger.debug(f"products deactivated. Seller_uuid: {seller_uuid}")
            db.commit()
        except SQLAlchemyError as ex:
            db.rollback()
            logger.error(f"Error deactivating seller products. Error: {ex}")
        return result
    
    def get_all_active_seller_products(self, seller_uuid):
        result = 'error'
        try:
            params = {'seller_uuid': seller_uuid}
            result = db.execute(text(GET_ALL_SELLER_ACTIVE_PRODUCTS_QUERY), params).fetchall()
            db.commit()
        except SQLAlchemyError as ex:
            db.rollback()
            logger.error(f"Error getting active products. seller_uuid: {seller_uuid}. Error: {ex}")
        return result
    
    def get_market_summary(self):
        result='error'
        try:
            result = db.execute(text(GET_MARKET_SUMMARY_QUERY)).fetchall()
            db.commit()
        except SQLAlchemyError as ex:
            db.rollback()
            logger.error(f"Error getting market_summary. Error: {ex}")
        return result
