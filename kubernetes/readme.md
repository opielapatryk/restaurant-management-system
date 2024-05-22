# Deploy services using ./install.sh 
run: <br> 
chmod +x install.sh <br>
./install.sh <br><br>

kubectl get svc api-gateway<br>
Connect with apigateway using NodePort: https  xxxxx/TCP<br><br>
menu_config: https://127.0.0.1:xxxxx/api/v1/config/docs<br>
menu_display: https://127.0.0.1:xxxxx/api/v1/display/docs<br>

# To install monitoring tools use: 
chmod +x install-observability-suite.sh<br>
./install-observability-suite.sh<br>