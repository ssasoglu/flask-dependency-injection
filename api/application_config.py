from dataclasses import dataclass
import os

@dataclass
class ApplicationConfig:
    FlaskEnv: str
    FlaskApp: str
    
    @classmethod
    def parse_config(cls) -> 'ApplicationConfig':
        return cls(
            FlaskEnv=os.getenv("FLASK_ENV"),
            FlaskApp=os.getenv("FLASK_APP")
        )