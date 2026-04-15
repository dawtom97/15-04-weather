

def paramsMapping(pl):
    params = {
        "Wilgotność":"humidity",
        "Ciśnienie":"pressure",
        "Prędkość Wiatru":"wind_speed"
    }

    value = params[pl]
    return value