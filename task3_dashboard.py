from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Read processed data
df = pd.read_csv("output.csv")

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Before and After the Price Increase"),
    dcc.Graph(figure=fig)
])

# Run application
if __name__ == "__main__":
    app.run(debug=True)