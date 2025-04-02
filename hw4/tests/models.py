from pydantic import BaseModel, RootModel, Field
from typing import Dict, List, Optional

# Dog API Models
class DogRandomImage(BaseModel):
    message: str
    status: str

class DogBreedList(BaseModel):
    message: Dict[str, List[str]]
    status: str

class DogSubBreedList(BaseModel):
    message: List[str]
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
    street: Optional[str] = None
    city: str
    state: str
    postal_code: str
    country: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    website_url: Optional[str] = None
    phone: Optional[str] = None
    updated_at: Optional[str] = None
    created_at: Optional[str] = None

class Breweries(RootModel):
    root: List[Brewery]