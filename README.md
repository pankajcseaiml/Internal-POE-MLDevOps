# Internal POE - MLOps & DevOps Pipeline Assignment

Comprehensive implementation of the 12-step MLOps/DevOps assignment for **hello.py**, VS Code project configuration, GitHub integration, Jenkins CI/CD automation, Docker containerization, Pytest unit testing, and Evidently AI monitoring.

**Repository:** [https://github.com/pankajcseaiml/Internal-POE-MLDevOps](https://github.com/pankajcseaiml/Internal-POE-MLDevOps)

---

## 📁 Project Structure

```text
Internal POE/
├── .vscode/
│   ├── settings.json         # VS Code workspace settings & pytest test discovery
│   └── launch.json           # VS Code debug and execution configurations
├── tests/
│   └── test_hello.py         # Pytest unit test case (Step 11)
├── Dockerfile                # Lightweight Python Docker image configuration (Steps 9 & 10)
├── hello.py                  # Single-file core application (Step 2)
├── evidently_monitor.py      # Evidently AI data drift and quality monitor (Step 12)
├── Jenkinsfile               # Declarative Jenkins CI/CD pipeline (Steps 5, 6, 7)
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore configuration
└── README.md                 # Detailed step-by-step documentation
```

---

## 📋 Step-by-Step Assignment Walkthrough

### Step 2: Very Simple Single File Application `hello.py`
The application `hello.py` contains a modular function `get_message()` returning `"Hello MLOps"` and a `main()` function printing it.

```python
# hello.py
def get_message() -> str:
    return "Hello MLOps"

def main():
    message = get_message()
    print(message)

if __name__ == "__main__":
    main()
```
**Execution:**
```bash
python hello.py
# Output: Hello MLOps
```

---

### Step 3: Create Project in VS Code Project
1. Open the project folder in VS Code:
   ```bash
   code "C:\Users\Pankaj\Documents\Internal POE"
   ```
2. Configuration files created under `.vscode/`:
   - `.vscode/settings.json`: Enables `pytest`, sets test directory to `tests`, and specifies the default Python interpreter.
   - `.vscode/launch.json`: Provides 1-click debug/run configurations for `hello.py`, `pytest`, and `evidently_monitor.py`.

---

### Step 4: Push Project Structure to Git
Initialize the local Git repository, configure the remote repository, and push to GitHub:

```bash
git init
git add .
git commit -m "feat: complete MLOps hello-pipeline project structure"
git branch -M main
git remote add origin https://github.com/pankajcseaiml/Internal-POE-MLDevOps.git
git push -u origin main
```

---

### Step 5: Install & Configure Jenkins
1. Jenkins is installed on Windows at `C:\Program Files\Jenkins` and runs as a Windows Service (`Jenkins`).
2. Jenkins web console is accessible at:
   ```text
   http://localhost:8081
   ```
   *(Note: Port 8081 is configured because Port 8080 is used by Steam web helper on this machine).*
3. Default Jenkins Home: `C:\ProgramData\Jenkins\.jenkins`
4. Plugins configured:
   - **Git Plugin** (`hudson.plugins.git.GitTool`)
   - **Pipeline Plugin**
   - **Windows Batch Plugin** (`hudson.tasks.BatchFile`)

---

### Step 6: Pull the Code from GitHub in Jenkins
In Jenkins, configure a new Pipeline or Freestyle job:
1. Open Jenkins Dashboard (`http://localhost:8081`).
2. Click **New Item** -> Name: `Internal-POE-MLDevOps` -> Select **Pipeline** -> Click **OK**.
3. Under **Pipeline** definition, select **Pipeline script from SCM**:
   - **SCM**: Git
   - **Repository URL**: `https://github.com/pankajcseaiml/Internal-POE-MLDevOps.git`
   - **Branch Specifier**: `*/main`
   - **Script Path**: `Jenkinsfile`
4. Click **Save**.

---

### Step 7: Run Jenkins Job
1. In the `Internal-POE-MLDevOps` project page, click **Build Now**.
2. Click on the running build (e.g., `#1`) -> **Console Output**.
3. The pipeline stages execute sequentially:
   - Stage 1: Checkout Code from GitHub
   - Stage 2: Install Dependencies from `requirements.txt`
   - Stage 3: Run Pytest test suite
   - Stage 4: Run Evidently AI Monitoring
   - Stage 5: Build and Run Docker Container
   - Post: Archive `evidently_report.html`

---

### Step 8: Install Docker
Docker Desktop for Windows is installed on the system:
```powershell
docker --version
# Output: Docker version 29.8.2
```
*Note: Make sure Docker Desktop is launched and running to enable the container daemon (`npipe:////./pipe/dockerDesktopLinuxEngine`).*

---

### Step 9: Pull Lightweight Python Docker Image
We use `python:3.11-slim`, which has minimal footprint (~50MB compressed) compared to the standard python image (>300MB):
```bash
docker pull python:3.11-slim
```

---

### Step 10: Add `hello.py` to Docker
Defined in `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY hello.py .
CMD ["python", "hello.py"]
```
**Build and Run Commands:**
```bash
# Build the Docker image
docker build -t hello-mlops:latest .

# Run the container
docker run --rm hello-mlops:latest
# Output: Hello MLOps
```

---

### Step 11: Configure Pytest and Print 1 Test Case
Pytest test file located at `tests/test_hello.py`:
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
**Execution:**
```bash
python -m pytest -v -s tests/test_hello.py
```
**Test Result Output:**
```text
tests/test_hello.py::test_hello_mlops_message 
[PYTEST OUTPUT] get_message() returned: 'Hello MLOps'
[PYTEST OUTPUT] captured stdout from main(): 'Hello MLOps'
PASSED [100%]
============================== 1 passed in 0.02s ==============================
```

---

### Step 12: Configuration Evidently Tool & Monitor
Configured in `evidently_monitor.py` using Evidently AI:
1. Generates reference (baseline) data and current (production) data with simulated distribution drift.
2. Computes **Data Drift** and **Data Summary** metric presets.
3. Exports an interactive HTML dashboard: `evidently_report.html`.

**Execution:**
```bash
python evidently_monitor.py
```
**Output:**
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
The resulting `evidently_report.html` can be opened directly in any browser for interactive visual inspection of feature drift and data quality metrics.

