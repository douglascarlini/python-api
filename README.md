# Python API RESTful

Simple Python RESTful API using FastAPI with WebSocket support.

### Deploy

- Create a `.env` file with the follow settings:

```
# JWT GENERATE CONFIG
JWT_SECRET=secret-key
JWT_EXPIRE=28800

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

- Load environment variable from `.env`:
    - `$ cat .env`

- Deploy:
    - `docker-compose up -d`

### WebSocket

```javascript
var token = 'JWT token generated from API'
var ws = new WebSocket(`ws://localhost/ws?token=${token}`)
```