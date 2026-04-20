"""Synthetic e-commerce data generation for the ShopSmart sales dashboard."""

import datetime

import numpy as np
import pandas as pd

PRODUCT_CATALOGUE = {
    "Electronics": [
        ("Laptop", 999.00),
        ("Tablet", 499.00),
        ("Smartphone", 299.00),
    ],
    "Accessories": [
        ("Keyboard", 79.00),
        ("Mouse", 29.00),
        ("USB Hub", 39.00),
        ("Cable", 9.00),
    ],
    "Audio": [
        ("Wireless Headphones", 199.00),
        ("Earbuds", 49.00),
        ("Speaker", 99.00),
    ],
    "Wearables": [
        ("Smartwatch", 349.00),
        ("Fitness Tracker", 99.00),
    ],
    "Smart Home": [
        ("Smart Bulb", 19.00),
        ("Smart Plug", 29.00),
        ("Thermostat", 149.00),
    ],
}

_REGIONS = ["North", "South", "East", "West"]
_START_DATE = datetime.date(2024, 1, 1)
_ALL_DATES = [_START_DATE + datetime.timedelta(days=i) for i in range(365)]


def _sample_dates(rng, n):
    indices = rng.integers(0, 365, size=n)
    return [_ALL_DATES[i] for i in indices]


def generate_data(seed=42):
    n = 1000
    rng = np.random.default_rng(seed)

    dates = _sample_dates(rng, n)
    order_ids = [f"ORD-{i:06d}" for i in range(n)]

    categories = list(PRODUCT_CATALOGUE.keys())
    cat_indices = rng.integers(0, len(categories), size=n)

    selected_categories = []
    selected_products = []
    unit_prices = []
    for cat_idx in cat_indices:
        category = categories[cat_idx]
        products = PRODUCT_CATALOGUE[category]
        prod_idx = rng.integers(0, len(products))
        product, price = products[prod_idx]
        selected_categories.append(category)
        selected_products.append(product)
        unit_prices.append(price)

    regions = [_REGIONS[i] for i in rng.integers(0, len(_REGIONS), size=n)]
    quantities = rng.integers(1, 6, size=n).tolist()
    total_amounts = [q * p for q, p in zip(quantities, unit_prices)]

    return pd.DataFrame({
        "date": dates,
        "order_id": order_ids,
        "product": selected_products,
        "category": selected_categories,
        "region": regions,
        "quantity": quantities,
        "unit_price": unit_prices,
        "total_amount": total_amounts,
    })


def kpi_metrics(df):
    return {
        "total_sales": df["total_amount"].sum(),
        "total_orders": df["order_id"].nunique(),
    }
