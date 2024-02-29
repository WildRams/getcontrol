---
sort: 1
---
**GetControl** software is designed to help with managing structural refinements (mainly using the powder diffraction data) performed using [FullProf Suite](https://www.ill.eu/sites/fullprof/) software.

It can help to visualise all PCR files in the directory, collect and aggregate the information from various files created during the structural
 refinement and visualise them. Furthermore, it facilitates easy access to the supplementary files with further analysis.

I developed it to help me get a quicker overview and control over a vast number of additional info you can obtain from the refinement. Of course, the way it works is not suitable for all, but someone can find it helpful.

The tool is under continuous development. All bug reports or suggestions are welcomed.

The lates is ![GitHub release (latest by date)](https://img.shields.io/github/v/release/wildrams/getcontrol) (see [Download](#download "Go to Download")).
Information about _What is new_ can be found [here](autoupdate/gcupdateinfo.txt?raw=true).

## Installation ##
There is no need for installation. For Windows and Linux, there are single-file executables. For the macOS, the image disk (DMG file) is available.

The program tries to search for the FullProf path automatically. If not found or you use a nonstandard path, please set it in the Preferences.

Additional 3rd party software facilitating the analysis and visualisation can also be linked. The links to the software webpages are provided by clicking the appropriate labels in the Preferences.

## Setting storage ##
The program stores its settings in the local profile directory. The path depends on the system and is the following

* Windows 🪟 ```c:\Users\Profile_name\AppData\Local\GetControl```
* Linux 🐧  ```~/config/GetControl```
* macOS 🍏 ```~/Library/Application Support/GetControl```

This directory can be accessed quickly via Preferences (General tab), and click on the Open directory button side by the LOG files info.

## Update ##
An automatic update check is set on by default (can be switched off in Preferences). After each program launch, a small file with the version info is downloaded from the server and compared with the local one. No local data are sent to the server.

## Licence
GetControl is developed as freeware. The licence can be accessed [here](LICENSE?raw=true). I keep the source closed for the moment as I develop it mainly for myself. There was no initial intention to share it, but some of my colleagues found it very useful. So you are free to use it if found appropriate for you.

The Python scripts generated for the plotters are free to be modified, and they are under MIT licence (see the header of the scripts).

## Download ##
Check the [releases](https://github.com/wildrams/getcontrol/releases/latest) section or follow the link below for the latest release

* [Windows 64-bit](https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64.exe?raw=true) ![GitHub release (latest by date and asset)](https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol-x64_86.exe)
* [Windows 32-bit](https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.exe?raw=true) ![GitHub release (latest by date and asset)](https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol.exe)
* [Linux 64-bit](https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64?raw=true) ![GitHub release (latest by date and asset)](https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol-x64_86)
* [Linux 32-bit](https://github.com/wildrams/getcontrol/releases/latest/download/GetControl?raw=true) ![GitHub release (latest by date and asset)](https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol)
* [mcOS 64-bit](https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.dmg?raw=true) ![GitHub release (latest by date and asset)](https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol.dmg)

## Usage ##
Open the directory with your PCR files using the Open button or Ctrl(Meta)+O shortcut. You can also drag&drop any file from the directory containing PCR files.


