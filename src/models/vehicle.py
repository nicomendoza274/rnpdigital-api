from models.camel import Camel


class GeneralFeatures(Camel):
    brand: str
    style: str
    category: str
    capacity: str
    serie_number: str
    empty_weight: str
    bodywork: str
    net_weight: str
    traction: str
    gross_weight: str
    chassis_number: str
    treasury_value: str
    manufacturing_year: str
    actual_status: str
    length: str
    tax_status: str
    cabin: str
    tax_class: str
    roof: str
    use: str
    trailer_weight: str
    contract_price: str
    color: str
    registration_number: str
    converted: str
    currency: str
    vin_number: str


class MotorFeatures(Camel):
    engine_number: str
    motor_brand: str
    motor_serie_number: str
    model: str
    cylinder_capacity: str
    cylinders: str
    potency: str
    fuel: str
    manufacturer: str
    origin: str

class Vehicle(Camel):
    general_features: GeneralFeatures
    motor_features: MotorFeatures