
import os

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

html_out = ""

with open(os.path.join('public','index.html'), 'r+') as html_file:
  parsed_html = BeautifulSoup(html_file, features="lxml")

  # Attribute xmlns:xsi not allowed here (in ul)
  illegal_ul_elts = parsed_html.find_all("ul", attrs={"xmlns:xsi": True})
  for elt in illegal_ul_elts:
    del elt['xmlns:xsi']

  # Combined iframe errors:
  # Error: Bad value 100% for attribute width on element iframe: Expected a digit but saw % instead.
  # Bad value 500px for attribute height on element iframe: Expected a digit but saw p instead
  # The align attribute on the iframe element is obsolete. Use CSS instead.
  illegal_iframe_elts = parsed_html.find_all("iframe", attrs={"width": "100%"})
  for elt in illegal_iframe_elts:
    elt['style'] = f"width: {elt['width']};"
    del elt['width']
    del elt['align'] # Align just does nothing if we have width=100%
    elt['height']=elt['height'].replace('px','')

  html_out = str(parsed_html)
  html_file.truncate(0)
  html_file.seek(0)
  html_file.write(html_out)