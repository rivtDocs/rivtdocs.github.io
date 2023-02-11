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
  <th style="text-align: center;border:none;background-color:#959396"><a href="https://rivtdocs.net"><b>rivtDocs (stack)</b></a></th>
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

----------------------------
### Reuse Calculation Documents Anywhere
----------------------------

## Introduction and Motivation

Engineering documents generally require tables, figures and many types of
calculations (in addition to text). Frequently they need to be presented as
formal letters or reports. Recent developments in open source software tools
dramatically improve the ease with which these documents can be compiled and
universally shared.

Engineering professions have an opportunity to produce reusable calculation
libraries that can grow and improve through open source contributions over
time. This model of shared, incremental improvement is effective in software
programming where chunks of code are repurposed and recombined. Although
software code is purely text, the application of this approach to general
engineering documents must be explored.

Many engineering technologies in the 21st century are evolving slowly. Design
procedures are often fixed for decades in standard codes, with little or no
change. Productive engineering work now lies, not so much in technological
innovation, but in understanding a range of established technologies enough to
cost-effectively combine them into a realized project. Engineering documents
are the working papers that describe precisely how the combinations will fit.
Being able to easily cut and paste common ideas from previous projects enables
an engineer to explore more options in order to improve performance, reduce
cost and respond to market changes.

A number of powerful engineering calculation programs are available, but they
incorporate barriers to widespread sharing. The first is high initial and
recurring software costs incurred by constantly changing file formats that
require program upgrades or subscriptions to maintain file compatibility. In
addition, because files and interfaces are incompatible between different
programs, multiple software purchases and learning curves are required.
Furthermore, current software does not typically produce formatted reports,
provide version control or easily integrate output from external programs.

**Program Comparison**

<img src="./assets/img/table1.png" width="900" height="300" />

Taken together these barriers prevent widespread sharing and result in nearly
identical calculations being rewritten many times. **rivt** and **rivtDocs** 
were developed as an an open source markup language and software stack that
minimizes these barriers and promotes reuse.


## **rivtDocs** Overview

**rivtDocs** is an integration of five open source programs and technologies:

1. Python 3.8 or higher  
2. **rivt** + other Python libraries
3. VSCode + extensions
4. LaTeX
5. Github

(note: the minimum software needed to run **rivt** with text output is a Python
installation with 8 additional libraries and a plain text processor.)

**rivt** is a Python package with an API of four functions (R(), I(), V(),
T()). It processes **rivtText**; a plain text, readable, calculation markup
language that wraps and extends **restructuredText**. As a Python package,
**rivt** can be tightly integrated with Python engineering and scientific
libraries.

**rivtDocs** installs as a system level program or a portable self contained
folder, and is available for every OS platforms. It can also be run in the
cloud using GitHub CodeSpaces or other cloud service providers. Installation
details are provided in the [rivtDocs User Manual](http://www.rivtmanual.net>)

## **rivt** Overview

**rivt** is a Python package providing an API for **rivtText**, a simple,
readable document markup language designed for calculations. **rivtText**
extends [reStructuredText(reST).](https://docutils.sourceforge.io/rst.html).
Formatted output documents can be UTF8, HTML and PDF from the same **rivtText**
file.

The program prioritizes three principles:

- *Cut and Paste Anything* - **rivt docs** are plain text
- *Integration* - **rivt** is built on Python which connects almost everywhere
- *Legibility* - **rivtText** uses less than 30 intuitive terms and commands
f
The **rivt** API also uses fixed file and folder conventions for input and output to
simplify formatting, navigation, and report assembly. Folder names are shown in
brackets. Fixed folder and file names and prefixes are shown italicized.


**rivt Folder Structure**

- **[*rivt*_Design_Project]** (user project and report name)
    - **[text]**
        - **[*rv00_config*]** (calc configuration data)
            - units.py
            - config.py
        - **[*rv0101*_Overview_and_Loads]**  (division name)
            - *r0101*_Gravity_Loads.py (file name) 
            - README.txt (output file)
            - data1.csv (source file)
            - functions1.py (function file)
        - **[*rv0102*]** 
            - *r0102*_Seismic_Loads.py
            - README.txt
            - data2.csv 
            - functions2.py 
         - **[*rv0201*_Foundations]**
            - *r0201*_Pile_Design.py
            - README.txt
            - paragraph1.txt
   - **[resource]**
        - **[r00]** (report configuration data)
            - pdf_style.sty
            - project_data.syk
            - report.txt
        - **[r01]** (division resources)
            - image1.jpg
        - **[r02]**
            - image2.jpg
            - attachment.pdf    
   - **[reference]**
        - **[user_folders]** (files not directly used in docs)
            - file1
            - file2
    - **[report]** (pdf output files)
        - r0101_Gravity_Loads.pdf
        - r0102_Seismic_Loads.pdf
        - r0201_Pile_Design.pdf
        - Design_Project.pdf  (collated report)
    - **[site]** (html output files)
        - **[resources]**
            - image1.png
            - image2.png
        - index.html  (table of contents)
        - s0101_Gravity_Loads.html
        - s0102_Seismic_Loads.html
        - s0201_Pile_Design.html

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
calculation and formatting. rvddss_docname.py is the file name where dd is the
division number, ss is the subdivision number and ddss is the document or file
number. The text folder includes the plain text input and output files. PDF and
HTML files are written to the report and site folders respectively.

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