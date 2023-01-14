### rivtSearch

### [RivtCalc Example 01 on repl.it](https://repl.it/@rivtcalc/tryrivt01#main.py)

Some description

### [RivtCalc Example 02 on repl.it](https://repl.it/@rivtcalc/tryrivt02#main.py)

## Search

Enter search terms separated by a + sign

Example: concrete+beam+bridge

<button id="bgnBtn" onclick="searchRivt()">Enter Search Terms</button>

recent search terms
<p id="output"></p>


Example list
```markdown
1. https://github.com/account_name/repo_name
    aslkfas dflas   asdflkas dflasdf asdf aslkfas  
    asdfklas dfasl dfasdf asdfklas dfasl dfasdf 

2. https://github.com/account_name/repo_name
    aslkfas dflas   asdflkas dflasdf asdf 
    asdfklas dfasl dfasdf asdfklas dfasl dfasdf 
```


### Support or Contact

The [documentation](https://docs.github.com/categories/github-pages-basics/) provides instructions for use and [contact support](oncexchange@gmail.com) can answer questions. 

<script> function searchRivt(){var terms = prompt("search terms");document.getElementById('output').innerHTML = name;URL = `https://github.com/search?q=rivt+${terms}+in%3Areadme`;window.open(URL,'_blank')}</script>