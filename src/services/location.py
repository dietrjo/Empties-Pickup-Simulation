from geopy import Nominatim

from src.utils.data_loader import load_json

data = load_json('data.json')
geolocator = Nominatim(user_agent="TSP_Jena")


class Location:
    def __init__(self, address: str, coords: tuple[any, any]):
        self.address = address
        self.coords = coords

    def __str__(self) -> str:
        return f'{self.address} {self.coords}'


def get_customer_locations() -> list[Location]:
    cust_locations = []
    for address in data["customers"]["addresses"]:
        loc = geolocator.geocode(address)

        if loc is None:
            print(f"Address couldn't be located: {address}")
            break

        cust_locations += [Location(address, (loc.latitude, loc.longitude))]
    return cust_locations


def get_warehouse_location() -> Location:
    warehouse_address = data["warehouse_address"]
    loc = geolocator.geocode(warehouse_address)
    return Location(warehouse_address, (loc.latitude, loc.longitude))