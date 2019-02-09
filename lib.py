def distance_approximation(fuel_consumption_100km, actual_fuel_value):
    """
    >>> distance_approximation(10,100)
    8
    """
    approximately_distance_km = round(( actual_fuel_value / fuel_consumption_100km )*0.8)
    return approximately_distance_km