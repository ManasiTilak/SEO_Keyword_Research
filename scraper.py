# Import the beautifulsoup
# and request libraries of python.
import requests
from bs4 import BeautifulSoup


# Add header User-Agent which is a string to tell the server what kind of device you are accessing the page with.
#This is very important.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them

text= "geekforgeeks"
url = 'https://google.com/search?q=' + text


# Fetch the URL data using requests.get(url),
# store it in a variable, r.
r = requests.get( url, headers=headers )
htmlContent = r.content
# print(htmlContent)

# Creating soup from the fetched request
soup = BeautifulSoup(htmlContent, "html.parser")
# print(soup.prettify())

# # HTML Tree traversal
# div = soup.find_all("div", class_="main")
# print(div)
total_results_text = soup.find("div", {"id": "result-stats"}).find(string=True, recursive=False)
results_num = ''.join([num for num in total_results_text if num.isdigit()]) # now will clean it up and remove all the characters that are not a number .
print(results_num)



