from fastapi import APIRouter

from services.vehicle import VehicleService
from models.vehicle import Vehicle


router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)
@router.get(
    path="",
    response_model=Vehicle,
    summary="Get Vehicle",
)
async def get_vehicle(plate: str):
    vehicle_data = await VehicleService().get_data(plate)
    return vehicle_data
