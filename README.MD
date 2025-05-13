# About
This is a simple project to walk through getting Nginx working. 

# Pre steps 
1. Ensure you have a K8 cluster and a way to build docker files. I have installed Docker and enables K8 via it. 
2. My system is via WSL Ubuntu 22

# Steps
Its expected the following instruction be ran in terminal.
1. Build containers
2. Push to to k8
3. Apply K8 configs
4. port forward 

# Build and deploy each component
cd /frontend
docker build -t frontend .
cd /nginx
docker build -t nginx-gateway .
cd /backend
docker build -t backend-api .

# Push to K8
First if using docker deskopt K8, and WSL. Ensure you have `Kind` installed
Kind load docker-image frontend:latest
Kind load docker-image backend-api:latest
Kind load docker-image nginx-gateway:latest

# Apply K8 configs
kubectl apply -f /frontend/frontend.yaml
kubectl apply -f /nginx/nginx.yaml
kubectl apply -f /backend/backend.yaml

# Delete use if needed 
kubectl delete -f /frontend/frontend.yaml
kubectl delete -f /nginx/nginx.yaml
kubectl delete -f /backend/backend.yaml

# port forward
kubectl port-forward svc/nginx-gateway 8080:80