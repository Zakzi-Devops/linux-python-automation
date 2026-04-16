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

## ▶️ How to Run

### Python

python script.py
 
### Bash

bash script.sh

📂 Output
- health_report.txt → Python-generated report
- system_report.log → Bash-generated system report

📌 Notes
- Log files are excluded using .gitignore
- Designed as a beginner DevOps automation project
- Tested in WSL (Ubuntu 22.04) for real Linux environment