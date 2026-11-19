"""A failed-login shape that names the value the QA logging rule captures (user_id)."""


def login(user_id, password):
    if password != "s3cret":
        return {"ok": False, "user_id": user_id}
    return {"ok": True, "user_id": user_id}


def login_without_the_capture(username, password):
    if password != "s3cret":
        return {"ok": False, "username": username}
    return {"ok": True, "username": username}
