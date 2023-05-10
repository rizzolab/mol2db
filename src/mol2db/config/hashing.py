from hashlib import sha256


def get_hash(pw):
    as_bytes = bytes(pw, "utf8")
    h = sha256()
    h.update(as_bytes)
    hash = h.hexdigest()
    return hash
