# Terraform for AKS Cluster in Azure

This repository contains the Terraform configuration files to provision a **AKS cluster** in Azure with the following setup:
- Resource Group creation
- Virtual Network (VNet) and Subnet configuration
- AKS Cluster setup
- Outputs for credentials and resource details

## Prerequisites

1. **Terraform**: Ensure that you have [Terraform](https://www.terraform.io/downloads.html) installed on your machine.
2. **Azure CLI**: Make sure you have the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and authenticated.
3. **Azure Subscription**: You need an active Azure subscription.
## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/sumit0012/hello-sql.git
cd hello-sql

### Step 2: Configure Terraform Variables

# Azure Subscription ID
subscription_id = "<your-subscription-id>"

# Resource Group Name
resource_group_name = "hello-world-rg"

# Location for Azure resources
location = "East US"

# Virtual Network Name
vnet_name = "hello-world-vnet"

# Subnet Name for AKS
subnet_name = "hello-world-subnet"

# AKS Cluster Name
aks_cluster_name = "hello-world-aks"

# Kubernetes Version
kubernetes_version = "1.21.2"

# Node Count and Size
node_count = 1
node_size = "Standard_DS2_v2"

### Step 3: Initialize Terraform
terraform init

### Step 4: Plan the Deployment
terraform plan

### Step 5: Apply the Configuration
terraform apply --auto-approve

### Step 6: Access the AKS Cluster
az aks get-credentials --resource-group hello-world-rg --name hello-world-aks

### Step 7: Verify AKS Cluster
kubectl get nodes

### Step 8: Cleanup (Optional)
terraform destroy --auto-approve
