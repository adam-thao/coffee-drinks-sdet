# pylint: disable=redefined-outer-name,missing-module-docstring,missing-function-docstring,unused-variable,implicit-str-concat,import-error

import pytest
from domain.model.coffee_information import CoffeeInformation
from domain.model.coffee_drink import CoffeeDrink


@pytest.fixture
def coffee_information():
    return CoffeeInformation(
        [
            CoffeeDrink(
                id="209f4328-001c-48ff-925a-bc4319443340",
                title="Black",
                description="Coffee served as a beverage without cream or milk.",
                ingredients=["Coffee"],
            ),
            CoffeeDrink(
                id="17575fe7-034c-4f5a-97c9-9ee8fc762c9a",
                title="Latte",
                description="A coffee drink of Italian origin made with espresso and steamed milk.",
                ingredients=["Espresso", "Steamed Milk", "Foamed Milk"],
            ),
            CoffeeDrink(
                id="01d8ddd3-f437-4313-991d-7d8bea95aee1",
                title="Cappuccino",
                description=(
                    "An espresso-based coffee drink that originated in Austria with later "
                    "development taking place in Italy, and is prepared with steamed milk foam."
                ),
                ingredients=["Espresso", "Steamed Milk"],
            ),
        ]
    )
