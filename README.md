# Universal Code Installer

Code repository for the new Universal Installer. The new code installer allows you to select which Oddworks project to install, one install for all the projects!

The installation couldn't be simpler!
# Installation
## Download appropiate installer
Under the releases tab, you'll find a download for both the Mac OS and Windows
versions of the installer. Download the appropriate installer to suit your operating system.

(Currently only Windows 11 x86, Windows 11 arm64 and MacOS arm64 has been tested.)


## Flash MicroPython
After downloading and unzipping your selected version of the installer, and accepting all the pop ups that warn you it's dangerous (it's 100% not, the code for the installer is in this repository)

Run the installer and you'll be greeted with this:

![Screenshot 2024-03-06 at 2 38 05 pm](https://github.com/oddworks3d/Universal-Installer/assets/46923688/5492b070-4161-43c0-b2c9-70f064c428e4)

*Before continuing, ensure your Pi Pico is in USB Mass Storage mode by holding down the BOOTSEL button while plugging the pico in to your computer.*



Select the project you want to install by clicking the card

Then click MicroPython

<img width="670" alt="Screenshot 2024-03-06 at 2 45 28 pm" src="https://github.com/oddworks3d/Universal-Installer/assets/46923688/2aa064c4-b3c6-47ab-9525-92d9c1b27d6e">

Then simply choose your Pi Pico

>On mac it will look something like:
>```/Volumes/RPI-RP2```

>On windows it will look something like: 
>```F:/```

After selecting your Pi Pico, hit `Install MicroPython` to begin installing MicroPython on your Pico.


## Install Project
After flashing MicroPython or if MicroPython is already installed, Click the Install Project button.

*Before continuing ensure your Pi Pico is **NOT** in USB Mass Storage mode and that it is connected to your computer*

<img width="670" alt="Screenshot 2024-03-06 at 2 44 27 pm" src="https://github.com/oddworks3d/Universal-Installer/assets/46923688/14f3fa22-b2d1-4341-b070-7ce93951fc6c">


From the dropdown, select your connected Pi Pico which will look different depending on what devices are connected and if you are on windows or MacOS.

If the correct com port isn't showing or you're unable to select the Pico, disconnect all other serial devices from your computer and hit `Refresh`

> For mac it will look similar to:
> `/dev/tty.usbmodem21301`

>For windows it will look similar to:
>`COM3`

After selecting the correct device from the list of devices, hit the `Install Code` button to begin installing.

If nothing fails and there are no errors, you're done! Enjoy!


# Troubleshooting

If you don't want to run the installer for whatever reason, the code is available to download and install on the Pi Pico using Thonny (https://thonny.org)

Simply download the `main.py` file from the project's repo and open it in thonny, save it to the pico, and that's it!.

# Building

cd into installer dir

For mac:
> python setup.py py2app

For WINDOWS:
> python -m PyInstaller --add-data 'render.html;.' --add-binary 'm.uf2;.' --add-data 'picnic.css;.' --add-data 'style.css;.' --distpath './Releases/Windows-Build' --onefile --noconsole installer.py 
