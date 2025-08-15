import pandas as pd
import plotly.express as px

def plot_price_history(prices, coin_id="bitcoin", days="30"):
    df = pd.DataFrame(prices, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
    fig = px.line(df, x="date", y="price", title=f"{coin_id.capitalize()} - Últimos {days} dias")
    return fig
