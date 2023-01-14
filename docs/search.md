# Search_GitHub

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


## Enter search terms separated by a + sign
## Example: concrete+beam+bridge
## Search will be a full text search over all GitHub rivt README files

<input type="text" id="terms" name="terms" size=100 style="height:100px;font-size:14ptp"><br><br>
<button class="button" id="bgnBtn" onclick="searchRivt()">Search</button>

<br>
<br>
<br>

## Most Recent Search

<p id="terms"></p>

<script> function searchRivt(){strng = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng}+in%3Areadme`;window.open(URL,'_blank')}</script>