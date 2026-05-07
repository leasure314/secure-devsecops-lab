# Secure DevSecOps Pipeline Lab

A hands-on DevSecOps lab project focused on building and securing a modern CI/CD pipeline using Docker, GitHub Actions, vulnerability scanning, and automated deployments.

This project was built to simulate a real-world secure software delivery workflow while developing operational experience in Linux, containers, networking, automation, and security engineering.

---

# Project Goals

This lab demonstrates:

- CI/CD pipeline automation
- Containerized application deployment
- Security scanning in the pipeline
- Secure SSH-based deployments
- Linux server administration
- Infrastructure troubleshooting
- DevSecOps workflow integration

---

# Architecture Overview

```text
Developer Pushes Code
        │
        ▼
GitHub Repository
        │
        ▼
GitHub Actions Pipeline
        │
 ┌──────┴──────┐
 ▼             ▼
Secret Scan    Vulnerability Scan
(Gitleaks)     (Trivy)
        │
        ▼
Docker Image Build
        │
        ▼
SSH Deployment to Ubuntu VM
        │
        ▼
Docker Compose Stack
        │
        ▼  
    Flask App    
        │
        ▼
  HTTPS Access
```

---

# Technologies Used

## DevOps

- Docker
- Docker Compose
- GitHub Actions
- Git
- Linux (Ubuntu Server)

## Security

- Trivy
- Gitleaks
- SSH Key Authentication


## Application Stack

- Python
- Flask
- Gunicorn

## Infrastructure

- Proxmox VE
- Ubuntu Server 24.04 LTS

---

# Features

## Security Features

- Non-root Docker container
- Automated vulnerability scanning
- Automated secret scanning
- SSH key-only authentication
- Minimal container image footprint

## DevOps Features

- Automated CI/CD pipeline
- Dockerized application deployment
- Infrastructure-as-code style configuration
- GitHub-triggered deployments
- Container rebuild automation

---

# Project Structure

```text
secure-ci-lab/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── .gitignore
└── .github/
    └── workflows/
        └── pipeline.yml
```

---

# CI/CD Pipeline Workflow

The GitHub Actions pipeline automatically executes when code is pushed to the `main` branch.

Pipeline stages:

1. Checkout repository
2. Install dependencies
3. Run vulnerability scans
4. Run secret detection scans
5. Build Docker image
6. Scan container image
7. Deploy application to Linux VM over SSH

---

# Vulnerability Scanning

## Trivy

Trivy scans:
- filesystem dependencies
- container images
- known CVEs
- vulnerable packages

Example pipeline stage:

```yaml
- name: Run Trivy Scan
  uses: aquasecurity/trivy-action@master
  with:
    scan-type: fs
    scan-ref: .
```

---

# Secret Detection

## Gitleaks

Gitleaks scans the repository for:
- API keys
- passwords
- private keys
- accidental secret exposure

Example pipeline stage:

```yaml
- name: Run Gitleaks
  uses: gitleaks/gitleaks-action@v2
```

---

# Docker Security Practices

The application container is hardened using:

- Minimal base image
- Dedicated non-root user
- Reduced attack surface
- Isolated runtime environment

Example:

```dockerfile
RUN useradd -m appuser
USER appuser
```

---

# Deployment Process

Deployment occurs automatically through GitHub Actions using SSH authentication.

Deployment flow:

1. GitHub Actions connects to VM
2. Repository updates with `git pull`
3. Existing containers stop
4. New containers rebuild
5. Updated application launches

Example deployment script:

```yaml
script: |
  cd /opt/secure-ci-lab
  git pull
  docker compose down
  docker compose up -d --build
```

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/secure-devsecops-pipeline-lab.git
cd secure-devsecops-pipeline-lab
```

## Build and Run

```bash
docker compose up --build
```

Application will be available at:

```text
http://localhost:5000
```

---

# Server Hardening Steps

The Ubuntu deployment VM includes:

- Disabled root SSH login
- SSH key authentication only
- Regular package updates
- Least privilege user configuration


# Lessons Learned

This project provided hands-on experience with:

- Linux server administration
- Docker troubleshooting
- CI/CD debugging
- SSH deployment automation
- Reverse proxy networking
- Secret management
- Vulnerability remediation
- Infrastructure organization
- Git workflow management

Key troubleshooting areas included:
- Docker networking issues
- SSH permission problems
- GitHub Actions pipeline failures
- Container port binding conflicts
- Reverse proxy configuration debugging

---

# Future Improvements

Planned upgrades include:

- Kubernetes deployment
- Terraform infrastructure provisioning
- Wazuh SIEM integration
- Centralized logging stack
- Dependency management automation
- CIS benchmark hardening
- Multi-environment deployments
- Infrastructure monitoring dashboards
- Reverse-Proxy via caddy
- Logging via docker

---

# Screenshots

## Planned Documentation

- GitHub Actions pipeline runs
- Trivy scan results
- Docker container status
- Reverse proxy configuration
- Infrastructure diagrams
- Deployment logs

---

# Resume Relevance

This project demonstrates practical experience with:

- DevSecOps workflows
- Linux administration
- CI/CD automation
- Security tooling
- Containerization
- Infrastructure troubleshooting
- Deployment pipelines
- Secure application delivery

---

# Disclaimer

This project is intended for educational and lab purposes to develop practical DevSecOps and cybersecurity engineering skills.
