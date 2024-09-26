from base64 import b64encode

import math
import pytest

from core.config import settings
from models.card import CardSetRequest, Card

ENDPOINT_PREFIX = "/api/v1/set/"


def generate_full_deck() -> CardSetRequest:
    """
    Generates the full deck of 81 unique cards for the Set game.
    """
    colors = ["red", "green", "purple"]
    shapes = ["oval", "squiggle", "diamond"]
    numbers = [1, 2, 3]
    shadings = ["solid", "striped", "outlined"]

    # Create the 81 unique cards by iterating over all combinations of attributes
    cards = [
        Card(color=color, shape=shape, number=number, shading=shading)
        for color in colors
        for shape in shapes
        for number in numbers
        for shading in shadings
    ]

    return CardSetRequest(cards=cards, set_size=3)


def expected_valid_sets(n: int, k: int) -> float:
    """
    Calculates the expected number of valid sets in a deck of n cards and k distinct attribute values.

    Args:
    - n (int): Number of cards in the partial deck (n <= 81)
    - k (int): Number of distinct attribute values (k <= 3)
    Returns:
    - float: The expected number of valid sets.
    """
    # See: https://wiki.math.wisc.edu/images/Set_sol.pdf
    return round((n * (n - 1)) / math.factorial(k), 0)


class TestCardSet:
    @pytest.fixture(scope="class")
    def auth_headers(self):
        encoded = b64encode(
            f"{settings.API_USERNAME.get_secret_value()}:{settings.API_PASSWORD.get_secret_value()}".encode(
                "utf-8"
            )
        )
        return {"Authorization": f"Basic {encoded.decode("utf-8")}"}

    @pytest.mark.parametrize("cards_in_deck", [9, 27, 81])
    def test_find_sets_partial_deck(self, client, cards_in_deck, auth_headers):
        """
        Test the find_sets endpoint with a subset of cards.
        """
        card_set_request = CardSetRequest(
            cards=generate_full_deck().cards[:cards_in_deck],
            set_size=3,
        )

        response = client.post(
            ENDPOINT_PREFIX, json=card_set_request.model_dump(), headers=auth_headers
        )
        response.raise_for_status()

        data = response.json()
        assert "sets" in data
        assert isinstance(data["sets"], list)

        # Assumes 3 unique values for all attributes
        expected_sets = expected_valid_sets(cards_in_deck, 3)
        assert len(data["sets"]) == expected_sets

    def test_find_sets_invalid_request(self, client, auth_headers):
        """Test the find_sets endpoint with an invalid request (missing cards)."""
        invalid_request = {"set_size": 3}  # Missing "cards" field

        response = client.post(
            ENDPOINT_PREFIX, json=invalid_request, headers=auth_headers
        )

        # Check that the status code is 422 (Unprocessable Entity)
        assert response.status_code == 422

    def test_find_sets_empty_cards(self, client, auth_headers):
        """Test the find_sets endpoint with an empty list of cards."""
        empty_request = {"cards": [], "set_size": 3}

        response = client.post(
            ENDPOINT_PREFIX, json=empty_request, headers=auth_headers
        )

        # Check that the response contains an empty set list
        assert response.status_code == 200
        data = response.json()
        assert "sets" in data
        assert data["sets"] == []
