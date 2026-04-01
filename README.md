# MLOps Solution for Network Security in Malicious URL Detection

This project delivers a production-grade MLOps solution for detecting and classifying malicious URLs using machine learning. It is designed as a scalable and automated system that integrates data ingestion, validation, model training, deployment, and monitoring into a unified pipeline.

The system supports both real-time and batch predictions, enabling organizations to proactively identify harmful URLs and mitigate cybersecurity risks. By combining modern MLOps practices with cloud infrastructure, this project demonstrates how machine learning systems can be reliably deployed and maintained in real-world environments.

---

## Introduction

Malicious URLs are widely used in phishing attacks, malware distribution, and social engineering campaigns. These attacks can lead to data breaches, financial loss, and compromised systems.

This project aims to solve this problem by building an intelligent URL classification system powered by machine learning. The system analyzes various structural and behavioral features of URLs to determine whether they are Safe, Suspicious, or Malicious.

Unlike a simple ML model, this project focuses on the **complete lifecycle of a machine learning system**, including:

- Automated data ingestion and validation  
- Feature engineering and preprocessing  
- Model training with hyperparameter tuning  
- Experiment tracking and model versioning  
- Continuous retraining using orchestration tools  
- Scalable deployment using containerization and cloud services  

This makes the project a strong example of a **real-world MLOps implementation** rather than just a standalone model.

---

## Architecture
![Architecture](_assets/network_architecture.gif)

The architecture follows a modular and scalable design:

- Data flows from MongoDB into the processing pipeline  
- Airflow orchestrates training and prediction workflows  
- Models and artifacts are stored in AWS S3  
- MLflow tracks experiments and model performance  
- FastAPI serves backend APIs  
- Streamlit provides a user-facing interface  
- Docker ensures consistent environments  
- GitHub Actions automates CI/CD pipelines  

---

## Tech Stack 🛠️

| Category         | Tools/Technologies    | Description                                                                 |
|------------------|-----------------------|-----------------------------------------------------------------------------|
| Frontend         | Streamlit             | Provides an intuitive UI for real-time predictions                          |
| Backend          | FastAPI               | Exposes APIs for training and batch predictions                             |
| Modeling         | Scikit-learn, Python  | Implements machine learning algorithms and preprocessing pipelines          |
| Database         | MongoDB               | Stores raw and processed data                                               |
| Orchestration    | Apache Airflow        | Schedules and manages ML pipelines                                          |
| Experiment Tracking| MLflow             | Tracks experiments, metrics, and model versions                             |
| CI/CD            | GitHub Actions        | Automates testing, building, and deployment                                 |
| Containerization | Docker, AWS ECR       | Packages application for consistent deployment                              |
| Cloud Storage    | AWS S3                | Stores models, datasets, and artifacts                                      |
| Cloud Hosting    | AWS EC2               | Hosts application and CI/CD runners                                         |

---

# Project Highlights 🌟

## ML Pipeline & Monitoring

- **End-to-End MLOps Pipeline**  
  The project implements a complete ML lifecycle pipeline, starting from raw data ingestion to final model deployment. Each stage is modular, reusable, and automated.

- **Real-time Single URL Predictions**  
  Users can interact with the system via a Streamlit UI to classify URLs instantly. This demonstrates how ML models can be exposed to end-users in an accessible way.

- **Batch Predictions for Large Datasets**  
  FastAPI enables users to upload CSV files containing multiple URLs, making the system suitable for enterprise-scale analysis.

- **Automated Model Retraining**  
  Airflow DAGs are used to schedule retraining pipelines. This ensures that the model adapts to new data and evolving attack patterns over time.

- **Comprehensive Metrics Tracking**  
  MLflow logs metrics such as Precision, Recall, and F1-score for each experiment. It also tracks model versions and artifacts, enabling reproducibility and comparison.

---

## Infrastructure & Deployment

- **Containerized with Docker**  
  The entire application is containerized to eliminate environment inconsistencies and simplify deployment.

- **Artifact & Model Storage**  
  AWS S3 is used as a centralized storage system for datasets, trained models, preprocessing pipelines, and logs.

- **Scalable Cloud Deployment on AWS EC2**  
  The application is deployed on EC2 instances, allowing flexible scaling and reliable performance.

- **Multiple Deployment Options**  
  - FastAPI provides REST APIs for integration with other systems  
  - Streamlit offers an interactive frontend for direct user interaction  

---

## CI/CD & Version Control

- **Automated CI/CD Pipeline**  
  GitHub Actions is used to automate the entire workflow:
  - Code validation and testing  
  - Docker image building  
  - Image push to AWS ECR  
  - Deployment to EC2  

- **Version Control for Code and Data**  
  - Git ensures proper versioning of code  
  - Data validation and drift detection mechanisms ensure data consistency  
  - The system is designed to handle evolving datasets without degrading performance  

---

## Dataset and Features

### URL Features

![URL Features](_assets/url_features.png)

The dataset consists of 30 engineered features derived from URLs. These features capture structural, lexical, and behavioral characteristics that help distinguish malicious URLs from legitimate ones.

### Key Features

| Feature Name           | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| `having_IP_Address`     | Identifies use of IP instead of domain name                            |
| `URL_Length`            | Longer URLs often indicate obfuscation                                 |
| `Shortening_Service`    | Detects shortened URLs (e.g., bit.ly)                                  |
| `having_At_Symbol`      | Flags '@' usage which can redirect users                               |
| `double_slash_redirecting` | Detects unusual redirection patterns                              |

<details>
<summary>Click here to view all features</summary>

(Keep your full table as it is)

</details>

---

## Components

### 1. Frontend (Streamlit)
The Streamlit application provides a clean and interactive interface for users to input URLs and receive predictions in real time. It is designed for simplicity and accessibility, making it easy for non-technical users to interact with the system.

---

### 2. Backend (FastAPI)
FastAPI serves as the backbone of the application by exposing APIs for:

- **Training Endpoint (`/train`)**  
  Triggers the model training pipeline manually or programmatically  

- **Prediction Endpoint (`/predict`)**  
  Accepts CSV files and returns predictions for multiple URLs  

This separation of concerns ensures scalability and flexibility.

---

### 3. MLOps Pipeline

#### Data Ingestion
- Fetches data from MongoDB  
- Converts raw data into structured format  
- Splits data into training and testing sets  

#### Data Validation
- Validates schema and column consistency  
- Detects missing or invalid values  
- Performs statistical tests for data drift  

#### Data Transformation
- Applies preprocessing pipelines  
- Handles missing values using KNNImputer  
- Converts features into numerical format suitable for ML models  

#### Model Training and Evaluation
- Trains multiple classification models  
- Performs hyperparameter tuning using GridSearchCV  
- Evaluates models using Precision, Recall, and F1-score  
- Logs experiments in MLflow  
- Saves the best-performing model and preprocessing pipeline  

---

### 4. CI/CD Pipeline with GitHub Actions

The CI/CD pipeline ensures rapid and reliable delivery:

- Uses EC2 as a self-hosted runner  
- Automatically triggers workflows on code changes  
- Builds and deploys Docker containers  
- Reduces manual intervention and deployment errors  

---

### 5. Docker Integration

- Packages the entire application into Docker containers  
- Ensures consistency across environments  
- Simplifies deployment and scaling  

---

### 6. Airflow Integration

- Defines workflows using DAGs  
- Automates training and prediction pipelines  
- Provides monitoring and logging through Airflow UI  
- Enables scheduling and dependency management  

---

## **How to Run the Project** 🚀

### **Installation**

1. Clone the repository:
```bash
git clone https://github.com/Neeraj876/network-security-system-mlops.git
cd network-security-system-mlops
