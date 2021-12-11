from typing import Optional
from pydantic import BaseModel, Field

class DestinationSchema(BaseModel):
    title: str = Field(...)
    country: str = Field(...)
    region: str = Field(...)
    content: str = Field(...)
    url: str = Field(...)
    coords: list = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "coords": [51.05, -0.09],
                "url": "https://www.youtube.com/watch?v=JwjiIK1m55c",
                "country": "Mexico",
                "region": "North America",
                "content": "Los tacos son bien chidos carnal",
                "title": "Como hacer unos tacos de asada bien chidos"
            }
        }


class UpdateDestinationModel(BaseModel):
    coords: Optional[list]
    url: Optional[str]
    name: Optional[str]
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "coords": [51.10, -0.19],
                "url": "https://www.youtube.com/watch?v=saVFFwtZ1FU",
                "name": "sebastian",
                "description": "Puebla is a beautiful place!",
            }
        }


def ResponseModel(data, message):
    return {"data": [data], "code": 200, "message": message}


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}