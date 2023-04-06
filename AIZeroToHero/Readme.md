
# Terraform Lesson for Azure

Pre-Reqs:
1. Terraform installed
2. Azure Cloud account setup
3. VSCode

Load resources to TF:
1. Create resources in AZ
2. Create TF files for resources
3. Run terraform apply
4. Run terraform import
5. Verify terraform state
6. Perform terraform destroy to clean up resources

Install VSCode.
In VS Code use the following steps to start TF
1. az login
2. terraform init
3. terraform plan out tfplan
4. terraform show -json tfplan >> tfplan.json
5. cat tfplan.json | more
