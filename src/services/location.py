class Location:
    def __init__(self, address: str, coords: tuple[any, any]):
        self.address = address
        self.coords = coords

    def __str__(self) -> str:
        return f'{self.address} {self.coords}'
