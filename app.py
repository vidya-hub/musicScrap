from bs4 import BeautifulSoup
import requests
import subprocess
import os


movie_name = input("Enter Movie Name :   ")
res = requests.get(f"https://naasongs.co/{movie_name}.html")
soup = BeautifulSoup(res.content, 'html.parser')
body = soup.find("body")
try:
    container = body.find("div", {"id": "page"})
    actual_content = ((container.find("div", {"id": "site-content"})).find("main", {"id": "main"}).find("div", {
        "id": "primary"}).find("div", {"id": "content"})).find("article").find("span").find_all("p")
    realmoviename = actual_content[0].find_all("b")[0].text
    songs_content = actual_content[2].find_all("a")
    print(realmoviename)
    print("==============Songs List============")
    song_links = []
    song_names = []
    for i in range(len(songs_content)):
        print(songs_content[i].text)
        song_names.append(songs_content[i].text)
        song_links.append(songs_content[i]["href"])
    confirm = input("   Download All the Songs ? [Y] or [N]  ")
    if confirm.lower() == "y":
        if os.path.exists(realmoviename):
            for i in range(len(song_links)):
                file_path = "./"+realmoviename+"/" + song_names[i]+".mp3"
                subprocess.check_output(['wget', '-O', file_path, song_links[i]])
        else:
            os.mkdir(realmoviename)
            for i in range(len(song_links)):
                file_path = "./"+realmoviename+"/" + song_names[i]+".mp3"
                subprocess.check_output(['wget', '-O', file_path, song_links[i]])
    elif (confirm.lower() == "n"):
        for i in range(len(song_names)):
            print(f"[ {i} ]" + song_names[i])
            
        if os.path.exists(realmoviename):
            selected_songno = int(input("Enter Song No... :     "))
            selected_songlink = song_links[selected_songno]
            selected_songname = song_names[selected_songno]
            file_path = "./"+realmoviename+"/" + selected_songname+".mp3"
            subprocess.check_output(['wget', '-O', file_path, selected_songlink])
        else:
            os.mkdir(realmoviename)        
            selected_songno = int(input("Enter Song No... :     "))
            selected_songlink = song_links[selected_songno]
            selected_songname = song_names[selected_songno]
            file_path = "./"+realmoviename+"/" + selected_songname+".mp3"
            subprocess.check_output(['wget', '-O', file_path, selected_songlink])
        
    # print(song_links)
    # for con in songs_content:
    #     print(con.text)
        # command=input("")
        # link = con["href"]
        # file_path = "./"+movie_name+"/" + (link.split('/')[-1]).split("20")[-1]
        # subprocess.check_output(['wget', '-O', file_path, link])
except:
    print("Enter Movie Name Correctly")
