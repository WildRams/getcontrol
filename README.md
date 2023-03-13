# GetControl <img src="https://github.com/WildRams/GetControl-code/blob/main/Graphics/GetControl-256.png?raw=true" alt="logo" width=48px/>


GetControl software is designed to help with managing structural refinements (mainly using the powder diffraction data) performed using [<a href="https://www.ill.eu/sites/fullprof/" target="_blank">FullProf Suite</a> software.

It can help to visualise all PCR files in the directory, collect and aggregate the information from various files created during the structural
 refinement and visualise them. Furthermore, it facilitates easy access to the supplementary files with further analysis.

I developed it to help me get a quicker overview and control over a vast number of additional info you can obtain from the refinement. Of course, the way it works is not suitable for all, but someone can find it helpful.

The tool is under continuous development. All bug reports or suggestions are welcomed.

Information about the updates can be found [here](https://github.com/WildRams/GetControl-code/blob/main/gcupdateinfo.txt?raw=true).

## Installation
There is no need for installation. For Windows and Linux, there are single-file executables. For the macOS, the image disk (DMG file) is available.

The program tries to search for the FullProf path automatically. If not found or you use a nonstandard path, please set it in the Preferences.

Additional 3rd party software facilitating the analysis and visualisation can also be linked. The links to the software webpages are provided by clicking the appropriate labels in the Preferences.

## Setting storage
The program stores its settings in the local profile directory
Windows - c:\Users\Profile\AppData\Local\GetControl
Linux - ~/config/GetControl
macOS - ~/Library/Application Support/GetControl

This directory can be accessed quickly via Preferences (General tab), and click on the Open directory button side by the LOG files info.

## Update
An automatic update routine check is set on by default (can be switched off in Preferences). After each program launch, a small file with the version info is downloaded from the server and compared with the local one. No local data are sent to the server.

##Usage
Open the directory with your PCR files using the Open button or Ctrl(Meta)+O shortcut. You can also drag&drop any file from the directory containing PCR files.