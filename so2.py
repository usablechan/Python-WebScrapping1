import requests
from bs4 import BeautifulSoup

URL=f"https://stackoverflow.com/jobs?q=python"

def extract_title(html):
  title=html.find("h2",{"class":"mb4"}).find("a")
  if title is not None:
    job_title=(title["title"])
  else:
    return
  
  company=html.find("h3").find("span").string
  company=str(company)
  print(company.strip())


request=requests.get(URL)
soup=BeautifulSoup(request.text,"html.parser")
pages=soup.find("div",{"class":"s-pagination"}).find_all("span")
page_numb=[]
for page in pages:
  page_numb.append(page.string)
last_page=page_numb[-2]
print(last_page)
for pn in range(8):
  result=requests.get(f"{URL}&pg={pn+1}")
  soup=BeautifulSoup(result.text,"html.parser")
  results=soup.find_all("div",{"class":"-job"})
  for job in results:
    extract_title(job)