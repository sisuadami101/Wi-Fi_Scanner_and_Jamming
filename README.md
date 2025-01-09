# Wi-Fi Scanner and Jamming Simulator

This project is a **Wi-Fi Scanner and Jamming Simulator** written in Python. It scans available Wi-Fi networks, allows the user to select a targbash
etwork, and simulates a jamming process for a user-defined duration. The script is designed to run on Termux, making it lightweight and easy to use.

---

## Features

1. **Wi-Fi Network Scanning**:  
   The script scans all available Wi-Fi networks in range and displays detailed information, including:
   - SSID (Wi-Fi name)
   - BSSID (MAC address of the access point)
   - Frequency
   - Signal strength

2. **Target Selection**:  
   After scanning, the user can select a specific Wi-Fi network to target by entering its corresponding number from the displayed list.

3. **Customizable Jamming Duration**:  
   The user can define the duration of the jamming simulation in seconds.

4. **Simulated Jamming**:  
   The script simulates the process of sending deauthentication packets to the selected Wi-Fi network (educational purpose only).

5. **Non-Root Compatible**:  
   The script works without requiring root access when used on Termux.

6. **Network Details**:  
   Displays the device's hostname and local IP address for debugging and informational purposes.

---

## Prerequisites

Before running the script, ensure you have the following installed on Termux:

**Python 3.x**:  
   Install Python:
 ```bash
 pkg update 
 pkg upgrade 
 pkg install python
 pkg install git
```



**Termux Tools:**
Install the necessary Termux tools:

```bash
pkg install termux-tools
```

## Termux API (optional for advanced functionalities): ##
**Install Termux API:**

```bash
pkg install termux-api
```


## Installation ##
**Clone the Repository:**

```bash
git clone https://github.com/sisuadami101/Wi-Fi_Scanner_and_Jamming.git
```

### Run the Script: ###

```bash
python3 wifi_jammer.py
```

## View Network Details:##
The script will display your device's hostname and local ***IP*** address.

## Scan Wi-Fi Networks: ##
The script scans all available Wi-Fi networks and displays them in a numbered list.

## Select a Target: ##
Enter the number corresponding to the network you want to target.

## Set Jamming Duration: ##
Specify the duration (in seconds) for which you want to simulate the jamming.

## Simulated Jamming: ##
The script simulates the jamming process and displays a message when completed.

# Example Output:
```yaml
[+] Hostname: termux-device
[+] Local IP: 192.168.1.5

[+] Starting Wi-Fi scanner...
[+] Found 3 networks:
[1] SSID: HomeWiFi, BSSID: aa:bb:cc:dd:ee:ff, Frequency: 2412 MHz, Signal: -40 dBm
[2] SSID: OfficeWiFi, BSSID: ff:ee:dd:cc:bb:aa, Frequency: 2437 MHz, Signal: -50 dBm
[3] SSID: PublicWiFi, BSSID: 11:22:33:44:55:66, Frequency: 2462 MHz, Signal: -60 dBm

[?] Enter the number of the target network (1-3): 1
[?] Enter jamming duration in seconds: 10

[+] Starting jamming on target:
    SSID: HomeWiFi
    BSSID: aa:bb:cc:dd:ee:ff
[!] Jamming simulation started for 10 seconds.
[...]: Jamming aa:bb:cc:dd:ee:ff...
[+] Jamming completed.
```


## Known Issues ##
**termux-wifi-scaninfo Not Found:**
If you encounter the **Error**:
```bash
[-] Missing tool: termux-wifi-scaninfo
[+] Please install it using `pkg install termux-tools.
```



**Ensure termux-tools is installed:**
```bash
pkg install termux-tools
```


## Wi-Fi Scan Not Working: ##
**Ensure your device has granted Termux the necessary permissions:**

```bash
termux-setup-storage
termux-wifi-enable true
```


## Disclaimer ##
This script is intended ONLY FOR **EDUCATIONAL AND RESEARCH PURPOSES.** The jamming functionality is a simulation and does not perform any real network interference.

## Important Notes: ##
Unauthorized interference with networks or devices is **illegal** in most countries.
The authors and contributors of this repository are not responsible for any misuse of this script.
Use this script only on networks you own or have explicit permission to test.


#License
This project is licensed under the ***MIT License***. See the LICENSE file for details.












