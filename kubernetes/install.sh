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

helm install --values values.yaml consul hashicorp/consul

retry_until_success "kubectl apply -f proxy-defaults.yaml" "proxy-defaults.yaml"

retry_until_success "kubectl apply -f redis.yaml" "redis.yaml"

retry_until_success "kubectl apply -f rabbitmq.yaml" "rabbitmq.yaml"

retry_until_success "kubectl apply -f mongodb.yaml" "mongodb.yaml"

retry_until_success "kubectl apply -f menu-config-mongodb.yaml" "menu-config-mongodb.yaml"

retry_until_success "kubectl apply -f menu.yaml" "menu.yaml"

retry_until_success "kubectl apply -f menu-config.yaml" "menu-config.yaml"

retry_until_success "kubectl apply -f postgres.yaml" "postgres.yaml"

retry_until_success "kubectl apply -f auth.yaml" "auth.yaml"

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
echo "Authentication: http://127.0.0.1:8000/api/v1/schema/auth"
echo "Cart: http://127.0.0.1:8000/api/v1/schema/cart"
echo "Config: http://127.0.0.1:8000/api/v1/schema/config"
echo "Display: http://127.0.0.1:8000/api/v1/schema/display"
echo "Order: http://127.0.0.1:8000/api/v1/schema/order"
echo "#######################################"

sleep 900 # Wait for services installation

# Determine the operating system and open URLs accordingly
OS="$(uname)"
if [ "$OS" == "Linux" ]; then
    if command -v xdg-open > /dev/null; then
        xdg-open "http://127.0.0.1:8000/api/v1/schema/auth"
        xdg-open "http://127.0.0.1:8000/api/v1/schema/cart"
        xdg-open "http://127.0.0.1:8000/api/v1/schema/config"
        xdg-open "http://127.0.0.1:8000/api/v1/schema/display"
        xdg-open "http://127.0.0.1:8000/api/v1/schema/order"
    elif command -v gnome-open > /dev/null; then
        gnome-open "http://127.0.0.1:8000/api/v1/schema/auth"
        gnome-open "http://127.0.0.1:8000/api/v1/schema/cart"
        gnome-open "http://127.0.0.1:8000/api/v1/schema/config"
        gnome-open "http://127.0.0.1:8000/api/v1/schema/display"
        gnome-open "http://127.0.0.1:8000/api/v1/schema/order"
    fi
elif [ "$OS" == "Darwin" ]; then
    open "http://127.0.0.1:8000/api/v1/schema/auth"
    open "http://127.0.0.1:8000/api/v1/schema/cart"
    open "http://127.0.0.1:8000/api/v1/schema/config"
    open "http://127.0.0.1:8000/api/v1/schema/display"
    open "http://127.0.0.1:8000/api/v1/schema/order"
elif [ "$OS" == "CYGWIN" ] || [ "$OS" == "MINGW" ] || [ "$OS" == "MSYS" ]; then
    start "http://127.0.0.1:8000/api/v1/schema/auth"
    start "http://127.0.0.1:8000/api/v1/schema/cart"
    start "http://127.0.0.1:8000/api/v1/schema/config"
    start "http://127.0.0.1:8000/api/v1/schema/display"
    start "http://127.0.0.1:8000/api/v1/schema/order"
else
    echo "Unsupported OS: $OS"
fi

kubectl get pods --watch