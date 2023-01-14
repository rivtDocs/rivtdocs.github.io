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
.button2 {background-color: #008CBA;} /* Blue */
.button3 {background-color: #f44336;} /* Red */ 
.button4 {background-color: #e7e7e7; color: black;} /* Gray */ 
.button5 {background-color: #555555;} /* Black */
</style>
</head>

## rivtSearch

## Enter search terms separated by a + sign


<button class="button" id="bgnBtn" onclick="searchRivt()">Click to Enter Terms</button>
Example: concrete+beam+bridge
<br>
<br>
<br>
Most Recent Search
<p id="output"></p>


<script> function searchRivt(){var terms = prompt("search terms");document.getElementById('output').innerHTML = name;URL = `https://github.com/search?q=rivt+${terms}+in%3Areadme`;window.open(URL,'_blank')}</script>