1. Introduction
This report provides a comprehensive guide to deploying a Machine Learning (ML)
model using Docker, Kubernetes, and Minikube. The model is packaged as a Flask API
and deployed on a local Kubernetes cluster.
2. Prerequisites
Before starting, ensure the following tools are installed:
 Python 3.9+
 Docker
 Minikube
 Kubectl
 Curl (for API testing)
3. Project Structure
C:\ujwal\
│-- app.py
│-- model.py
│-- model.pkl
│-- requirements.txt
│-- Dockerfile
│-- deployment.yaml
│-- service.yaml
4. Build & Run the Docker Image
cd "your dockerfile path"
docker build -t ml-flask-app .
docker run -p 5000:5000 ml-flask-app
5. Deploying with Kubernetes & Minikube
   5.1. Start Minikube
    minikube start
   5.2. Load the Docker Image into Minikube
    minikube image load ml-flask-app
   5.3. Deploy the Application
    kubectl apply -f C:\Gururaj\deployment.yaml #your yaml file path
    kubectl apply -f C:\Gururaj\service.yaml #your yaml file path
   5.4. Verify Deployment
    kubectl get pods
    kubectl get services
6. Accessing the Application
  6.1. Get Service URL
    minikube service ml-flask-service --url
    Example Output:
    http://127.0.0.1:51813
   6.2. Test API Endpoints
    Home Route
    curl http://127.0.0.1:51813/   
   
