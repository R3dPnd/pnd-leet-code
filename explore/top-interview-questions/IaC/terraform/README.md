# Top 10 Terraform Interview Questions

## 1. What is Terraform and what are its key features?

**Answer:** Terraform is an Infrastructure as Code (IaC) tool developed by HashiCorp that allows you to define and provision infrastructure resources using declarative configuration files.

**Key Features:**
- **Declarative Configuration**: Define what you want, not how to create it
- **Multi-Cloud Support**: Works with AWS, Azure, GCP, and many others
- **State Management**: Tracks resource state and dependencies
- **Plan and Apply**: Preview changes before applying them
- **Version Control**: Configuration files can be version controlled

**Example:**
```hcl
# Define an AWS EC2 instance
resource "aws_instance" "web_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}
```

## 2. Explain the difference between Terraform and other IaC tools like Ansible or CloudFormation.

**Answer:**

| Feature               | Terraform   | Ansible    | CloudFormation |
|-----------------------|-------------|------------|----------------|
| **Type**              | Declarative | Imperative | Declarative    |
| **Multi-Cloud**       | Yes         | Yes        | AWS Only       |
| **State Management**  | Built-in    | External   | AWS-managed    |
| **Agent Required**    | No          | Yes (SSH)  | No             |
| **Learning Curve**    | Moderate    | Low        | Moderate       |

**Terraform Advantages:**
- Provider-agnostic (works with any cloud)
- Strong state management
- Rich ecosystem of providers
- Better for infrastructure provisioning

## 3. What is Terraform state and why is it important?

**Answer:** Terraform state is a snapshot that maps real-world resources to your configuration, keeps track of metadata, and improves performance for large infrastructures.

**Key Points:**
- **Resource Mapping**: Links configuration to actual resources
- **Dependency Tracking**: Manages resource relationships
- **Performance**: Avoids unnecessary API calls
- **Concurrency**: Prevents conflicts when multiple users run Terraform

**State Backend Example:**
```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "us-west-2"
  }
}
```

**Best Practices:**
- Use remote state storage (S3, Azure Storage, GCS)
- Enable state locking (DynamoDB, Azure Table Storage)
- Use workspaces for environment separation
- Never edit state files manually

## 4. Explain Terraform providers, resources, and data sources.

**Answer:**

### Providers
Providers are plugins that Terraform uses to interact with cloud providers, SaaS providers, and other APIs.

```hcl
# Configure AWS Provider
provider "aws" {
  region = "us-west-2"
  profile = "default"
}

# Configure Azure Provider
provider "azurerm" {
  features {}
}
```

### Resources
Resources are the infrastructure objects that Terraform manages.

```hcl
# AWS EC2 Instance Resource
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}

# Azure Virtual Network Resource
resource "azurerm_virtual_network" "main" {
  name                = "main-network"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  address_space       = ["10.0.0.0/16"]
}
```

### Data Sources
Data sources allow Terraform to fetch information about existing resources.

```hcl
# Get existing VPC
data "aws_vpc" "existing" {
  id = "vpc-12345678"
}

# Use data source in resource
resource "aws_subnet" "main" {
  vpc_id     = data.aws_vpc.existing.id
  cidr_block = "10.0.1.0/24"
}
```

## 5. What are Terraform modules and how do you use them?

**Answer:** Modules are reusable, self-contained packages of Terraform configurations that manage a set of related resources.

**Benefits:**
- **Reusability**: Write once, use many times
- **Encapsulation**: Hide complexity
- **Consistency**: Standardize infrastructure patterns
- **Versioning**: Use specific module versions

**Module Structure:**
```
module/
├── main.tf          # Main configuration
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
└── README.md        # Documentation
```

**Example Module Usage:**
```hcl
# Call a VPC module
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr = "10.0.0.0/16"
  environment = "production"
  
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
}

# Use module outputs
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_ids[0]
}
```

## 6. Explain Terraform variables, locals, and outputs.

**Answer:**

### Variables
Variables allow you to customize configurations without changing the code.

```hcl
# variables.tf
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
  
  validation {
    condition     = contains(["t2.micro", "t2.small", "t2.medium"], var.instance_type)
    error_message = "Instance type must be t2.micro, t2.small, or t2.medium."
  }
}

variable "environment" {
  description = "Environment name"
  type        = string
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

### Locals
Locals assign a name to an expression, making the configuration more readable.

```hcl
# locals.tf
locals {
  common_tags = {
    Environment = var.environment
    Project     = "MyApp"
    ManagedBy   = "Terraform"
  }
  
  instance_name = "${var.environment}-web-server"
}
```

### Outputs
Outputs expose specific values from your configuration.

```hcl
# outputs.tf
output "instance_id" {
  description = "ID of the created EC2 instance"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP of the instance"
  value       = aws_instance.web.public_ip
}

output "private_ip" {
  description = "Private IP of the instance"
  value       = aws_instance.web.private_ip
}
```

## 7. What is Terraform workspace and when would you use it?

**Answer:** Terraform workspaces allow you to manage multiple state files within a single Terraform configuration.

**Use Cases:**
- **Environment Separation**: dev, staging, prod
- **Feature Branches**: Different configurations for testing
- **Parallel Development**: Multiple developers working simultaneously

**Workspace Commands:**
```bash
# List workspaces
terraform workspace list

# Create new workspace
terraform workspace new dev

# Switch to workspace
terraform workspace select prod

# Show current workspace
terraform workspace show
```

**Example Usage:**
```hcl
# Use workspace in configuration
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  tags = {
    Name        = "WebServer-${terraform.workspace}"
    Environment = terraform.workspace
  }
}

# Conditional resources based on workspace
resource "aws_instance" "monitoring" {
  count = terraform.workspace == "prod" ? 1 : 0
  
  ami           = "ami-87654321"
  instance_type = "t2.small"
  
  tags = {
    Name = "MonitoringServer"
  }
}
```

## 8. Explain Terraform data sources and when to use them.

**Answer:** Data sources allow Terraform to fetch information about resources that exist outside of Terraform's management.

**Common Use Cases:**
- **Existing Infrastructure**: Reference resources created manually
- **Shared Resources**: Use resources managed by other teams
- **Lookup Information**: Get AMIs, VPCs, subnets, etc.

**Example Data Sources:**
```hcl
# Get latest Amazon Linux AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn-ami-hvm-*-x86_64-gp2"]
  }
  
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Get existing VPC
data "aws_vpc" "existing" {
  tags = {
    Name = "MyVPC"
  }
}

# Get availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Use data sources in resources
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"
  subnet_id     = data.aws_subnet.selected.id
}

data "aws_subnet" "selected" {
  vpc_id = data.aws_vpc.existing.id
  availability_zone = data.aws_availability_zones.available.names[0]
}
```

## 9. What are Terraform provisioners and what are their limitations?

**Answer:** Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction.

**Types of Provisioners:**
- **local-exec**: Execute commands locally
- **remote-exec**: Execute commands on remote resources
- **file**: Copy files to remote resources
- **null_resource**: Execute provisioners without a specific resource

**Example:**
```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  # Copy file to instance
  provisioner "file" {
    source      = "scripts/setup.sh"
    destination = "/tmp/setup.sh"
    
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }
  
  # Execute script on instance
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/setup.sh",
      "/tmp/setup.sh"
    ]
    
    connection {
      type        = "ssh"
      user        = "ec2-user"
      private_key = file("~/.ssh/id_rsa")
      host        = self.public_ip
    }
  }
}
```

**Limitations:**
- **State Dependency**: Provisioners run only when resource is created/destroyed
- **Error Handling**: Difficult to handle provisioner failures
- **Idempotency**: Scripts must be idempotent
- **Security**: Credentials and scripts in plain text
- **Maintenance**: Hard to maintain and debug

**Best Practices:**
- Use provisioners as last resort
- Prefer cloud-init or user data scripts
- Keep provisioners simple and idempotent
- Use external tools (Ansible, Chef, Puppet) for complex configuration

## 10. How do you handle secrets and sensitive data in Terraform?

**Answer:** Terraform provides several ways to handle sensitive data securely.

### Environment Variables
```bash
export TF_VAR_db_password="secret123"
export TF_VAR_api_key="abc123"
```

### Variable Definitions File
```hcl
# terraform.tfvars (never commit to version control)
db_password = "secret123"
api_key     = "abc123"
```

### Sensitive Variables
```hcl
# variables.tf
variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

variable "api_key" {
  description = "API key"
  type        = string
  sensitive   = true
}

# Use in resources
resource "aws_db_instance" "main" {
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  db_name              = "mydb"
  username             = "admin"
  password             = var.db_password  # Terraform will hide this in logs
}
```

### AWS Secrets Manager Integration
```hcl
# Get secret from AWS Secrets Manager
data "aws_secretsmanager_secret" "db_password" {
  name = "prod/db/password"
}

data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = data.aws_secretsmanager_secret.db_password.id
}

# Use in resource
resource "aws_db_instance" "main" {
  engine               = "mysql"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  db_name              = "mydb"
  username             = "admin"
  password             = jsondecode(data.aws_secretsmanager_secret_version.db_password.secret_string)["password"]
}
```

### Best Practices:
- **Never commit secrets** to version control
- Use **sensitive = true** for sensitive variables
- Use **cloud-native secret management** (AWS Secrets Manager, Azure Key Vault)
- Use **environment variables** for local development
- Use **CI/CD secrets** for automated deployments
- **Rotate secrets** regularly
- Use **least privilege** access policies

---

## Additional Resources

- [Terraform Official Documentation](https://www.terraform.io/docs)
- [Terraform Best Practices](https://www.terraform.io/docs/cloud/guides/recommended-practices/index.html)
- [Terraform Provider Registry](https://registry.terraform.io/)
- [Terraform Modules Registry](https://registry.terraform.io/browse/modules)
