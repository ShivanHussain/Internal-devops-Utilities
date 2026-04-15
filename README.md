# Internal DevOps Utilities Platform

A lightweight **FastAPI-based DevOps utility platform** built using **Python, FastAPI, Boto3, and psutil**. This project provides APIs to monitor system health, interact with AWS services, and automate basic cloud operations.

---

##  Features

###  System Monitoring

* CPU usage monitoring
* Memory usage monitoring
* Disk usage monitoring
* Health status based on configurable CPU threshold

### AWS Utilities

* List S3 buckets (new vs old buckets)
* Fetch EC2 instance details
* List IAM users
* Create EC2 instances dynamically:

  * Automatically creates key pair
  * Generates `.pem` file locally
  * Tags instance with name
  * Returns launch time in IST

### Utility APIs

* Simple **Hello API** for testing and health checks

---

##  Project Structure

```
internal-devops-utilities/
│
├── app/
│   ├── api.py                # FastAPI app initialization
│   │
│   ├── routers/
│   │   ├── aws.py            # AWS routes
│   │   ├── metrics.py        # System metrics routes
│   │   └── hello.py          # Health/test route
│   │
│   ├── services/
│   │   ├── aws_service.py     # AWS logic (boto3)
│   │   ├── metrics_service.py # Metrics logic
│   │   └── hello_service.py   # Hello logic
│   │
│   ├── schema/
│   │   └── ec2_instance.py    # EC2 schema
│
├── main.py                   # Entry point
├── requirements.txt
├── README.md
└── .env (optional)
```

---

##  Tech Stack

* **Python 3.9+**
* **FastAPI** (Web Framework)
* **Uvicorn** (ASGI Server)
* **Boto3** (AWS SDK)
* **psutil** (System Metrics)
* **pytz** (Timezone Handling)

---

##  Installation & Setup

### Clone Repository

```bash
git clone https://github.com/ShivanHussain/Internal-devops-Utilities.git
cd internal-devops-utilities
```

### Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS Credentials

#### Option 1: AWS CLI

```bash
aws configure
```

#### Option 2: Environment Variables

```bash
export AWS_ACCESS_KEY_ID=xxxx
export AWS_SECRET_ACCESS_KEY=xxxx
export AWS_DEFAULT_REGION=us-east-1
```

---

## Running the Application

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000

OR
 
python main.py
```

###  Access URLs

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

##  API Endpoints

### 🔹 Health Check

```
GET /
```

**Response:**

```json
{
  "message": "Hello Dosto"
}
```

---

### 🔹 System Metrics

```
GET /metrics
```

**Response:**

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

### 🔹 S3 Buckets

```
GET /aws/s3
```

---

### 🔹 EC2 Instances

```
GET /aws/ec2
```

---

### 🔹 IAM Users

```
GET /aws/iam
```

---

### 🔹 Create EC2 Instance

```
POST /aws/create-instance
```

**Request Body:**

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

**Response:**

```json
{
  "message": "EC2 instance created successfully",
  "instance_id": "i-0123456789",
  "launch_time": "26-01-2026 14:32:10 IST"
}
```

---

## Best Practices

*  Never commit AWS credentials or `.pem` files
*  Store `.pem` keys securely
*  Use IAM roles instead of hardcoded credentials (recommended for EC2)

### Required IAM Permissions:

* EC2 (Create, Describe)
* S3 (Read)
* IAM (List users)

---

##  Future Enhancements

* Authentication & RBAC
* Prometheus & Grafana integration
* CloudWatch metrics support
* Alerting system (Slack / Email)
* Docker & Kubernetes deployment
* Multi-region AWS support

---

##  Docker Support

###  Build Docker Image

```bash
docker build -t internal-devops-utils .
```

### Run Docker Container

```bash
docker run -d -p 8000:8000 \
  -e AWS_ACCESS_KEY_ID=your_key \
  -e AWS_SECRET_ACCESS_KEY=your_secret \
  -e AWS_DEFAULT_REGION=us-east-1 \
  internal-devops-utils
```


---

##  Summary

This project is a **mini DevOps toolkit** that combines:

* System monitoring
* AWS automation
* API-based architecture


---

*Built for learning, automation, and scalability.*

