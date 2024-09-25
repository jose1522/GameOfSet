from itertools import combinations
from typing import List

from interfaces.set_finder import SetFinderInterface
from models.card import Card, CardAttributeNames


class SetFinder(SetFinderInterface):
    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    @staticmethod
    def _attributes_match(attribute_values: List) -> bool:
        """Helper function. Checks if the attribute values are either all the same or all different."""
        unique_values_count = len(set(attribute_values))
        values_count = len(attribute_values)
        return unique_values_count == 1 or unique_values_count == values_count

    def find_sets(self, set_size: int = 3) -> List[List[Card]]:
        return [
            list(combo)
            for combo in combinations(self.cards, set_size)
            if self._is_valid_set(combo)
        ]

    def _is_valid_set(self, cards: List[Card]) -> bool:
        """Check if the given cards form a valid set based on the game rules."""
        for attribute in CardAttributeNames:
            attribute_values = [card[attribute] for card in cards]
            if not self._attributes_match(attribute_values):
                return False
        return True
