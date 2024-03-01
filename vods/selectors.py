from members.models import Member
from vods.models import Vod

def get_all():
    return Vod.objects.all()

def get_played_by(*, player: str):
    return Vod.objects.filter(played_by__iexact=player)

def get_by_uploader(*, user_id: int):
    return Vod.objects.filter(belongs_to=user_id)
