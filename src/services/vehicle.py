from functions.scraping import login, scraping_vehicle
from models.vehicle import Vehicle

class VehicleService():

    async def get_data(self, plate: str) -> Vehicle:
        auth = await login()
        vehicle_data = await scraping_vehicle(auth, plate)
        return vehicle_data
