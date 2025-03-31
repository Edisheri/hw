from pydantic import BaseModel
from typing import Dict, List, Optional

class DogRandomImage(BaseModel):
    message: str
    status: str

class DogBreedList(BaseModel):
    message: Dict[str, List[str]]
    status: str

class DogErrorResponse(BaseModel):
    code: int
    message: str
    status: str

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str

class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    street: Optional[str]
    city: str
    state: str
    postal_code: str
    country: str
    longitude: Optional[str]
    latitude: Optional[str]
    website_url: Optional[str]
    updated_at: str
    created_at: str