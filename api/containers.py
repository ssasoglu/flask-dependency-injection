"""Containers module."""

from dependency_injector import containers, providers

from api.application import ApplicationConfig
from api.display_service import IDisplayService, DisplayService
from api.view_service import IViewService, ViewService
from api.application_config import ApplicationConfig

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["api.routes"])

    config = providers.Configuration()
    application_config : ApplicationConfig = providers.Singleton(ApplicationConfig.parse_config)
    view_service: IViewService = providers.Factory(ViewService, application_config=application_config)
    display_service: IDisplayService = providers.Factory(DisplayService, view_service=view_service)