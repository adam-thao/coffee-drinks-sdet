# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,unused-variable,implicit-str-concat,import-error

# from testcontainers.mongodb import MongoDbContainer
# import pytest

# DATABASE = "coffee"
# COLLECTION = "coffee_information"


# def describe_get_coffee_information():
#     def test_should_return_all_coffee_information_from_database(
#         database_mock, coffee_drinks
#     ):
#         # with MongoDbContainer() as mongodb:
#         #     mongo_client = mongo.get_connection_client()
#         #     mongo_client[DATABASE][COLLECTION].insert_many()
#         print(coffee_drinks)


# @pytest.fixture
# def database_mock(mocker):
#     return mocker.Mock(client=None)


# @pytest.fixture
# def coffee_drinks(coffee_information):
#     coffee_drinks = vars(coffee_information)["coffee_drinks"]
#     coffee_drinks_json = [vars(coffee_drink) for coffee_drink in coffee_drinks]

#     return coffee_drinks_json
