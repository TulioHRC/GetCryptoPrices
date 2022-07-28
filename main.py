# Importing Libs
import requests
import os
from bs4 import BeautifulSoup as BS

while True:
	print("\nWelcome to my simple Crypto Prices app\n")

	name = input("What Crypto do you want to know the actual price (1 to exit)? ")
	if name == "1": break

	print("\n\n")

	try:
		page = requests.get(f"https://coinmarketcap.com/pt-br/currencies/{name.lower()}/")

		soup = BS(page.text, "html.parser")

		print(str(soup.find(class_="priceValue smallerPrice").find("span").string.strip()))

	except Exception as e:
		print(e)
		print("This crypto was not found, try again!")
	
	input("\n\nENTER to Continue...")
	os.system('cls' if os.name == 'nt' else 'clear')
