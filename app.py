from flask import Flask, request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import socket
import concurrent.futures
import re
import ipaddress
from typing import List, Dict, Union

app = Flask(__name__)

 IP
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["10 per minute"],
    storage_uri="memory://",
)

# Configuration
MAX_PORTS = 200
SCAN_TIMEOUT = 2.0
MAX_WORKERS = 50

# Common ports mapping
COMMON_PORTS = {
    '21': 'FTP',
    '22': 'SSH',
    '23': 'Telnet',
    '25': 'SMTP',
    '53': 'DNS',
    '80': 'HTTP',
    '110': 'POP3',
    '115': 'SFTP',
    '135': 'RPC',
    '139': 'NetBIOS',
    '143': 'IMAP',
    '194': 'IRC',
    '443': 'SSL',
    '445': 'SMB',
    '993': 'IMAPS',
    '995': 'POP3S',
    '1433': 'MSSQL',
    '3306': 'MySQL',
    '3389': 'Remote Desktop',
    '5632': 'PCAnywhere',
    '5900': 'VNC',
    '25665': 'Minecraft'
}

def validate_host(host: str) -> bool:
    """Validate hostname or IP address"""
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', host):
            return True
        return False

def parse_ports(ports_str: str) -> List[int]:
    """Parse ports string into list of port numbers"""
    ports = set()
    
    parts = ports_str.split(',')
    
    for part in parts:
        part = part.strip()
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                if 1 <= start <= end <= 65535:
                    ports.update(range(start, end + 1))
            except ValueError:
                raise ValueError(f"Invalid port range: {part}")
        else:
            try:
                port = int(part)
                if 1 <= port <= 65535:
                    ports.add(port)
            except ValueError:
                raise ValueError(f"Invalid port: {part}")
    
    return sorted(ports)

def scan_port(host: str, port: int) -> Dict[str, Union[int, bool, str]]:
    """Scan a single port"""
    try:
        with socket.create_connection((host, port), timeout=SCAN_TIMEOUT):
            service_name = COMMON_PORTS.get(str(port))
            if not service_name:
                try:
                    service_name = socket.getservbyport(port)
                except OSError:
                    service_name = "Ashish"
            
            return {
                "port": port,
                "open": True,
                "service": service_name
            }
    except (socket.timeout, ConnectionRefusedError, OSError):
        return {
            "port": port,
            "open": False,
            "service": COMMON_PORTS.get(str(port), "Unknown")
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
@limiter.limit("10 per minute")
def scan():
    """
    Port scanning endpoint for EDUCATIONAL USE ONLY
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        host = data.get('host', '').strip()
        ports_str = data.get('ports', '').strip()
        scan_all_common = data.get('scan_all_common', False)
        
        # Validate host
        if not host:
            return jsonify({"error": "Domain/IP is required"}), 400
        
        if not validate_host(host):
            return jsonify({"error": "Invalid domain or IP address"}), 400
        
        # Determine which ports to scan
        if scan_all_common:
            ports = [int(port) for port in COMMON_PORTS.keys()]
        elif ports_str:
            try:
                ports = parse_ports(ports_str)
            except ValueError as e:
                return jsonify({"error": str(e)}), 400
        else:
            return jsonify({"error": "No ports specified"}), 400
        
        # Check port limits
        if len(ports) > MAX_PORTS:
            return jsonify({"error": f"Too many ports requested. Maximum is {MAX_PORTS}"}), 400
        
        # Security warning for private networks
        try:
            ip = ipaddress.ip_address(socket.gethostbyname(host))
            if ip.is_private:
                app.logger.warning(f"Scanning private IP: {host}")
        except:
            pass
        
        # Perform scan with thread pool
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_port = {executor.submit(scan_port, host, port): port for port in ports}
            
            for future in concurrent.futures.as_completed(future_to_port):
                results.append(future.result())
        
        # Sort results by port number
        results.sort(key=lambda x: x['port'])
        
        open_ports = [r for r in results if r['open']]
        
        return jsonify({
            "host": host,
            "scanned_ports_count": len(ports),
            "open_ports_count": len(open_ports),
            "results": results
        })
        
    except Exception as e:
        app.logger.error(f"Scan error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/common-ports', methods=['GET'])
def get_common_ports():
    """Return common ports list"""
    return jsonify({"common_ports": COMMON_PORTS})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)