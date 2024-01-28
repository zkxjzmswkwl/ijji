from members.logic.selectors import get_member_by_username


def mark_member_inactive(*, username: str) -> None:
    member = get_member_by_username(username=username)
    member.is_active = False
    member.save(update_fields=["is_active"])


def change_member_username(*, username: str, new_username: str) -> None:
    member = get_member_by_username(username)
    member.username = new_username
    member.save(update_fields=["username"])
