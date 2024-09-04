from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://username:password@localhost/hotel_management_db"

settings = Settings()


# class Settings(BaseSettings):
#     DATABASE_URL: str = "postgresql://username:password@localhost/hotel_management_db"
#     SECRET_KEY: str = "YOUR_SECRET_KEY"
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

# settings = Settings()
