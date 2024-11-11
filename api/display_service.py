
# Create abstract class IDisplayService
# Create DisplayService class that implements IDisplayService
# Add constructor with dependency to ViewService
# Add method index and move the logic from ViewService to DisplayService

from abc import ABC, abstractmethod
from api.view_service import IViewService

class IDisplayService(ABC):
    @abstractmethod
    def index(self):
        pass

class DisplayService(IDisplayService):
    def __init__(self, view_service: IViewService):
        self.view_service = view_service

    def index(self):
        flask_app = self.view_service.get_flask_app()
        flask_env = self.view_service.get_flask_env()
        return f"Hello, World from {flask_app} in {flask_env} environment!"
