from fastapi import APIRouter

v1_router = router = APIRouter()


@router.get("/")
async def getUser():
    return "<h1>This is User Page</h1>"
