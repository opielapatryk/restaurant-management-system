![Container Diagram](./container.png)


https://github.com/opielapatryk/restaurant-management-system/assets/104018084/dbb944c0-71a2-469e-9c6f-ecbfbd6f7ebb


# Restaurant Management System
To run project you need running kubernetes i.e. on Docker Desktop.<br>
Instruction for installation is located in kubernetes/readme.md<br>

## Goals and scope of project:
This system will be created using microservices, <br>
right now there will be only five of them:<br>
- Display Menu Service<br>
- Config Menu Service<br>
- Auth Service<br>
- Cart Service<br>
- Order Service<br>
In the future I will fill up the project with other functionalities :)<br>

## Used technology and tools
API Gateway: Consul<br>
Service Discovery: Consul<br>
Communication between client and microservices: REST API<br>
Sync communication between microservices: gRPC<br>
Async communication between microservices: RabbitMQ<br>
Cache: Redis<br>
Database Menu: MongoDB<br>
Database Employees: PostgreSQL<br>
Microservices: Fast API<br>
