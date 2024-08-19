# WEB Environtment Display Variable Project

This project is a simple web application that displays the api of requeriment. It uses Flask for the backend. The application is deployed on AWS ECS and uses GitHub Actions for CI/CD, along with Terraform for infrastructure on AWS.

## Project Structure
```
project-root/
│
├── app/
│ ├── __init__.py
│ ├── routes.py
│
├── terraform/
│ ├── .terraform/
│ │ ├── .terraform.lock.hcl
│ ├── main.tf
│ ├── outputs.tf
│ ├── provider.tf
│ ├── variables.tf
│ ├── variables.tf.example
│
├── tests/
│ ├── __init__.py
│ ├── test_routes.py
│
├── .github/
│ ├── workflows/
│
├── venv/
│ ├── .coverage
│ ├── coverage.xml
│
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```
## Backend

- **Framework**: Flask
- **Language**: Python
- **Dockerfile**: Defines the Docker image for the Flask backend.

## Infrastructure with Terraform

- **Terraform**: Used to define and deploy the infrastructure on AWS.

## CI/CD with GitHub Actions

The CI/CD pipeline is configured in GitHub Actions to install dependencies, build the container image, test the image, publish the image to a container registry, and deploy the image on AWS ECS.

## Commands to Build, Deploy, and Test Locally

### Build and Run Containers Locally

1. **Build the image:**
   ```sh
   docker build -t flask-devops .
   ```

2. **Run the container:**
   ```sh
   docker run  -p 5000:5000 --name flask-devops-container flask-devops-app
   ```
   
3. **Access the application:**
   Open your web browser and go to `http://localhost:5000`. You should see the deployment environment displayed on the screen.

4. **Test endpoints of the Api:**


### Parte 4: Endpoints
   #### Health Check

   - **Método**: `GET`
   - **URL**: `/health`

   ```sh
   curl -X GET http://HOST:5000/health
   ```

   Response
   ```sh
   {
      "status": "OK"
   }
   ```
   #### Generate JWT

   - **Método**: `POST`
   - **URL**: `/jwt`

   ```sh
   curl -X POST http://HOST:5000/jwt \
   -H "Content-Type: application/json" \
   -d '{
   "username": "neoris",
   "password": "abc123"
   }'
   ```

   Response
   ```sh
   {
    "jwt": "<JWT_TOKEN>"
   }
   ```

   #### Response Devops

   - **Método**: `POST`
   - **URL**: `/DevOps`

   ```sh
   curl -X POST http://HOST:5000/DevOps \
   -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
   -H "X-JWT-KWY: <JWT_TOKEN>" \
   -H "Content-Type: application/json" \
   -d '{
   "message": "This is a test",
   "to": "Juan Perez",
   "from": "Rita Asturia",
   "timeToLifeSec": 45
   }'

   ```
   Response
   ```sh
   {
    "message": "Hello Juan Perez, your message will be send"
   }
   ```

5. **Destroy image Docker:**
   ```sh
       docker rm flask-devops-container
   ```

### Deploy Infrastructure with Terraform

1. **Configure AWS CLI:**
   ```sh
   aws configure
   ```

2. **Initialize Terraform:**
   ```sh
   cd terraform
   terraform init
   ```

3. **Apply Terraform configuration:**
   ```sh
   terraform apply
   ```

## CI/CD Configuration with GitHub Actions

The GitHub Actions workflow file is located at `.github/workflows/test|develop.yml`. This pipeline runs automatically on commits to either the `develop`, `testing` and `main` branches, setting the `ENVIRONMENT_NAME` environment variable based on the branch.

### Environment Variables

Make sure to set the following environment variables in your GitHub repository secrets (Settings > Secrets):

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`
- `AWS_REGION`
- `ECR_REPOSITORY_BACKEND`
- `ECR_REPOSITORY_FRONTEND`
- `ECS_CLUSTER_NAME`
- `ECS_SERVICE_NAME`
- `ECS_TASK_DEFINITION_NAME`

## Additional Notes

- **Environment Variables:**
  - Ensure that environment variables are set correctly for both local development and AWS deployment.
- **AWS Credentials:**
  - Set up your AWS credentials in your local environment to allow Terraform and AWS commands to work correctly.
