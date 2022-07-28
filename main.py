from fastapi import FastAPI
from Service.Energy.Electricity import electricity

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
# Electricity
# Energy
