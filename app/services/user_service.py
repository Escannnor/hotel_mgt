

from app.db.base import database
from app.models.user import User

# Example function to fetch a user by username using async `databases` query
async def get_user_by_username(username: str):
    query = "SELECT * FROM users WHERE username = :username"
    return await database.fetch_one(query=query, values={"username": username})
