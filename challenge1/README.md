# devops-hiring-challenge

### challenge 1

A 3-tier environment is a common setup, Use a tool of your choosing/familiarity create those resources

Tech Used: Cloudformation Templates

Multiple AWS Cloudformation yml templates are created

1. VPC-setup.yml -> This template will create VPC, SGs, subnets, routing tables, NATs
2. ECS-cluster -> Define Cluster for 3-tier architecture
3. database.yml -> This template will setup the MYSQL RDS instance
4. AutoScaling-setup.yml -> This template will launch Multi-AZ EC2 instances in private and public subnets
5. ALB-setup -> Since we have a multi-region setup, an application load balancer is a must for dynamic port number
   mapping. This template will create appropriate application load balancers

6. Log-setup.yml -> Basic log setup for our application