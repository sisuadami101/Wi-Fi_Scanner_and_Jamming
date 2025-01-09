#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import time
from subprocess import Popen, PIPE

# Console colors
W = '\033[0m'  # white (normal)
G = '\033[32m'  # green
R = '\033[31m'  # red
B = '\033[34m'  # blue
T = '\033[93m'  # tan

def check_dependencies():
    """Check if required tools are installed."""
    required_tools = ["termux-wifi-scaninfo"]
    for tool in required_tools:
        if not shutil.which(tool):
            print(f"{R}[-]{W} Missing tool: {tool}")
            print(f"{B}[+]{W} Please install it using `pkg install termux-tools`.")
            exit(1)

def scan_wifi():
    """Scan available Wi-Fi networks."""
    try:
        proc = Popen(["termux-wifi-scaninfo"], stdout=PIPE, stderr=PIPE)
        output, error = proc.communicate()

        if error:
            print(f"{R}[-]{W} Error: {error.decode()}")
            return []

        # Parse output
        networks = eval(output.decode())  # Output is in JSON format
        return networks
    except Exception as e:
        print(f"{R}[-]{W} Failed to scan Wi-Fi networks: {e}")
        return []

def display_networks(networks):
    """Display the scanned Wi-Fi networks."""
    if not networks:
        print(f"{R}[-]{W} No networks found.")
        return

    print(f"{G}[+]{W} Found {len(networks)} networks:")
    for i, net in enumerate(networks, 1):
        ssid = net.get("ssid", "Unknown")
        bssid = net.get("bssid", "Unknown")
        frequency = net.get("frequency", "Unknown")
        level = net.get("level", "Unknown")
        print(f"{T}[{i}]{W} SSID: {B}{ssid}{W}, BSSID: {G}{bssid}{W}, "
              f"Frequency: {B}{frequency} MHz{W}, Signal: {G}{level} dBm{W}")

def select_target(networks):
    """Allow user to select a target network."""
    try:
        choice = int(input(f"{B}[?]{W} Enter the number of the target network (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            return networks[choice - 1]
        else:
            print(f"{R}[-]{W} Invalid choice. Exiting.")
            exit(1)
    except ValueError:
        print(f"{R}[-]{W} Invalid input. Exiting.")
        exit(1)

def get_jamming_duration():
    """Get the duration of jamming in seconds."""
    try:
        duration = int(input(f"{B}[?]{W} Enter jamming duration in seconds: "))
        if duration <= 0:
            print(f"{R}[-]{W} Duration must be greater than 0. Exiting.")
            exit(1)
        return duration
    except ValueError:
        print(f"{R}[-]{W} Invalid input. Exiting.")
        exit(1)

def start_jamming(target, duration):
    """Simulate jamming the selected target."""
    ssid = target.get("ssid", "Unknown")
    bssid = target.get("bssid", "Unknown")
    print(f"{G}[+]{W} Starting jamming on target:")
    print(f"    SSID: {B}{ssid}{W}")
    print(f"    BSSID: {G}{bssid}{W}")
    print(f"{T}[!]{W} Jamming simulation started for {duration} seconds.")

    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            # Simulating jamming activity
            print(f"{T}[...]{W} Jamming {G}{bssid}{W}...")
            time.sleep(2)
        print(f"{G}[+]{W} Jamming completed.")
    except KeyboardInterrupt:
        print(f"\n{R}[!]{W} Jamming stopped manually. Exiting.")
        exit(0)

def main():
    print(f"{G}[+]{W} Starting Wi-Fi scanner...")

    # Scan networks
    networks = scan_wifi()
    if not networks:
        print(f"{R}[-]{W} No networks found. Exiting.")
        exit(1)

    # Display scanned networks
    display_networks(networks)

    # Let user select target
    target = select_target(networks)

    # Get jamming duration
    duration = get_jamming_duration()

    # Start jamming
    start_jamming(target, duration)

if __name__ == "__main__":
    check_dependencies()
    main()
