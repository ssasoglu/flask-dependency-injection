from api.display_service import IDisplayService
from dependency_injector.wiring import inject, Provide
from api.containers import Container

@inject
def index(display_service: IDisplayService = Provide[Container.display_service]):
    print(display_service)
    return display_service.index()
