# Linux Python Automation

A DevOps-focused project using Python and Bash for system checks, automation, and basic monitoring.

## 🚀 Features

### 🐍 Python Script
- Collects detailed system information
- Checks multiple APIs (GitHub, Google, etc.)
- Uses lists and loops to handle multiple endpoints
- Handles API responses (status codes, success/failure)
- Saves results to `health_report.txt`

### 🐧 Bash Script
- Displays system information (user, date, directory, hostname)
- Checks uptime, disk usage, and memory
- Performs network checks
- Uses `tee` to log output while displaying it
- Saves results to `system_report.log`

## 🧠 Concepts Practiced
- Python scripting for automation
- API calls with `requests`
- Lists and loops (handling multiple inputs)
- Bash scripting
- Logging (`tee`)
- Output redirection (`/dev/null`)
- Basic monitoring concepts

## 📂 Project Structure

```text
linux-python-automation/
├── script.py
├── script.sh
├── health_report.txt
├── system_report.log
├── requirements.txt
└── README.md
```

## ▶️ How to Run

### Python
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
python -m pip install -r requirements.txt
python script.py
``` 
### Bash
```bash
bash script.sh
```
### 📂 Output

- Python-generated report
- Bash-generated system report

## 📊 Sample Output

```text
=== API Check ===

URL: https://api.github.com
Status Code: 200
Success: True
```

### 📌 Notes
- Activate the `.venv` environment before running `python script.py`
- Use `requirements.txt` to install Python dependencies before running the script
- Log files are excluded using .gitignore
- Designed as a beginner DevOps automation project
- Tested in WSL (Ubuntu 22.04) for real Linux environment
