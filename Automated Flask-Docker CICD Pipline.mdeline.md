## 📘 Project: Automated Flask-Docker CI/CD Pipeline

### 1. Prerequisites (Before You Start)

Before building this pipeline, ensure you have the following accounts and tools ready:

* **GitHub Account:** To host the source code and run GitHub Actions.
* **Docker Hub Account:** To act as the "Registry" where your final images will be stored.
* **Git Installed:** To manage version control from your terminal.
* **Docker Installed:** To test your containers locally.
* **GitHub PAT (Personal Access Token):** Required for secure terminal-to-GitHub authentication.
* **Docker Hub PAT:** Required for GitHub-to-Docker Hub authentication (stored as a Secret).

---

### 2. Project Architecture & File Logic

Every file in this project serves a specific purpose in the automated flow.

| File | Why we use it | How it works |
| --- | --- | --- |
| **`app.py`** | **The Application** | A Python script using the Flask framework to create a web-based calculator. |
| **`requirements.txt`** | **Dependencies** | Lists `flask`. It tells Docker exactly which libraries need to be installed to run the code. |
| **`Dockerfile`** | **Container Blueprint** | A script that tells Docker how to build the environment (OS, Python version, copying files, and starting the app). |
| **`.github/workflows/main.yml`** | **The Pipeline** | The "brain" of the project. It detects code pushes and triggers the build and push process to Docker Hub. |

---

### 3. Step-by-Step Execution Flow

#### **Step 1: Local Project Initialization**

We create the folder structure and initialize Git to track changes.

```bash
mkdir Calculator_App_2025 && cd Calculator_App_2025
git init
mkdir -p .github/workflows

```

#### **Step 2: Connecting to GitHub**

We link the local folder to the cloud repository using your credentials.

```bash
# Connect to your GitHub repo
git remote add origin https://18shubham:YOUR_GITHUB_TOKEN@github.com/18shubham/Github_Action_Project_2025.git

```

#### **Step 3: Configuring GitHub Secrets**

You cannot put passwords in code. We use GitHub Secrets to store Docker Hub credentials securely.

* Go to **Settings > Secrets and variables > Actions**.
* Add `DOCKERHUB_USERNAME` (your username).
* Add `DOCKERHUB_TOKEN` (the token from Docker Hub Security).

#### **Step 4: Pushing Code to Trigger Automation**

When you run these commands, GitHub Actions automatically starts the build.

```bash
git add .
git commit -m "Deploying CI/CD Pipeline"
git push -u origin main

```

---

### 4. Error Resolution Log (Common Issues)

DevOps is 90% troubleshooting. Here are the specific errors we encountered and solved:

| Error Message | Why it happened | How to resolve |
| --- | --- | --- |
| **`403 Forbidden`** | Git was using old/cached credentials or an expired token. | Remove the remote (`git remote remove origin`) and re-add it using a fresh Personal Access Token. |
| **`No workflows found`** | The folder name was wrong or the file wasn't pushed. | Ensure the path is exactly `.github/workflows/main.yml` (plural "workflows"). |
| **`failed to read dockerfile: no such file...`** | The `context` in the YAML didn't match the file location. | Move all files to the "root" of the repository or update `context: ./folder_name` in the YAML. |
| **`YAML Red Underlines`** | Indentation or spacing error in the `main.yml` file. | Use 2 spaces for indentation. Never use "Tabs" in YAML files. |

---

### 5. Final Verification & Deployment

Once the GitHub Action turns **Green**, the image is live. You can deploy it on any server in the world using:

```bash
# 1. Download the image from your registry
docker pull 183shubham/flask-calculator:latest

# 2. Run the image as a background container
docker run -d -p 5000:5000 183shubham/flask-calculator:latest

```

**Access the app at:** `http://localhost:5000`

---
<img width="1121" height="1003" alt="image" src="https://github.com/user-attachments/assets/f32bf2a3-dc88-4e9a-901d-c8d35341244b" />

