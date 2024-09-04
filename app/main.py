from fastapi import FastAPI
from app.routes import user_routes, room_routes, reservation_routes, service_routes
from app.db.base import database 
app = FastAPI()

# Register routes
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(room_routes.router, prefix="/rooms", tags=["Rooms"])
app.include_router(reservation_routes.router, prefix="/reservations", tags=["Reservations"])
app.include_router(service_routes.router, prefix="/services", tags=["Services"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hotel Management System API"}


# Event handlers to connect and disconnect from the database
@app.on_event("startup")
async def startup():
    await database.connect()  # Connect to the database when the app starts

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()  # Disconnect from the database when the app stops
