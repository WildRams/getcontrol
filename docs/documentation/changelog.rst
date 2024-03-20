.. _WhatIsNew:

What is news
############

Compiled with `CT <https://www.pilotlogic.com>`__ 8.3

All suggestions are welcomed at prema@email.cz

Version 0.8
^^^^^^^^^^^

Version 0.8.0 build 2
-----------------------------------------------
:Date: 20/03/2024

- The old PCR format created out of the DICVOL program was not read properly; now corrected (thanks, Stefan, for reporting)
- Creating "cryscalc" input file via CC was not working when there were no atoms in the phase; not corrected
- Some minor adjustments to the layout
- First draft of documentation published on `<https://wildrams.github.io/getcontrol/>`__ (link added in the About form)

Version 0.8.0 build 1
-----------------------------------------------
:Date: 28/02/2024

- Updated the Python scripts (SXY and MIC plotter) to use UTF8 charset
- Not possible to change the axes title is corrected
- Corrected the wrong formatting of the edited hints file
- Some improvements of the FP hints strings
- Corrected wrong reading of the atomic parameters when using atomic types with negative signs
  (ex. O-2); thanks, Stefan, for reporting
- Changed the colours for the MIC tab for better visibility; it is possible to reset the marks' colour
- The font of the FP hints is set to one with the fixed pitch for better formatting
- Added an extraction of the negative FWHM points from '*'.out file; the list of points is shown
  at the "Refinement summary" tab at the end (folding is available)
- Added the site fraction (0-1 notation) for each atom (suggested by Stefan); useful when not the full site
  or mixed-site occupancy
- Double-click on the `*`.PCR file in the list opens the PCR file in an editor (suggested by Vitalii)
- When you provide the number of formula units on the line with the phase title, GC can calculate the composition
  based on the chemical formula, not by the unit cell; put "Z=x" where x is your formula unit number; this will not
  affect the FP refinement or VARY and FIX commands; for example: My new phase Z=4 VARY xyz FIX b; note capital Z
- A link to the license was added to the About form

Version 0.7
^^^^^^^^^^^

Version 0.7.2 build 2
-----------------------------------------------
:Date: 01/08/2023

- Ctrl+T (open terminal) shortcut didn't work when the cursor in editors now corrected
- Splitter position not correctly recovered when in high-DPI now corrected
- In Preferences, the tab Colour schema was renamed Colour/layout. You can adjust the size of the button and menu
  icons (normal/medium/large) and also the font size for all hints (useful for long FP hints in high-DPI).

Version 0.7.2 build 1
-----------------------------------------------
:Date: 24/07/2023

- New bottom toolbar was added to access the "cryscalc" tool (CC). First, you create a `*`_cc_`*`.cfl file, which can
  be edited, and then you launch it, and the result file (`*`.cci) is automatically opened. Some more hits for
  cryscalc are shown. The file can be modified as necessary. Cryscalc can be launched directly from
  the internal editor when `*`_cc_`*`.cfl file is active.
- Open terminal in the working directory menu was added to the Tools menu
- Open COD (Crystallographic Open Database) link was added to the Tools menu
- Mouse position info now shows when over the WH plot
- Some small improvements in the script hints and layout 

Version 0.7.1 build 1
-----------------------------------------------
:Date: 10/07/2023

- wrong pattern plotting by the SXY plotter in the multi-pattern mode in some
  particular settings was corrected
- when backing up the structure, the Dysnomia outputs were copied wrongly, now corrected
- Microstructure plotter (Python script) was added. It can be accessed by the Export menu.
  The form is similar to the SXY plotter one. The script can be adapted if necessary.
- update of the SXY plotter script
- better identification of the terminal application on Linux (used in Python script export)
- a lot of small enhancements in the layout

Version 0.7.0 build 1
-----------------------------------------------
:Date: 06/02/2023

- X-axis reset from Q or d to Theta/TOF after the change of the PCR file corrected
- errors for C4-C6 were not read - corrected
- update of the export to the SXY file when there is no pattern contribution, now the Python SXY-plotter
  should show all patterns even if some phases don't contribute.
- some update in the summary info when magnetic phases are used
- the project was moved to Github as there will be disruption of the old server for external users
- update the Linux and Windows updater to version 0.3.1.1

Version 0.6
^^^^^^^^^^^

Version 0.6.2 build 2
-----------------------------------------------
:Date: 06/02/2023

- wrong read of the big negative hkl indexes from PRF (example "-14-10  5") is corrected
- ad-hoc signature of macOS bundle
- some small improvement in FP hints

Version 0.6.2 build 1
-----------------------------------------------
:Date: 06/02/2023

- improvement of the Drag&Drop in PCR list (dragged file stays in focus)
- open the Linux terminal in the Python export should work now
- Bragg highlighter works on all platforms; some settings added to the preferences
- Linux about form show now the full description
- in About form, the link to the download web page was added
- better extraction of the information about the magnetic space group
- phase name was not properly shown when COMMANDS were used
- some more improvements in the background extraction functions

Version 0.6.1 build 1
-----------------------------------------------
:Date: 11/11/2022

- multi-pattern TOF PCR loaded wrongly Dtt1 and Dtt2 parameters for Pattern#1 and Pattern#2,
  the other patterns were not affected; this error is now corrected (thanks, Johan, for reporting)
- update of the editor FP hints
- for Jbt=10 the magnetic and nuclear R-factors are read from `*`.out file instead of `*`.sum
- when Dysnomia is created, the additional `*`.vesta file combining both the density map and
  CIF file is created, accessible through the Dysnomia menu (Density map with structure)
- microstructure information is read from the `*`.mic file written in the Profile tab
- if the microstructure model is used, the Williamson-Hall plot is shown in the new tab,
  some more info and adjustments can be made on the new tab; the tab is visible only when there is
  none-zero microstructure

Version 0.5
^^^^^^^^^^^

Version 0.5.1 build 2
-----------------------------------------------
:Date: 22/09/2022

- shortcuts for a jump to phases in Editor form updated to Alt+1-9 (some collisions found for F-keys)
- shortcut for FullProf manual changed on Wind/Linux to Ctrl+Shift+M (Ctrl+M is for measuring tool)
- conversion to Q and d for TOF data didn't work when not IRF used and Fp version > 7.30; now
  it should be corrected, but some more tests will be in the future (thanks Johan for reporting)

Version 0.5.1 build 1
-----------------------------------------------
:Date: 14/09/2022

- folding in the information tabs was added to handle long lists better
- the position of the cursor and the folding are preserved for reloading on the same CPR
- separation lines in the phase info tab were replaced because they are not visible on all OSs the same way
- some minor updates in the layout and reading process

Version 0.5.0 build 1
-----------------------------------------------
:Date: 22/04/2022

- update server changed to HTTPS, error during auto-update, added OpenSSL 1.1.1m libraries
  to executables (Win, Linux) and the bundle (macOS), now the update should work again
- when reloading the directory and an error occurred, the old PCR was still loaded - corrected
- propagation vector/composition of value 2/3 was shown as 0.2 - corrected
- adjustment of SySin systematic shift for the phase contributions was wrong in some cases - corrected
- in some cases, the conversion to Q for multidetector TOF didn't work properly - corrected
- not possible to select FP path on macOS - corrected
- Shortcut for a jump to phases in Editor form updated to Alt+F1-F12 (it collided with MainForm tab change)
- some adjustments for dark mode on macOS and Linux (on Windows still doesn't work)
- wrong phase name jump menu in Editor for multipattern files corrected
- some layout improvements
- new measurement tool added (Ctrl+M)
- update of the FP hints

Version 0.4
^^^^^^^^^^^

Version 0.4.9 build 1
-----------------------------------------------
:Date: 15/11/2021

- updated the Python sxy-plotter script to better handle the PCRs with Jbt=±10 + some updates for Python compatibility
- new default colour schema (need reset in Setup if you want to update), which works better in dark theme
- the chart and series lines thickness adjusted based on DPI, should look better on HiDPI screens (test and report)
- better description of the magnetic contributions, extraction of the propagations vectors and print on the phase info tab
- some update on the phase info tab
- export menu also added to the main menu for better visibility
- updated FullProf hints
- in Editor added some new buttons for folding and unfolding and jumping to the phase info for PCR files
- updated reload function, which should keep the scroll on the page properly now

Version 0.4.8 build 2
-----------------------------------------------
:Date: 24/10/2021

- corrected error introduced in 0.4.7.3 when the export to `*`.sxy doesn't saved Bragg reflections
  and Python plot didn't work properly (thanks Cecilia for reporting)

Version 0.4.8 build 1
-----------------------------------------------
:Date: 20/10/2021

- not able to launch on macOS BigSur sorrected (thanks Priyank for report and tests)
- Update for macOS works now. It downloads GetControl.dgm package which is opened when click Install.
  So you can use drag&drop to Applications as usual. (thanks Priyank for test)
- in Preferences added link to FullProf and VESTA web sites (same as for Dysnomia)
- link should work also on Linux now
- download progress bar during update download should work on Linux now
- some further minor changes

Version 0.4.7 build 3
-----------------------------------------------
:Date: 27/09/2021

- corrected error when Braggs were not loaded when Ycalc=0 in the case of Jbt=10 on Windows systems

Version 0.4.7 build 2
-----------------------------------------------
:Date: 23/09/2021

- corrected error when About dialog was initiated
- corrected error when position of the splitter was not properly handled when scaling was different
  from 100% (thanks Cecilia to report)

Version 0.4.7 build 1
-----------------------------------------------
:Date: 22/09/2021

- not accessible Setup and Exit menu item are again available (thanks Cecilia for reporting)
- write Debug Log menu off by default
- the Bragg hint info in the chart were rewritten and consolidated for better experience
- Setup renamed to Preferences
- for macOS the About and Preferences menu are placed as default by system under GetControl menu item
- some small improvements everywhere

Version 0.4.6 build 1
-----------------------------------------------
:Date: 28/07/2021

- some minor layout update
- Editor - added function to run the dummy cycle (set Aut and number of refined parameters to zero) with shortcut
  Shift+F9. It is useful when you manually adjust the parameter and want to see the effect on fitting. The dummy cycle
  is run automatically after.
- Editor - status of the parameter 'Aut' is shown and can be switched on and of by the button. Switching it off 
  doesn't mean directly not refine any parameter. It is useful when after the dummy cycle, you want to switch 
  the refinement back on.
- Editor - removal of the old Chi2 value stored in PCR and used to check if the refinement is better than 
  the last one. It can create unnecessary warnings, which can be overcome by deleting the old value.   

Version 0.4.5 build 5
-----------------------------------------------
:Date: 19/04/2021

- the backup/clone now use '-backup' instead of '_bakcup' as an appendix; there were some interference during the file search
- the FP news short-cut changed to Alt+Ctrl(command)+M, the FP manual is still Ctrl(command)+M
- in the internal editor menu 'Help' item added when one can access the FP news and manual (short-cut the same as for the main form)
- updated FP-hints; if someone edited it before using the 'Special' menu in the editor, then you need to delete the FP-hints.txt file form
  your config directory to see the new one; if you have made some serious update of the hints and you want to share it
  then drop me an email (thanks)

Version 0.4.5 build 4
-----------------------------------------------
:Date: 25/03/2021

- corrected reading of `*`.PCR and `*`.pcr in Linux
- corrected error when it was not possible to remove external editor from Setup form (thanks to Stefan from FRMII)
- corrected pattern shift for phase contributions when SySin or SyCos is used 
- increased the number of decimals on 2Theta show bellow the chart from 2 to 4 

Version 0.4.5 build 3
-----------------------------------------------
:Date: 01/03/2021

- corrected reading of `*`.PCR and `*`.pcr in macOS
- corrected reading of IRF file when it contains multiple inputs
- corrected the wrong display of Q and d-spacing below the chart for TOF

Version 0.4.5 build 2
-----------------------------------------------
:Date: 11/02/2021

- corrected error of loading the cell parameters in some never version of FP
- corrected error of copy to clipboard in Python form only a part of the command in Windows

Version 0.4.5 build 1
-----------------------------------------------
:Date: 18/12/2020

- menu added to editor form
- editor PCR hints updated, you can edit and update them in Special menu
- SXY-viewer renamed to SXY-plotter, script export form was update additional parameters can be edited directly in the form
- some improvement in the sxy-plotter.py script
- layout of additional files changed, a lot of re-arrangement and improvements
- JANA support was removed as complicated to maintain all together
- access to Dysnomia (MEM analysis - use Fou=6) output was added among additional files, launching, editing and viewing sorted by phase
- the possibility of the launching of the new instance was added in the menu
- the recent open directories (10) menu and toll button were added a lot of small layout improvements

Version 0.4.0 build 2
-----------------------------------------------
:Date: 28/09/2020

- corrected error of saving SXY files under different name and with wrong header

Version 0.4.0 build 1
-----------------------------------------------
:Date: 25/09/2020

- improvements when launching external applications especially GFourier (report problems)
- lot of improvements in editor: added simple search tool (F3), hints for some parameters (more will come),
  folding in some places to shorten the long PCR files for editing (it keeps when realod), loading is much faster 
- some layout and extraction improvements for MacOS and Linux
- many of improvements on layout: HiDPI ready, dark them in Linux and MacOS works quite fine
- new application main icon and some new icons within the menu
- Python3 script for plotting of more camera ready charts available in Export menu (any script improvements appreciated)
- for MacOS version still send email for obtaining new version  

Version 0.3
^^^^^^^^^^^

Version 0.3.5 build 1
-----------------------------------------------
:Date: 27/05/2019

- wrong recalculation to Q and d for TOF using IRF file and D2TOF keyword corrected (thanks Mathias from Arhus Uni. for info)
- saving of SXY with excluded region shrink the phase contribution was corrected (thanks Mathias from Arhus Uni. for info)
- description of the magnetic moments using spherical coordinates (Jbt < 0) is now corrected (thanks Mathias from Arhus Uni. for info)
- in the Setup form (Line chart tab) added option to save the data to SXY also for excluded regions (default is False)
- some improvements in the layout
- for MacOS the auto-update still not work (check for new version works), send an email if you need the new version 

Version 0.3.4 build 1
-----------------------------------------------
:Date: 16/11/2018

- added button for quick launch of the MagSymmCal
- added extraction of the errors for magnetic moments errors from `*`.out file for Jbt=10
- improvement of error extraction routines
- Setup menu item was temporarily moved under the File menu item
- some updates of the layout 
- first compilation for the MacOS, who is interested, please send the email

Version 0.3.3 build 2
-----------------------------------------------
:Date: 6/11/2017 

- calculation of nuclear contribution for Jbt=10 for TOF again enabled (still not work for more phases)
- when the PCR is incomplete (as export from SARAh) the load is stopped without error (info shown in status bar)
- in Help menu added links to FullProf news and Manual (PDF)

Version 0.3.3 build 1
-----------------------------------------------
:Date: 3/11/2017 

- added possibility to select custom editor in Setup form
- in delete and clean up form added option for selecting and deselecting all
- disabled calculation of nuclear contribution when Jbt=10 for TOF, only magnetic contribution is shown

Version 0.3.2 build 3
-----------------------------------------------
:Date: 3/3/2017 

- wrong reading of Scor parameter when larger than 10 corrected
- if PCR file is shorter than 10 lines then program crashed - corrected
- error when empty chart accessed corrected

Version 0.3.2 build 2
-----------------------------------------------
:Date: 24/2/2017 

- unable to change colour of excluded region corrected
- no more warnings when CIF path is empty 

Version 0.3.2 build 1
-----------------------------------------------
:Date: 24/2/2017 

- open LOG folder button added
- better extraction of the space group for magnetic phases
- when save SXY you can select in setup form how to deal with multiple phase Bragg
- when save XY the `*`.sub files are stored with separate X column for each phase
- when backup or rename the check for bad characters (`*`, \, /) in file name is made; replacement by `_`
- some minor changes in layout

Version 0.3.1 build 2
-----------------------------------------------
:Date: 20/1/2017 

- corrected error of launching external applications under linux

Version 0.3.1 build 1
-----------------------------------------------
:Date: 20/1/2017 

- corrected thread update check
- information about LOG file size and clean button added to setup form
- better handling of extracted error, added option to define error length in setup form
- composition is rounded to 2 decimals if not refined
- better handling of errors extraction and formatting
- tool bar buttons hint are shown in the status bar
- improved LaTeX and TAB export including also multi-pattern information
- LaTeX export whole table for each phase

Version 0.3.0 build 5
-----------------------------------------------
:Date: 25/10/2016

- corrected error of reading of error of cell parameters form out file

Version 0.3.0 build 4
-----------------------------------------------
:Date: 3/8/2016 

- checking for update procedure in separate thread (not quenching when server not available)
- error when automatic status of check for updates in setup form was not stored was corrected

Version 0.3.0 build 3
-----------------------------------------------
:Date: 2/8/2016 

- corrected error of file load in editor (additional text from other files was added)
- adjustment of limits of Y axis when changing Y axis state
- added plot of magnetic and nuclear contribution when Jbt=10
- small improvements of layout

Version 0.3.0 build 2
-----------------------------------------------
:Date: 21/7/2016 

- cursor position show x axis in original, Q and d values in Profile view
- editor and also pcr files now can read properly the UTF8 and ANSI characters

Version 0.3.0 build 1
-----------------------------------------------
:Date: 20/7/2016 

- big improvements in extracting routines for PCR, SUM and OUT files
- number of last cycles preformed and convergence status printed in Refinement Summary tab
- lot of small improvements in layout

Version 0.2
^^^^^^^^^^^

Version 0.2.0 build 1
-----------------------------------------------
:Date: 23/12/2015

- improvements in reading of PCR files
- improved Clean/Delete procedure for FullProf (get more files)
- added option to ask for new name when use backup (Ctrl+B)
- added different colour for excluded regions
- excluded region options for colour and visibility in Setup
- internal code improvements
- Updater version 0.2.2.1

Version 0.1
^^^^^^^^^^^

Version 0.1.1 build 1
-----------------------------------------------
:Date: 22/1/2015 

- added launching of CIF and mCIF files from toolbar button (in Setup form need to specify CIF viewer)
- updated input of FullProf and Jana executables path, check is performed
- added visualization of size and strain bin files created when JVI = 5 in GFourier
- when VESTA is CIF viewer then visualization of ggrid and pgrid file form toolbar button
- automatic actualization routine added (can be disabled in Setup form)
- corrected display of file names with accents
- some minor layout changes
- Updater version 0.2.1.1 - minor improvements

Version 0.1.0 build 3
-----------------------------------------------
:Date: 1/12/2014 

- changed shortcut for cleanup routine from Ctrl-X to Ctrl+Y (conflict with "Cut" function in Editor)
- `*`.sub will be read now also for complex path with spaces and special characters
- minor changes in layout

Version 0.1.0 build 2
-----------------------------------------------
:Date: 7/8/2014 

- native compilation also for win64 and linux64
- small changes in update routines

Version 0.1.0 build 1
-----------------------------------------------
:Date: 5/8/2014 

- initial zoom issue corrected
- reading Bragg positions with excluded region corrected
- reading Bragg information from OUT corrected
- improved reading of PCR and SUM file information
- in the export of cell parameters added also the phase fraction
- export of cell parameters and phase fraction for all files in the list
- possible to change file order in list by drag&drop method
- added popup menu for file list
- added functions of delete, backup and rename of selected structure
- clean up procedure for FullProf to delete of supplementary files (it can save disk usage)
- new updater

Version 0.0
^^^^^^^^^^^

Version 0.0.9 build 2
-----------------------------------------------
:Date: 16/9/2013 

- corrected reading of the Bragg position when second Ioc=2

Version 0.0.9 build 1
-----------------------------------------------
:Date: 9/9/2013 

- corrected error shift of the PRF file due to the sysin
- each phase has coloured the Bragg positions
- small layout improvements
- path can now contain the UTF8 characters or spaces (GFourier doesn't like 
  spaces in file names but in path should be OK)
- selected zoom is now preserved when change the X axis state
- phases colour schema changed and in setup form you can put your own colours
- chart axis font label size can be adjusted in setup form
- new application icon added

Version 0.0.8 build 8
-----------------------------------------------
:Date: 27/11/2012

- maximized window position is now properly set
- some minor update when multi-pattern PRF and SUB files are loaded

Version 0.0.8 build 7
-----------------------------------------------
:Date: 21/11/2012

- shift of the PRF file for the TOF experiment corrected

Version 0.0.8 build 6
-----------------------------------------------
:Date: 21/11/2012

- shift of the PRF file is read no correctly (shift due to zero, sycos, sysin)
- added hint for the Bragg reflections (not only in the status bar)
- difference pattern normalized to the max of measured intensity, in status bar is shown in %
- background is shown on small graph with the same y-scale as main chart

Version 0.0.8 build 5
-----------------------------------------------
:Date: 6/11/2012 

- automatic detection of `*`.sub format; so the `*`.sub files are read properly
- disable FullProf when FullProf path added automatically corrected

Version 0.0.8 build 4
-----------------------------------------------
:Date: 29/6/2012 

- error of reading the multi-axial preferred orientation for multiphase system corrected 

Version 0.0.8 build 3
-----------------------------------------------
:Date: 22/6/2012 

- wrong file name when profile saved as picture corrected

Version 0.0.8 build 2
-----------------------------------------------
:Date: 22/6/2012 

- preferred orientation extraction from PCR added

Version 0.0.8 build 1
-----------------------------------------------
:Date: 14/6/2012 

- max phase count set to 15 (tell me if it is not enough)
- fixed phases colours. all the time now will have the phases the same colours in the same order.
- improved colour phase scheme in the phases info tab
- cursor position in phases tab preserved in the same position
- colour scheme added also to the profile and refinement summary tabs
- cursor position in profile and refinement summary tabs preserved in the same position
- extraction of correlated parameters if Mat=1 was added
- extraction of FP rating for each pattern added
- weight of each pattern added
- extraction of excluded region added
- extraction of other useful information from sum file when Ana=1 added

Version 0.0.7 build 1
-----------------------------------------------
:Date: 11/6/2012 

- save PRF image to wrong path corrected
- save buttons added to the main menu. Short-cuts added Ctr+S for save info, Ctrl+Alt+S for save PRF as SXY file and
  Ctrl+Shift+S for save PRF as image
- back colour of the chart was set to clear white - better when save as image
- editor window title changed to "edited_file_name - Editor"
- phases information tab make the each phases background text colour the same as the colour of pattern contribution of each phase in profile viewer

Version 0.0.6 build 1
-----------------------------------------------
:Date: 6/6/2012

- error when Res file is provided with full path corrected
- layout of the main form redesigned. New arrangement of tabs should more likely provided the overview for the
  refinement. Short-cuts for changing the tabs are Ctrl+position_of_tab
- last open file path is stored and applied when open dialogue executed
- in setup form you can find the path to the FullProf and Jana2006 installation directory which was find in the
  environments variables. If is empty you can provide it by yourself. 
- you will not be informed after GetControl execution about the missing FullProf and Jana2006 directories. Check setup 
  form if they are properly set. 
- new layout of profile viewer. Bragg, Background and Difference pattern are plotted in separate charts. You can zoom or drag
  move them like the main chart. 
- new item in the Y axis option. Relative zero = Min(Y) added. It is more reliable when you want to compare the patterns
  with different background level.
- save PRF pattern together with each phase contribution to the SXY file importable to other graphical programs
- save PRF pattern also like images of different formats
- debug log disabled by default - you can delete all the log file in the config directory 
  (in Win7 or Vista $YourProfilePath$\AppData\Local\GetControl\ in Linux /home/user_name/.config/GetControl)
- new icons in the main form added
- Linux version released and the update procedure changed to accommodate also Linux updater

Version 0.0.5 build 2
-----------------------------------------------
:Date: 7/3/2012

- resolution file info read from the file and printed
- improvement stability of read of the PCR file
- TOF profile parameters read
- wrong Q and d calculation for TOF when IRF file used corrected
- reading of number of reflection in multi-pattern multi-phase case corrected
- improved of loading magnetic phase information
- improved loading information from SUM and OUT files
- HKL information about reflections is back again
- wrong setting of position for editor window corrected
- error occurred when press F4 for reload folder content fixed
- density of each phase extracted from SUM file
- Scor factor is extracted and in setup form can be applied to the sigma values

Version 0.0.5 build 1
-----------------------------------------------
:Date: 29/2/2012 

- improvements in loading of multi-pattern multiphase pcr files
- application title = "structure_file_name - GetControl"
- the data of TOF refinement loaded in the graph with correct x axis description
- splitter added between list of files and printing results - you can adjust the size.
- improvements in reading the PCR file - now it is more stable
- debugging is back on by default for now. It creates *debug_"date and time".log* file in the config
  directory (in Win7 or Vista $YourProfilePath$\AppData\Local\GetControl\)
- setup form created and added option for save settings and position and size of each window

Version 0.0.4 build 110
-----------------------------------------------
:Date: 8/11/2011 

- fixed color for the individual phase patterns (when Ipr = 2 or 3)
- stability improvements during pcr file loading
- added button to run Powder pattern simulation from `*`.cfl and `*`.cif files (part of FullProf Suite)

Version 0.0.4 build 109
-----------------------------------------------
:Date: 14/10/2011

- added ability to reload folder for check for new pcr/m50 files (F4)
- short cuts for edit PCR/M50 (F6), OUT/M40 (F7), SUM/M41 (F8) added
- editor form reload file short cut F5
- some short cuts changed Check for update F2, Reload pcr/jana file F5
- prompt when "save as" the file what already exists
- in Editor form when reload is applied the caret stay at the same position
- short cuts added for lunching FullProf(F9), EdPCR(F10), Winplotr(F11) and Jana2006(F12)
- debugging set off by default 
- debugging log named GetControl-XXX.log (random number) can be deleted or send with debug report

Version 0.0.4 build 108
-----------------------------------------------
:Date: 19/7/2011 

- debug log added

Version 0.0.4 build 107
-----------------------------------------------
:Date: 3/5/2011 

- new editor
- new updater
- retaking the development

Version 0.0.4 build 100
-----------------------------------------------
:Date: 12/10/2010

- rebuild the data collection routine 
- editor is no more in modal mode, you are able to edit files and work with application together
- adding tab in Structure summary with profile parameters
- some more information extracted mainly in Refinement summary tab
- in profile viewer the printing in d-spacing now works
- information about each reflection is read out from `*`.out file if exported
- Save summary to the text file button save now all three tabs information together

Version 0.0.3 build 1306
-----------------------------------------------

:Date: 12/08/2010

- added routine to control the error number format as (NaN, `****`, etc.),
  in this case the number is showed as -999

Version 0.0.3 build 1305
-----------------------------------------------
:Date: 11/08/2010

- added some new buttons for lunching external applications
- again enabled auto update after file change (if cause problems please refer)

Version 0.0.3 build 1304
-----------------------------------------------
:Date: 10/08/2010

- Internet update available
