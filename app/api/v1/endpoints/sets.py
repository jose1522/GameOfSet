from fastapi import Depends, APIRouter

from core.set_finder import SetFinder
from interfaces.set_finder import SetFinderInterface
from models.card import CardSetResponse, CardSetRequest

router = APIRouter(prefix="/set", tags=["sets"])


def get_set_finder() -> SetFinderInterface:
    """Factory function for creating a SetFinder instance."""
    return SetFinder()


@router.post("/", response_model=CardSetResponse)
def find_sets(
    params: CardSetRequest,
    set_finder: SetFinderInterface = Depends(get_set_finder),
):
    for card in params.cards:
        set_finder.add_card(card)
    possible_sets = set_finder.find_sets(params.set_size)
    return CardSetResponse(sets=possible_sets)
