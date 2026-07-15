function openPortScanner() {
    window.location.href = "/port_scanner";
}

function getStarted() {
    window.location.href = "/port_scanner";
}

function scanPorts() {
    const target = document.getElementById("target").value;
    const portRange = document.getElementById("port-range").value || "1-65535";
    
    // Split portRange into start and end ports
    const [startPort, endPort] = portRange.split("-");

    const requestData = {
        target: target,
        ports: { start: parseInt(startPort, 10), end: parseInt(endPort, 10) },
    };

    fetch("http://localhost:5000/scan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("Scan results:", data);
        displayResults(data);
    })
    .catch((error) => {
        console.error("Error during scan:", error);
    });
}


function displayResults(data) {
    const resultsBody = document.getElementById("results-body");

    // Clear previous results
    resultsBody.innerHTML = "";

    // Populate new results
    for (const [host, info] of Object.entries(data)) {
        info.ports.forEach(portInfo => {
            const row = document.createElement("tr");

            const portCell = document.createElement("td");
            portCell.textContent = portInfo.port;

            const serviceCell = document.createElement("td");
            serviceCell.textContent = portInfo.name;

            const statusCell = document.createElement("td");
            statusCell.textContent = portInfo.state;

            row.appendChild(portCell);
            row.appendChild(serviceCell);
            row.appendChild(statusCell);

            resultsBody.appendChild(row);
        });
    }
}

function clearInput() {
    document.getElementById("target").value = "";
    document.getElementById("port-range").value = "";
    document.getElementById("protocol").value = "tcp";
    document.getElementById("results-body").innerHTML = "";
}

function scrollToPortScanner() {
    document.getElementById("port-scanner").scrollIntoView({ behavior: "smooth" });
}
