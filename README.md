Web-Based Port Scanner Manual 
PBL-214 
Table of Contents 
1. Introduction 
2. System Requirements 
3. Installation 
4. Configuration 
5. Usage 
6. Troubleshooting 
7. FAQ 
8. Contact Information 


1. Introduction 

Welcome to the Web-Based Port Scanner Manual. This tool allows you to scan open ports on a 
specified IP address from a web interface. It is built using Flask for the backend and JavaScript 
for the frontend. 

2. System Requirements

 Python 3.8 or higher 
 Flask 2.0 or higher 
 Node.js 14 or higher (for frontend development) 
 Basic understanding of network protocols and port scanning 

4. Installation 

Backend 

1. Clone the Repository 
git clone https://github.com/rori78/PortScanner-Web.git 

cd web-port-scanner 

2. Create a Virtual Environment 

python3 -m venv venv 

source venv/bin/activate 

3. Install Dependencies 

pip install -r requirements.txt 

4. Run the Application 

flask run 

Frontend 

1. Navigate to Frontend Directory 

cd frontend 

2. Install Dependencies 

npm install 

3. Run the Development Server 

npm start 

4. Configuration 

Edit the app.py file to set any specific configurations such as allowed IP ranges, logging 
preferences, and other settings. 

5. Usage 

1. Access the Web Interface 

Start debugging app.py code and click Running on http://127.0.0.1:5000 

2. Enter IP Address 

Enter the IP address you want to scan in the input field. 

3. Select Ports 

Choose the ports you want to scan  

4. Start Scan 

Click on the "Start Scan" button to begin scanning. Results will be displayed in the 
results section. 

6. Troubleshooting 


Common Issues 
1. Application Not Starting 

Ensure all dependencies are installed and the virtual environment is activated. 

source venv/bin/activate 

flask run 

2. Frontend Not Loading 

Ensure the Node.js server is running. 

cd frontend 

npm start 

Logs 

Check the logs directory for any error logs.
