<head>
<style>
.button {
  background-color: #4CAF50; /* Green */
  border: 2 px solid black;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<script> function searchRivt(){var strng1 = document.getElementById("terms");var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

</head>

<table width="75%">
<colgroup>
  <col width="25%" />
  <col width="25%" />
  <col width="25%" />
</colgroup>
<thead>
<tr class="header">
  <th style="text-align: center;border:none"><a href="https://rivtdocs.net"><b>rivtDocs (installers)</b></a></th>
  <th style="text-align: center;border:none"><a href="https://rivtcode.net"><b>rivt (source code)</b></a></th>
  <th style="text-align: center;border:none;background-color:#959396"><a href="https://rivtdocs.net/search"><b>rivtSearch (GitHub)</b></a></th>
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

------------------

# Search GitHub

------------------

### Enter search terms separated by a + sign
Executes full text search across **rivt** README files on GitHub

<input type="text" id="terms" name="terms" size=100 style="height:50px;font-size:14pt; font-weight: bold">
<br>
Example: concrete+beam+bridge

<button class="button" id="searchBtn" onclick="searchRivt()">Search [ ctrl+enter ]</button>


