from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_snake


class Base(BaseModel):
    model_config = ConfigDict(alias_generator=to_snake)
