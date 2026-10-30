# MLOps & DevOps End-to-End Pipeline Assignment

[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.13-blue.svg)](https://www.python.org/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red.svg)](https://www.jenkins.io/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![Pytest](https://img.shields.io/badge/Pytest-Unit%20Tested-0A9EDC.svg)](https://docs.pytest.org/)
[![Evidently AI](https://img.shields.io/badge/Evidently%20AI-Monitoring-purple.svg)](https://www.evidentlyai.com/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Internal--POE--MLDevOps-success.svg)](https://github.com/pankajcseaiml/Internal-POE-MLDevOps)

An end-to-end beginner MLOps/DevOps project demonstrating modular application development (`hello.py`), VS Code workspace configuration, GitHub version control, Jenkins declarative CI/CD automation, Docker containerization with a lightweight base image, Pytest unit testing, and Evidently AI data drift and model quality monitoring.

**GitHub Repository:** [https://github.com/pankajcseaiml/Internal-POE-MLDevOps](https://github.com/pankajcseaiml/Internal-POE-MLDevOps)

---

## 📁 Clean Project Structure

```text
Internal POE/
├── .vscode/
│   ├── settings.json         # VS Code workspace settings & pytest test discovery
│   └── launch.json           # VS Code debug & run configurations
├── tests/
│   └── test_hello.py         # Pytest unit test case (Step 11)
├── Dockerfile                # Lightweight Python container image (Steps 9 & 10)
├── hello.py                  # Single-file core application (Step 2)
├── evidently_monitor.py      # Evidently AI drift and quality monitoring (Step 12)
├── Jenkinsfile               # Declarative Jenkins CI/CD automation (Steps 5, 6, 7)
├── requirements.txt          # Production dependencies
├── .gitignore                # Clean Git exclusion rules
└── README.md                 # Complete documentation & execution guide
```

---

## 🔄 Architecture & CI/CD Pipeline

```
┌─────────────┐       ┌──────────────┐       ┌─────────────────┐
│  hello.py   │ ────> │  Git/GitHub  │ ────> │ Jenkins (CI/CD) │
└─────────────┘       └──────────────┘       └────────┬────────┘
                                                      │
         ┌───────────────────┬────────────────────────┴─────────────────────┐
         ▼                   ▼                                              ▼
 ┌───────────────┐   ┌──────────────────────────────┐              ┌────────────────┐
 │ Pytest Test   │   │ Evidently AI Data Monitoring │              │ Docker Build   │
 │ (Unit verify) │   │ (Drift & Summary Dashboard)  │              │ & Run Container│
 └───────────────┘   └──────────────────────────────┘              └────────────────┘
```

---

## 📋 Step-by-Step Assignment Walkthrough

### Step 2: Very Simple Single-File Application (`hello.py`)
Modular Python application returning and printing the expected message:
```python
# hello.py
def get_message() -> str:
    """Return the welcome message."""
    return "Hello MLOps"

def main():
    """Print the welcome message for the project."""
    message = get_message()
    print(message)

if __name__ == "__main__":
    main()
```
**Run in CMD:**
```cmd
python hello.py
```
*Output:*
```text
Hello MLOps
```

---

### Step 3: Create Project in VS Code
The workspace includes `.vscode` configurations:
* [`.vscode/settings.json`](.vscode/settings.json): Enables `pytest` auto-discovery in `tests/`.
* [`.vscode/launch.json`](.vscode/launch.json): 1-click debug/run configurations for `hello.py`, `pytest`, and `evidently_monitor.py`.

**Run in CMD:**
```cmd
code .
```

---

### Step 4: Push Project Structure to Git
Initialize Git, track files, and push to GitHub:
```cmd
git status
git add .
git commit -m "feat: complete MLOps project pipeline structure"
git branch -M main
git remote add origin https://github.com/pankajcseaiml/Internal-POE-MLDevOps.git
git push -u origin main
```

---

### Step 5: Install & Configure Jenkins
1. Jenkins is installed locally on Windows and accessible at:
   ```text
   http://localhost:8081
   ```
   *(Port `8081` is configured to avoid conflicts with Steam's web helper on port `8080`).*
2. Jenkins plugins configured:
   * **Git Plugin**
   * **Pipeline Plugin**
   * **Windows Batch Plugin**

**Test Jenkins in CMD:**
```cmd
curl -I http://localhost:8081
start http://localhost:8081
```

---

### Step 6: Pull the Code from GitHub in Jenkins
In the Jenkins Web UI:
1. Click **New Item** ➔ Enter name `Internal-POE-MLDevOps` ➔ Select **Pipeline** ➔ Click **OK**.
2. Scroll to the **Pipeline** section at the bottom:
   * **Definition**: Select `Pipeline script from SCM`
   * **SCM**: Select `Git`
   * **Repository URL**: `https://github.com/pankajcseaiml/Internal-POE-MLDevOps.git`
   * **Branch Specifier**: `*/main`
   * **Script Path**: `Jenkinsfile`
3. Click **Save**.

---

### Step 7: Run Jenkins Pipeline
1. On the `Internal-POE-MLDevOps` page, click **Build Now**.
2. Click on the build number ➔ **Console Output**.
3. All stages execute automatically:
   * **Checkout Code:** Fetches latest commit from GitHub.
   * **Install Dependencies:** Installs packages from `requirements.txt`.
   * **Run Pytest:** Executes test suite with `-p no:dash`.
   * **Evidently AI Monitoring:** Generates data drift report.
   * **Docker Build and Run:** Builds and executes the container.
   * **Post Action:** Archives `evidently_report.html` as a build artifact.

---

### Step 8: Install & Verify Docker
Docker Desktop with the WSL 2 backend is installed on Windows:
```cmd
docker --version
docker ps
```
*Output:*
```text
Docker version 29.8.2
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

---

### Step 9: Pull Lightweight Python Docker Image
Pulls `python:3.11-slim` (~50 MB compressed vs > 300 MB standard image):
```cmd
docker pull python:3.11-slim
```

---

### Step 10: Add `hello.py` to Docker (Build & Run Container)
Defined in [`Dockerfile`](Dockerfile):
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
```

**Build Image:**
```cmd
docker build -t hello-mlops:latest .
```

**Run Container:**
```cmd
docker run --rm hello-mlops:latest
```
*Output:*
```text
Hello MLOps
```

---

### Step 11: Configure Pytest and Print 1 Test Case
Test file located at [`tests/test_hello.py`](tests/test_hello.py):
```python
from hello import get_message, main

def test_hello_mlops_message(capsys):
    """Test 1: Verify get_message returns expected greeting and main prints it."""
    message = get_message()
    print(f"\n[PYTEST OUTPUT] get_message() returned: '{message}'")
    assert message == "Hello MLOps"

    main()
    captured = capsys.readouterr()
    print(f"[PYTEST OUTPUT] captured stdout from main(): '{captured.out.strip()}'")
    assert "Hello MLOps" in captured.out
```

**Run in CMD:**
```cmd
python -m pytest -p no:dash -v -s tests/test_hello.py
```
*Output:*
```text
tests/test_hello.py::test_hello_mlops_message 
[PYTEST OUTPUT] get_message() returned: 'Hello MLOps'
[PYTEST OUTPUT] captured stdout from main(): 'Hello MLOps'
PASSED [100%]
============================== 1 passed in 0.02s ==============================
```

---

### Step 12: Configure Evidently Tool & Monitor
Configured in [`evidently_monitor.py`](evidently_monitor.py):
1. Generates reference (baseline) and current (production) datasets with simulated drift on `feature_1`.
2. Computes **Data Drift** and **Data Summary** metric presets.
3. Exports an interactive dashboard: `evidently_report.html`.

**Run in CMD:**
```cmd
python evidently_monitor.py
```
*Output:*
```text
==================================================
  Evidently AI Tool - Data & Model Monitoring     
==================================================
[INFO] Reference dataset shape: (150, 4)
[INFO] Current (production) dataset shape: (150, 4)
[INFO] Computing Data Drift and Summary metrics...
[SUCCESS] Evidently report generated successfully: evidently_report.html
[REPORT LOCATION] C:\Users\Pankaj\Documents\Internal POE\evidently_report.html
==================================================
```

**Open in Browser:**
```cmd
start evidently_report.html
```

---

## 🛠️ Verification & Tech Stack

| Step | Tool / Technology | Status | Output / Link |
| :--- | :--- | :--- | :--- |
| **2** | Python 3 | ✅ Verified | `Hello MLOps` |
| **3** | VS Code | ✅ Configured | `.vscode/settings.json`, `.vscode/launch.json` |
| **4** | Git / GitHub | ✅ Verified | [Internal-POE-MLDevOps](https://github.com/pankajcseaiml/Internal-POE-MLDevOps) |
| **5** | Jenkins Service | ✅ Running | `http://localhost:8081` |
| **6** | Jenkins SCM Pull | ✅ Verified | GitHub webhook / Git SCM polling |
| **7** | Jenkins Pipeline | ✅ Verified | `Jenkinsfile` automated stages |
| **8** | Docker Engine | ✅ Running | Docker Desktop (WSL 2) |
| **9** | Docker Hub | ✅ Verified | `python:3.11-slim` |
| **10** | Docker Container | ✅ Verified | `hello-mlops:latest` |
| **11** | Pytest | ✅ Passed | 1/1 test passed (`test_hello.py`) |
| **12** | Evidently AI | ✅ Generated | `evidently_report.html` interactive dashboard |
