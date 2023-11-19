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

![alt text](https://github.com/oddworks3d/Universal-Installer/blob/48f0ab8d143c9523bcb4724efd9da35fe8e16f96/step1.png?raw=true)
*Before continuing, ensure your Pi Pico is in USB Mass Storage mode by holding down the BOOTSEL button while plugging the pico in to your computer.*



Click `Select Pi Pico Directory` and search your filesystem for the mounted drive that is your Pi Pico.

>On mac it will look something like:
>```/Volumes/RPI-RP2```

>On windows it will look something like: 
>```F:/```

After selecting your Pi Pico, hit `Install MicroPython` to begin installing MicroPython on your Pico.


## Choose Project
After flashing MicroPython (or choosing to skip) you'll move on to step 2:
![alt text](https://github.com/oddworks3d/Universal-Installer/blob/48f0ab8d143c9523bcb4724efd9da35fe8e16f96/step2.png?raw=true)
Select which oddworks project you want to install from the above dropdown.

To view all projects head [Here](https://github.com/oddworks3d)

## Install The Code

Next you'll move onto step 3:

![alt text](https://github.com/oddworks3d/Universal-Installer/blob/48f0ab8d143c9523bcb4724efd9da35fe8e16f96/step3.png?raw=true)
*Before continuing ensure your Pi Pico is **NOT** in USB Mass Storage mode and that it is connected to your computer*

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
