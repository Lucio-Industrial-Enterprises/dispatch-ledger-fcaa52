"""Shipping rate calculations."""

_ZONE_BASE = {"local": 5.0, "regional": 8.0}
_SERVICE_SURCHARGE = {"standard": 0.0, "express": 7.0}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone – ``"local"`` or ``"regional"``.
        service: Service level – ``"standard"`` (default) or ``"express"``.
            Express adds a flat $7 surcharge on top of the standard rate.

    Returns:
        Quoted price in dollars, rounded to two decimal places.

    Raises:
        ValueError: If *weight_kg* is not positive, *zone* is unknown, or
            *service* is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in _ZONE_BASE:
        raise ValueError(f"unknown zone: {zone!r}")
    if service not in _SERVICE_SURCHARGE:
        raise ValueError(f"unknown service: {service!r}")
    base = _ZONE_BASE[zone] + _SERVICE_SURCHARGE[service]
    return round(base + 1.5 * weight_kg, 2)
