import json
import pytest
import requests


class Test_Api:
    base_url = "https://api.punkapi.com/v2/beers/8"

    @classmethod
    def test_delete_api(cls):
        response = requests.delete(cls.base_url)
        actual_status = response.status_code

        assert actual_status == 404, f"Expected status: 404, Actual status: {actual_status}"
        print("Data wasn't deleted")

    @classmethod
    def test_response_content(cls):
        expected_name = 'Fake Lager'
        expected_abv = 4.7
        response = requests.get(cls.base_url)
        data = response.json()

        actual_status = response.status_code

        query_params = {"name": "Fake Lager", "abv": 4.7}
        testr = requests.get(cls.base_url, params=query_params).json()
        print(testr)

        actual_name = data[0]['name']
        actual_abv = data[0]['abv']

        assert actual_status == 200, f"Expected status code: 200, Actual name: {actual_status}"

        assert actual_name == expected_name, f"Expected name: {expected_name}, Actual name: {actual_name}"
        assert actual_abv == expected_abv, f"Expected name: {expected_abv}, Actual name: {actual_abv}"


if __name__ == "__main__":
    pytest.main([__file__])
