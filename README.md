# AWS Devops Infrastructure: Automated Continuous Delivery Pipeline

A GitOps and DevSecOps platform that automates the deployment of a containerized Flask application to Kubernetes. Built with Jenkins, Trivy, ArgoCD, NGINX Ingress, Terraform, and Docker.

## Architecture

```
[GitHub Push]
      |
      v
[Jenkins CI]
      |
      v
[Trivy Scan]
      |
      v
[Docker Build]
      |
      v
[Container Registry]
      |
      v
[ArgoCD GitOps Sync]
      |
      v
[Kubernetes (EKS)]
      |
      v
[NGINX Ingress]
      |
      v
[Users]
```



## Detailed Steps to Execute the Code

### Prerequisites

- Docker Desktop installed and running
- Git Bash (Windows) or Terminal (Mac/Linux)
- Terraform installed (for infrastructure validation)
- kubectl installed (for Kubernetes validation)
- Git installed

### 1. Clone the Repository

```bash
git clone https://github.com/farzeenmuneer/aws-devops-infrastructure.git
cd aws-devops-infrastructure
```

### 2. Build the Docker Image

```bash
docker build -t aws-devops-infrastructure/prod-app:latest ./app
```

### 3. Run the Application Locally

```bash
docker run -d -p 8080:8080 --name prod-app aws-devops-infrastructure/prod-app:latest
```

### 4. Test the Application

```bash
curl http://localhost:8080/
```

Expected output:

```json
{
  "service": "aws-devops-engine",
  "version": "1.0.0",
  "status": "running",
  "message": "Deployed via GitOps pipeline"
}
```

Test health endpoint:

```bash
curl http://localhost:8080/health
```

Expected output:

```json
{
  "status": "healthy",
  "service": "aws-devops-engine"
}
```

### 5. Stop the Container

```bash
docker stop prod-app
docker rm prod-app
```

### 6. Validate Terraform Configuration

```bash
cd terraform
terraform init
terraform validate
cd ..
```

Expected output:

```
Success! The configuration is valid.
```

### 7. Validate Kubernetes Manifests (requires running cluster)

```bash
kubectl apply -f k8s-gitops/namespace.yaml
kubectl apply -f k8s-gitops/deployment.yaml
kubectl apply -f k8s-gitops/service.yaml
kubectl apply -f k8s-gitops/ingress.yaml
```

### 8. Deploy ArgoCD Application (requires ArgoCD installed)

```bash
kubectl apply -f k8s-gitops/argocd-app.yaml
```

---

## Technologies Used

- Python
- Flask
- Docker and Docker Compose
- Jenkins (Declarative Pipeline)
- Groovy scripting
- Trivy security scanner
- Terraform 1.9+
- AWS VPC, EKS, IAM
- Kubernetes (EKS)
- ArgoCD
- NGINX Ingress Controller
- GitHub Actions
- Linux Bash
