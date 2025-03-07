### 1️. Docker Setup

Build and Push Docker Image

docker build -t hello-world:latest .
docker tag hello-world:latest sam3ctc/hello-world:latest  
docker push sam3ctc/hello-world:latest  

### 2️. Deploy with Helm

Add Helm Repo and Install Dependencies

helm repo add bitnami https://charts.bitnami.com/bitnami  

Deploy MySQL and the Application

helm install hello-world-release ./helm-chart -n hwsql

### 3️. Provision AKS with Terraform

Initialize and Apply Terraform Configuration

terraform init
terraform apply -auto-approve

### 4. Enable TLS with Cert-Manager

Install Cert-Manager

helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --set installCRDs=true

Configure TLS Certificate

Create a ClusterIssuer for Let's Encrypt.

Apply TLS certificate and update Ingress.

### 5️. Access the Application

🔗 https://sumit.cfs.in.net