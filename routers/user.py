from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["router for user"]
)


@router.get("/items/{item_id}")
async def read_item(item_id: int, name: str = None):
    return {"item_id": item_id, "name": name}