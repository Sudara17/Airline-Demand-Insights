import pandas as pd

def analyze_trends(df):
    df['flight_date'] = pd.to_datetime(df['flight_date'])

    # Popular routes
    df['route'] = df['departure_airport'] + " → " + df['arrival_airport']
    popular_routes = df['route'].value_counts().head(10).reset_index()
    popular_routes.columns = ['Route', 'Search_Interest']

    # Trends over time
    price_trends = df.groupby('flight_date').size().reset_index(name='Search_Interest')

    return {
        "popular_routes": popular_routes,
        "price_trends": price_trends
    }
