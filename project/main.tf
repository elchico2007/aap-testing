variable "ami" {}
variable "instance_type" {}
variable "name" {}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  alias  = "west"
  region = "us-west-1"
}

resource "aws_instance" "web" {
  provider      = aws.west
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = "aap-ssh-key"
  security_groups = [ "MyTestSecurityGroup" ]
  tags = {
    Name = var.name
  }
}