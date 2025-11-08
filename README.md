# 🔒 CyberShield Port Scanner

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

A professional, educational port scanning web application built with Python Flask and modern JavaScript. Designed for network security professionals and cybersecurity students to learn about port scanning methodologies in a safe, controlled environment.

## 🚀 Features

- **🔍 Advanced Port Scanning** - TCP connect scanning with service detection
- **⚡ High Performance** - Concurrent scanning with configurable workers
- **🛡️ Security First** - Rate limiting, input validation, and abuse prevention
- **📱 Responsive Design** - Mobile-friendly interface with real-time updates
- **🎯 Multiple Input Formats** - Support for single ports, ranges, and lists
- **📊 Detailed Reporting** - Comprehensive results with service identification

## 🛠️ Tech Stack

**Backend:**
- Python 3.9+
- Flask & Flask-Limiter
- Concurrent.Futures for parallel processing
- Socket programming for network operations

**Frontend:**
- Vanilla JavaScript (ES6+)
- HTML5 with semantic markup
- CSS3 with Grid & Flexbox
- Responsive design principles

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/cybershield-port-scanner.git
cd cybershield-port-scanner

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
