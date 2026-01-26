# Internal DevOps Utilities

An internal **FastAPI-based DevOps utility platform** built using **Python**, **FastAPI**, **Boto3**, and **psutil**. This project provides APIs to monitor system metrics, fetch AWS resource details, and perform basic AWS operations like EC2 instance creation.

---

## Features

### System Monitoring

* CPU usage monitoring
* Memory usage monitoring
* Disk usage monitoring
* Health status based on configurable CPU threshold

### AWS Utilities

* List S3 buckets (new vs old buckets)
* Fetch EC2 instance details
* List IAM users
* Create EC2 instances dynamically

  * Automatically creates key pair
  * Generates `.pem` file locally
  * Tags instance with name
  * Returns launch time in IST

### Utility APIs

* Simple **Hello API** for health check/testing

---

## Project Structure

```
internal-devops-utilities/
│
├── app/
│   ├── api.py                # FastAPI app initialization
│   │
│   ├── routers/
│   │   ├── aws.py             # AWS related routes
│   │   ├── metrics.py         # System metrics routes
│   │   └── hello.py           # Test/health route
│   │
│   ├── services/
│   │   ├── aws_service.py     # AWS business logic (boto3)
│   │   ├── metrics_service.py # System metrics logic
│   │   └── hello_service.py   # Hello service
│   │
│   ├── schema/
│   │   └── ec2_instance.py    # Pydantic schema for EC2 creation
│
├── main.py               # Uvicorn entry point
├── requirements.txt
├── README.md
└── .env (optional)
```

---

## Tech Stack

* **Python 3.9+**
* **FastAPI** – Web framework
* **Uvicorn** – ASGI server
* **Boto3** – AWS SDK
* **psutil** – System metrics
* **pytz** – Timezone handling

---

## Installation & Setup

### 1 Clone Repository

```bash
git clone https://github.com/ShivanHussain/Internal-devops-Utilities.git
cd internal-devops-utilities
```

### 2 Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 Configure AWS Credentials

Make sure AWS credentials are configured:

```bash
aws configure
```

OR using environment variables:

```bash
export AWS_ACCESS_KEY_ID=xxxx
export AWS_SECRET_ACCESS_KEY=xxxx
export AWS_DEFAULT_REGION=us-east-1
```

---

##  Running the Application

```bash
python3 main.py
```

App will be available at:

* **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---


Response:

```json
{
  "messsage": "Hello Dosto"
}
```

---

### System Metrics

```
GET /metrics
```

Response:

```json
{
  "cpu_percentage": 18.2,
  "memory_percentage": 62.4,
  "disk_percentage": 40.1,
  "cpu_threshold": 25,
  "system_status": "Healthy"
}
```

---

### 🔹 S3 Buckets Info

```
GET /aws/s3
```

---

### 🔹 EC2 Instances Info

```
GET /aws/ec2
```

---

### 🔹 IAM Users Info

```
GET /aws/iam
```

---

### 🔹 Create EC2 Instance

```
POST /aws/create-instance
```

Request Body:

```json
{
  "ami_id": "ami-0abcdef123",
  "instance_type": "t2.micro",
  "key_name": "my-key",
  "instance_name": "devops-test",
  "min_count": 1,
  "max_count": 1
}
```

Response:

```json
{
  "message": "EC2 instance created successfully",
  "instance_id": "i-0123456789",
  "launch_time": "26-01-2026 14:32:10 IST"
}
```

---

## ⚠️ Notes & Best Practices

* `.pem` key files are generated locally — **store securely**
* Avoid committing AWS credentials or `.pem` files
* IAM user running this app must have:

  * EC2FullAccess (or limited EC2 permissions)
  * S3 read permissions
  * IAM list permissions

---

##  Future Enhancements

* Authentication & RBAC
* Prometheus / Grafana integration
* CloudWatch metrics support
* Alerting system (Slack / Email)
* Docker support
* Multi-region AWS support

---

