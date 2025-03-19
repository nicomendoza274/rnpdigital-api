from functions.scraping import scraping_vehicle
from models.vehicle import Vehicle

class VehicleService():

    def get_data(self, plate: str) -> Vehicle:
        # auth = login()
        vehicle_data = scraping_vehicle(plate)
        return vehicle_data
