from bs4 import BeautifulSoup
import requests
import subprocess
import os


movie_name=input("Enter Movie Name :   ")
os.mkdir(movie_name)
res = requests.get(f"https://naasongs.co/{movie_name}.html")
soup = BeautifulSoup(res.content, 'html.parser')
body = soup.find("body")
container = body.find("div", {"id": "page"})
content = ((container.find("div", {"id": "site-content"})).find("main", {"id": "main"}).find("div", {
           "id": "primary"}).find("div", {"id": "content"})).find("article").find("span").find_all("p")[2].find_all("a")

for con in content:
    link = con["href"]
    file_path= "./"+movie_name+"/"+ (link.split('/')[-1]).split("20")[-1]
    subprocess.check_output(['wget', '-O',file_path, link])
