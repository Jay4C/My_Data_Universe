import unittest
import requests
import json


class UnitTestsEnergyElectricity(unittest.TestCase):
    def test_get_the_list_of_countries_by_electricity_consumption(self):
        print('test_get_the_list_of_countries_by_electricity_consumption')

        response = requests.get("http://127.0.0.1:8000/energy/electricity/list_of_countries_by_electricity_consumption")

        first_item = json.loads(response.text)[0]

        print(first_item)


if __name__ == '__main__':
    unittest.main()
