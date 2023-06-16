# Import the beautifulsoup
# and request libraries of python.
import requests
from bs4 import BeautifulSoup


# Add header User-Agent which is a string to tell the server what kind of device you are accessing the page with.
#This is very important.

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

'''
Make two strings: 
1) default google search URL
2) customized search keyword.
Concatenate them
'''
text= "how to format beautiful soup"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests. Get data content.
r = requests.get( url, headers=headers )
htmlContent = r.content

# Creating soup from the fetched request
soup = BeautifulSoup(htmlContent, "html.parser")

# HTML Tree traversal

# this finds the string in thr div "result-stats". the result should be something like "About 1234 results"
total_results_text = soup.find("div", {"id": "result-stats"}).find(string=True, recursive=False)

# clean it up the result and remove all the characters that are not a number .
results_str = ''.join([num for num in total_results_text if num.isdigit()]) 
results_num = int(results_str)
print(results_num)



