# Network Security Project for Phishing Data

## Overview

This project features an **end-to-end MLOps pipeline** for **phishing detection**, designed to classify websites as safe or unsafe and enhance network security. It automates the machine learning lifecycle for intelligent data analysis.

## Key Features

The pipeline includes:

* **Automated Data Ingestion & Validation**: Efficiently handles and validates incoming data.
* **ETL Processes**: Transforms raw data for model readiness.
* **Model Training & Hyperparameter Tuning**: Develops and optimizes machine learning models.
* **MLflow Experiment Tracking**: Ensures reproducibility and governance of experiments.
* **Artifact Management**: Manages and versions all pipeline outputs.
* **Scalable Deployment**: Facilitates robust model deployment for real-time predictions.

## Technologies and Tools

Key technologies utilized:

* **Python**
* **Pandas, NumPy, Scikit-learn**
* **MongoDB Atlas**
* **MLflow**
* **AWS S3**
* **Docker**
* **GitHub Actions**
* **Dagshub**

## Setup and Usage

1.  **Clone the Repository:** `git clone <your-repository-url>`
2.  **Install Dependencies:** `pip install -r requirements.txt`
3.  **Configure Environment Variables:** Set up necessary credentials (MongoDB, AWS, MLflow) in a `.env` file.
4.  **Run Training Pipeline:** `python main.py`
5.  **Run Prediction App:** `python app.py`
