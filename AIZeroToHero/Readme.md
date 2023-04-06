
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

Powershell:
1. Change dir to location you landed TF files
2. terraform init
3. terraform validate
4. terraform apply

![image](https://user-images.githubusercontent.com/30595158/230362828-beba9230-24fb-45bd-a5a9-6f904eb09812.png)
