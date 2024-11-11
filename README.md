# Flask Dependency Injection Example

This is a simple example of how to use dependency injection in a Flask application.

## Installation

Run poetry install to install the dependencies.

```bash
poetry install
```

Activate .venv created by poetry

```bash
source .venv/bin/activate
```

## Understanding dependency injection

The code has 2 services:

1. ViewService - This service is responsible for providing the Flask environment and app.
2. DisplayService - This service is responsible for displaying the Flask environment and app.

The routes packages is wired in the WiringConfiguration of the container. That means, any class in the routes package can have its dependencies injected.
Check [Wiring](https://python-dependency-injector.ets-labs.org/wiring.html#wiring-configuration) to read more about wiring.

The DisplayService has a dependency on the ViewService. The ViewService is injected into the DisplayService.
The container is responsible for wiring the services together.
Check the `containers.py` file to see how the services are wired together. The file also includes the config that is read from Environment Variables.
The variables `FLASK_ENV` and `FLASK_APP` are used to configure the Flask application.

Refer to these links for more information:

* [Flask Dependency Injection Example](https://python-dependency-injector.ets-labs.org/examples/flask.html)
* [Wiring](https://python-dependency-injector.ets-labs.org/wiring.html#wiring-configuration)
