#!/usr/bin/env python3
import subprocess
import argparse
import re


def get_args():
    parser = argparse.ArgumentParser(description="Change MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True,
                        help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True,
                        help="New MAC address")
    args = parser.parse_args()
    return args


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["ifconfig", interface, "down"], check=True)
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac], check=True)
    subprocess.run(["ifconfig", interface, "up"], check=True)


def get_current_mac(interface):
    try:
        ifconfig_results = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC address")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Could not execute ifconfig on interface {interface}")
        return None


if __name__ == "__main__":
    options = get_args()
    current_mac = get_current_mac(options.interface)
    if current_mac:
        print("Current MAC =", current_mac)
        change_mac(options.interface, options.new_mac)
        current_mac = get_current_mac(options.interface)
        if current_mac == options.new_mac:
            print(f"[+] MAC address was successfully changed to {current_mac}")
        else:
            print("[-] MAC address did not get changed.")
