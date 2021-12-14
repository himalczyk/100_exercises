import webbrowser

query = str(input("Enter your Google query: "))

url = 'https://www.google.com/search?q='
new_tab = 2 #opens in a new tab, if possible

search_query = url + query

webbrowser.open_new_tab(search_query)