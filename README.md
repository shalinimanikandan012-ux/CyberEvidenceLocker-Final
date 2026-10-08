# Cyber Evidence Locker

## Project Overview

Cyber Evidence Locker is a Digital Forensics and Cybersecurity web application developed using Python Flask and MySQL. The system securely stores, manages, and verifies digital evidence files while maintaining data integrity and audit records.

This project demonstrates how digital evidence can be securely handled using forensic principles such as hashing, integrity verification, and audit logging.

---

## Features

- User Registration
- User Login Authentication
- Secure Evidence Upload
- SHA-256 Hash Generation
- Evidence Integrity Verification
- Evidence List Management
- Audit Log Tracking
- Dashboard Statistics
- Digital Evidence Storage

---

## Technologies Used

- Python
- Flask
- MySQL
- HTML
- SHA-256 Hashing
- XAMPP
- phpMyAdmin

---

## Project Structure

```
CyberEvidenceLocker
│
├── app.py
├── requirements.txt
├── Procfile
│
└── templates
    ├── register.html
    ├── login.html
    ├── dashboard.html
    ├── upload.html
    ├── verify.html
    ├── audit_log.html
    └── evidence_list.html
```

---

## How It Works

1. User registers and logs in.
2. Evidence files are uploaded to the system.
3. SHA-256 hash values are generated and stored.
4. Uploaded evidence is recorded in the database.
5. Evidence can be verified using hash comparison.
6. User activities are tracked through audit logs.
7. Dashboard displays project statistics.

---

## Objective

To create a secure digital evidence management system that helps investigators store, verify, and track digital evidence while maintaining integrity and chain-of-custody principles.

---

## Future Enhancements

- Role-Based Access Control
- File Encryption
- Evidence Download Tracking
- Cloud Storage Integration
- Advanced Audit Reporting

---

## Author

Shalini M

B.Sc. Digital and Cyber Forensic Science

Rathinam Global Deemed to be University
