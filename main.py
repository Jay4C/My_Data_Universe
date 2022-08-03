from fastapi import FastAPI
from Service.Energy.Electricity import electricity
from Service.Energy.Natural_Gas import natural_gas
from Service.Energy.Coal import coal

app = FastAPI()


@app.get("/")
def welcome():
    return "Welcome to the App"


# Energy
# Electricity
# Get the list of countries by electricity consumption
@app.get("/energy/electricity/list_of_countries_by_electricity_consumption")
def energy_electricity_get_the_list_of_countries_by_electricity_consumption():
    return electricity.get_the_list_of_countries_by_electricity_consumption()


# Get the list of countries by electricity production
@app.get("/energy/electricity/list_of_countries_by_electricity_production")
def energy_electricity_get_the_list_of_countries_by_electricity_production():
    return electricity.get_the_list_of_countries_by_electricity_production()


# Get the list of countries by electricity production by source
@app.get("/energy/electricity/list_of_countries_by_electricity_production_by_source")
def energy_electricity_get_the_list_of_countries_by_electricity_production_by_source():
    return electricity.get_the_list_of_countries_by_electricity_production_by_source()


# Get the list of countries by renewable electricity production
@app.get("/energy/electricity/list_of_countries_by_renewable_electricity_production")
def energy_electricity_get_the_list_of_countries_by_renewable_electricity_production():
    return electricity.get_the_list_of_countries_by_renewable_electricity_production()


# Get the list of countries by renewable electricity imports
@app.get("/energy/electricity/list_of_countries_by_electricity_imports")
def energy_electricity_get_the_list_of_countries_by_electricity_imports():
    return electricity.get_the_list_of_countries_by_electricity_imports()


# Get the list of countries by renewable electricity exports
@app.get("/energy/electricity/list_of_countries_by_electricity_exports")
def energy_electricity_get_the_list_of_countries_by_electricity_exports():
    return electricity.get_the_list_of_countries_by_electricity_exports()
# Electricity


# Natural gas
# Get the list of countries by natural gas proven reserves
@app.get("/energy/natural_gas/list_of_countries_by_natural_gas_proven_reserves")
def energy_natural_gas_get_the_list_of_countries_by_natural_gas_proven_reserves():
    return natural_gas.get_the_list_of_countries_by_natural_gas_proven_reserves()


# Get the list of countries by natural gas consumption
@app.get("/energy/natural_gas/list_of_countries_by_natural_gas_consumption")
def energy_natural_gas_get_the_list_of_countries_by_natural_gas_consumption():
    return natural_gas.get_the_list_of_countries_by_natural_gas_consumption()


# Get the list of countries by natural gas production
@app.get("/energy/natural_gas/list_of_countries_by_natural_gas_production")
def energy_natural_gas_get_the_list_of_countries_by_natural_gas_production():
    return natural_gas.get_the_list_of_countries_by_natural_gas_production()


# Get the list of countries by natural gas imports
@app.get("/energy/natural_gas/list_of_countries_by_natural_gas_imports")
def energy_natural_gas_get_the_list_of_countries_by_natural_gas_imports():
    return natural_gas.get_the_list_of_countries_by_natural_gas_imports()


# Get the list of countries by natural gas exports
@app.get("/energy/natural_gas/list_of_countries_by_natural_gas_exports")
def energy_natural_gas_get_the_list_of_countries_by_natural_gas_exports():
    return natural_gas.get_the_list_of_countries_by_natural_gas_exports()
# Natural gas


# Coal
# Get the list of countries by coal proven reserves
@app.get("/energy/coal/list_of_countries_by_coal_proven_reserves")
def energy_coal_get_the_list_of_countries_by_coal_proven_reserves():
    return coal.get_the_list_of_countries_by_coal_proven_reserves()


# Get the list of countries by coal consumption
@app.get("/energy/coal/list_of_countries_by_coal_consumption")
def energy_coal_get_the_list_of_countries_by_coal_consumption():
    return coal.get_the_list_of_countries_by_coal_consumption()


# Get the list of countries by coal production
@app.get("/energy/coal/list_of_countries_by_coal_production")
def energy_coal_get_the_list_of_countries_by_coal_production():
    return coal.get_the_list_of_countries_by_coal_production()


# Get the list of countries by natural gas imports
@app.get("/energy/coal/list_of_countries_by_coal_imports")
def energy_coal_get_the_list_of_countries_by_coal_imports():
    return coal.get_the_list_of_countries_by_coal_imports()


# Get the list of countries by natural gas exports
@app.get("/energy/coal/list_of_countries_by_coal_exports")
def energy_coal_get_the_list_of_countries_by_coal_exports():
    return coal.get_the_list_of_countries_by_coal_exports()
# Coal
# Energy
