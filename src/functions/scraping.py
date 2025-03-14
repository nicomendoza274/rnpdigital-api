from playwright.async_api import async_playwright, StorageState
from models.vehicle import Vehicle, GeneralFeatures, MotorFeatures
from constants.xpath import *
from constants.credentials import USER_CREDENTIAL, PASS_CREDENTIAL
from constants.urls import LOGIN_URL, VEHICLE_QUERY


async def login() -> StorageState:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()

        page = await context.new_page()
        await page.goto(LOGIN_URL)
        await page.locator(USER_INPUT).type(USER_CREDENTIAL)
        await page.locator(PASS_INPUT).type(PASS_CREDENTIAL)
        await page.locator(BTN_ENTER).click(force=False)
        await page.wait_for_timeout(2000)
        auth = await context.storage_state()
        return auth


async def scraping_vehicle(auth: StorageState, plate: str) -> Vehicle:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(storage_state=auth)
        page = await context.new_page()

        await page.goto(VEHICLE_QUERY)
        await page.wait_for_timeout(1000)
        await page.locator(PLATE_NUMBER_INPUT).type(plate)
        await page.locator(BTN_CONSULT).click(force=False)
        await page.wait_for_timeout(1000)

        brand = await page.locator(BRAND).inner_text()
        style = await page.locator(STYLE).inner_text()

        category = await page.locator(CATEGORY).inner_text()
        capacity = await page.locator(CAPACITY).inner_text()

        serie_number = await page.locator(SERIE_NUMBER).inner_text()
        empty_weight = await page.locator(EMPTY_WEIGHT).inner_text()

        bodywork = await page.locator(BODYWORK).inner_text()
        net_weight = await page.locator(NET_WEIGHT).inner_text()

        traction = await page.locator(TRACTION).inner_text()
        gross_weight = await page.locator(GROSS_WEIGHT).inner_text()

        chassis_number = await page.locator(CHASSIS_NUMBER).inner_text()
        treasury_value = await page.locator(TREASURY_VALUE).inner_text()

        manufacturing_year = await page.locator(MANUFACTURING_YEAR).inner_text()
        actual_status = await page.locator(ACTUAL_STATUS).inner_text()

        length = await page.locator(LENGTH).inner_text()
        tax_status = await page.locator(TAX_STATUS).inner_text()

        cabin = await page.locator(CABIN).inner_text()
        tax_class = await page.locator(TAX_CLASS).inner_text()

        roof = await page.locator(ROOF).inner_text()
        use = await page.locator(USE).inner_text()

        trailer_weight = await page.locator(TRAILER_WEIGHT).inner_text()
        contract_price = await page.locator(CONTRACT_PRICE).inner_text()

        color = await page.locator(COLOR).inner_text()
        registration_number = await page.locator(REGISTRATION_NUMBER).inner_text()

        converted = await page.locator(CONVERTED).inner_text()
        currency = await page.locator(CURRENCY).inner_text()

        vin_number = await page.locator(VIN_NUMBER).inner_text()

        engine_number = await page.locator(ENGINE_NUMBER).inner_text()
        motor_brand = await page.locator(MOTOR_BRAND).inner_text()

        motor_serie_number = await page.locator(MOTOR_SERIE_NUMBER).inner_text()
        model = await page.locator(MODEL).inner_text()

        cylinder_capacity = await page.locator(CYLINDER_CAPACITY).inner_text()
        cylinders = await page.locator(CYLINDERS).inner_text()

        potency = await page.locator(POTENCY).inner_text()
        fuel = await page.locator(FUEL).inner_text()

        manufacturer = await page.locator(MANUFACTURER).inner_text()
        origin = await page.locator(ORIGIN).inner_text()

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
