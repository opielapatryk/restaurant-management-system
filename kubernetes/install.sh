helm repo add hashicorp https://helm.releases.hashicorp.com && \
helm install --values values-v1.yaml consul hashicorp/consul --version "1.2.0" && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f proxy-defaults.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f redis.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f rabbitmq.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f mongodb.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f menu-config-mongodb.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f menu.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f menu-config.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f postgres.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f auth.yaml && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f nginx.yaml && \
kubectl apply -f allow.yaml && \
kubectl apply -f consul-api-gateway.yaml && \
kubectl apply -f routes.yaml && \
kubectl apply -f referencegrant.yaml && \
kubectl apply -f rbac.yaml && \
echo "#######################################" && \
echo "Deployment Complete" && \
echo "#######################################"
