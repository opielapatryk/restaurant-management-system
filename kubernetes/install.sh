#!/bin/bash

set -e

function retry_until_success {
  local cmd=$1
  local yaml_file=$2

  until $cmd; do
    echo "Retrying $yaml_file due to previous failure..."
    sleep 5
  done
}

helm repo add hashicorp https://helm.releases.hashicorp.com

helm repo update

# helm install --values values-eks.yaml consul hashicorp/consul #aws
helm install --values values.yaml consul hashicorp/consul --version "1.2.0"

retry_until_success "kubectl apply -f proxy-defaults.yaml" "proxy-defaults.yaml"

retry_until_success "kubectl apply -f redis.yaml" "redis.yaml"

retry_until_success "kubectl apply -f rabbitmq.yaml" "rabbitmq.yaml"

retry_until_success "kubectl apply -f mongodb.yaml" "mongodb.yaml"

retry_until_success "kubectl apply -f menu-config-mongodb.yaml" "menu-config-mongodb.yaml"

retry_until_success "kubectl apply -f menu.yaml" "menu.yaml"

retry_until_success "kubectl apply -f menu-config.yaml" "menu-config.yaml"

retry_until_success "kubectl apply -f postgres.yaml" "postgres.yaml"

retry_until_success "kubectl apply -f auth.yaml" "auth.yaml"

retry_until_success "kubectl apply -f order-mongodb.yaml" "order-mongodb.yaml"

retry_until_success "kubectl apply -f order-grpc.yaml" "order-grpc.yaml"

retry_until_success "kubectl apply -f order.yaml" "order.yaml"

retry_until_success "kubectl apply -f cart-redis.yaml" "cart-redis.yaml"

retry_until_success "kubectl apply -f cart.yaml" "cart.yaml"

retry_until_success "kubectl apply -f nginx.yaml" "nginx.yaml"

retry_until_success "kubectl apply -f allow.yaml" "allow.yaml"

retry_until_success "kubectl apply -f consul-api-gateway.yaml" "consul-api-gateway.yaml"

retry_until_success "kubectl apply -f routes.yaml" "routes.yaml"

retry_until_success "kubectl apply -f referencegrant.yaml" "referencegrant.yaml"

retry_until_success "kubectl apply -f rbac.yaml" "rbac.yaml"

echo "#######################################"
echo "Deployment Complete"
echo "Grab your coffe and come back in 15 minutes :)"
echo "Endpoints:"
echo "Config: http://127.0.0.1:8000/api/v1/config/docs"
echo "Display: http://127.0.0.1:8000/api/v1/display/docs"
echo "Cart: http://127.0.0.1:8000/api/v1/cart/docs"
echo "Orders: http://127.0.0.1:8000/api/v1/orders/docs"
echo "#######################################"