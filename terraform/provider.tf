terraform {
    required_version = ">= 1.0"
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~>5"
        }
    }

    backend "s3" {
        bucket               = "neoris-devops-infra"
        workspace_key_prefix = "environments"
        key                  = "terraform.tfstate"
        region               = "us-east-2"
        acl                  = "private"
    }
  
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      ManagedBy   = "Terraform"
    }
  }
}

