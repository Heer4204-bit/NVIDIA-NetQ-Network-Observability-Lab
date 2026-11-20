
# NVIDIA NetQ Network Observability Lab
## Deployment Guide

Welcome to the NVIDIA NetQ Network Observability Lab!

This guide explains how to set up and run the educational network observability project locally.

> Note: This is an independent educational simulation inspired by network observability concepts. It is not an official NVIDIA product or a real NetQ deployment.

---

## 1. Prerequisites

Make sure you have:

- Python 3.10 or later
- pip (Python package manager)
- Git
- A modern web browser
- A code editor (VS Code recommended)

## 2. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Heer4204-bit/NVIDIA-NetQ-Network-Observability-Lab.git
```

Navigate to the project directory:

```bash
cd NVIDIA-NetQ-Network-Observability-Lab
```

## 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 5. Run the Flask Backend

Execute:

```bash
python backend/app.py
```

The development server will start at:

http://127.0.0.1:5000/

## 6. Available API Endpoints

| Endpoint | Description |
|---|---|
| `/api/status` | Backend status |
| `/api/devices` | Network device information |
| `/api/health` | Network health statistics |
| `/api/alerts` | Network alerts |

## 7. Verify the Installation

Open these URLs in your browser:

- http://127.0.0.1:5000/api/status
- http://127.0.0.1:5000/api/devices
- http://127.0.0.1:5000/api/health
- http://127.0.0.1:5000/api/alerts

You should receive JSON responses from the Flask backend.

## 8. Project Data

Sample network telemetry is stored in:

`data/network_telemetry.json`

The dataset includes:

- Network devices
- Device status
- Latency
- Packet loss
- Network traffic
- Network links
- Simulated alerts

## 9. Deployment Notes

For public deployment:

- Host the frontend on GitHub Pages or another static hosting provider.
- Host the Flask backend on a suitable Python application hosting service.
- Configure the frontend API URL to point to the deployed backend.
- Enable HTTPS and configure appropriate security settings.

GitHub Pages does not execute Python Flask applications.

## 10. Disclaimer

This project uses simulated network telemetry for educational and demonstration purposes.

It does not represent a live NVIDIA NetQ environment.

---

**Developed by Heer Patel**

GitHub: https://github.com/Heer4204-bit
