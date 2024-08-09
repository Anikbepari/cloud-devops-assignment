CI/CD Pipeline with GitHub Actions and AWS ECS

Assignment Completion Report

Overview

In this assignment, I successfully implemented a CI/CD pipeline using GitHub Actions to deploy a containerized Flask application on AWS ECS. The pipeline automates the build, test, and deployment process, ensuring faster delivery and easier rollbacks. The application is a simple Flask app that responds with a message set as an environment variable.

reated a GitHub Actions workflow: Defined a workflow to automate the build, test, and deployment process.

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

Conclusion

This assignment demonstrated the power of CI/CD pipelines in automating software delivery processes. By using GitHub Actions and AWS ECS, I successfully deployed a containerized Flask application with automated build, test, and deployment capabilities, including integration testing and rollback functionality. The pipeline ensures faster delivery, easier rollbacks, and improved collaboration among team members.
