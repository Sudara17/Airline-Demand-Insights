import plotly.express as px
import pandas as pd

def plot_popular_routes(route_df):
    # Ensure correct columns
    if len(route_df.columns) == 3:
        route_df.columns = ['Route', 'Popularity', 'Color']
    elif len(route_df.columns) == 2:
        route_df.columns = ['Route', 'Popularity']
    else:
        raise ValueError("Unexpected number of columns in popular_routes dataframe")

    fig = px.bar(
        route_df,
        x='Popularity',
        y='Route',
        orientation='h',
        color='Route',
        title='Most Searched Routes (Google Trends)',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    return fig


def plot_price_heatmap(price_df):
    price_df = price_df.copy()
    price_df['flight_date'] = pd.to_datetime(price_df['flight_date'])
    price_df['day'] = price_df['flight_date'].dt.date
    price_df['weekday'] = price_df['flight_date'].dt.day_name()

    grouped = price_df.groupby(['day', 'weekday'])['Search_Interest'].mean().reset_index()

    fig = px.density_heatmap(
        grouped,
        x='weekday',
        y='day',
        z='Search_Interest',
        color_continuous_scale='Blues',
        title='Search Interest by Weekday and Date'
    )
    return fig



def plot_status_pie(df):
    status_counts = df['status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    fig = px.pie(status_counts, names='Status', values='Count', title='Flight Status Distribution')
    return fig

def plot_airline_volume(df):
    if 'airline' not in df.columns:
        import plotly.graph_objects as go
        return go.Figure().update_layout(
            title="Airline column not available in dataset",
            annotations=[dict(text="Column 'airline' missing", showarrow=False)]
        )

    airline_counts = df['airline'].value_counts().reset_index()
    airline_counts.columns = ['Airline', 'Flights']
    fig = px.bar(airline_counts, x='Airline', y='Flights',
                 title='Number of Flights by Airline', color='Flights',
                 color_continuous_scale='Blues')
    return fig

def plot_demand_trend(price_df):
    price_df = price_df.copy()
    fig = px.line(
        price_df,
        x="flight_date",
        y="Search_Interest",
        title="Daily Flight Search Trend",
        markers=True
    )
    return fig