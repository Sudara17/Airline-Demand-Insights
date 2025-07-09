import pandas as pd
import requests

def get_trend_data():
    api_key = ("AVIATIONSTACK_API_KEY")
    url = f"http://api.aviationstack.com/v1/flights?access_key={api_key}&limit=100"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "data" not in data:
            raise ValueError("No 'data' field in API response")

        flights = data["data"]

        records = []
        for flight in flights:
            records.append({
                "airline": flight["airline"]["name"] if flight["airline"] else None,
                "flight_iata": flight["flight"]["iata"] if flight["flight"] else None,
                "departure_airport": flight["departure"]["airport"] if flight["departure"] else None,
                "arrival_airport": flight["arrival"]["airport"] if flight["arrival"] else None,
                "status": flight["flight_status"],
                "departure_time": flight["departure"]["scheduled"],
                "arrival_time": flight["arrival"]["scheduled"]
            })

        df = pd.DataFrame(records)

        # Generate synthetic values for plotting
        df["flight_date"] = pd.to_datetime(df["departure_time"]).dt.date
        df["search_interest"] = 1  # Assign a dummy search count for now

        return df

    except Exception as e:
        raise RuntimeError(f"Failed to fetch data from AviationStack API: {e}")


