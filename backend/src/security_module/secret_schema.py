import json
from pydantic import BaseModel, model_validator


class Secret_schema(BaseModel):
    password: str

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
