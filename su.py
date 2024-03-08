Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... 
... # Album information
... albums = [
...     {
...         "Album Title": "Album1",
...         "Artist": "eminem",
...         "Songs": ["love", "rock", "class", "hit", "out"],
...         "Release Year": "Year1"
...     },
...     # Repeat for other albums
... ]
... 
... # Create HTML file
... html_content = """
... <!DOCTYPE html>
... <html>
... <head>
...   <title>Albums Information</title>
... </head>
... <body>
... 
... <table border="1">
...   <tr>
...     <th>Album Title</th>
...     <th>Artist</th>
...     <th>Songs</th>
...     <th>Release Year</th>
...   </tr>
... """
... 
... for album in albums:
...     html_content += f"""
...   <tr>
...     <td>{album['Album Title']}</td>
...     <td>{album['Artist']}</td>
...     <td>{', '.join(album['Songs'])}</td>
    <td>{album['Release Year']}</td>
  </tr>
"""

html_content += """
</table>

</body>
</html>
"""

# Save HTML content to a file
with open('albums.html', 'w') as html_file:
    html_file.write(html_content)

# Save JSON content to a file
with open('albums.json', 'w') as json_file:
    json.dump(albums, json_file)
