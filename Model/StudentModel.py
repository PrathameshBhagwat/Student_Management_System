from pydantic import BaseModel,Field
from typing import Annotated

class StudentStructure(BaseModel):
    roll:Annotated[int,Field(title="Enter your roll no ")]
    name:Annotated[str,Field(title="Enter your name ")]
    age:Annotated[int,Field(title="Enter your age ")]