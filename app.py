from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    # print(data)
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    cf = fetch_conversion_factor(source_currency,target_currency)
    final_amount = amount * cf
    final_amount = round(final_amount,2)
    print(final_amount)
    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    return jsonify(response)

def fetch_conversion_factor(source,target):
    url= f'https://open.er-api.com/v6/latest/{source}'
    response = requests.get(url)
    response = response.json()
    
    # print(response["rates"][target])
    amount=response["rates"][target]
    dictAmount = { f"{source}_{target}" : amount}
    print(dictAmount)
    

    return dictAmount['{}_{}'.format(source,target)]


if __name__ == "__main__":
    app.run(debug=True)