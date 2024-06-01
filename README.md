# MAC Address Changer

This is a simple Python script to change the MAC address of a network interface. It uses the `ifconfig` command to bring down the interface, change its MAC address, and then bring it back up.

## Prerequisites

- Python 3.x
- `ifconfig` command (available in Unix-based systems)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/P4R4D0X-HACKS/MAC_Changer.git
    cd mac-address-changer
    ```

2. **Make the script executable** (optional):
    ```bash
    chmod +x mac_changer.py
    ```

## Usage

Run the script with the interface and new MAC address as arguments:

```bash
./mac_changer.py -i <interface> -m <new_mac_address>
```
