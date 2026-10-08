# 🌞 Solar Panel Live Monitoring System

A Python-based desktop application for **real-time solar panel monitoring** using an **ESP32 over Wi-Fi**.

The system retrieves voltage, current, and power measurements from an ESP32 through an HTTP API, displays the readings in a graphical interface, plots live voltage/current values, and automatically stores monitoring data in a CSV file for later analysis.

---

## 📌 Project Overview

The **Solar Panel Live Monitoring System** provides a simple desktop dashboard for monitoring solar panel electrical parameters in real time.

The Python application communicates with an ESP32 through a local Wi-Fi network. The ESP32 provides measurement data through the following HTTP endpoint:

```text
http://<ESP32-IP>/data
```

The application continuously retrieves:

* ⚡ Voltage
* 🔌 Current
* 🔋 Power

The received information is displayed on the GUI and automatically recorded in `solar_log.csv`.

---

## ✨ Features

### 1. Real-Time Monitoring

The application continuously retrieves data from the ESP32 every second.

It displays:

```text
Voltage: XX V
Current: XX mA
Power: XX W
```

The application uses an HTTP request to communicate with the ESP32.

---

### 2. ESP32 Wi-Fi Communication

The desktop application communicates with the ESP32 using the ESP32's IP address.

The IP address can be configured directly in the Python source code:

```python
ESP_IP = "192.168.137.60"
```

Change this value to the current IP address assigned to your ESP32.

Both the computer and ESP32 should be connected to the same Wi-Fi/network.

---

### 3. Live Graph

The application provides a real-time graph using Matplotlib.

The graph displays:

* Voltage vs. Time
* Current vs. Time

## The graph continuously updates and retains the latest **60 data points**.

### 4. Automatic CSV Data Logging

Every successful reading is automatically stored in:

```text
solar_log.csv
```

Each record contains:

```text
Timestamp, Voltage, Current, Power
```

The application appends new measurements to the CSV file during monitoring.

Example:

```text
10:30:01,18.5,420,7.77
10:30:02,18.6,425,7.90
10:30:03,18.7,430,8.04
```

---

### 5. Monitoring Log

A text-based log area displays the incoming readings along with their timestamps.

Example:

```text
10:30:01 | V: 18.5V | I: 420mA | P: 7.77W
10:30:02 | V: 18.6V | I: 425mA | P: 7.90W
```

---

### 6. Connection Error Handling

If the application cannot communicate with the ESP32, the GUI displays an error state and records a connection-error message.

For example:

```text
Connection Error - Check ESP32 IP/WiFi
```

The application uses a request timeout of two seconds when communicating with the ESP32.

---

### 7. Save Log

The GUI contains a **Save Log Now** button.

The project already writes monitoring data automatically to `solar_log.csv`; the button provides a confirmation that the data has been saved.

---

### 8. Clear Log

The **Clear Log** button clears the displayed monitoring messages from the GUI.

This does not remove the CSV data file; it only clears the text displayed in the application's log area.

---

# 🏗️ System Architecture

```text
             ☀️ SOLAR PANEL
                   │
                   ▼
          ┌─────────────────┐
          │ Voltage/Current │
          │    Sensors      │
          └────────┬────────┘
                   │
                   ▼
             ┌───────────┐
             │   ESP32   │
             │ Controller│
             └─────┬─────┘
                   │
             Wi-Fi / HTTP
                   │
                   ▼
        ┌─────────────────────┐
        │ Python Monitoring   │
        │     Application     │
        └──────────┬──────────┘
                   │
        ┌──────────┼───────────┐
        ▼          ▼           ▼
     Voltage     Current      Power
        │          │           │
        └──────────┼───────────┘
                   │
                   ▼
          📈 Live Graph
                   │
                   ▼
            📄 CSV Logger
```

---

# 🖥️ Technologies Used

## Software

* Python
* Tkinter
* Matplotlib
* Requests
* CSV
* Threading
* HTTP/REST communication

The main application imports Tkinter, Requests, threading, CSV handling, datetime, and Matplotlib components.

## Hardware

* ESP32
* Solar panel
* Voltage measurement circuit/sensor
* Current measurement circuit/sensor
* Wi-Fi network

> The uploaded Python application specifically handles the desktop monitoring side. The exact ESP32 sensor hardware and firmware are not included in the uploaded files.

---

# 📂 Project Structure

Recommended project structure:

```text
solar-panel-monitor/
│
├── solar_monitor.py
├── requirements.txt
├── README.md
│
└── solar_log.csv
```

### File Description

| File               | Description                             |
| ------------------ | --------------------------------------- |
| `solar_monitor.py` | Main Python GUI monitoring application  |
| `requirements.txt` | Python package dependencies             |
| `README.md`        | Project documentation                   |
| `solar_log.csv`    | Automatically generated monitoring data |

---

# ⚙️ Requirements

The project requires Python and the packages listed in `requirements.txt`.

Important dependencies include:

```text
matplotlib==3.10.8
numpy==2.4.3
requests==2.32.5
pillow==12.1.1
pyinstaller==6.19.0
```

These versions are specified in the uploaded requirements file.

The requirements file also contains supporting packages required by Matplotlib and PyInstaller.

---

# 🚀 Installation

## Step 1: Install Python

Install Python on your computer.

Verify the installation:

```bash
python --version
```

or:

```bash
py --version
```

---

## Step 2: Clone or Download the Project

Place the project files in a folder:

```text
solar-panel-monitor/
```

Make sure the following files are present:

```text
solar_monitor.py
requirements.txt
```

---

## Step 3: Create a Virtual Environment

Recommended:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## Step 4: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

The required packages include Requests and Matplotlib.

---

# 🔧 ESP32 Configuration

Before running the application, determine the IP address of the ESP32.

Open:

```text
solar_monitor.py
```

Find:

```python
ESP_IP = "192.168.137.60"
```

Replace it with your ESP32's actual IP address.

For example:

```python
ESP_IP = "192.168.1.105"
```

The application will then request:

```text
http://192.168.1.105/data
```

The ESP32 must provide a JSON response containing:

```json
{
    "voltage": 18.5,
    "current": 420,
    "power": 7.77
}
```

The Python application reads the `voltage`, `current`, and `power` fields from the returned JSON data.

> The exact ESP32 firmware/API implementation is not included in the uploaded project files, so the JSON format above represents the interface expected by the Python application.

---

# ▶️ Running the Application

After configuring the ESP32 IP address, run:

```bash
python solar_monitor.py
```

or:

```bash
py solar_monitor.py
```

The application will open a desktop window titled:

```text
Solar Panel Live Monitor - Harish
```

The GUI displays the solar monitoring dashboard.

---

# 📊 Dashboard

The dashboard contains:

```text
┌─────────────────────────────────────────────┐
│     🌞 Solar Panel Live Monitoring System   │
│                                             │
│        Voltage: XX V                        │
│        Current: XX mA                       │
│        Power: XX W                          │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │          Monitoring Log                 │ │
│ │  10:30:01 | V: 18.5V | I: 420mA       │ │
│ │  10:30:02 | V: 18.6V | I: 425mA       │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│              Live Graph                     │
│                                             │
│ [ Save Log Now ]       [ Clear Log ]        │
└─────────────────────────────────────────────┘
```

---

# 🔄 Data Flow

The monitoring process works as follows:

```text
1. ESP32 measures solar parameters
              ↓
2. ESP32 exposes measurements through HTTP
              ↓
3. Python sends GET request to /data
              ↓
4. ESP32 returns JSON data
              ↓
5. Python extracts voltage/current/power
              ↓
6. GUI displays live values
              ↓
7. Data is added to monitoring log
              ↓
8. Data is saved to solar_log.csv
              ↓
9. Live graph is updated
```

The monitoring thread performs the update approximately once per second.

---

# 🧵 Multithreading

The project uses a background daemon thread for periodic data collection.

This allows the application to continue updating the ESP32 data while the Tkinter GUI remains active.

The monitoring process runs continuously with a one-second delay between updates.

---

# 📈 Live Graph Operation

The Matplotlib graph contains two plotted values:

```text
Voltage (V)
Current (mA)
```

The graph uses time/data points as the X-axis and automatically rescales as new measurements arrive.

## Only the most recent 60 points are retained for the live display.

# 📁 Data Logging

The monitoring data is automatically stored in:

```text
solar_log.csv
```

The CSV records:

```text
Timestamp
Voltage
Current
Power
```

This makes the collected measurements available for future analysis, reporting, or visualization.

---

# 🛠️ Troubleshooting

## ESP32 Connection Error

If the dashboard shows:

```text
Voltage: Error
Current: Error
Power: Error
```

check:

1. ESP32 is powered ON.
2. ESP32 is connected to Wi-Fi.
3. Computer and ESP32 are on the same network.
4. ESP32 IP address is correct.
5. ESP32 provides the `/data` endpoint.
6. The endpoint returns valid JSON.
7. No firewall is blocking the connection.

---

## Wrong IP Address

Update:

```python
ESP_IP = "YOUR_ESP32_IP"
```

For example:

```python
ESP_IP = "192.168.1.105"
```

---

## Missing Python Package

If Python reports:

```text
ModuleNotFoundError
```

run:

```bash
pip install -r requirements.txt
```

---

## CSV File

The application creates/updates:

```text
solar_log.csv
```

in the application's working directory when successful readings are received.

---

# 📦 Creating a Standalone Windows EXE

The project includes PyInstaller in its requirements, making it possible to package the Python application as a Windows executable.

Install the requirements:

```bash
pip install -r requirements.txt
```

Then build:

```bash
pyinstaller --onefile --windowed solar_monitor.py
```

The generated executable will normally be available inside:

```text
dist/
```

You can then run the application without manually launching the Python source file, provided the packaged application has the required runtime resources.

---

# 🔐 Network Considerations

This application currently communicates with the ESP32 through an HTTP request on the local network.

Therefore:

```text
Computer
    │
    │ Wi-Fi
    │
    ▼
 Router / Hotspot
    │
    │ Wi-Fi
    ▼
 ESP32
```

The computer must be able to reach the configured ESP32 IP address.

---

# 🎯 Project Objectives

The main objectives of the project are:

* Monitor solar panel voltage in real time.
* Monitor solar panel current in real time.
* Monitor calculated/received power values.
* Provide a simple desktop monitoring interface.
* Display measurements graphically.
* Maintain a timestamped monitoring log.
* Automatically store readings in CSV format.
* Provide basic connection-error feedback.
* Enable future analysis of collected solar data.

---

# 🔮 Future Enhancements

The current implementation can be extended with:

### Hardware

* Solar irradiance sensor
* Temperature sensor
* Battery voltage monitoring
* Battery State of Charge (SOC)
* Multiple solar panels
* Energy generation measurement

### Software

* Daily/monthly energy reports
* Historical data graphs
* Database storage
* Excel export
* PDF reports
* Data filtering
* Minimum/maximum value tracking
* Efficiency calculation
* Solar performance analytics
* Automatic alerts
* Cloud data synchronization
* Web dashboard
* Mobile application
* Remote monitoring
* Authentication and user accounts

### Advanced Analytics

Future versions could calculate:

```text
Energy Generated
      ↓
Performance Analysis
      ↓
Daily/Weekly/Monthly Trends
      ↓
Solar Panel Efficiency
      ↓
Fault/Anomaly Detection
```

---

# 🧪 Testing

Basic testing should verify:

| Test                | Expected Result                 |
| ------------------- | ------------------------------- |
| ESP32 powered OFF   | Connection error displayed      |
| Correct ESP32 IP    | Live measurements displayed     |
| Incorrect IP        | Connection error displayed      |
| Valid JSON response | Voltage/current/power displayed |
| New measurement     | Log entry created               |
| Successful reading  | CSV entry created               |
| GUI running         | Live graph updates              |
| Clear Log clicked   | GUI log is cleared              |

---

# 📌 Current Project Limitations

Based on the supplied files, the current application:

* Uses a manually configured ESP32 IP address.
* Requires the ESP32 to expose an HTTP `/data` endpoint.
* Uses local network communication.
* Displays voltage and current in the live graph.
* Does not include cloud storage.
* Does not include user authentication.
* Does not include a database.
* Does not include the ESP32 firmware in the supplied files.
* Does not include a dedicated web/mobile interface.

These limitations can be addressed in future versions.

---

# 👨‍💻 Author

**Harish**

**Project:** Solar Panel Live Monitoring System

**Technology:** Python + Tkinter + Matplotlib + ESP32 + Wi-Fi

---

# 📄 License

This project can be modified and extended for educational, academic, and personal development purposes.

---

# ⭐ Project Summary

The **Solar Panel Live Monitoring System** combines an ESP32-based measurement system with a Python desktop application to provide real-time monitoring of solar panel electrical parameters.

The application communicates with the ESP32 through Wi-Fi, retrieves voltage, current, and power values, displays them in a graphical interface, plots live measurements, and automatically records the collected data into a CSV file.

It provides a foundation that can be extended into a complete **IoT-based solar energy monitoring and analytics platform**.
