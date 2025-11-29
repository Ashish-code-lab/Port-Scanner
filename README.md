# CyberShield Port Scanner

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

A professional, educational port scanning web application built with Python Flask and modern JavaScript. Designed for network security professionals and cybersecurity students to learn about port scanning methodologies in a safe, controlled environment.

## Features

- ** Advanced Port Scanning** - TCP connect scanning with service detection
- ** High Performance** - Concurrent scanning with configurable workers
- ** Security First** - Rate limiting, input validation, and abuse prevention
- ** Responsive Design** - Mobile-friendly interface with real-time updates
- ** Multiple Input Formats** - Support for single ports, ranges, and lists
- ** Detailed Reporting** - Comprehensive results with service identification

## Tech Stack

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

## Installation

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
Usage
Basic Scanning
Enter a target (domain or IP address)

Specify ports (e.g., 22,80,443 or 1-100)

Click "Start Port Scan"

Common Ports
Click any common port to add it to your scan

Use "Scan All Common Ports" for quick assessment

Example Targets for Testing
bash
# Educational targets (always get permission first)
scanme.nmap.org
localhost
127.0.0.1
API Documentation
Scan Endpoint
http
POST /scan
Content-Type: application/json

{
  "host": "example.com",
  "ports": "22,80,443",
  "scan_all_common": false
}
Response:

json
{
  "host": "example.com",
  "scanned_ports_count": 3,
  "open_ports_count": 2,
  "results": [
    {"port": 22, "open": true, "service": "ssh"},
    {"port": 80, "open": true, "service": "http"},
    {"port": 443, "open": false, "service": "https"}
  ]
}
Testing
Run the test suite to verify functionality:

bash
# Run all tests
python -m pytest tests/

# Run specific test module
python -m pytest tests/test_scanner.py -v
Security Features
Rate Limiting: 10 requests per minute per IP

Input Validation: Comprehensive host and port validation

Private IP Detection: Warnings for internal network scanning

Concurrency Limits: Maximum 50 concurrent socket connections

Timeout Protection: 2-second socket timeout per port

Legal Disclaimer
This tool is for educational and authorized testing purposes only.

Only scan systems you own or have explicit permission to test

Unauthorized port scanning may be illegal in your jurisdiction

Use responsibly and ethically for learning purposes

The developers are not responsible for any misuse of this software.

Contributing
We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

Development Setup
bash
# Fork and clone the repository
git clone https://github.com/yourusername/cybershield-port-scanner.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
Contribution Guidelines
Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Project Stats
https://img.shields.io/github/languages/code-size/yourusername/cybershield-port-scanner
https://img.shields.io/github/last-commit/yourusername/cybershield-port-scanner
https://img.shields.io/github/issues/yourusername/cybershield-port-scanner

Skills Demonstrated
Full-Stack Development: Flask backend + vanilla JavaScript frontend

Network Programming: Socket programming and TCP/IP protocols

Security Engineering: Rate limiting, input validation, secure coding

Performance Optimization: Concurrent programming and resource management

UI/UX Design: Responsive, accessible web interface

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Inspired by professional security tools like Nmap

Built for educational purposes in cybersecurity

Thanks to the open-source community for invaluable resources

If you find this project useful, please give it a star on GitHub!



