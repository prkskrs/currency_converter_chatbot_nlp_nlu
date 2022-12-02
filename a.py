import requests

url = "https://hajana1-free-currency-converter-by-hajana-one-v1.p.rapidapi.com/currency-api.php"

querystring = {"amount":"500","from":"PKR","to":"USD"}

headers = {
	"X-RapidAPI-Key": "58c16120e0msh450e89c6f7ec42ep1de31djsn8805be75421f",
	"X-RapidAPI-Host": "hajana1-free-currency-converter-by-hajana-one-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)