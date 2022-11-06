# Python API RESTful

Python API RESTful using FastAPI framework with WebSocket support and PostgreSQL database.

### Configure

- Create a `.env` file with the follow settings:

```
# JWT GENERATE CONFIG (IN HOURS)
JWT_SECRET=secret-key
JWT_EXPIRE=24

# APPLICATION CONFIG
APP_VERSION=1.0.0
APP_DESC=Mega API
APP_NAME=My API
APP_PORT=80
MODE=dev

# DATABASE CONFIG
DB_PASS=123456
DB_USER=root
DB_PORT=5432
DB_NAME=app
DB_HOST=db

# DATABASE ADMIN
DBA_PASS=123456
DBA_USER=admin
DBA_PORT=8080
```

> Set `MODE` to `production` when run on Docker.

### Deploy

- Load `.env`:
    - `$ cat .env`

- Deploy:
    - `$ docker-compose up -d`

### WebSocket Manager

To use manager to send messages to websocket clients, use:

```python
# Import manager
from common.ws import manager

# Create async function
async def my_async_function():

    # Use manager (send broadcast event)
    await manager.event("my_event", {"my": "data"})
```

### WebSocket Client (JavaScript)

```javascript
var token = 'JWT token generated from API'
var ws = new WebSocket(`ws://localhost/ws?token=${token}`)
```