<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
 "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
 <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
 <link rel="stylesheet" type="text/css" media="screen" href="meredit.css"/>
 <meta name="keywords" content="neutron, diffraction, powder, cryostat, furnace, magnetism, structure, magnetic structure, experimenet"/>
  <meta name="robots" content="all"/>
  <meta name="revisit-after" content="30 days"/>
  <meta name="identifier-url" content="http://neutron.ujf.cas.cz/meredit/"/>
  <meta name="copyright" content="&copy; 2009 - 2010 WildRam"/> 
 <link rel="shortcut icon" type="image/x-icon" href="favicon.ico"/>
 <link rel="icon" type="image/png" href="favicon.png"/> 
 <?php include("functions.php") ?> 
 <title>MEREDIT - parameters</title>
</head>
<body>
 <h1>MeReDit - parameters</h1> 
 <div id="main">
 <h3>Monochromators</h3>
 <p>
  Adjustable lift system is used to hold the monochromators. There are three positions available in the lift. One slot is still empty and will be used in the future. Two other slots are occupied with:
 </p>
 <ul> 
  <li>
   Bent three silicon single crystals in special bending holder. Value of bent is adjustable. The best result concerning intensity and peak shape is at the bent to 140&micro;m. Symmetric reflection is from planes (422). By rotation the crystals about 10&#176; is possible to have asymmetric reflection (311) satisfying the Bragg's condition. So this monochromator provides two different wavelength.
  </li>
  <li>
   <a href="">Three mosaic copper<img src="img/mono_cu.png" alt="Cu monochromator"/></a> crystals adjusted to focus vertically. This monochromator provide one wavelength with reflection (220).
  </li>
 </ul>
 
 <h3>Wavelength and secondary beam parameters</h3>
 <br/>
 <table cellpadding="0" cellspacing="0" border="1">
 <col width="18%" />
 <col width="10%" />
 <col width="12%" />
 <col width="20%" />
 <col width="15%" />
 <col width="15%" />
  <tbody>
    <tr valign="top">
      <td>Monochromator</td>
      <td>Reflection</td>
      <td>Wavelength</td>
      <td>Minimum &Delta;d/d <br />(x10<sup>-3</sup>)</td>
      <td>Neutron flux <br />(n.cm<sup>-2</sup>.s<sup>-1</sup>)</td>
      <td>Beam size</td>
    </tr>
    <tr valign="middle">
     <td align="left" rowspan="2">3 bent Si single-crystals</td>
     <td>(422)</td>
     <td>1.271 &Aring;</td>
     <td>3.9 (at 56&#176; 2&theta;)</td>
     <td>&#126;8.8x10<sup>5</sup></td>
     <td><a href="">2x4 cm<sup>2</sup><img src="img/flux_si422.png" alt="Flux of Si(422)" /></a></td>
    </tr>
    <tr valign="middle">
     <td>(311)</td>
     <td>1.877 &Aring;</td>
     <td>4.4 (at 59&#176; 2&theta;)</td>
     <td>&#126;8.6x10<sup>5</sup></td>
     <td><a href="">2x4 cm<sup>2</sup><img src="img/flux_si311.png" alt="Flux of Si(311)" /></a></td> 
    </tr>
    <tr valign="middle">
     <td align="left">3 mosaic Cu crystals</td>
     <td>(220)</td>
     <td>1.460 &Aring;</td>
     <td>4.9 (at 59&#176; 2&theta;)</td>
     <td>&#126;3.6x10<sup>6</sup></td>
     <td><a href="">4x4 cm<sup>2</sup><img src="img/flux_cu220.png" alt="Flux of Cu(220)" /></a></td>
    </tr>
  </tbody>
 </table>
 <h3>Other parameters</h3>
 <ul>
  <li>2&theta; range form 2 to 148&#176;</li>
  <li>adjustable slits in the full range of beam size</li>
  <li>step size down to 0.02&#176; in 2&theta;</li>
 </ul>
 <h3>Files to download</h3><a name="download"></a>
 <p>Here you can find the IRF (Instrument Resolution Files) for the <a href="http://www.ill.eu/sites/fullprof" title="FullProf Suite - refinement program" onclick="window.open(this.href); return false;">FullProf</a> refinement program.</p>
 <table  cellpadding="0" cellspacing="0" border="1">
  <tbody>
   <tr>
    <td></td>
    <td>Si(422)</td>
    <td>Si(311)</td>
    <td>Cu(220)</td>
   </tr>
   <tr>
    <td>IRESO=1</td>
    <td><a href="download/si422_ireso1.irf" title="Si(422) irf file for IRESO=1">si422_ireso1.irf</a></td>
    <td><a href="download/si311_ireso1.irf" title="Si(311) irf file for IRESO=1">si311_ireso1.irf</a></td>
    <td><a href="download/cu220_ireso1.irf" title="Cu(220) irf file for IRESO=1">cu220_ireso1.irf</a></td>
   </tr>
   <tr>
    <td>IRESO=4</td>
    <td><a href="download/si422_ireso4.irf" title="Si(422) irf file for IRESO=4">si422_ireso4.irf</a></td>
    <td><a href="download/si311_ireso4.irf" title="Si(311) irf file for IRESO=4">si311_ireso4.irf</a></td>
    <td><a href="download/cu220_ireso4.irf" title="Cu(220) irf file for IRESO=4">cu220_ireso4.irf</a></td>
   </tr>
  </tbody>
 </table>
 </div> <!-- div main -->
 
 <?php
 include("sidebar.php");
 ?>

</body>
</html>
