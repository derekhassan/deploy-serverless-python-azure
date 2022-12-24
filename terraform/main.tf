terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.0"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "resource_group" {
  name     = "rg-${var.project}-${var.environment}-001"
  location = var.location
}

resource "azurerm_storage_account" "storage_account" {
  name                     = "st${var.project}${var.environment}001"
  resource_group_name      = azurerm_resource_group.resource_group.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_application_insights" "application_insights" {
  name                = "appi-${var.project}-${var.environment}-001"
  location            = var.location
  resource_group_name = azurerm_resource_group.resource_group.name
  application_type    = "other"
}

# A Function App must always be associated with an App Service Plan
resource "azurerm_service_plan" "service_plan" {
  name                = "asp-${var.project}-${var.environment}-001"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = var.location
  os_type             = "Linux"
  sku_name            = "Y1"
}


resource "azurerm_linux_function_app" "function_app" {
  name                = "func-${var.project}-${var.environment}-001"
  resource_group_name = azurerm_resource_group.resource_group.name
  location            = var.location

  storage_account_name       = azurerm_storage_account.storage_account.name
  storage_account_access_key = azurerm_storage_account.storage_account.primary_access_key
  service_plan_id            = azurerm_service_plan.service_plan.id

  site_config {}
}
