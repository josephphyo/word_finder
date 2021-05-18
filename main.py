import requests
import json

## https://developer.oxforddictionaries.com/documentation/languages
## For APP ID & API Key , Please register at https://developer.oxforddictionaries.com/

application_id = input("Please enter your app_id -> ")
api_key = input("Please enter your api_key -> ")
print("Language Code -> en-gb, en-us")
language_code = input("Please enter your language code, en-gb (or) en-us -> ")
word = input("Please enter your word -> ")

app_id = application_id
app_key = api_key
language = language_code
word_id = word

url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}) 
words = r.json()

print("Word: {}\nMeaning: {}\n".format(words["id"],words["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]))