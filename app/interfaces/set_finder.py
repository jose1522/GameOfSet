from abc import ABC, abstractmethod
from typing import List
from models.card import Card


class SetFinderInterface(ABC):
    """Interface for finding sets in a deck of cards"""

    def __init__(self):
        self.cards: List[Card] = []

    @abstractmethod
    def add_card(self, card: Card) -> None:
        """Adds a card to the deck."""

    @abstractmethod
    def find_sets(self, set_size: int) -> List[List[Card]]:
        """Finds all sets of the given size in the deck."""
