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
.button2 {background-color: #008CBA;} /* Blue */
.button3 {background-color: #f44336;} /* Red */ 
.button4 {background-color: #e7e7e7; color: black;} /* Gray */ 
.button5 {background-color: #555555;} /* Black */
</style>
</head>


## Enter search terms separated by a + sign
## Example: concrete+beam+bridge
## Search will be a full text search over rivt README files

<input type="text" id="terms" name="terms"><br><br>
<button class="button" id="bgnBtn" onclick="searchRivt()">Search</button>

<br>
<br>
<br>

## Most Recent Search

<p id="terms"></p>


<script> function searchRivt(){URL = `https://github.com/search?q=rivt+${terms}+in%3Areadme`;window.open(URL,'_blank')}</script>