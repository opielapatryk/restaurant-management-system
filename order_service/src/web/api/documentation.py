from fastapi import Path

# Local modules
from ...core.setup import config

order_id_documentation = Path(
    ...,
    description='**Order ID**: *Example `dbb86c27-2eed-410d-881e-ad47487dd228`*. '
                'A unique identifier for an existing Order.',
)
""" OpenAPI order ID documentation. """


tags_metadata = [
    {
        "name": "Orders",
        "description": f"The ***{config.service_name}*** handle Orders for the Fictitious Company.",
    }
]
""" OpenAPI Orders endpoint documentation. """

license_info = {
    "name": "License: Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}
""" OpenAPI license documentation. """

servers = [
    {
        "url": "http://127.0.0.1:1030",
        "description": "URL for local development and testing"
    }
]
""" OpenAPI API platform servers. """

description = """
<img width="50%" align="right" alt="container-diagram" src="https://raw.githubusercontent.com/opielapatryk/restaurant-management-system/main/container.png"/>
<br><br><br><br>
**This service implements a Facade pattern to simplify the complexity between the MicroServices in the system 
and the WEB GUI program.** 

The OrderService handles multiple status updates from several services during the lifecycle of an Order. These 
responses are asynchronous events spread out over time and to be able to handle this type of dynamic the RabbitMQ 
message broker is used. The RabbitMQ queue routing technique is used since it is designed to scale with the growing 
needs of the service.

<br>**The following HTTP status codes are returned:**
  * `200:` Successful GET response.
  * `202:` Successful POST response.
  * `204:` Successful DELETE response.
  * `400:` Failed updating Order in DB.
  * `404:` Order not found in DB.
  * `422:` Validation error, supplied parameter(s) are incorrect.
  * `500:` Failed to connect to internal MicroService.
<br><br>
---
"""
""" OpenAPI main Order documentation. """

