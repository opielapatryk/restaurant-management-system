helm repo add hashicorp https://helm.releases.hashicorp.com && \
helm install --values values-v1.yaml consul hashicorp/consul --version "1.2.0" && \
kubectl wait --for=condition=available --timeout=90s deployment/consul-connect-injector && \
kubectl apply -f proxy-defaults.yaml && \
kubectl apply -f redis.yaml && \
kubectl apply -f mongodb.yaml && \
kubectl apply -f menu.yaml && \
kubectl apply -f allow.yaml && \
kubectl apply -f consul-api-gateway.yaml && \
kubectl apply -f routes.yaml && \
kubectl apply -f referencegrant.yaml && \
kubectl apply -f rbac.yaml && \
echo "#######################################" && \
echo "Deployment Complete" && \
echo "#######################################"