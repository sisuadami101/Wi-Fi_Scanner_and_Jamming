# Wi-Fi_Scanner_and_Jamming

# Wi-Fi Scanner and Jamming Simulator

This Python script is a **Wi-Fi Scanner and Jamming Simulator** designed for educational purposes. It scans available Wi-Fi networks in range, allows the user to select a target network, and performs a **simulated jamming operation** on the selected network for a user-defined duration.

## Features

- **Wi-Fi Network Scanning**: Lists all available Wi-Fi networks with detailed information (SSID, BSSID, frequency, signal strength).
- **Target Selection**: Allows the user to select a specific Wi-Fi network for simulated jamming.
- **Custom Jamming Duration**: User can define how long the simulated jamming will run.
- **Non-Root Compatible**: Works in Termux without requiring root access.

---

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system.  
   On Termux, you can install Python with:
   ```bash
   pkg install python
   pkg install termux-tools
