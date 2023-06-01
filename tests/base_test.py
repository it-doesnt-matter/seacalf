import json
from pathlib import Path

from jsonschema import validate
import pytest


class TestSchemas:
    def test_countries_schema(self, countries):
        with open("countries.schema.json", "r", encoding="utf-8") as file:
            schema = json.load(file)

        validate(instance=countries, schema=schema)

    def test_uk_schema(self, uk):
        with open("uk.schema.json", "r", encoding="utf-8") as file:
            schema = json.load(file)

        validate(instance=uk, schema=schema)

    def test_currencies_schema(self, currencies):
        with open("currencies.schema.json", "r", encoding="utf-8") as file:
            schema = json.load(file)

        validate(instance=currencies, schema=schema)

    def test_border_total(self, countries):
        for key in countries:
            if countries[key]["land_borders"]["countries"] is None:
                continue

            total = sum(country["length"] for country in countries[key]["land_borders"]["countries"])
            assert countries[key]["land_borders"]["total"] == total

    def test_border_cross_reference(self, countries):
        for key in countries:
            if countries[key]["land_borders"]["countries"] is None:
                continue

            for neighbour in countries[key]["land_borders"]["countries"]:
                reference_length = [
                    reference["length"]
                    for reference in countries[neighbour["iso_a3"]]["land_borders"]["countries"]
                    if reference["iso_a3"] == key
                ][0]
                assert reference_length == neighbour["length"]

    def test_countries_to_currencies_cross_reference(self, countries, currencies):
        for key, country in countries.items():
            for currency in country["currencies"]:
                reference = {"iso_a3": key, "name": country["name"]["short"]}
                assert reference in currencies[currency["iso_a3"]]["used_by"]

    def test_currencies_to_countries_cross_reference(self, countries, currencies):
        for key, currency in currencies.items():
            for country in currency["used_by"]:
                reference = {"iso_a3": key, "name": currency["name"]}
                assert reference in countries[country["iso_a3"]]["currencies"]

    def test_passports_cross_reference(self, countries):
        passport_picture_paths = (Path.cwd().parent / "datasets/passports/countries").glob("*")

        passport_codes = {path.stem for path in passport_picture_paths}
        country_codes = set(countries)
        
        assert passport_codes.issubset(country_codes)

    def test_flags_cross_reference(self, countries, uk):
        country_flag_paths = (Path.cwd().parent / "datasets/flags/countries").glob("*")
        uk_flag_paths = (Path.cwd().parent / "datasets/flags/uk").glob("*")

        country_flag_codes = {path.stem for path in country_flag_paths}
        uk_flag_codes = {path.stem for path in uk_flag_paths}
        country_codes = set(countries)
        uk_codes = set(uk)

        assert country_flag_codes == country_codes
        assert uk_flag_codes == uk_codes

    def test_countries_area_sum(self, countries):
        for country in countries.values():
            if (country["area"]["land"] is None
                    or country["area"]["water"] is None
                    or country["area"]["total"] is None):
                continue
            assert country["area"]["land"] + country["area"]["water"] == country["area"]["total"]

    def test_uk_area_sum(self, uk):
        for country in uk.values():
            if (country["area"]["land"] is None
                    or country["area"]["water"] is None
                    or country["area"]["total"] is None):
                continue
            assert country["area"]["land"] + country["area"]["water"] == country["area"]["total"]

    def test_geojson_cross_reference(self, countries, uk):
        country_geojson_paths = (Path.cwd().parent / "datasets/geojson/countries").glob("*.json")
        uk_geojson_paths = (Path.cwd().parent / "datasets/geojson/uk").glob("*.json")

        country_geojson_codes = {path.stem for path in country_geojson_paths}
        country_geojson_codes.add("ATA")
        uk_geojson_codes = {path.stem for path in uk_geojson_paths}
        country_codes = set(countries)
        uk_codes = set(uk)
        
        assert country_geojson_codes == country_codes
        assert uk_geojson_codes == uk_codes

    def test_countries_independence(self, countries):
        for country in countries.values():
            if country["iso"]["a3"] == "ATA":
                continue
            if country["independence"]["is_independent"]:
                assert country["independence"]["sovereign_state"]["iso_a3"] is None
                assert country["independence"]["sovereign_state"]["name"] is None
                assert country["independence"]["status"] is None
            else:
                assert country["independence"]["sovereign_state"]["iso_a3"] is not None
                assert country["independence"]["sovereign_state"]["name"] is not None
                assert country["independence"]["status"] is not None

    def test_uk_independence(self, uk):
        for country in uk.values():
            if country["independence"]["is_independent"]:
                assert country["independence"]["sovereign_state"]["iso_a3"] is None
                assert country["independence"]["sovereign_state"]["name"] is None
                assert country["independence"]["status"] is None
            else:
                assert country["independence"]["sovereign_state"]["iso_a3"] is not None
                assert country["independence"]["sovereign_state"]["name"] is not None
                assert country["independence"]["status"] is not None


@pytest.fixture
def countries():
    with open("../datasets/countries/countries.json", "r", encoding="utf-8") as file:
        countries = json.load(file)
    return countries


@pytest.fixture
def uk():
    with open("../datasets/uk/uk.json", "r", encoding="utf-8") as file:
        uk = json.load(file)
    return uk


@pytest.fixture
def currencies():
    with open("../datasets/currencies/currencies.json", "r", encoding="utf-8") as file:
        currencies = json.load(file)
    return currencies