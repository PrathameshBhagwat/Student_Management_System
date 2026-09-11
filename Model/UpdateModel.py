from pydantic import BaseModel, Field
from typing import Annotated,Optional

class updateStructure(BaseModel):
    name:Annotated[Optional[str],Field(title="Enter the name ",default=None)]
    age:Annotated[Optional[int],Field(title="Enter your age ",default=None)]
    