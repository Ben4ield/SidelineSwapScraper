from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://sidelineswap.com/shop/lacrosse/sticks/heads/maverik/tactik-2-0/l12090?q=tactik%202.0").text
soup = BeautifulSoup(source, "lxml")

items = soup.find_all("div", class_="sls-thumb--bottom-section")
prices = soup.find_all("div", class_="sls-thumb--price")
picture_boxes = soup.find_all("img", class_="sls-thumb--image")

head_list= []
price_list = []
pictures = []

csv_file = open("sls_tactik_scrape.txt", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Head", "Price", "Image Link"])

for item in items:
	item_name = item.a.text
	head_list.append(item_name)

for price in prices:
	price_narrowed = str(price).split(">")[1]
	price_value = price_narrowed.split("<")[0]
	price_list.append(price_value)

x=0
c=0

for picture in picture_boxes:
	picture = picture_boxes[c]["src"]
	# print(picture)
	pictures.append(picture)
	c += 1

for head in head_list:
	print(f"{head} - {price_list[x]} - {pictures[x]}")
	csv_writer.writerow([head, price_list[x], pictures[x]])
	x += 1

csv_file.close()
