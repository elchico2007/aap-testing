terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
resource "aws_instance" "web" {
  ami           = ami
  instance_type = instance_type
  tags = {
    Name = name
  }
}