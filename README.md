# Universal Code Installer

Code repository for the Universal Installer. The Universal Code Installer allows you to select which Oddworks project to install — one installer for all the projects!

---

## 🌐 New: Install Online

**The easiest way to install any Oddworks project is now via the web installer, no download required!**

👉 **[oddworks.uk](http://oddworks.uk)**

Just open the link in Chrome, Edge, or Opera, select your project, connect your Pi Pico, and you're done.

---

## Desktop Installer (Legacy)

The original desktop installer is still available if you prefer a local install.

### Download

Under the **Releases** tab you'll find downloads for Windows and macOS.
Currently tested on:
- Windows 11 x86
- Windows 11 arm64
- macOS arm64

### Flash MicroPython

After downloading and unzipping your selected version, run the installer. Accept any warnings (the code is fully open source and available in this repository).

You'll be greeted with the project selector screen.

*Before continuing, ensure your Pi Pico is in USB Mass Storage mode by holding down the BOOTSEL button while plugging it into your computer.*

Select your project by clicking the card, then click **MicroPython**, then choose your Pi Pico:

- **Mac:** something like `/Volumes/RPI-RP2`
- **Windows:** something like `F:/`

Hit **Install MicroPython** to begin.

### Install Project

After flashing MicroPython (or if it's already installed), click **Install Project**.

*Ensure your Pi Pico is **NOT** in USB Mass Storage mode and is connected to your computer.*

From the dropdown, select your connected Pi Pico — it will look different depending on your OS and connected devices:

- **Mac:** something like `/dev/tty.usbmodem21301`
- **Windows:** something like `COM3`

If the correct port isn't showing, disconnect all other serial devices and hit **Refresh**.

Hit **Install Code** and you're done!

---

## Troubleshooting

If you'd rather not use either installer, all project code is available to install manually using [Thonny](https://thonny.org). Download `main.py` from the project's repo, open it in Thonny, and save it to the Pico.

---

## Building (Developers)

`cd` into the installer directory.

**Mac:**
```
python setup.py py2app
```

**Windows:**
```
python -m PyInstaller --add-data 'render.html;.' --add-binary 'm.uf2;.' --add-data 'picnic.css;.' --add-data 'style.css;.' --distpath './Releases/Windows-Build' --onefile --noconsole installer.py
```
