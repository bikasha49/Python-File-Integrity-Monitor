## Python File Integrity Monitor

### Project Overview
This project implements a File Integrity Monitoring system using Python.
It detects unauthorized file changes by comparing current file hashes against a trusted baseline.
The project demonstrates core defensive security concepts used in SOC environments.
### Workflow Diagram 
<p align="left">
  <img src="https://github.com/bikasha49/python_file_integrity_monitor/blob/eba1bf311ad936367f736f6428f0a45c0a870ae4/images/execution_flow_chart.png" width="60%" style="margin-left:60%;">
</p>

### Project Objective
* Demonstrate hands on understanding of file integrity monitoring.
* Show how baseline driven hash comparison detects malicious or unauthorized changes.
* Practice a SOC style monitoring and alerting workflow using Python.

### Security Capabilities Demonstrated
* File integrity monitoring fundamentals.
* Baseline creation and validation.
* Detection of file modification events.
* Detection of file creation events.
* Detection of file deletion events.
* Practical defensive security logic.

### How It Works
* The tool scans a target directory.
* It generates SHA256 hashes for each file.
* It stores these hashes as a trusted baseline.
* It continuously monitors the directory for changes.
* It compares current file hashes against the baseline.
* It alerts when differences are detected.

### Detected Security Events
* Modified files
* Newly created files
* Deleted files

### Environment
* Operating system Kali Linux
* Programming language Python 3
* Hashing algorithm SHA256

### Project Structure
* baseline.txt stores trusted file hashes
* fim.py main monitoring script
* Target directory monitored for file changes

### Usage
* Run the script.
* Select option A to collect a baseline.
* Modify files inside the Target directory.
* Run the script again.
* Select option B to start monitoring.
* Observe real time detection alerts.

### Screenshots and Evidence
This section provides execution proof of the monitoring workflow.
Each screenshot demonstrates a real security outcome produced by the tool.

#### Baseline Creation:
Shows successful generation of trusted file hashes.
<p align="left">
  <img src="https://github.com/bikasha49/python_file_integrity_monitor/blob/eba1bf311ad936367f736f6428f0a45c0a870ae4/images/screenshot_fim_baseline_collected.png" width="60%" style="margin-left:60%;">
</p>

#### Monitoring Started:
Shows the tool running in active monitoring mode using the saved baseline.
<p align="left">
  <img src="https://github.com/bikasha49/python_file_integrity_monitor/blob/eba1bf311ad936367f736f6428f0a45c0a870ae4/images/screenshot_fim_monitoring_started.png" width="60%" style="margin-left:60%;">
</p>

#### Integrity Alerts Detected:
Shows detection of file modification creation and deletion events.
<p align="left">
  <img src="https://github.com/bikasha49/python_file_integrity_monitor/blob/eba1bf311ad936367f736f6428f0a45c0a870ae4/images/screenshot_fim_monitoring_results.png" width="60%" style="margin-left:60%;">
</p>

### Potential Improvements
* Log security alerts to a file for audit and review.
* Implement ignore rules for specific file types or directories.
* Add configuration file support for flexible deployment.
* Integrate email or webhook notifications for alert delivery.


<div align="center">
   <p> 
I am always open to connecting and discussing Cybersecurity opportunities!
  </p>
  <a href="https://www.linkedin.com/in/bikasha-gurung" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect_with_Me-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" />
  </a>

</div>
