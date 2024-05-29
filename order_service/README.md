# Order Service implemented with Hexagonal structure 
Create key and cert in certs/ dict using:<br>
openssl req -x509 -newkey rsa:4096 -nodes -out public-cert.pem -keyout private-key.pem -days 730<br>
also remember to create .env file in core directory<br><br>

Create 4 secret files: mongo_url, redis_url and rabbit_url, service_api_key<br>
on macos: /home/**********/.local/secrets<br>
on windows: C:\\Users\\**********\\AppData\\Roaming\\Python\\secrets<br><br>

mongo_url_dev: mongodb://phoenix:**********@localhost:27017/<br>
redis_url_dev: redis://localhost:6379/0<br>
rabbit_url_root_dev: amqp://guest:guest@127.0.0.1//<br>
service_api_key: ec42bd5f-e187-49f3-bbe5-2d70c9bd1a2e

## Security
API Endpoints are secured so to each request you need to apply X-API-Key header with value that you set in .env file i.e. SERVICE_API_KEY="0eeb3dba-b3a7-43ee-8b28-8d8e058e2f2c"