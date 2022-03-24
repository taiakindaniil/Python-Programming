import requests

headers = {
    "x-api-key": open("./api.key", "r").read()
}

# hardcoded:
# - 6 months for lab task
# - US region
# - 1 day interval
def get_chart(symbol="AAPL"):
    url = f"https://yfapi.net/v8/finance/chart/{symbol}"
    querystring = {
        "range": "max",
        "region": "US",
        "interval": "1mo",
        "lang": "en"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    with open(f"./saved_api_responses/{symbol}.json", "w") as f:
        f.write(response.text)

    return response