"""
    Stage: Development-01
    @author: Deniz Günenç, 120200078
    @author: Melike Zeynep Tapci, 120200067
"""

#import libraries
import requests
from bs4 import BeautifulSoup as bs

# function: get_news() 
# params
# date: string "YYYY/MM/DD"
# genre: string "science"
def get_news(date, genre):
    # define the url
    url = "https://www.nytimes.com/section/" + genre
    # get the html content
    html = requests.get(url)
    # parse the html content
    soup = bs(html.content, "html.parser")
    # find the news
    news = soup.find_all("div", {"class": "css-1cp3ece"})
    # print the news according to date
    for new in news:
        if date == ' '.join([str(elem) for elem in new.find("a")["href"].split("/")[1:4]]).replace(" ", "/"):
            print(new.find("h2").text)


print("politics")
get_news("2022/12/01", "politics")
print("\nscience")
get_news("2022/11/30", "science")
