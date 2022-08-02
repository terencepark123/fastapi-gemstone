from sqlmodel import SQLModel, Field
from enum import Enum, IntEnum
from typing import Union

class GemTypes(str,Enum):
    DIAMONDS = 'DIAMONDS'
    RUBY = 'RUBY'
    EMERALD = 'EMERALD'

class GemClarity(IntEnum):
    SI = 1
    VS = 2
    VSS = 3
    FL = 4

class GemColor(str, Enum):
    D = 'D'
    E = 'E'
    G = 'G'
    F = 'F'
    H = 'H'
    I = 'I'
    
class GemProperties(SQLModel, table=True):
    id: Union[int,None] = Field(primary_key=True)
    size: float = 1
    clarity: Union[GemClarity,None] = None
    color: Union[GemColor,None] = None
    
class Gem(SQLModel, table = True):
    id: Union[int,None] = Field(primary_key=True)
    price: float
    available: bool = True
    gem_type: GemTypes = GemTypes.DIAMONDS

    gem_properties_id: Union[int,None] = Field(default=None, foreign_key='gemproperties.id')


