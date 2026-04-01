# MLOps Solution for Network Security in Malicious URL Detection

[![CI/CD Pipeline](https://github.com/yourusername/your-repo-name/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/your-repo-name/actions/workflows/ci-cd.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-deployed-orange.svg)](https://aws.amazon.com/)

This is a comprehensive, end-to-end MLOps solution designed to detect and classify malicious URLs, ensuring user safety by identifying harmful links through machine learning. The solution integrates data ingestion, model training, deployment, and continuous monitoring, delivering both real-time and batch URL safety assessments, providing an automated, scalable approach to web security.

---

## 📋 Table of Contents
- [Introduction](#introduction)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Highlights](#project-highlights)
- [Dataset and Features](#dataset-and-features)
- [Components](#components)
- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Monitoring and Observability](#monitoring-and-observability)

## Introduction

Malicious URLs are commonly used by cybercriminals in phishing attacks, social engineering schemes, and malware attacks, posing significant risks to individuals and organizations. The Malicious URL Detection project uses machine learning to identify and classify these harmful links, enabling timely interventions and improved web security. This solution includes a robust pipeline for detecting malicious URLs, offering both real-time single URL predictions and batch predictions through an interactive user interface.

### Key Objectives
- **Real-time Detection**: Instantly classify URLs as safe, suspicious, or malicious
- **Batch Processing**: Handle large datasets efficiently for bulk analysis
- **Automated Retraining**: Keep the model updated with new threat patterns
- **Scalable Infrastructure**: Cloud-native architecture for high availability
- **Comprehensive Monitoring**: Track model performance and data drift

## Architecture

┌─────────────────────────────────────────────────────────────────────────────┐
│ USER INTERFACE │
│ ┌─────────────────────────────┐ ┌─────────────────────────────┐ │
│ │ Streamlit Frontend │ │ FastAPI Backend │ │
│ │ - Single URL Predictions │ │ - Batch Predictions │ │
│ │ - Interactive Dashboard │ │ - Training Triggers │ │
│ │ - Real-time Results │ │ - API Documentation │ │
│ └─────────────────────────────┘ └─────────────────────────────┘ │
│ │ │ │
└────────────────────┼───────────────────────────┼────────────────────────────┘
│ │
▼ ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ MLOps ORCHESTRATION │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ Apache Airflow │ │
│ │ • Data Ingestion Pipeline • Model Retraining Scheduler │ │
│ │ • Batch Job Management • Workflow Orchestration │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ DATA & MODEL MANAGEMENT │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ MongoDB │ │ MLflow │ │ AWS S3 │ │ Feature │ │
│ │ Database │ │ Tracking │ │ Storage │ │ Store │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ AWS CLOUD INFRASTRUCTURE │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ EC2 │ │ ECR │ │ S3 │ │ CloudWatch │ │
│ │ Compute │ │ Registry │ │ Storage │ │ Monitoring │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘


---

## Tech Stack 🛠️

| Category | Tools/Technologies | Description |
|----------|-------------------|-------------|
| **Frontend** | Streamlit | Provides a simple UI for real-time single URL predictions with interactive visualizations |
| **Backend** | FastAPI | Handles batch predictions, API endpoints, and model serving with automatic OpenAPI documentation |
| **Modeling** | RandomForestClassifier, Scikit-learn, XGBoost | Machine learning models for detecting malicious URLs with hyperparameter tuning |
| **Database** | MongoDB | Stores data records for ingestion and model training with schema flexibility |
| **Orchestration** | Apache Airflow | Orchestrates training, retraining, and batch prediction pipelines with DAG-based workflows |
| **Experiment Tracking** | MLflow | Tracks model metrics like F1-score, Precision, and Recall, with data stored in AWS S3 and running on AWS EC2 |
| **CI/CD** | GitHub Actions | Automates CI/CD pipelines, including Docker build, testing, and deployment |
| **Containerization** | Docker, AWS ECR | Docker images stored securely in ECR for consistent deployment across environments |
| **Cloud Storage** | AWS S3 | Stores artifacts, trained models, logs, and preprocessing pipelines |
| **Cloud Hosting** | AWS EC2 | Serves as a self-hosted runner for GitHub Actions and hosts production applications |
| **Monitoring** | CloudWatch, MLflow UI | Tracks system metrics, model performance, and alerts for anomalies |
| **Version Control** | Git, GitHub | Manages code versioning, collaboration, and pull request workflows |

---

## Project Highlights 🌟

### ML Pipeline & Monitoring
- **End-to-End MLOps Pipeline**: From data ingestion to deployment, ensuring seamless integration and automated workflows with zero manual intervention
- **Real-time Single URL Predictions**: Users can instantly interact with the model via a Streamlit app for real-time safety assessments on individual URLs with sub-100ms latency
- **Batch Predictions for Large Datasets**: Efficiently process thousands of URLs at once using FastAPI, designed for batch predictions with CSV upload support
- **Automated Model Retraining**: Ensure that the model stays up-to-date with new data through an Apache Airflow powered retraining pipeline, running at scheduled intervals (daily/weekly) or triggered manually via API
- **Comprehensive Metrics Tracking**: All experiments are logged and tracked with MLflow in AWS, providing a centralized dashboard to compare and monitor model performance, hyperparameters, and facilitate easy experimentation

### Infrastructure & Deployment
- **Containerized with Docker**: The entire application is containerized using Docker, ensuring consistent environments from development to production with multi-stage builds for optimization
- **Artifact & Model Storage**: Models, artifacts, experiments and other intermediate data are securely stored in AWS S3 with versioning enabled, ready for deployment at any stage
- **Scalable Cloud Deployment on AWS EC2**: Deployed on AWS EC2 instances with auto-scaling capabilities, enabling scalable cloud infrastructure for reliable performance under varying loads
- **Multiple Deployment Options**:
  - **FastAPI** for efficient API endpoints with automatic rate limiting and request validation
    - `/train` - POST endpoint for triggering model training with existing data
    - `/predict` - POST endpoint for making batch predictions on input data (CSV/JSON)
    - `/health` - GET endpoint for health checks and readiness probes
    - `/metrics` - GET endpoint for exposing Prometheus metrics
  - **Streamlit** for an interactive web interface, enabling easy user interaction with the model for real-time predictions with visual feedback

### CI/CD & Version Control
- **Automated CI/CD Pipeline**: Streamline the conversion, deployment, and management with a fully automated GitHub Actions pipeline, integrating with AWS ECR and Amazon EC2
  - **Docker Image Build & Push**: Converts the application into a Docker image with multi-stage builds and pushes to Amazon ECR, ensuring consistent and traceable deployments
  - **Deployment to Production**: Pulls the Docker image from Amazon ECR and deploys it to AWS EC2 with zero-downtime deployment strategies (blue/green or rolling updates)
  - **Automated Testing**: Runs unit tests, integration tests, and model validation before deployment
- **Version Control for Code and Data**:
  - **Code Versioning** via Git and GitHub ensures codebase is always up-to-date with proper branching strategies (GitFlow)
  - **Data Versioning** with DVC (Data Version Control) for schema tracking and drift detection, ensuring high data quality and maintaining model integrity over time

---

## Dataset and Features

### URL Features Overview

The dataset contains **30+ features** extracted from URLs to classify them as **Malicious**, **Suspicious**, or **Safe**. These features are derived from:
- URL structure and syntax
- Domain characteristics
- SSL certificate information
- Page content analysis
- External service indicators

### Key Features

| Feature Name | Description | Importance |
|--------------|-------------|------------|
| `having_IP_Address` | Checks if URL contains IP address instead of domain name | High |
| `URL_Length` | Measures URL length; longer URLs often hide malicious content | High |
| `Shortening_Service` | Detects use of URL shortening services like bit.ly, tinyurl | Medium |
| `having_At_Symbol` | Flags presence of '@' in URL (often used for redirection) | High |
| `double_slash_redirecting` | Identifies multiple slashes after protocol indicating redirects | Medium |
| `prefix_suffix` | Detects hyphens and other suspicious characters in domain | Medium |
| `having_Sub_Domain` | Counts number of subdomains in URL (excessive = suspicious) | Medium |
| `SSLfinal_State` | Analyzes SSL certificate validity and trust level | High |
| `Domain_registeration_length` | Checks domain registration duration (short = suspicious) | Medium |
| `Favicon` | Verifies if favicon is loaded from trusted source | Low |
| `port` | Detects non-standard ports in URL | Medium |
| `HTTPS_token` | Checks if HTTPS appears suspiciously in domain name | Medium |
| `Request_URL` | Analyzes if external objects are loaded from other domains | High |
| `URL_of_Anchor` | Checks if anchor tags point to other domains | Medium |
| `Links_in_tags` | Counts links in meta, script, and link tags | Medium |
| `SFH` | Analyzes Server Form Handler for suspicious behavior | High |
| `Submitting_to_email` | Detects forms that submit to email addresses | High |
| `Abnormal_URL` | Checks if URL is abnormal compared to domain | High |
| `Redirect` | Counts number of redirects | Medium |
| `on_mouseover` | Detects JavaScript on mouseover events | Medium |
| `RightClick` | Checks if right-click is disabled | Low |
| `popUpWidnow` | Detects popup windows | Medium |
| `iframe` | Checks for iframe usage | Medium |
| `age_of_domain` | Domain age in days | High |
| `DNSRecord` | Checks if DNS record exists | High |
| `web_traffic` | Website traffic rank | High |
| `Page_Rank` | Google PageRank | Medium |
| `Google_Index` | Checks if page is indexed by Google | Medium |
| `Links_pointing_to_page` | Number of links pointing to page | Low |
| `Statistical_report` | Reports from security services | High |

---

## Components

### 1. Frontend (Streamlit)

The Streamlit app provides an intuitive interface for users to predict single URLs with real-time feedback and visual indicators.

#### Features
- **Single URL Input**: Text input with URL validation
- **Real-time Prediction**: Instant classification with confidence scores
- **Visual Indicators**: Color-coded results (Green: Safe, Yellow: Suspicious, Red: Malicious)
- **Feature Visualization**: Display extracted features for transparency
- **History Tracking**: Local storage of recent predictions
- **Export Results**: Download predictions as CSV

#### Example Outputs

| URL | Prediction | Confidence | Risk Level |
|-----|------------|------------|------------|
| `https://www.google.com` | 🟢 **Safe** | 98.5% | Low |
| `http://bit.ly/2XyZabc` | 🟡 **Suspicious** | 76.2% | Medium |
| `http://malware-site.com/virus.exe` | 🔴 **Malicious** | 94.7% | High |
| `https://drive.google.com/redirect?url=http://suspicious.com` | 🟡 **Suspicious** | 82.1% | Medium |

### 2. Backend (FastAPI)

FastAPI handles the model's operational tasks with high performance and automatic documentation.

#### API Endpoints

| Endpoint | Method | Description | Request Body | Response |
|----------|--------|-------------|--------------|----------|
| `/` | GET | Root endpoint | - | Welcome message |
| `/health` | GET | Health check | - | Service status |
| `/train` | POST | Trigger model training | `{ "force": boolean }` | Training status |
| `/predict` | POST | Batch predictions | CSV/JSON file | Predictions results |
| `/predict/single` | POST | Single URL prediction | `{ "url": "string" }` | Classification result |
| `/metrics` | GET | Model performance metrics | - | F1, Precision, Recall |
| `/features` | GET | List all features | - | Feature descriptions |

#### Storage Locations

| Resource | AWS S3 Bucket | Purpose |
|----------|---------------|---------|
| Model Artifacts | `networksecurity3` | Stores `model.pkl`, `preprocessor.pkl`, and feature mappings |
| Batch Uploads | `my-network-datasource-neeraj` | Temporary storage for CSV files uploaded to `/predict` |
| MLflow Tracking | `mlflowtrackingnetwork` | All experiments, metrics, parameters, and artifacts |
| Training Data | `networksecurity3/data` | Historical training datasets with versioning |

### 3. MLOps Pipeline

#### Data Ingestion
- **Source**: MongoDB database with real-time URL data
- **Process**: 
  - Extract data from MongoDB collections
  - Validate schema and data types
  - Export processed data to feature store
  - Split into training (80%) and testing (20%) datasets
  - Ensure no data leakage with temporal splitting
- **Storage**: Parquet format in S3 for efficient processing

#### Data Validation
- **Schema Validation**:
  - Ensure all 30+ features are present
  - Validate data types (numerical, categorical)
  - Check for null values and outliers
- **Drift Detection**:
  - Statistical tests (Kolmogorov-Smirnov, Chi-square)
  - Population stability index (PSI) calculation
  - Automated alerts when drift exceeds thresholds
- **Reports**: Generate HTML reports with visualizations

#### Data Transformation
- **Preprocessing Steps**:
  - Handle missing values with KNNImputer (k=5)
  - Scale numerical features with StandardScaler
  - Encode categorical features with OneHotEncoder
  - Create feature interactions for high-correlation pairs
- **Pipeline**:
  - Build sklearn Pipeline with all transformers
  - Save as `preprocessor.pkl` for consistency
  - Version control with MLflow

#### Model Training and Evaluation
- **Algorithms Tested**:
  - Random Forest (selected as best)
  - XGBoost
  - Gradient Boosting
  - Logistic Regression
  - Support Vector Machine
  - AdaBoost
  - Neural Networks (MLP)
- **Hyperparameter Tuning**:
  - GridSearchCV with 5-fold cross-validation
  - RandomizedSearchCV for initial exploration
  - Bayesian optimization for fine-tuning
- **Evaluation Metrics**:
  - Accuracy, Precision, Recall, F1-Score
  - ROC-AUC, PR-AUC
  - Confusion Matrix
  - Classification Report
- **Model Persistence**:
  - Save as `model.pkl` with joblib
  - Register in MLflow Model Registry
  - Versioning for production deployment

#### MLflow Tracking
- **Experiment Tracking**:
  - Log all hyperparameters
  - Track metrics across runs
  - Store confusion matrices and feature importance plots
  - Record training and validation times
- **Artifacts Storage**: S3 bucket `mlflowtrackingnetwork`
- **Model Registry**: Staging → Production → Archived lifecycle
- **Dashboard**: Web UI at `http://ec2-instance:5000`

### 4. CI/CD Pipeline with GitHub Actions

The project leverages a robust CI/CD pipeline to automate the integration, delivery, and deployment processes.

#### GitHub Actions Workflow

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:  # Manual trigger

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: |
          pytest tests/ --cov=app --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run linters
        run: |
          pip install flake8 black isort
          flake8 app/
          black --check app/
          isort --check-only app/

  build:
    needs: [test, lint]
    runs-on: self-hosted
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v1
      - name: Build Docker image
        run: |
          docker build -t malicious-url-detection:${{ github.sha }} .
          docker tag malicious-url-detection:${{ github.sha }} \
            ${{ steps.login-ecr.outputs.registry }}/malicious-url-detection:latest
      - name: Push to ECR
        run: |
          docker push ${{ steps.login-ecr.outputs.registry }}/malicious-url-detection:latest
          docker push ${{ steps.login-ecr.outputs.registry }}/malicious-url-detection:${{ github.sha }}

  deploy:
    needs: build
    runs-on: self-hosted
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Pull Docker image
        run: |
          docker pull ${{ secrets.ECR_REGISTRY }}/malicious-url-detection:latest
      - name: Stop existing container
        run: |
          docker stop malicious-url-app || true
          docker rm malicious-url-app || true
      - name: Run new container
        run: |
          docker run -d \
            --name malicious-url-app \
            -p 8000:8000 \
            -p 8501:8501 \
            -e MONGODB_URI="${{ secrets.MONGODB_URI }}" \
            -e AWS_ACCESS_KEY_ID="${{ secrets.AWS_ACCESS_KEY_ID }}" \
            -e AWS_SECRET_ACCESS_KEY="${{ secrets.AWS_SECRET_ACCESS_KEY }}" \
            --restart unless-stopped \
            ${{ secrets.ECR_REGISTRY }}/malicious-url-detection:latest
      - name: Health check
        run: |
          sleep 10
          curl -f http://localhost:8000/health || exit 1
