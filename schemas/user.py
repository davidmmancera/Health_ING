def userEntity(item) -> dict:
    return {
        "id": str(item["id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }