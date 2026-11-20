# NVIDIA NetQ – Network Observability Lab

<p align="center">
  <img src="https://img.shields.io/badge/Project-Network%20Observability-76B900?style=for-the-badge" alt="Project"/>
  <img src="https://img.shields.io/badge/Domain-Networking-blue?style=for-the-badge" alt="Domain"/>
  <img src="https://img.shields.io/badge/Status-Educational%20Simulation-success?style=for-the-badge" alt="Status"/>
</p>

# 🌐 Live Demo
https://heer4204-bit.github.io/NVIDIA-NetQ-Network-Observability-Lab/

"Launch NVIDIA NetQ Network Observability Lab" (https://heer4204-bit.github.io/NVIDIA-NetQ-Network-Observability-Lab/)

# 📌 About the Project
NVIDIA NetQ Network Observability Lab is an interactive educational project inspired by modern data center networking, network observability, and AI infrastructure monitoring concepts.

The project demonstrates a simulated Spectrum-X AI Ethernet reference architecture with network topology visualization, fabric validation, fault injection, telemetry inspection, and NetQ-style CLI diagnostics.

It is designed to help learners understand network monitoring, troubleshooting, and data center fabric observability concepts.

# 🚀 Key Features
- Network Dashboard: Overview of simulated network health and device status.
- Fabric Validation: Visual representation of network validation and assurance.
- Spine-Leaf Topology: Interactive visualization of data center network connectivity.
- Node Telemetry Inspector: Displays simulated switch and node telemetry.
- Fault Injection Lab: Demonstrates BGP flap, CRC errors, and PFC watchdog scenarios.
- NetQ CLI Shell: Interactive educational command interface with preset diagnostic commands.
- Network Monitoring: Demonstrates simulated throughput and congestion telemetry.
- Troubleshooting: Provides a dedicated troubleshooting interface.

# 📸 Project Screenshots

1. Dashboard Overview

<img width="4320" height="2220" alt="16140" src="https://github.com/user-attachments/assets/c4a6cddc-37e7-41e0-81b6-6bd5f7991066" />

2. Network Topology

<img width="4320" height="2460" alt="16142" src="https://github.com/user-attachments/assets/f9443fe3-b024-4b22-b23b-747836619067" /><

3. Fault Injection Lab

img width="4320" height="3240" alt="16144" src="https://github.com/user-attachments/assets/9a37511d-0bc3-402c-8f26-c91942f98bff" />

4. NetQ CLI Diagnostics

<img width="4320" height="2124" alt="16154" src="https://github.com/user-attachments/assets/a0a4c9c2-0295-4aff-a219-2526a264b2cf" />

# 🛠️ Technology Stack
Technology| Purpose
HTML5| Web page structure
CSS3| Styling and responsive interface
JavaScript| Interactive dashboard functionality
Python| Supporting backend components
JSON| Sample network telemetry data
Git & GitHub| Version control and hosting
GitHub Pages| Static website deployment

# 🏗️ Project Structure
NVIDIA-NetQ-Network-Observability-Lab/
│
├── backend/
│   ├── app.py
│   └── network_monitor.py
│
├── css/
│   └── style.css
│
├── data/
│   └── network_telemetry.json
│
├── docs/
│   ├── deployment-guide.md
│   └── troubleshooting-guide.md
│
├── js/
│   ├── dashboard.js
│   ├── topology.js
│   └── monitoring.js
│
├── screenshots/
│   ├── dashboard-overview.jpg
│   ├── network-topology.jpg
│   ├── fault-injection-lab.jpg
│   └── netq-cli-diagnostics.jpg
│
├── .gitignore
├── LICENSE
├── README.md
├── index.html
├── dashboard.html
├── topology.html
├── alerts.html
└── troubleshooting.html

# ⚙️ Getting Started

Prerequisites
- A modern web browser
- Git
- Python 3 (for running a local static web server)

Clone the Repository:
git clone https://github.com/Heer4204-bit/NVIDIA-NetQ-Network-Observability-Lab.git

Navigate to the Project:
cd NVIDIA-NetQ-Network-Observability-Lab

Run the Frontend Locally:

python -m http.server 8000

Open the following address:
http://localhost:8000/

The static frontend can also be accessed through the GitHub Pages live demo.

For backend setup, refer to the deployment guide and the actual dependencies configured in the backend application.

# 📚 Documentation
- "Deployment Guide" (docs/deployment-guide.md)
- "Troubleshooting Guide" (docs/troubleshooting-guide.md)

# 🎯 Learning Objectives
- Understand data center network observability.
- Explore Spine-Leaf network architecture.
- Learn network health monitoring concepts.
- Understand BGP and EVPN diagnostic workflows.
- Explore RoCEv2, ECN, and PFC telemetry concepts.
- Practice network fault identification and troubleshooting.

# ⚠️ Disclaimer
This is an independent educational simulation project inspired by NVIDIA NetQ and Spectrum-X AI Ethernet networking concepts.

It is not an official NVIDIA product, certified deployment, or real production network monitoring system.

All network devices, telemetry, topology metrics, and diagnostic outputs shown in the simulation are illustrative.

NVIDIA and NetQ are trademarks of NVIDIA Corporation. This project is not affiliated with or endorsed by NVIDIA.

# 👨‍💻 Author
Heer Patel
B.Tech Information Technology | 3rd Year
GitHub: "@Heer4204-bit" (https://github.com/Heer4204-bit)

# 📄 License
This project is distributed under the MIT License. See the "LICENSE" (LICENSE) file for details.

---

# ⭐ If you find this educational project useful, consider giving the repository a star!
