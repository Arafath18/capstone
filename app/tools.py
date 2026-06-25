from google.adk.tools import ToolContext

async def get_inventory_levels() -> dict:
    """Fetches current inventory levels for products."""
    return {
        "status": "success",
        "data": [
            {"product_id": "SKU-1001", "name": "Wireless Mouse", "stock": 50, "reorder_point": 60},
            {"product_id": "SKU-1002", "name": "Mechanical Keyboard", "stock": 15, "reorder_point": 20},
            {"product_id": "SKU-1003", "name": "USB-C Hub", "stock": 120, "reorder_point": 50}
        ]
    }

async def get_sales_history() -> dict:
    """Fetches historical sales data for forecasting."""
    return {
        "status": "success",
        "data": [
            {"product_id": "SKU-1001", "last_30_days_sales": 120, "trend": "steady"},
            {"product_id": "SKU-1002", "last_30_days_sales": 45, "trend": "increasing"},
            {"product_id": "SKU-1003", "last_30_days_sales": 200, "trend": "decreasing"}
        ]
    }

async def get_supplier_delays() -> dict:
    """Fetches known supplier delays."""
    return {
        "status": "success",
        "data": [
            {"supplier": "TechParts Inc", "delay_days": 5, "affected_products": ["SKU-1002"]}
        ]
    }
