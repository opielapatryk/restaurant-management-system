# Deploy services using ./install.sh 
run: <br> 
chmod +x install.sh <br>
./install.sh <br><br>

kubectl get svc api-gateway<br>
Connect with apigateway using NodePort: https  xxxxx/TCP<br>
https://127.0.0.1:xxxxx/<br>

# To install monitoring tools use: 
chmod +x install-observability-suite.sh<br>
./install-observability-suite.sh<br>


# Or do everything manually
helm repo add hashicorp https://helm.releases.hashicorp.com<br>
helm install --values values-v1.yaml consul hashicorp/consul --version "1.2.0"<br>
export CONSUL_HTTP_TOKEN=$(kubectl get secrets/consul-bootstrap-acl-token --template={{.data.token}} | base64 -d)<br>       
export CONSUL_HTTP_ADDR=https://127.0.0.1:8501<br>
export CONSUL_HTTP_SSL_VERIFY=false<br>
kubectl port-forward svc/consul-ui 8501:443<br>
consul catalog services<br>
consul<br>
consul members<br>
consul-server-0<br>
<br>
kubectl apply -f proxy-defaults.yaml<br>
kubectl apply -f redis.yaml<br>
kubectl apply -f mongodb.yaml<br>
kubectl apply -f menu.yaml<br>
kubectl apply -f allow.yaml<br>
<br>
kubectl apply -f consul-api-gateway.yaml<br>
kubectl apply -f routes.yaml<br>
kubectl apply -f referencegrant.yaml<br> 
kubectl apply -f rbac.yaml<br>  
<br>
kubectl get svc api-gateway<br>
Connect with apigateway using NodePort: https  xxxxx/TCP<br>
https://127.0.0.1:xxxxx/<br>