helm repo add hashicorp https://helm.releases.hashicorp.com <br>
helm repo update <br>
helm install --values ./consul-values.yaml consul hashicorp/consul --version "1.2.0" <br>
kubectl apply -f ./mongodb.yaml <br>
kubectl apply -f ./proxy-defaults.yaml <br>
kubectl apply -f ./menu-service.yaml <br>
kubectl apply -f ./intentions.yaml <br>
helm repo add kong https://charts.konghq.com <br>
helm repo update <br>
helm install external kong/kong --version 2.3.0 --values ./kong.yaml <br>
kubectl apply -f ./kong-service-default.yaml <br>
kubectl apply -f ./kongtoweb.yaml <br>
kubectl apply -f ./ingresskong.yaml <br>