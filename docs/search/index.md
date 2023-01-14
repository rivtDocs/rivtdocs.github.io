### rivtSearch

## Enter search terms separated by a + sign

Example: concrete+beam+bridge

<button id="bgnBtn" onclick="searchRivt()">Enter Search Terms</button>

recent search terms
<p id="output"></p>


<script> function searchRivt(){var terms = prompt("search terms");document.getElementById('output').innerHTML = name;URL = `https://github.com/search?q=rivt+${terms}+in%3Areadme`;window.open(URL,'_blank')}</script>