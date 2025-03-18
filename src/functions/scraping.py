from playwright.sync_api import sync_playwright, StorageState
from models.vehicle import Vehicle, GeneralFeatures, MotorFeatures
from constants.xpath import *
from constants.credentials import USER_CREDENTIAL, PASS_CREDENTIAL
from constants.urls import LOGIN_URL, VEHICLE_QUERY


def login() -> StorageState:
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        page = context.new_page()
        page.goto(LOGIN_URL)
        page.locator(USER_INPUT).type(USER_CREDENTIAL)
        page.locator(PASS_INPUT).type(PASS_CREDENTIAL)
        page.locator(BTN_ENTER).click(force=False)
        page.wait_for_timeout(2000)
        auth = context.storage_state()
        return auth


def scraping_vehicle(auth: StorageState, plate: str) -> Vehicle:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=auth)
        page = context.new_page()

        page.goto(VEHICLE_QUERY)
        page.wait_for_timeout(1000)
        page.locator(PLATE_NUMBER_INPUT).type(plate)
        page.locator(BTN_CONSULT).click(force=False)
        page.wait_for_timeout(1000)

        brand = page.locator(BRAND).inner_text(timeout=60000)
        style = page.locator(STYLE).inner_text(timeout=60000)

        category = page.locator(CATEGORY).inner_text(timeout=60000)
        capacity = page.locator(CAPACITY).inner_text(timeout=60000)

        serie_number = page.locator(SERIE_NUMBER).inner_text(timeout=60000)
        empty_weight = page.locator(EMPTY_WEIGHT).inner_text(timeout=60000)

        bodywork = page.locator(BODYWORK).inner_text(timeout=60000)
        net_weight = page.locator(NET_WEIGHT).inner_text(timeout=60000)

        traction = page.locator(TRACTION).inner_text(timeout=60000)
        gross_weight = page.locator(GROSS_WEIGHT).inner_text(timeout=60000)

        chassis_number = page.locator(CHASSIS_NUMBER).inner_text(timeout=60000)
        treasury_value = page.locator(TREASURY_VALUE).inner_text(timeout=60000)

        manufacturing_year = page.locator(MANUFACTURING_YEAR).inner_text(timeout=60000)
        actual_status = page.locator(ACTUAL_STATUS).inner_text(timeout=60000)

        length = page.locator(LENGTH).inner_text(timeout=60000)
        tax_status = page.locator(TAX_STATUS).inner_text(timeout=60000)

        cabin = page.locator(CABIN).inner_text(timeout=60000)
        tax_class = page.locator(TAX_CLASS).inner_text(timeout=60000)

        roof = page.locator(ROOF).inner_text(timeout=60000)
        use = page.locator(USE).inner_text(timeout=60000)

        trailer_weight = page.locator(TRAILER_WEIGHT).inner_text(timeout=60000)
        contract_price = page.locator(CONTRACT_PRICE).inner_text(timeout=60000)

        color = page.locator(COLOR).inner_text(timeout=60000)
        registration_number = page.locator(REGISTRATION_NUMBER).inner_text(timeout=60000)

        converted = page.locator(CONVERTED).inner_text(timeout=60000)
        currency = page.locator(CURRENCY).inner_text(timeout=60000)

        vin_number = page.locator(VIN_NUMBER).inner_text(timeout=60000)

        engine_number = page.locator(ENGINE_NUMBER).inner_text(timeout=60000)
        motor_brand = page.locator(MOTOR_BRAND).inner_text(timeout=60000)

        motor_serie_number = page.locator(MOTOR_SERIE_NUMBER).inner_text(timeout=60000)
        model = page.locator(MODEL).inner_text(timeout=60000)

        cylinder_capacity = page.locator(CYLINDER_CAPACITY).inner_text(timeout=60000)
        cylinders = page.locator(CYLINDERS).inner_text(timeout=60000)

        potency = page.locator(POTENCY).inner_text(timeout=60000)
        fuel = page.locator(FUEL).inner_text(timeout=60000)

        manufacturer = page.locator(MANUFACTURER).inner_text(timeout=60000)
        origin = page.locator(ORIGIN).inner_text(timeout=60000)

        response_data = Vehicle(
            general_features=GeneralFeatures(
                brand=brand,
                style=style,
                category=category,
                capacity=capacity,
                serie_number=serie_number,
                empty_weight=empty_weight,
                bodywork=bodywork,
                net_weight=net_weight,
                traction=traction,
                gross_weight=gross_weight,
                chassis_number=chassis_number,
                treasury_value=treasury_value,
                manufacturing_year=manufacturing_year,
                actual_status=actual_status,
                length=length,
                tax_status=tax_status,
                cabin=cabin,
                tax_class=tax_class,
                roof=roof,
                use=use,
                trailer_weight=trailer_weight,
                contract_price=contract_price,
                color=color,
                registration_number=registration_number,
                converted=converted,
                currency=currency,
                vin_number=vin_number,
            ),
            motor_features=MotorFeatures(
                engine_number=engine_number,
                motor_brand=motor_brand,
                motor_serie_number=motor_serie_number,
                model=model,
                cylinder_capacity=cylinder_capacity,
                cylinders=cylinders,
                potency=potency,
                fuel=fuel,
                manufacturer=manufacturer,
                origin=origin
            )
        )

        return response_data
