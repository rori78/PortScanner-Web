from flask import Flask, render_template, jsonify, request
import nmap

app = Flask(__name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ScanResultLinkedList:
    def __init__(self):
        self.head = None

    def add_scan_result(self, host_info):
        new_node = Node(host_info)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_dict(self):
        result_dict = {}
        current = self.head
        while current:
            for hostname, host_data in current.data.items():
                result_dict[hostname] = host_data
            current = current.next
        return result_dict

linked_list = ScanResultLinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/port_scanner')
def port_scanner():
    return render_template('port_scanner.html')

@app.route('/scan', methods=['POST'])
def scan_ports():
    data = request.get_json()  
    target = data.get("target")  
    ports = data.get("ports", "1-65535")  

    if not target:
        return jsonify({"error": "Target is required"}), 400

    nm = nmap.PortScanner()  

    try:
        nm.scan(hosts=target, arguments=f'-p {ports}')  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    # Memproses hasil pemindaian dan menyimpannya dalam linked list
    scan_result = {}
    for host in nm.all_hosts():
        host_info = {
            "hostname": host,
            "status": nm[host].state(),
            "ports": []
        }
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                port_info = {
                    "port": port,
                    "state": nm[host][proto][port]["state"],
                    "name": nm[host][proto][port].get("name", "")
                }
                host_info["ports"].append(port_info)

        scan_result[host] = host_info

    # Menyimpan hasil pemindaian dalam linked list
    linked_list.add_scan_result(scan_result)

    return jsonify(scan_result), 200

@app.route('/results', methods=['GET'])
def get_results():
    results = linked_list.to_dict()  
    return jsonify(results), 200

# untuk melihat hasil ketik "curl http://localhost:5000/results" pada command prompt

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)