.. GetControl documentation introduction page

.. Links:
.. _FullProf Suite: https://www.ill.eu/sites/fullprof/
.. _releases: https://github.com/wildrams/getcontrol/releases/latest
.. _Win32: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.exe?raw=true
.. _Win64: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64.exe?raw=true
.. _Lin32: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl?raw=true
.. _Lin64: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl-x86_64?raw=true
.. _Mac64: https://github.com/wildrams/getcontrol/releases/latest/download/GetControl.dmg?raw=true

.. _introduction:

Introduction
############

Installation
============

There is no need for installation. For **Windows** and **Linux**, there are single-file executables. Just copy the executable file to the location of your choice and launch it. For the **macOS**, the image disk (DMG file) is available (see Download_ section).

.. caution::
    Copy the executable to the folder to which you have writing permission. Don't use the system folders. Try not to use the directory names with spaces.

The program tries to search for the *FullProf* path automatically. If not found or you use a nonstandard path, please set it in the :ref:`Pref->General <General setup>` setup tab.

Additional 3rd party software facilitating the analysis (*Dysnomia* - MEM) and visualisation (*VESTA* - CIF viewer) can also be linked. The links to the software webpages are provided by clicking the appropriate labels in the :ref:`Pref->General <General setup>` setup tab.

.. tip::
    For a visualisation of the refinement results, there is no need to have *FullProf* installed. You will need it only when you want to perform further calculations.

.. _SettingStorage:

Configuration storage
=====================

The program stores its settings in the local *config* directory. The path depends on the system and is the following

* Windows 🪟 ``c:\Users\Profile_name\AppData\Local\GetControl``
* Linux 🐧  ``~/config/GetControl``
* macOS 🍏 ``~/Library/Application Support/GetControl``

This directory can be accessed quickly via :ref:`Pref->General <General setup>` setup tab, and click on the *Open directory* button side by the *LOG files* info.

Update
======

An automatic update check is set on by default (can be switched off in :ref:`Pref->General <General setup>` setup tab). After each program launch, a small file (in the order of 50 kB) with the version info is downloaded from the server and compared with the local one. No local data are sent to the server.

Only the major versions are released. The *builds* are distributed through the *auto-update* feature.

.. note::
    The file downloaded within the auto-update also contains the information about the hash-sum for each executable and "What is new" information. Especially useful when only the builds are distributed.

License
=======

**GetControl** is developed as **freeware**. The licence can be accessed `here <https://raw.githubusercontent.com/WildRams/getcontrol/main/LICENSE>`__. I keep the source closed for the moment as I develop it mainly for myself. I had no initial intention to share it, but some of my colleagues found it very useful. So you are free to use it if it is found appropriate for you.

.. _Download:

Download
========

Check the releases_ section or follow the link below for the direct download of the appropriate file for your system.

+------------------------+----------+----------+
|                        |  32-bit  |  64-bit  |
+------------------------+----------+----------+
| Windows (win widgets)  | `Win32`_ | `Win64`_ |
+------------------------+----------+----------+
| Linux (gtk2 widgets)   | `Lin32`_ | `Lin64`_ |
+------------------------+----------+----------+
| macOS (DMG image disk) |          | `Mac64`_ |
+------------------------+----------+----------+

.. _Contact:

Contact
=======

Přemysl (Premek) Beran at prema@email.cz
