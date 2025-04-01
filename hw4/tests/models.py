from pydantic import BaseModel, RootModel
from typing import Dict, List, Optional

# Dog API Models
class DogRandomImage(BaseModel):
    message: str
    status: str

class DogBreedList(BaseModel):
    message: Dict[str, List[str]]
    status: str

class DogErrorResponse(BaseModel):
    message: str
    status: str
    code: int

# JSONPlaceholder Models
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

class Posts(RootModel):
    root: List[Post]

class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str

class Comments(RootModel):
    root: List[Comment]

# OpenBreweryDB Models
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
    phone: Optional[str]
    updated_at: str
    created_at: str

class Breweries(RootModel):
    root: List[Brewery]