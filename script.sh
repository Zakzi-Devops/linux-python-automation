#!/bin/bash

LOG_FILE="system_report.log"

{
echo "==== System Report ==="
echo "User: $(whoami)"
echo "Hostname: $(hostname)"
echo "Date: $(date)"
echo "Current Directory: $(pwd)"
echo

echo "=== Uptime ===="
uptime
echo

echo "=== Disk Usage ==="
df -h
echo

echo "=== Memory Info ==="
free -h 2>/dev/null || echo "free command not available on this system"
echo

echo "=== Network Check ==="
ping -c 3 github.com 2>/dev/null || echo "ping command not available or blocked"
curl -I https://github.com 2>/dev/null || echo "curl github.com failed"
echo
ping -c 3 google.com 2>/dev/null || echo "ping command not available or blocked"
curl -I https://www.google.com 2>/dev/null || echo "curl google.com failed"
} | tee "$LOG_FILE"

echo
echo "Report saved to $LOG_FILE"
