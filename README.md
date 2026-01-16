# Server Log Analysis Tool

## Project Overview
This project is a security automation tool designed to detect brute-force attacks and unauthorized access attempts in server logs. It analyzes log data to identify suspicious IP addresses based on HTTP status codes.

## Features
- **Automated Scanning:** Parses server access logs (CSV format).
- **Threat Detection:** Identifies users attempting to access restricted areas (Status Code 403).
- **Reporting:** Outputs alerts to the console for immediate action.

## How to Use
1. Ensure you have Python installed.
2. Place your log file named `server_logs.csv` in the same directory.
3. Run the script:
   ```bash
   python analyzer.py
