from abc import ABC, abstractmethod
from typing import List, Set
from models.card import Card


class SetFinderInterface(ABC):
    """Interface for finding sets in a deck of cards"""

    def __init__(self):
        self.cards: Set[Card] = set()

    def add_card(self, card: Card) -> None:
        self.cards.add(card)

    @abstractmethod
    def find_sets(self, set_size: int) -> List[List[Card]]:
        """Finds all sets of the given size in the deck."""
