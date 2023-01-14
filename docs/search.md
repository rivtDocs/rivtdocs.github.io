# Search GitHub

<head>
<style>
.button {
  background-color: #4CAF50; /* Green */
  border: none;
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
</head>

<script> function searchRivt(){strng = document.getElementById("terms").value;document.getElementById('output').innerHTML = strng;URL = `https://github.com/search?q=rivt+${strng}+in%3Areadme`;window.open(URL,'_blank')}</script>

<br>

### Enter search terms separated by a + sign
### Example: concrete+beam+bridge
### Full text search over all GitHub rivt README files

<br>

<input type="text" id="terms" name="terms" size=100 style="height:50px;font-size:14pt; font-weight: bold"><br><br>
<button class="button" id="bgnBtn" onclick="searchRivt()">Search</button>

<br>

## Most Recent Search

<p style="height:50px;font-size:14pt; font-weight: bold" id="output"></p>


