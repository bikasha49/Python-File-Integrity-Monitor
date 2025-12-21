# 🛡️ Python File Integrity Monitor (FIM)

> **Role:** Cybersecurity Analyst Portfolio Project 
> **Concept:** Integrity Monitoring & Intrusion Detection

## 📌 Project Overview
A custom-built **File Integrity Monitor (FIM)** developed in Python. This tool monitors a target directory for unauthorized changes, creating a baseline of file hashes (SHA-512) and continuously checking for modifications, creations, or deletions.

This project demonstrates the core concept of **Integrity** within the CIA Triad, a fundamental principle of Security Operations Center (SOC) activities.

## 🚀 Features
* **SHA-512 Hashing:** Uses robust cryptographic hashing to fingerprint files (significantly more secure than MD5).
* **Baseline Creation:** Generates a "known-good" state of the target directory to identify deviations.
* **Real-Time Monitoring:** Continuously scans for unauthorized changes in an infinite loop.
* **Granular Alerting:** Distinguishes between three types of incidents:
    * `[NEW]` File Created
    * `[CHANGED]` File Modified (Integrity Compromised)
    * `[DELETED]` File Removed

## 🛠️ Tools & Technologies Used
* **Core Language:** Python 3
* **Operating System:** Kali Linux (Virtual Machine)
* **Encryption Standard:** SHA-512 Hashing Algorithm
* **Version Control:** Git & GitHub
* **Text Editor:** Nano (CLI based editing)
* **Python Libraries:**
    * `hashlib`: For generating cryptographic signatures.
    * `os`: For interacting with the operating system file paths.
    * `time`: For controlling the monitoring loop intervals.

### 1. Real-Time Detection ("The Money Shot")
*The FIM detects a file modification instantly as it happens. The split-screen view shows the attack commands (left) and the automated detection (right).*
### ![Real Time Alerts](https://github.com/bikasha49/Python-File-Integrity-Monitor/raw/6751b2acf466efd1dcdd418ba972c903e7f3d611/demo.png)

### 2. Baseline Creation
*Establishing the initial "Known Good" state. The script calculates SHA-512 hashes for all target files to create a fingerprint.*
### ![Baseline Collection](https://github.com/bikasha49/Python-File-Integrity-Monitor/raw/6751b2acf466efd1dcdd418ba972c903e7f3d611/Baseline.png)

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bikasha49/Python-File-Integrity-Monitor.git

2. **Navigate to the directory:**
   ```bash
   cd Python-File-Integrity-Monitor
3. **Run the script:**
   ```bash
   python3 fim.py
4. **Initialize the Baseline**
   Select **Option A**. The script will calculate the hash of every file in the `Target` folder and save it to `baseline.txt`. This teaches the tool what "normal" looks like.

5. **Start Monitoring**
   Select **Option B**. The tool will load the saved baseline and begin continuously checking files for changes.

5. **Verify Alerts**
   While the script is running, open a second terminal and modify, add, or delete files in the `Target` folder. You will see real-time alerts in the monitoring window.

---

<div align="center">

  <p>
    If you found this project useful, please consider giving it a <strong>Star</strong> ⭐<br>
    I am always open to connecting and discussing Cybersecurity opportunities!
  </p>

  <a href="https://www.linkedin.com/in/bikasha-gurung" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Connect_with_Me-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn" />
  </a>

</div>
