#!/bin/python3


import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote
from string import Template


domain = sys.argv[1]
payloads = [
    ['subdomains','*'],
    ['config files exposed','ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env | inurl:log.txt | inurl:.config | inurl:.passwd | inurl:.jsp | inurl:.asp | inurl:.htaccess | inurl:.env | inurl:.json | ext:json' ],
    ['Database files exposed:','ext:sql | ext:dbf | ext:mdb'],
    ['Sensitive files exposed','inurl:"/phpinfo.php" | inurl:".htaccess" | inurl:"/.git"  -github'],
    ['Log files exposed','ext:log'],
    ['Backup and old files','ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup'],
    ['Directory listing Vulnerabilities','intitle:index.of'],
    ['php error or warnings','"PHP Parse error" | "PHP Warning" | "PHP Error"'],
    ['SQL errors ','intext:"sql syntax error" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"'],
    ['Finding backdoor','inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor | inurl:mini | inurl:fw | inurl:4m3rr0r | inurl:evil | inurl:class'],
    ['php info','ext:php intitle:phpinfo published by the PHP Group'],
    ['Install/setup files','inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config | inurl:package.json'],
    ['Apache Struts RCE','ext:action | ext:struts | ext:do'],
    ['Open redirect','inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http'],
    ['Pubicly exposed documents','ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv | ext:pdf | ext:doc | ext:xls'],
    ['Login pages','inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth | inurl:admin'],
    ['Signup page','inurl:signup | inurl:register | intitle:Signup | intitle:registration']
]

print("please be patient till we generate result...")

i = 0
def get_reqno(sq,i):
    # Define the search query
    search_query = sq
    print(f"process completed {i}/17...")
    # Send the GET request to Google search
    url = quote(search_query)

    response = requests.get("https://www.google.com/search?q=" + url)
    # print(url)
    # print(response.status_code)
    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content of the response
        html_content = response.text

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all search result links
        search_results = soup.find_all('a')

        # Count the number of search results
        result_count = 0

        # Save the links in a Python list
        links = []

        # Iterate through each search result
        for result in search_results:
            link = result.get('href')
            if link.startswith('/url?q='):
                link = link[7:]  # Remove the '/url?q=' prefix
                
                # Parse the link URL to extract the domain
                parsed_url = urlparse(link)
                domain = parsed_url.netloc
                
                # Exclude Google related domains
                if 'google.com' not in domain:
                    links.append(link)
                    result_count += 1
        
        # Print the result count
        # print(f"Number of search results: {result_count}")
        return result_count
        
        # Print the links
        # print("Links:")
        # for link in links:
        #     print(link)
    else:
        print("Error occurred while making the request")
        return 0;

html_template = '''
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{card_title} : results: {req_no}</h5>
    <p class="card-text">{card_text}</p>
    <a href="{card_link}" class="btn btn-primary">{card_button_text}</a>
  </div>
</div>
'''


overall_output = ""
for payload in payloads:
    key, value = payload
    if(key == 'subdomains'):
        search_string = f"*.{domain}"
    else:    
        search_string = f"site:{domain} {value}"
    card_title = key  
    i = i + 1 
    req_no = f"{get_reqno(search_string,i)}"

    card_text = "payload: " + value

    card_link = f"https://www.google.com/search?q={search_string}"
   
    card_button_text = "visit link"

    # Render the HTML template with the provided values
    html_output = html_template.format(card_title=card_title,req_no=req_no, card_text=card_text, card_link=card_link, card_button_text=card_button_text)
    overall_output += html_output
    
# print(overall_output)
total_html = '''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">


    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Results</title>
    <style>
    #alllists{
    display:flex;
    flex-direction: row;
    justify-content: space-between;
    flex-wrap: wrap;

    }

    </style>
  </head>
  <body>
   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Results</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
    
        
     
      </ul>
   
    </div>
  </div>
</nav>
<div class="all_results">
  <h1>Results</h1>  <div id="alllists">''' + overall_output + '''
</div>
</div>



  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>


  </body>
</html> '''

file_name = "./"+domain+".html"
with open(file_name,"w") as file:
    file.write(total_html)
print("File created")    
