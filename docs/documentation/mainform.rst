.. _Main Form:

Main form
#########

Introduction
============

The **GetControl** window contains several main parts: `Menu and Toolbar`_, `File list`_, `Information pages`_, `FP applications`_, and `Supplementary files`_, which are described in more detail below. The main windows appear on the application launch.

.. figure:: ./img/mainform-empty.jpg
    :width: 80%
    :align: center

    Main GetControl window. Green - `Menu and Toolbar`_, Red - `Information pages`_, Blue - `File list`_, Pink - `FP applications`_, Black - `Supplementary files`_

First step
----------

To start using the **GetControl**, go to the menu ``File -> Open Directory``, use the ``Ctrl(Command)-O`` or ``Drag&Drop`` any file from your working directory. The application will search all the PCR files in the selected directory, sort them in the `File list`_ and automatically load the info from the first PCR file.

.. _Menu and Toolbar:

Menu and Toolbar
================

Menu and Toolbar provide quick access to the program functions, visualisations and tools.

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
    The menu for macOS is located in the system menu. The :ref:`Preferences <Preferences>` and *About* dialogs are located under **GetControl** main menu item as usual for the system.

.. tip::
    When you use the ``Backup structure`` function with the enabled **Ask for name when backup?** (see :ref:`Preferences<Preferences>`), it works like a backup and rename together.

.. _File list:

File list
=========

In the *File list*, all PCR files found in the working directory are listed. You can select the file by the mouse click or by using the keyboard arrows. By right-click, you will have the access to the selected functions dedicated to the currently selected PCR file (``Delete file``, ``Clear supplementary files``, ``Reload``, ``Backup``, and ``Rename structure``).

You can change the order of the PCR file by the ``click&drag`` method. It is particularly useful when the searched order is not the one you like. The order should be preserved even when you do the ``Reload directory``, but it will be lost when you load the different directory and come back.

It is possible to select multiple files by holding *Ctrl* or *Command* and clicking. This is useful when you want to export ``Fraction and Cell for selected``.

.. tip::
    The current working directory is shown in the status bar of the main application window.

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

In the **Profile parameters** tab, there are extracted some useful information about the profile for each phase as profile type, IRF used, profile parameters, ... If the preferred orientation correction is used the parameters are also listed here. If microstructure is calculated, a summary is provided for size and strain broadening.

If the ``Ana`` parameter is set to **1**, then also info about the sharpest reflection is extracted together with the *Effective number of reflections*.

.. figure:: ./img/profileparameters.jpg
    :width: 80%
    :align: center

    Profile parameters tab

Information is sorted by phases and colourised with the same pattern as in the `Phases info`_ tab. In a multi-pattern setting, the info for each pattern is connected with each phase.

.. attention::
    The parameter *Effective number of reflection* should be greater than **4**, meaning that you have more than four independent reflections per intensity affecting parameter. Otherwise, your refinement result may not be accurate.

.. _Refinement summary:

Refinement summary tab
----------------------

**Refinement summary** tab shows the information about the *Chi2*, number of parameters and some info about the last refinement run.

If parameter ``Mat`` is set to **1**, the list of correlated parameters is listed (only for correlation greater than 50%).

The following block contains information about the patterns (data file, pattern contribution, zero shift, etc.). It also, for each phase, provides the R-factors and the *Scor* parameter. According to the FP manual, all the errors of the refinement should be multiplied by this *Scor* factor to obtain more realistic values. The **GetControl** can do it for you when you check out this option in the :ref:`Preferences<Preferences>`. If done so, you will see the text **(applied!)** after the *Scor* value.

.. figure:: ./img/refinementsummary.jpg
    :width: 80%
    :align: center

    Refinement summary tab

After all patterns, there is a list of potentially negative FWHM points. If your refinement is good, you should see nothing in the list.

.. _Profile viewer:

Profile viewer tab
------------------

The **Profile viewer** tab visualises the PRF file with some advanced features. In a multi-pattern setup, there is a button for each pattern on the top of the tab to switch between them. The hint on each button provides information on the pattern radiation and file name.

Braggs are coloured with the same pattern as phases in the `Phases info`_ tab. The same applies when the phase contribution is calculated.

.. figure:: ./img/profileviewer.jpg
    :width: 80%
    :align: center

    Profile viewer tab

.. tip::
    To get the contribution for each phase, set the ``Ipr`` parameter to **3**. Then launch the FP refinement and when you reload the file the application will automatically search for the phases contributions and will load them.

If you hang over the Bragg positions, a hint pops up to show the extensive information gathered from the OUT and PRF files about the pointed position.

.. figure:: ./img/profile-braggs.jpg
    :width: 60%
    :align: center

    Bragg information

Axis manipulations
^^^^^^^^^^^^^^^^^^

At the bottom of the tab, there is a drop-down menu to adjust the X and Y axis. For the X-axis, there is an option to plot in the original (**2Theta**/**TOF**), **d** or **Q** spacing. For the Y-axis, there is an option for the **original**, **relative**, **relative with zero=Ymin** and **Square root**. Next to those options, there are informative labels showing the position of the cursor in various units.

.. tip::
    To easily compare the multi-pattern setup, set the X-axis in **Q** or **d** spacing and the Y-axis to **relative with zero=Ymin**. Then, you can switch between patterns and see how each pattern contributes to the same reciprocal space region.

Chart navigation
^^^^^^^^^^^^^^^^

The navigation on the chart is a bit different from the *Winplotr* navigation. Below is a description of the possible manipulations:

- **ZOOM IN**
    Use the mouse ``drag&drop`` technique from *left-to-right* and from *top-to-bottom*, in other words, in diagonal to **down-right**.
- **ZOOM OUT**
    This means undo-zoom, use the mouse ``drag&drop`` technique in the opposite direction than *ZOOM IN*. It means diagonal to **top-left**. The single **left-click** does the same job.
- Chart **positioning**
    Use the mouse **right** ``click&drag`` method to move the chart freely in any direction.

.. note::
    There is no **double-click** routine for *Winplotr*. *Undo-zoom* is done by a simple click.

Chart export
^^^^^^^^^^^^

You can export charts in several ways. You can save the **Profile viewer** screen as a *picture* of various formats (see `Menu and Toolbar`_ -> ``Export``). You can save the data as *SXY file* (header describes the meaning of the columns) and import it to your favourite data plotting software (see `Menu and Toolbar`_ -> ``Export``). Or you can use Python script - **SXY plotter**.

.. figure:: ./img/sxy-plotter-example.jpg
    :width: 90%
    :align: center

    Example of the *SXY plotter* output

Measuring tool
^^^^^^^^^^^^^^

When the **Profile viewer** is active tab, you can use the **Measuring tool**, which allows you to measure along X, Y or general directions. The info about the measured distances is visualised on the measuring tool form.

.. figure:: ./img/profile-measuring.jpg
    :width: 70%
    :align: center

    Measuring tool example

.. note::
    The **ZOOM** options will not work when *Measuring form* is visible. You need to use the **Ctrl** to enable it within the measuring mode.

.. _Microstructure viewer:

Microstructure viewer tab
-------------------------

The **Microstructure viewer** tab is only visible when the microstructure effects are calculated, and the IRF (instrument resolution file) is provided. The basic setting is to plot the Williamson-Hall (WH) plot. In the top part of the tab, you can select the appropriate phase or pattern. If the phase or pattern name is *grey*, it means that there is no microstructure implemented in the refinement for this phase/pattern.

.. figure:: ./img/microstructureviewer.jpg
    :width: 80%
    :align: center

    Microstructure viewer tab

.. note::
    **Microstructure viewer** visualise the content of the MIC file created during refinement.

The WH plot can be plotted using the Python script - **MIC plotter**.

.. _FP applications:

FP applications
---------------

The panel provides access to a quick launch of the selected *FullProf* applications.

- **FullProf** (shortcut **F9**)
    Launching the FullProf (*wfp2k*) with the selected PCR file.
- **EdPcr** (shortcut **F10**)
    Open the selected PCR file with the *EdPcr* tool
- **WinPlotr** (shortcut **F11**)
    Opens the PRF file with the *WinPlotr* tool. This tool is not available on *Unix-based* systems.
- **WinPlotr2006**
    Opens the PRF file with the *WinPlotr2006* tool.
- **Symmcal**
    It opens the *Symmcal* tool for information about the space groups
- **MagSymmCal**
    It opens the *MagSymmCal* tool for information about the magnetic space groups
- **powderpat**
    It opens the *Powder Pattern Calculation* tool. It can import CIF files and simulate the powder patterns for various settings and radiations, etc.

.. caution::
    Those tools are available only when the *FullProf* path is properly set up in the :ref:`Preferences<Preferences>`.

.. _Spplementary files:

Supplementary files
-------------------

The **Supplementary files** button bar provide an easy access to the various supplementary files created during the refinement. You can edit them or launch additional tools (FPStudio, GFourier, ...) with the proper input files and perform further analysis. The buttons act as a single buttons, or by clicking a drop-down menu that appears for a more concrete action selection. If the button name is *grey*, it means that the supplementary file of the particular kind doesn't exist.

- **PCR** (shortcut **F6**)
    It opens the selected PCR file in the editor
- **OUT** (shortcut **F7**)
    It opens the selected OUT file in the editor
- **SUM** (shortcut **F8**)
    It opens the selected SUM file in the editor
- **DIS**
    If the distances/angles or BVS are calculated, it opens the results in the editor
- **MIC**
    If microstructure files are created, then it allows them to open, and if the 3D visualisation is initiated, then it opens it in the *VESTA* viewer. The MIC files are provided for each phase.

.. tip::
    To enable the 3D visualisation of the microstructure, you need to put the parameter ``Jvi`` to **5** and have the IRF file defined.

- **FST**
    The **FPStudio** files can be opened and modified in the editor or directly opened by the *FPStudio* tool to visualise. The FST files are provided for each phase.
- **INP**
    The **GFrourier** files can be opened and modified in the editor or directly opened by the *GFourier* tool to analyse. If the analysis is done, there will be access to the output or to the Fourier maps visualisation.
- **CFL**
    The files for **BondStr** tool. You can edit the input files in the editor or open them directly with the *BondStr* tool. If the analysis is done by the tool, there will be access to the results and visualisation (BVS maps, etc.).
- **CIF**
    If CIF files is created and viewer provided (see :ref:`Preferences<Preferences>`) then there is an access to directly open the created CIF file.
- **Dys**
    If the input files for Dysnomia (MEM analysis) are created, there is access to open the input files in the editor to launch the analysis and, after the analysis is done, to visualise the output and Fourier maps.

.. tip::
    To enable the creation of the Dysnomia (MEM analysis) input files, set the parameter ``Fou`` to **6**.

- **CC**
    The *crystallographic calculations* input files. First, you need to create the CC files for your PCR file. It will create the text file with some basic input for each phase. Then, you can launch the *cryscalc* tool on this input or edit and adjust the input. There are preset options from which some of them are disabled (see description inside the input file). The *cryscalc* tool can calculate useful crystallographic information as absorption per unit cell, show the scattering coefficients for atoms, and many more. Please consult the *help* of the tool for more information.




