import requests


resrponse = requests.get("https://api-inextlynk.upgrow.uz/api/v1/marketplace/home-page-product-categories/?page=1")
print(resrponse)