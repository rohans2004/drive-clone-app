## 📁 My Drive Clone Project —

This project is a simple **Google Drive Clone** that allows users to upload and view files. It is built with **Flask**, stores metadata in **SQLite**, and uploads files to **AWS S3**. The full stack is **Dockerized** and deployed on an **AWS EC2** instance.

---

### ✅ Features

* Upload files from a browser interface
* Files are stored in **Amazon S3**
* Metadata is stored using **SQLite**
* Flask backend to handle upload & listing
* Fully containerized using Docker
* Deployed on AWS EC2 Ubuntu server

---

## 🔧 Local Development Setup (Mac / Windows)

1. **Clone the Project**

   ```bash
   git clone https://github.com/rohans2004/drive-clone-app.git
   cd drive-clone-app
   ```

2. **Create Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Update Your Flask App Port**

   * Make sure `app.py` runs on port `5050`:

     ```python
     if __name__ == '__main__':
         app.run(debug=True, host='0.0.0.0', port=5050)
     ```

5. **Update AWS Credentials in `app.py` or configure IAM role**

   ```python
   s3 = boto3.client('s3')  # Uses IAM role on EC2 OR credentials locally
   ```

---

## 🐳 Docker Setup

1. **Build Docker Image**

   ```bash
   docker build -t drive-clone-app .
   ```

2. **Run Docker Container**

   ```bash
   docker run -p 5000:5050 drive-clone-app
   ```

---

## ☁️ AWS EC2 Deployment

1. **Launch EC2 Ubuntu Instance**

   * Create and login via SSH

2. **Install Docker on EC2**

   ```bash
   sudo apt update
   sudo apt install docker.io -y
   sudo usermod -aG docker $USER
   ```

3. **Clone Repo & Build Image**

   ```bash
   git clone https://github.com/rohans2004/drive-clone-app.git
   cd drive-clone-app
   docker build -t drive-clone-app .
   ```

4. **Run Container**

   ```bash
   docker run -p 5000:5050 drive-clone-app
   ```

---

## 🪪 AWS S3 Configuration

### Option 1: IAM Role (Recommended on EC2)

* Create an IAM Role with **AmazonS3FullAccess**
* Attach this role to the EC2 instance

### Option 2: Manual Credential Config (Only for local testing)

```bash
aws configure
# Enter Access Key, Secret Key, Region, Output Format
```

---

## 🌐 Access Your App

* Open EC2 public IP:

  ```
  http://<your-ec2-public-ip>:5000
  ```

---

## 📤 Uploading Files

* Upload file via browser
* Files are sent to S3 bucket
* File names and sizes are stored in SQLite

---

## 🧠 Technologies Used

* Python3 + Flask
* SQLite
* AWS S3
* Docker
* EC2 (Ubuntu 22.04)

