# MLOps Solution for Network Security in Malicious URL Detection

A comprehensive, end-to-end MLOps solution designed to detect and classify malicious URLs, ensuring user safety by identifying harmful links through machine learning. The solution integrates data ingestion, model training, deployment, and continuous monitoring — delivering both real-time and batch URL safety assessments through an automated, scalable approach to web security.

---

## Introduction

Malicious URLs are commonly used by cybercriminals in phishing attacks, social engineering schemes, and malware distribution, posing significant risks to individuals and organizations. This project leverages machine learning to identify and classify harmful links, enabling timely interventions and improved web security.

The pipeline supports both **real-time single URL predictions** via an interactive UI and **batch predictions** through a robust API backend.

## Architecture

---

## Tech Stack 🛠️

| Category               | Tools / Technologies              | Description                                                                                   |
|------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------|
| **Frontend**           | Streamlit                         | Interactive UI for real-time single URL predictions                                           |
| **Backend**            | FastAPI                           | Handles batch predictions and API endpoints                                                   |
| **Modeling**           | RandomForestClassifier, Python    | Machine learning model for detecting malicious URLs                                           |
| **Database**           | MongoDB                           | Stores data records for ingestion and model training                                          |
| **Experiment Tracking**| MLflow                            | Tracks model metrics (F1-score, Precision, Recall); artifacts stored in AWS S3 on AWS EC2    |
| **CI/CD**              | GitHub Actions                    | Automates CI/CD pipelines including Docker build and deployment                               |
| **Containerization**   | Docker, AWS ECR                   | Docker images stored securely in ECR for consistent deployment                                |
| **Cloud Storage**      | AWS S3                            | Stores artifacts, trained models, and logs                                                    |
| **Cloud Hosting**      | AWS EC2                           | Serves as self-hosted runner for GitHub Actions and hosts the application                     |

---

## Project Highlights 🌟

### ML Pipeline & Monitoring

- **End-to-End MLOps Pipeline** — Seamless integration from data ingestion to deployment with fully automated workflows.
- **Real-time Single URL Predictions** — Instant safety assessments on individual URLs via a **Streamlit** app.
- **Batch Predictions for Large Datasets** — Efficiently process multiple URLs at once using **FastAPI**.
- **Comprehensive Metrics Tracking** — All experiments logged and tracked with **MLflow on AWS**, providing a centralized dashboard for performance comparison.

### Infrastructure & Deployment

- **Containerized with Docker** — Consistent environments from development to production.
- **Artifact & Model Storage** — Models, artifacts, and experiments securely stored in **AWS S3**.
- **Scalable Cloud Deployment** — Hosted on **AWS EC2** for reliable, scalable performance.
- **Multiple Deployment Options**:
  - **FastAPI** with two routes: `/train` for model training and `/predict` for batch predictions.
  - **Streamlit** for an interactive web interface enabling real-time predictions.

### CI/CD & Version Control

- **Automated CI/CD Pipeline** via **GitHub Actions** integrating with **AWS ECR** and **EC2**:
  - Builds and pushes Docker images to **Amazon ECR**.
  - Pulls and deploys the image to **AWS EC2** automatically.
- **Code Versioning** via **Git/GitHub** keeps the codebase always up-to-date.
- **Data Versioning** with schema tracking and drift detection ensures data quality and model integrity over time.

---

## Dataset & Features

### URL Features

The dataset contains **30 features** extracted from URLs to classify them as **Malicious**, **Suspicious**, or **Safe**.

### Key Features

| Feature Name                | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| `having_IP_Address`         | Checks if URL contains an IP address instead of a domain name     |
| `URL_Length`                | Measures URL length; longer URLs often hide malicious content     |
| `Shortening_Service`        | Detects use of URL shortening services like `bit.ly`              |
| `having_At_Symbol`          | Flags presence of `@` in the URL                                  |
| `double_slash_redirecting`  | Identifies multiple slashes after the protocol                    |

<details>
<summary>View all 30 features</summary>

| Feature Name                  | Description                                    |
|-------------------------------|------------------------------------------------|
| `Prefix_Suffix`               | Checks for dashes in the domain                |
| `having_Sub_Domain`           | Counts the number of subdomains                |
| `SSLfinal_State`              | Analyzes the SSL certificate                   |
| `Domain_registration_length`  | Measures domain registration duration          |
| `Favicon`                     | Checks favicon source                          |
| `port`                        | Detects unusual ports                          |
| `HTTPS_token`                 | Flags `HTTPS` in the domain name               |
| `Request_URL`                 | Checks resource loading domains                |
| `URL_of_Anchor`               | Analyzes anchor tag destinations               |
| `Links_in_tags`               | Measures links in HTML tags                    |
| `SFH`                         | Checks form handler locations                  |
| `Submitting_to_email`         | Flags form submission to email                 |
| `Abnormal_URL`                | Identifies URL-domain mismatches               |
| `Redirect`                    | Counts redirections                            |
| `on_mouseover`                | Detects JavaScript hover events                |
| `RightClick`                  | Identifies right-click disabling               |
| `popUpWindow`                 | Flags popup windows                            |
| `Iframe`                      | Detects invisible iframes                      |
| `age_of_domain`               | Analyzes domain age                            |
| `DNSRecord`                   | Checks DNS records                             |
| `web_traffic`                 | Measures website traffic                       |
| `Page_Rank`                   | Checks page rank                               |
| `Google_Index`                | Identifies Google indexing status              |
| `Links_pointing_to_page`      | Counts inbound links                           |
| `Statistical_report`          | Flags reported suspicious activity             |

</details>

---

## Components

### 1. Frontend — Streamlit

<img width="1920" height="1080" alt="Screenshot 2026-03-29 170644" src="https://github.com/user-attachments/assets/87ee6a1c-e4a8-486c-853a-a6501ed5e210" />


The Streamlit app provides an intuitive interface for predicting individual URLs as **Malicious**, **Suspicious**, or **Safe**.

|------------|------------|

---

### 2. Backend — FastAPI

FastAPI handles model operations including training and batch predictions.

- **`/train`** — Triggers the model training process.
- **`/predict`** — Accepts CSV files for batch URL classification, returning results in JSON format.

|------|------------|

**AWS S3 Buckets:**

![Uploading Screenshot 2026-03-31 191346.png…]()

![Uploading Screenshot 2026-03-31 191409.png…]()

<img width="1920" height="1080" alt="Screenshot 2026-03-31 191425" src="https://github.com/user-attachments/assets/e145d43e-ab4a-4a1b-94d3-c5383d6eaa56" />


- `networksecurity3` — Stores artifacts, `model.pkl`, and `preprocessor.pkl`.

- `my-network-datasource-neeraj` — Stores CSV files uploaded via the `/predict` route.

---

### 3. MLOps Pipeline

#### Data Ingestion
- Fetches data from **MongoDB** and exports it to a feature store.
- Splits data into training and testing sets with no data leakage.

#### Data Validation
- Validates schema to ensure all required columns are present.
- Checks numerical columns for correctness and detects **data drift** using statistical tests.
- Generates detailed drift reports for dataset consistency monitoring.

#### Data Transformation
- Imputes missing values using a **KNNImputer**.
- Prepares transformed **NumPy arrays** for model training.
- Saves the transformation pipeline and preprocessing steps as **pickle artifacts**.

#### Model Training & Evaluation
- Trains multiple classifiers: **Random Forest**, Gradient Boosting, Decision Tree, Logistic Regression, and AdaBoost.
- Performs hyperparameter tuning via **GridSearchCV** for optimal performance.
- Evaluates models on **Precision**, **Recall**, and **F1-score**, all tracked in **MLflow on AWS**.
- Saves the best-performing model as a pickle file.

|-------------|------------|

> MLflow experiments, models, and artifacts are stored in the `mlflowtrackingnetwork` S3 bucket.

---

### 4. CI/CD Pipeline — GitHub Actions

Every code update triggers automated workflows for testing, building, and deploying the application.

- **Self-Hosted Runner** on AWS EC2:

|-------|------------|

---

### 5. Docker & AWS ECR

The full application is containerized with Docker. Images are built, tagged, and stored in **Amazon ECR** for versioned and traceable deployments.

---

## How to Run the Project 🚀

### Installation

```bash
git clone https://github.com/Neeraj876/network-security-system-mlops.git
cd network-security-system-mlops
pip install -r requirements.txt
```

### Local Setup

**Launch the Streamlit App** (single URL prediction):
```bash
streamlit run streamlit.py
```

**Run the FastAPI Backend** (batch predictions):
```bash
uvicorn app:app --reload
```

### Deployment

**Build and push Docker image to AWS ECR:**
```bash
docker build -t your-docker-image .
docker tag your-docker-image:latest <AWS_ECR_URI>
docker push <AWS_ECR_URI>
```

**Run the container on EC2:**
```bash
docker run -d -p 80:8080 your-docker-image
```

### Running Project Components

1. **MLflow Setup** — Ensure MLflow is running on your AWS EC2 instance to track experiments and store artifacts in S3.
2. **Data Ingestion** — Fetch data from MongoDB using the `data_ingestion` module.
3. **Model Training** — Trigger training via the FastAPI `/train` endpoint.
4. **Batch Prediction** — Upload a CSV via the FastAPI `/predict` route to receive JSON predictions.
5. **Single Prediction** — Use the Streamlit app for real-time, single URL classification.
6. **Monitoring** — Track all experiments, metrics, and logs through the MLflow UI.

---
