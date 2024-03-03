.. GetControl documentation introduction page

.. Links:
.. _FullProf Suite: https://www.ill.eu/sites/fullprof/
.. _releases: https://github.com/wildrams/getcontrol/releases/latest
.. _Windows 32-bit: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.exe?raw=true
.. _Windows 64-bit: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64.exe?raw=true
.. _Linux 32-bit: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl?raw=true
.. _Linux 64-bit: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64?raw=true
.. _macOS 64-bit: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.dmg?raw=true

.. _introduction:

Introduction
############

Installation
------------

There is no need for installation. For **Windows** and **Linux**, there are single-file executables. Just copy the executable file to the location of your choise and launch it. For the **macOS**, the image disk (DMG file) is available (see Download_ section).

.. warning::
    Copy the executable to the folder to which you have writing permission. Don't use the system folders. Try not to use the directory names with spaces.

The program tries to search for the *FullProf* path automatically. If not found or you use a nonstandard path, please set it in the :ref:`Preferences <Preferences>`.

Additional 3rd party software facilitating the analysis (*Dysnomia* - MEM) and visualisation (*VESTA* - CIF viewer) can also be linked. The links to the software webpages are provided by clicking the appropriate labels in the :ref:`Preferences <Preferences>`.

.. note::
    For a visualisation of the refinement results, there is not needed to have *FullProf* installed. You will need it only when you want to perform further calculations.

Setting storage
---------------

The program stores its settings in the local profile directory. The path depends on the system and is the following

* Windows 🪟 ``c:\Users\Profile_name\AppData\Local\GetControl``
* Linux 🐧  ``~/config/GetControl``
* macOS 🍏 ``~/Library/Application Support/GetControl``

This directory can be accessed quickly via :ref:`Preferences<Preferences>` (General tab), and click on the *Open directory* button side by the :guilabel:`LOG files` info.

Update
------

An automatic update check is set on by default (can be switched off in :ref:`Preferences <Preferences>`). After each program launch, a small file with the version info is downloaded from the server and compared with the local one. No local data are sent to the server.

License
-------

**GetControl** is developed as **freeware**. The licence can be accessed `here <https://raw.githubusercontent.com/WildRams/getcontrol/main/LICENSE>`__. I keep the source closed for the moment as I develop it mainly for myself. There was no initial intention to share it, but some of my colleagues found it very useful. So you are free to use it if found appropriate for you.

.. _Download:

Download
--------

.. image:: https://img.shields.io/github/v/release/wildrams/getcontrol

.. image:: https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol-x64_86.exe
.. image:: https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol.exe

.. image:: https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol-x64_86
.. image:: https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol

.. image:: https://img.shields.io/github/downloads/wildrams/getcontrol/latest/getcontrol.dmg

Check the releases_ section or follow the link below for the direct download.

* Binnary file for `Windows 64-bit`_
* Binnary file for `Windows 32-bit`_
* Binnary file for `Linux 64-bit`_
* Binnary file for `Linux 32-bit`_
* Image disk file for `macOS 64-bit`_

.. _Contact:

Contact
-------

Přemysl (Premek) Beran at prema@email.cz
