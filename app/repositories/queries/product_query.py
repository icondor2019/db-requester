CREATE_SELLER_PRODUCT_QUERY = """
    INSERT INTO `products` (uuid, seller_uuid, product_uuid, raw_description, stock, price, status)
    VALUES (:uuid, :seller_uuid, :product_uuid, :raw_description, :stock, :price, :status)
"""

DEACTIVATE_SELLER_PRODUCTS_QUERY = """
    UPDATE `products`
    SET
        status = 'inactive'
    WHERE seller_uuid = :seller_uuid
    AND status = 'active'
"""

GET_ALL_SELLER_ACTIVE_PRODUCTS_QUERY = """
    SELECT
        raw_description,
        stock,
        price
    FROM products
    WHERE seller_uuid = :seller_uuid
    AND status = 'active'
"""

GET_MARKET_SUMMARY_QUERY = """
    SELECT
        p.product_uuid,
        c.name,
        c.color,
        c.size,
        c.stems,
        count(DISTINCT p.seller_uuid) as total_sellers,
        sum(p.stock) as market_stock,
        round(avg(p.stock), 2) as avg_seller_stock,
        round(avg(p.price), 2) as avg_price,
        round(median(p.price),2) as median_price,
        max(p.price) as max_price,
        min(p.price) as min_price
    FROM products p
    LEFT JOIN catalogue c
    ON p.product_uuid  = c.uuid
    WHERE status = 'active'
    GROUP BY 1,2,3,4,5
    ORDER BY 2,4 asc
"""