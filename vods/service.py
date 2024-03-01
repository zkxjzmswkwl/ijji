from .models import *
import members.logic.selectors as member_selectors


def create_game_details(*,
    map: str, winning_team: str, length: int, vod: Vod
):
    return GameDetails.objects.create(
        map=map,
        winning_team=winning_team,
        length=length,
        vod=vod
    )


def create_vod(
    **kwargs
    # *, title: str, description: str, video, belongs_to: int, played_by: str
):
    return Vod.objects.create(
        title=kwargs.get("title"),
        description=kwargs.get("description"),
        video=kwargs.get("video"),
        belongs_to=member_selectors.get_member_by_id(kwargs.get("belongs_to")),
        played_by=kwargs.get("played_by"),
    )
