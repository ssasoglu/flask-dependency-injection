"""Views module."""
from abc import ABC, abstractmethod
from api.application_config import ApplicationConfig

class IViewService(ABC):
    @abstractmethod
    def get_flask_env(self):
        pass
    
    @abstractmethod
    def get_flask_app(self):
        pass

class ViewService(IViewService):

    def __init__(self, application_config: ApplicationConfig):
        self.application_config = application_config

    def get_flask_env(self):
        return self.application_config.FlaskEnv
    
    def get_flask_app(self):
        return self.application_config.FlaskApp