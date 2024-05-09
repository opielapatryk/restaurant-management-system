# Display Menu Microservice
## Project is created with Clean Architecture <br>

## External systems
Web Framework: Fast API <br>
Repository: MongoDB <br>

## Gateways
DB Interface <br>
i.e. class MongoRepo <br>

## Use Cases: "business logic"
### Receive repo + parameters, returns results
GET: List whole menu <br>
GET{id}: Get certain dish <br>

## Entities
### Modules:
Menu <br>
With embedded Dishes <br>