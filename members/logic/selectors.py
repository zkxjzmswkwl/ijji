from members.models import Member


def get_member_by_id(member_id):
    return Member.objects.get(id=member_id)


def get_member_by_email(email):
    return Member.objects.get(email__iexact=email)


def get_member_by_username(username) -> Member | None:
    query = Member.objects.filter(username__iexact=username)
    if query.exists():
        return query.first()
    return None
