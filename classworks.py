# Number 1 
# import re
# sentence = "John is a student of cyclobold and his matriculation number is M123d but he often says he is 'the scholar of our time'. "
# big_letters = re.findall ("\w", sentence)
# numbers = re.findall ("\d", sentence)
# spaces = re.findall ("\s", sentence)
# print(big_letters)
# print(numbers)
# print(spaces)

# # Number 2
# import re
# string = "Joshua "
# match = re.sub("\s", "_23", string)
# print(match)

# Number 3
# import re
# matches = "no53, Tunde21, cutie436, Temi, Wole419"
# match = re.findall("\w" "+" "\d", matches)
# print(match)

# Number 4
# import re
# space = "I am John, the name of my tech academy is cyclobold."
# spaces = re.findall("\s", space)
# spaced = re.sub(",", " and", space)
# print(spaces)
# print(spaced)

# # Number 5
# import re
# words = "apple, oranges, elephant, grass, anthill, beans, ears"
# word = re.findall("\w" "+" "[^a  | ^e]", words)
# print(word)

# Number 6
# import re
# email = input("Enter your email: ")
# email_input = re.findall("\w" "+" "(\.com |\.net |\.org |\.edu&)", email)
# print(email_input)

# Number 7
# import re
# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://cyclobold.com/")
# soup = BeautifulSoup(r.content, "html.parser")
# data = soup.prettify()
# find_data = data.find_all('p')
# data_string = str(find_data)
# print(data_string)
# scrape = "movies, form"
# scraped = re.findall(r"movies" "form" "\s" "\d", data_string)
# if scraped:
#     print("successful")
# else:
#     raise TypeError("unsuccessful")

# # Number 8
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# pretty = data.prettify()
# data_find = data.find_all('p')
# text = str(data_find)
# pdf = open("exec.pdf", "w")
# pdf.write(text)
# pdf.close()

# Number 9
# import webbrowser
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('img')
# test = str(para)
# img = open("imgg.html", "w")
# img.write(test)
# img.close()
# webbrowser.open("imgg.html")









