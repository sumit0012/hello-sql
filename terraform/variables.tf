variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "c7c0c81d-79ac-49eb-8aa0-c9f16e51cca1"
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "hello-world-rg"
}

variable "location" {
  description = "Azure region to deploy resources"
  type        = string
  default     = "East US"
}

variable "vnet_name" {
  description = "Name of the virtual network"
  type        = string
  default     = "hello-world-vnet"
}

variable "vnet_address_space" {
  description = "Address space for the virtual network"
  type        = list(string)
  default     = ["10.0.0.0/16"]
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
  default     = "hello-world-subnet"
}

variable "subnet_address_prefix" {
  description = "Subnet address prefix"
  type        = list(string)
  default     = ["10.0.1.0/24"]
}

variable "aks_name" {
  description = "Name of the AKS cluster"
  type        = string
  default     = "hello-world-aks"
}

variable "dns_prefix" {
  description = "DNS prefix for the AKS cluster"
  type        = string
  default     = "helloaks"
}

variable "node_count" {
  description = "Number of nodes in the cluster"
  type        = number
  default     = 1
}

variable "vm_size" {
  description = "VM size for AKS nodes"
  type        = string
  default     = "Standard_D2_v2"
}
