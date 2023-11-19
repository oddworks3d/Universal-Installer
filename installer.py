# Coded by Tea S.
# 2022
import os
import shutil
import sys
import glob
import pyboard
import serial
import webview
import requests


default_page = 'render.html'



def loadConfig():
    with requests.get("https://raw.githubusercontent.com/oddworks3d/Universal-Installer/master/config.json") as url:
        data = url.json()
        return data



config = loadConfig()
print(config)
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class Api():
    def openDialog(self):
        result = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG, allow_multiple=False)
        return result

    def installMP(self, path):
        try:
            filepath = path[0]
            shutil.copyfile("m.uf2", filepath + "/m.uf2")
            return "success"
        except Exception as e:
            print(e)
            return str(e)

    def getComPorts(self):
        return serial_ports()

    def getProjects(self):
        return config['projects']

    def installCode(self, port, project):
        try:
            print("download file")
            response = requests.get(config["projects"][int(project)]['url'])
            print(config["projects"][int(project)]['url']);
        except Exception as e:
            print(e)
            return str(e)
        try:
            pyb = pyboard.Pyboard(port, 115200)
            print("connection made");
            pyb.enter_raw_repl()
            print("entered repl");
            # Delete all contents
            if pyb.fs_exists("config"):
                pyb.fs_rm("config")
            if pyb.fs_exists("main.py"):
                pyb.fs_rm("main.py")
            if pyb.fs_exists("ssd1306.py"):
                pyb.fs_rm("ssd1306.py")
            pyb.fs_put_direct(response.content, "main.py")
            print("copied");
            pyb.exit_raw_repl()
            print("exit raw repl")
            return "success"
        except Exception as e:
            print(e)
            return str(e)


api = Api()
window = webview.create_window('Universal Code Installer', "render.html", js_api=api, width=450, height=350,
                               resizable=False)
webview.start()
