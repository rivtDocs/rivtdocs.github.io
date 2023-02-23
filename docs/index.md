---
layout: default
---

<table style="width:75%">
<colgroup>
  <col width="25%" />
  <col width="25%" />
  <col width="25%" />
</colgroup>
<thead>
<tr class="header">
  <th style="text-align: center;border:none;background-color:#959396"><a href="https://rivtdocs.net"><b>rivtDocs (installer)</b></a></th>
  <th style="text-align: center;border:none"><a href="https://rivtcode.net"><b>rivt (code)</b></a></th>
  <th style="text-align: center;border:none"><a href="https://rivtdocs.net/search"><b>rivtSearch (GitHub)</b></a></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:center;border:none"><a href="https://rivtdocs.net"><img src="./assets/img/rivtdocs03.png" width="90" height="65" /></a></td>
  <td style="text-align: center;border:none"><a href="https://rivtcode.net"><img src="./assets/img/rivt03.png" width="100" height="75"/></a></td>
  <td style="text-align: center;border:none"><a href="https://rivtdocs.net/search"><img src="./assets/img/search03.png" width="105" height="80" /></a></td>
</tr>
</tbody>
</table>

### Universally Shared Calculation Documents

## Introduction and Motivation

Engineering documents include formulas and calculations from standard sources,
calculated tables, figures and footnotes - all in addition to explanatory text.
They often need to be presented as formal letters or reports for review. Recent
developments in open source software tools dramatically improve the ease with
which these documents can be compiled and universally shared.

Engineering professions have an opportunity to produce reusable calculation
libraries that can grow and improve through open source contributions over
time. This model of shared, incremental improvement is effective in software
programming where chunks of code are repurposed and recombined. Although
software code is purely text, the application of this approach to general
engineering documents needs to be explored for its potential positive impact on
productivity and design solutions.

Many engineering technologies in the 21st century are evolving slowly. Design
procedures are often fixed for decades in standard codes, with little or no
change. Productive engineering work now lies, not so much in technological
innovation, but in understanding a range of established technologies. With
adequate understanding they can then be effectively combined into an efficient
project. Engineering calculations and drawings are the working papers that
describe how various combinations fit. Enabling cut and paste of common ideas
from previous projects, including calculations, enables an engineer to explore
more options to improve performance, reduce cost and respond to industry changes.

Many effective engineering calculation programs are available, but they include
barriers to widespread sharing. A few well known programs are listed in the
table below. The first is high initial software costs that continue because of
constantly changing file formats requiring program upgrades. In addition,
because files and interfaces are incompatible between the different programs,
multiple software purchases and learning curves are required when sharing.
Other limitations include software that does not easily produce formatted
reports, provide version control or easily integrate with external programs.

**Program Comparison**

<img src="./assets/img/table1.png" width="900" height="300" />

Taken together these limitations prevent widespread sharing of editable
calculation documents and result in nearly identical calculations being
rewritten in different ways countless times. **rivtText**, along with the
program, **rivt**, and open source stack installer, **rivtDocs**, were
developed to eliminate these barriers and promote calculation document reuse.


## **rivtDocs** Overview

The minimum software needed to run **rivt** with utf8 text output is a Python
installation and a plain text processor. The minimum version runs on mobile
platforms. **rivtDocs** is an installer that integrates five open source
programs to provide a complete document production system:

- Python 3.8 or higher (required)  
- Python libraries + **rivt** (required)
- VSCode + extensions (recommended for efficiency)
- LaTeX (recommended for output quality)
- Github (recommended for collaboration and version control)

**rivtDocs** installs as a system level program or portable folder and is
available for Windows, Mac, and Linux. It also runs in the cloud using GitHub
CodeSpaces or other cloud service providers. Installation details are provided
in the [rivtDocs User Manual](http://www.rivtmanual.net>)

## **rivt** Overview

**rivt** is a Python package with four API functions: (R(), I(), V(), T()). It
processes **rivtText** - a plain text, readable, calculation markup language
that wraps and extends
[reStructuredText(reST)](https://docutils.sourceforge.io/rst.html). Formatted
output documents can be in UTF8, HTML and PDF formats, all from the same
**rivtText** file. **rivt** is written as a pure Python package that can be
integrated with the large library of Python engineering and scientific
libraries.

The program prioritizes four design principles:

- *Cut and Paste Everything* - **rivtText** content is plain text
- *Short Learning Curve* - **rivtText** uses less than 30 intuitive terms
- *Integration* - **rivt** is built on the highly integrated Python language
- *Standardization* - **rivt** uses a standard folder structure for input and output

**rivt** is designed for simple, single calculations as well as large, extensive
reports. The **rivt** report folder structure shown below is designed to
support both. Folder names are shown in brackets. Folder and file name prefixes
that are fixed are shown italicized. The four top-level folder names (text,
resource, report and site) are required verbatim. Other file names are
combinations of specified prefixes and user titles. Underscores and hyphens
that separate words in file and folder names are stripped out when used as
document and division names in the document.

Document input files are separated into folders labeled text and resource.
Files in the text folder are rivtText files that contain the primary
calculation information. The resource folder includes supporting files (images,
pdf etc.) and other files that may include confidential project information or
copyrighted material. The resource folder often contains binary information and
that may not be shareable.

Output files are written to three folders, depending on the output type. The
UTF8 output is written to a README.txt file within the text folder (displayed
and searchable on version control platforms like GitHub). PDF output is written
to the report folder, and HTML output to the website folder.

**Folder Structure Example**

- **[*rivt_*Design-Project]** (user project and report name)
    - **[*text*]**
        - README.txt                        (project abstract)
        - units.py
        - **[*r0101_*Gravity-Loads]**       (rivt document title)
            - *r0101.py*                    (file name) 
            - README.txt                    (utf document output file)
            - data1.csv                     (source file)
            - functions1.py                 (function file)
        - **[*r0102_*Seismic-Loads]** 
            - *r0102.py*
            - README.txt
            - data2.csv 
            - functions2.py 
        - **[*r0201_*Pile-Design]** 
            - *r0201.py*
            - README.txt
            - paragraph1.txt
            - functions3.py 
    - **[*resource*]**
        - report_gen.txt                (report generation style)
        - site_gen.txt                  (website generation style)
        - pdf_style.sty                 (LaTeX style override)
        - utf_style.txt                 (utf style override)
        - project_data.xls              (project data)
        - **[*rv01_*Overview-and-Loads]**   (division title)
            - image1.jpg
        - **[*rv02_*Foundations]**   
            - image2.jpg
            - attachment.pdf    
    - **[*report*]**                        (PDF dcoument output files)
        - r0101_Gravity-Loads.pdf
        - r0102_Seismic-Loads.pdf
        - r0201_Pile-Design.pdf
        - Design-Project.pdf                (PDF collated report)
    - **[*site*]**                          (HTML site)
        - **[*resources*]**             
            - image1.png
            - image2.png
            - html_style.css                (HTML style override)
        - index.html                        (table of contents)
        - s0101_Gravity-Loads.html
        - s0102_Seismic-Loads.html
        - s0201_Pile-Design.html

The API is designed so that only files in the text folder are uploaded for
version control and sharing. They are the essential core of the calculation -
the text, equations, functions, tables and image references. Files in the
resource folder are not shared and are typically binary and proprietary files
such as images, pdf attachments and proprietary data (e.g. client contact
information and costs). This folder and file structure makes it easy to share
and apply version control on the primary calculation inputs.

A rivt file is a Python file that imports the rivt api and calls one of four
functions on rivt-strings. Rivt-strings are free-form plain text strings
enclosed in triple quotes that include commands and tags defining the
calculation and formatting. rvddss_docname.py is the file name where dd is the
division number, ss is the subdivision number and ddss is the document or file
number. The text folder includes the plain text input and output files. PDF and
HTML files are written to the report and site folders respectively.

A rivt project is typically started by copying from a similar existing
projects, then combining, rearranging and editing. Any shared project includes
as a minimum the text folder. The resource folder will typically need to be
recreated. In summary, rivt reads string functions in a .py file as input and
outputs a plain text document to the same folder. Fully formatted pdf or html
files are output to the report or site folders respectively. A simple text
editor may be used for writing the files, but writing speed is dramatically
improved with a full-featured IDE (e.g. VSCode) with extensions that improve
efficiency. Execution steps are summarized as :

<pre> 
                 --------------------------
                 |  Run entire rivt file  |
                 |      or run parts      |
                 |     interactively:     |
                 |    R(), I(), V(), T()  |
                 ------------  ------------
                             ||
===============  ------------\/------------   =========
|   Write     |  |   Working through       |  | Write |
|   utf8 to   |  |   interactive IDE?      |  | utf8  |
|   terminal  <== YES                    NO ==> file  |
===============  ---------------------------  ====  ===
                                                  ||
                              +===================+
                             ||
===============  ------------\/------------  ---------
|  Write HTML |  |      Write report?     |  |  End  |
| or PDF file <== YES                   NO ===>      |
======  =======  --------------------------  ---------
      ||
      ||         ---------------------------  --------
      ||         |     Collate reports?    |  | End  |
      +==========>                       NO ==>      |
                 |          YES            |  --------
                 ------------  ------------- 
                             ||
                  ===========\/=============
                  | Write PDF report file  |
                  |  or HTML site          |
                  ==========================

</pre>


[rivtDocs User Manual](http://www.rivtmanual.net>)