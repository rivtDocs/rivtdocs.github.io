---
layout: default
---

<table>
<colgroup>
  <col width="30%" />
  <col width="30%" />
</colgroup>
<thead>
<tr class="header">
  <th style="text-align: center;border:none;background-color:#959396"><a href="https://rivtdocs.net"><b>rivtDocs (installers)</b></a></th>
  <th style="text-align: center;border:none"><a href="https://rivtcode.net"><b>rivt (source code)</b></a></th>
  <th style="text-align: center;border:none"><a href="https://rivtsearch.net"><b>rivtSearch (GitHub)</b></a></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:center;border:none"><a href="https://rivtdocs.net"><img src="./assets/img/rivtdocs.png" width="85" height="60" style="border:2px solid #5c5962"/></a></td>
  <td style="text-align: center;border:none"><a href="https://rivtcode.net"><img src="./assets/img/rivt01.png" width="80" height="60" style="border:2px solid #5c5962"/></a></td>
  <td style="text-align: center;border:none"><a href="https://rivtsearch.net"><img src="./assets/img/search01.png" width="85" height="65" style="border:2px solid #5c5962"/></a></td>
</tr>
</tbody>
</table>
<p style="text-align:center; font-weight:bold"> Share Docs and Calcs Anywhere, Anytime </p>
-----------------------------------------

## Introduction

Engineering documents and calcs include text, tables, figures and calculations
organized in letter and report formats. Recent developments in open source
software tools dramatically improve the ease with which these documents can be
compiled and shared. This has important implications for engineering design
quality and productivity.

Many engineering technologies in the 21st century are evolving slowly. Design
procedures are often fixed for decades in standard codes, with little or no
change. Good engineering work now lies, not so much in technological
innovation, but in understanding a range of established technologies well
enough to efficiently and cost-effectively combine them to fit project
requirements. Calculation documents are the working papers that describe
precisely how the combinations fit. Being able to easily cut, paste and share
from previous projects lets an engineer explore more options, focus on key
issues, respond to market changes and improve solutions.

Engineering professions have an opportunity to produce large, general
calculation libraries that can be reused and recombined as needed. The model of
shared, incremental improvement in open source software code has proven
effective in programming. Although code is only text, the extension of this
approach to more general engineering calculation documents is promising.

A number of powerful calculation programs exist, but they include barriers to
widespread sharing. These include high initial and substantial recurring
software costs. Costs are further increased by constantly changing file formats
that require program upgrades or subscriptions to maintain file compatibility.
In addition, file incompatibility between different programs requires multiple
software purchases and programs to learn. Furthermore current software does not
easily generate reports, version control or integrate output from external
programs.

Taken together these barriers prevent widespread sharing and result in nearly
identical calculations being rewritten many times. **rivtDocs** and **rivt**
were conceived as an an open source software stack to minimize these barriers
and promote sharing.

**Program Comparison**

<img src="./assets/img/table1.png" width="900" height="300" />

## **rivtDocs** Overview

**rivtDocs** is an integration of four open source programs and technologies
(listed below) that process **rivtText**, a plain text, human readable,
calculation markup language derived from restructuredText. **rivt** and other
Python libraries process **rivtText**. **VSCode** is the primary interface.
**LaTeX** provides document formatting. **Github** repositories are the primary
platform for version control, search and distribution or *rivt* documents. 

**rivt** can be installed on the desktop or run in the cloud.  The absolute
minimum software needed is a Python installation with 8 additional libraries and
a plain text processor. The basic installation required for efficient workflow
and formal document production includes: 

1. Python 3.8 or above + libraries
2. VSCode + extensions
3. LaTeX
4. Github

**rivtDoc** installers are available for every OS platforms. It can also be run
in the cloud using GitHub CodeSpaces (or other cloud service providers).
Installation details are provided in the user manual ___here ____.


## **rivt** Overview

**rivt** is a Python package providing an API for **rivtText**, a simple,
readable document markup language designed for calculations. **rivtText** wraps
and extends [reStructuredText(reST).](https://docutils.sourceforge.io/rst.html). 
Ouptut documents include UTF8, HTML and PDF from the same **rivtText** file.

The program design follows three principles:

- **Maximize Cut and Paste** - Calculations are text
- **Integrate easily** - Python libraries connect with external programs and data
- **Respect your time** - Only two dozen intuitive syntax terms in the language

The **rivt** API uses fixed file and folder conventions for input and output to
simplify formatting, navigation, and report assembly. Folder names are shown in
brackets. Fixed folder and file names and prefixes are shown italicized.


**rivt Folder Structure**

- **[*rivt*_project_name]** (user project_name)
    - **[text]**
        - **[*rv00_config*]** (calc configuration data)
            - units.py
            - config.py
        - **[*rv0101*_division_name]**  (folder report division name)
            - *rv0101*_doc_name.py (file name) 
            - README.txt (doc output file)
            - chart.csv (doc source file)
            - functions.py (doc function file)
        - **[*rv0102*_division_name]** 
            - *rv0102*_doc_name.py
            - README.txt
            - chart1.csv 
            - functions1.py 
         - **[*rv0201*_division_name]**
            - r0201_doc_name.py
            - README.txt
            - paragraph.txt
   - **[resource]**
        - **[r00]** (report configuration data)
            - pdf_style.sty
            - project_data.syk
            - *report.txt*
        - **[r01]**
            - image1.jpg
        - **[r02]**
            - image2.jpg
            - attachment.pdf    
   - **[reference]**
        - **[user_folders]** (files not used in docs)
            - file1
            - file2
    - **[report]** (pdf output files)
        - r0101_loads.pdf
        - r0102_foundation.pdf
        - r0201_floor.pdf
        - r0202_roof.pdf
        - report.pdf
    - **[site]** (html output files)
        - **[resources]**
            - image1.png
            - image2.png
        - index.html
        - s0101_loads.html
        - s0102_foundation.html
        - s0201_floor.html
        - s0202_roof.html

The four top-level folder names (text, resource, report and site) are required.
Other file names are user determined using the specified prefixes. Underscores
that separate words in file and folder names are stripped out when used as
document and division names in the report. The API is designed so that only
files in the text folder are uploaded for version control and sharing. They are
the essential core of the calculation - text, equations, functions, tables and
image references. Files in the resource folder are not shared and are typically
binary files such as images, pdf attachments and proprietary data (e.g. client
contact information and costs). This folder and file structure makes it easy to
share and assert version control on the primary calculation inputs. 

A rivt file is a Python file that imports rivtapi and calls one of four
functions on rivt-strings. Rivt-strings are free-form plain text strings
enclosed in triple quotes that include commands and tags defining the
calculation and formatting. rvddnn_docname.py is the file name where dd is the
division number, nn is the subdivision number and ddnn is the document number.
The text folder includes all of the plain text input files and output doc
files.

A rivt project is typically started by copying from a similar existing project.
The text folder will be available. The resource folder may have to be
recreated. In summary, rivt reads string functions in a .py file as input and
outputs a plain text document to the text folder. Fully formatted pdf or html
files are output to the report or site folders respectively. A simple text
editor may be used, but writing speed is dramatically improved if a
full-featured IDE (i.e. VSCode) is used. rivt_strings may be executed
interactively using the standard cell tag (# %%). Execution steps are
summarized as :

<pre> 
                    ---------------------------------
                    |     Edit and run rivt file    |
                    |     or interactive cells.     |
                    |                               |
                    |    cell or function types:    |
                    |       R(), I(), V(), T()      |
                    ----------------+----------------
                                   ||
 -----------------  ----------------------------------  ---------------
 |   Process     |  |   Working in interactive IDE?  |  |  Process    |
 |   cell to     |  |   (e.g. VSCode, Spyder, Pyzo)  |  |  file       |
 |   terminal    <--+ YES                         NO +-->             |
 -------+---------  ----------------------------------  -------+-------
       ||           ==================================         ||
       ||           |    Write utf-8, reST, TeX      |         ||
        +===========>    calc to file                <=========+
                    |================+===============|
                                    ||
 =================  +--------------------------------+
 | Write HTML    |  |                                |  -----------
 | or PDF doc    |  |         Write docs?            |  |   End   |
 | files         <==+ YES                         NO +==>         |
 =====+===========  ----------------------------------  -----------
     ||
     ||            +--------------------------------+  -----------
     ||            |         Write report?          |  |   End   |
      +============>               YES           NO +==>         |
                   +----------------+---------------+  -----------
                                   ||
                   ==================================
                   |    Write PDF report file       |
                   ==================================
</pre>

rivtDocs can be installed in several ways:

- Local install with configuration of individual components.

- Portable install through pre-configured zip file (Windows only).

- Installation on a remote server.


[Rivt User Manual](http://www.rivtmanual.net>)
