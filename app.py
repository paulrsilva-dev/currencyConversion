# currency_converter_app.py

from davia import Davia
import requests

app = Davia()

@app.task
def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert currency from one to another using live rates.
    """
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
        response = requests.get(url)
        data = response.json()
        rate = data["rates"].get(to_currency.upper())

        if rate is None:
            raise ValueError(f"No rate found for {to_currency.upper()}")

        return round(amount * rate, 2)

    except Exception as e:
        raise ValueError(f"Conversion failed: {str(e)}")

if __name__ == "__main__":
    app.run()
