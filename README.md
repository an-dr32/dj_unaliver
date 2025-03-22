# dj_unaliver

Ever had a neighbor who thinks they're the weekend DJ at 7 AM? This tool is here to give them a reality check. A spiritual successor to *Party Pooper*, which sadly stopped working on newer hardware, this app brings back the ability to silence unwanted Bluetooth devices with extreme prejudice.

## Testbed

This tool was developed and tested on:

- **Hardware:** Raspberry Pi 4B
- **Target Device:** Samsung Soundbar J Series

## How It Works

This app exploits a vulnerability in certain Bluetooth devices, sending packets that cause them to disconnect or become unresponsive. Not all devices are affected, but many older or poorly secured ones will just give up and stop playing music.

## How to Use

1. Clone the repo:
   ```sh
   git clone https://github.com/an-dr32/dj_unaliver.git
   cd dj_unaliver
   ```
2. Install dependencies (if any are required):
   ```sh
   sudo apt-get install bluez
   ```
3. Run the script and select your target:
   ```sh
   sudo python3 dj_unaliver.py
   ```
4. Enjoy the silence.

## App Options Explained

Here’s what each option in the app does:

- **"Scan for nearby devices"**: Lists nearby Bluetooth devices you can target, by their MAC address.
- **"Lookup MAC address info"**: Will search the MAC address info online in macvendors or maclookup.
- **"Info on selected device"**: This will attempt to get the info directly from the hardware.
- **"L2Ping of Death"**: On older hardware, it can disrupt it, on newer, serves to check its pinging.
- **"RFCOMM Hostage Connection"**: As it says, it will take hostage the hardware. Cool, huh?
- "Forced Pairing": This will try to force the pairing. You can loop it, or try to do it once.



## Ethical and Legal Considerations

Alright, jokes aside, this tool is for educational and research purposes only. Using it to intentionally disrupt devices you don’t own may be illegal in your country, so don’t go using this on random people just because they have bad taste in music. If you’re testing it, make sure you have permission to mess with the device.

## Disclaimer

I take no responsibility for any misuse of this tool. Use at your own risk, and don’t be a jerk with it. Seriously... Don't be.

---

That’s it! Have fun, and use responsibly.
