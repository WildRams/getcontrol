Main form
#########

Introduction
============

The **GetControl** window contains several main parts: `Menu and Toolbar`_, `File list`_, `Information pages`_, ... which are described in more detail below. The main windows appear on the application launch.

.. figure:: ./img/mainform-empty.jpg
    :width: 80%
    :align: center

    Main GetControl window. Green - `Menu and Toolbar`_, Red - `Information pages`_, Blue - `File list`_, Pink - FP applications, Black - Additional files

To start using the **GetControl**, go to the menu ``File -> Open Directory``, use the ``Ctrl(Command)-O`` or ``Drag&Drop`` any file from your working directory. The application will search all the PCR files in the selected directory, sort them in the `File list`_ and automatically load the info from the first PCR file.

.. _Menu and Toolbar:

Menu and Toolbar
================

Menu and Toolbar provides a quick access to the program functions, visualisations and tools.

Most of the Menu items have their corresponding Toolbar buttons. Below is the list with a quick explanation:

- **File**
    * ``Open directory`` - it searches the path to your working directory
    * ``Reload folder`` - it again searches for the PCR file in the directory (use when you copy/add/delete the PCR files)
    * ``Recent directories`` - the list of 10 previously used directories
    * ``Save`` [1]_ - it saves text info from phases/profile/refinement tabs or a SXY [2]_ file of the pattern tab or the picture of the pattern tab
    * ``Delete file`` - it deletes the PCR file and all supplementary files; the form when you can filter by extension what to delete will popup
    * ``Editor`` - it opens the internal or external (see :ref:`Preferences<Preferences>`) editor
    * ``New instance`` [3]_ - it opens the new instance of the **GetControl** application
    * ``Exit`` [3]_ - it closes the application
- **Edit**
    * ``Clear supplementary files`` - it will allow you to delete selected (the new form when the filer can be selected will pop-up) supplementary files for the selected PCR file (it can free the space on your disk)
    * ``Clear supplementary files for ALL`` - the same as above but for all the PCR files in the working directory
    * ``Backup structure`` - it backups the selected PCR file together with the supplementary files by adding `-backup` to their file name; see :ref:`Preferences<Preferences>` to allow the selection of the *suffix*
    * ``Rename structure`` - it renames the select PCR file with all supplementary files
- **View**
    * ``Phases info`` - it shows the `Phases info`_ tab
    * ``Profile parameters`` - it shows `Profile parameters`_ tab
    * ``Refinement summary`` - it shows `Refinement summary`_ tab
    * ``Profile viewer`` - it shows `Profile viewer`_ tab
    * ``Microstructure viewer`` - it shows `Microstructure viewer`_ tab
    * ``Reload`` - it reloads structure info from the selected PCR file
- **Export**
    * ``"Phases info" TAB separation`` [4]_ - it copies to the clipboard information about all the phases from the `Phases info`_ tab; atomic positions are separated by TAB
    * ``"Phases info" in Latex`` [4]_ - it exports to the clipboard information about all phases from the `Phases info`_ tab in the Latex table format
    * ``Fraction and Cell for active`` [4]_ - it copies to the clipboard the name, fraction and cell parameters separated by TAB for all the phases in the one currently selected PCR
    * ``Fraction and Cell for selected`` [4]_ - it copies to the clipboard the name, fraction and cell parameters separated by TAB for all the phases in the all selected PCR; easy to paste to worksheet-like software for quick plotting of the cell parameter evolution
    * ``Python script for SXY plotter`` [4]_ - it opens the form when you can adjust the command for the Python script, which allows you to plot the pattern(s)
    * ``Python script for MIC plotter`` [4]_ - it opens the form when you can adjust the command for the Python script, which allows you to plot the Williamson-Hall plot to visualise the microstructure
- **Tools**
    * ``Measure distance`` - the tools to measure different distances on the pattern chart; an additional form opens to select the measurement along various axes and visualise the results
    * ``Open Terminal`` [3]_ - it will try to open the default system terminal
    * ``Open COD`` [3]_ - it opens the web page of the Crystallographic Open Database (COD)
- **Help**
    * ``Check for update`` - it opens the dialogue for checking the availability of the new version and the updating process
    * ``What is new`` - it opens in the editor the update information changelog
    * ``FullProf News`` - it opens in the editor the FullProf changelog
    * ``FullProf Manual`` - it opens the FullProf manual (PDF file from 2000)
    * ``Write debug log`` - it enable to write the debug log in the :ref:`Setting storage <SettingStorage>` directory

.. [1] **SXY** is a single-X and multi-Y file format
.. [2] The save sub-menu buttons are located at the right part of the toolbar, but they have the same icon
.. [3] It exists only in **Menu**
.. [4] In the Toolbar, it is hidden under the **Export option** button

.. note::
    Menu at macOS are located at the system menu. The :ref:`Preferences <Preferences>` and *About* dialogs are located under **GetControl** main menu item as usual for the system.

.. tip::
    When you use the ``Backup structure`` function with the enabled **Ask for name when backup?** (see :ref:`Preferences<Preferences>`), it works like a backup and rename together.

.. _File list:

File list
=========

In the *File list*, all PCR files found in the working directory are listed. You can select the file by the mouse click or by using the keyboard arrows. By right-click, you will have the access to the selected functions dedicated to the currently selected PCR file (``Delete file``, ``Clear supplementary files``, ``Reload``, ``Backup``, and ``Rename structure``).

You can change the order of the PCR file by the ``click&drag`` method. It is particularly useful when the searched order is not the one you like. The order should preserve even when you do ``Reload directory``, but it will be lost when load the different directory and come back.

It is possible to select multiple files by holding *Ctrl* or *Command* and clicking. This is useful when you want to export ``Fraction and Cell for selected``.

.. tip::
    Current working directory is shown in the statusbar of the main application window.

.. note::
    In macOS, the multi-file selection with Command pressed works properly **only** when selection starts from the bottom of the list.

.. _Information pages:

Information pages (TABs)
========================

.. _Phases info:

Phases info tab
---------------

In the **Phases info** tab, the application collects various information about all phases. If **OUT** and **SUM** files exist the *errors*, *phase fraction*, *density*, *R-factors*, *site multiplicity*, etc. are extracted as well and properly shown. The unit cell composition and site fractions are also calculated.

The info for each phase is coloured based on the preselected pattern (see :ref:`Preferences<Preferences>`). If it is too long, it can be folded on the phases or atoms level (click the small rectangles on the left side of the text).

.. figure:: ./img/phasesinfo.jpg
    :width: 80%
    :align: center

    Phases info tab

.. tip::
    If you want to calculate the composition in the *formula units*, provide the number of formula units (Z value -> ``Z=x``) in the PCR file just behind the phase title

    .. parsed-literal::

        !-------------------------------------------------------------------------------
        !  Data for PHASE number:   1  ==> Current R_Bragg for Pattern#  1:   4.7090
        !-------------------------------------------------------------------------------
        Fe2P - structural - 1 **Z=3** magph2
        !
        !Nat Dis Ang Jbt Isy Str Furth        ATZ     Nvk More
          8   0   0   0   0   0   0        423.0645   0   0

.. _Profile parameters:

Profile parameters tab
----------------------

.. _Refinement summary:

Refinement summary tab
----------------------

.. _Profile viewer:

Profile viewer tab
------------------

.. _Microstructure viewer:

Microstructure viewer tab
-------------------------




