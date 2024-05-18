# Restaurant Management System

## Goals and scope of project:
This system will be created using microservices, <br>
right now there will be only three of them:<br>
- Display Menu Service<br>
- Config Menu Service<br>
- Auth Service<br>
In the future I will fill up the project with other functionalities :)<br>

## Used technology and tools
API Gateway: Kong<br>
Service Discovery: Consul<br>
Communication between client and microservices: REST API<br>
Sync communication between microservices: gRPC<br>
Async communication between microservices: Kafka<br>
Cache: Redis<br>
Database Menu: MongoDB<br>
Database Employees: PostgreSQL<br>
Microservices: Fast API<br>

## System Architecture
For modeling system architecture I used technique called [c4model](https://c4model.com/)<br>
![Context Diagram](./context.png)
![Container Diagram](./container.png)