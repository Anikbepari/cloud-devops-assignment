CI/CD Pipeline with GitHub Actions and AWS ECS

Assignment Completion Report

Overview

In this assignment, I successfully implemented a CI/CD pipeline using GitHub Actions to deploy a containerized Flask application on AWS ECS. The pipeline automates the build, test, and deployment process, ensuring faster delivery and easier rollbacks. The application is a simple Flask app that responds with a message set as an environment variable.

Steps Completed

1. Created IAM users and roles: Set up IAM users and roles with necessary permissions for AWS services, including AmazonEC2FullAccess, AmazonEC2ContainerRegistryFullAccess, and AmazonECS_FullAccess.

2. Configured Elastic Container Registry (ECR): Created an ECR repository to store Docker images.

3. Set up Elastic Container Service (ECS): Created an ECS cluster, task definition, and service for deploying the application.

4. Created a GitHub repository: Pushed the Flask application code and Dockerfile to a GitHub repository.

5. Configured GitHub Secrets: Stored AWS credentials as GitHub secrets for secure access.

6. Created a GitHub Actions workflow: Defined a workflow to automate the build, test, and deployment process.

7. Deployed the application: Successfully deployed the application on AWS ECS using the CI/CD pipeline.

8. Performed integration tests: Ran integration tests using Pytest to test the Flask application's functionality.

9. Implemented rollback functionality: Added steps to check for deployment success and rollback in case of failure.

GitHub Actions Workflow

The workflow consists of the following steps:

1. Checkout code: Checks out the code from the GitHub repository.

2. Configure AWS credentials: Configures AWS credentials using GitHub secrets.

3. Login to Amazon ECR: Logs in to Amazon ECR using AWS credentials.

4. Build, tag, and push image to Amazon ECR: Builds a Docker image, tags it, and pushes it to Amazon ECR.

5. Fill in the new image ID in the Amazon ECS task definition: Updates the ECS task definition with the new image ID.

6. Deploy Amazon ECS task definition: Deploys the updated ECS task definition.

7. Run integration tests: Runs integration tests using Pytest.

8. Check deployment success: Checks if the deployment was successful.

9. Rollback deployment: Rolls back the deployment in case of failure.

Environment Variables

The following environment variables were set up:

- AWS_REGION: Operating region of AWS services.
- ECR_REPOSITORY: Name of the ECR repository.
- ECS_SERVICE: Service name of the ECS cluster.
- ECS_CLUSTER: Name of the ECS cluster.
- ECS_TASK_DEFINITION: Path of the ECS task definition in JSON format.
- CONTAINER_NAME: Docker container name under the ECS task definition.

Setup

1. Clone this repository to your local machine.
2. Create an AWS account and set up IAM users and roles with necessary permissions.
3. Create an ECR repository and an ECS cluster, task definition, and service.
4. Configure GitHub Secrets with your AWS credentials.
5. Update the environment variables in the GitHub Actions workflow file (.yml) with your AWS region, ECR repository, ECS service, and cluster.

Usage

1. Make changes to the Flask application code or Dockerfile.
2. Commit and push the changes to the GitHub repository.
3. The GitHub Actions workflow will automatically trigger and execute the pipeline.

Testing

1. Run integration tests using Pytest by executing the command pytest tests/ in the terminal.
2. Verify that the tests pass successfully.

Pipeline Details

1. The pipeline checks out the code from the GitHub repository.
2. Configures AWS credentials using GitHub Secrets.
3. Logs in to Amazon ECR using AWS credentials.
4. Builds, tags, and pushes the Docker image to Amazon ECR.
5. Updates the ECS task definition with the new image ID.
6. Deploys the updated ECS task definition.
7. Runs integration tests using Pytest.
8. Checks for deployment success and rolls back in case of failure.

Rollback Functionality

In case of deployment failure, the pipeline will automatically roll back to the previous successful deployment.
