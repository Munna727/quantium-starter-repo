import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")
df = df.sort_values("date")

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div([

    html.H1(
        "📊 Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#ffffff",
            "backgroundColor": "#2c3e50",
            "padding": "20px",
            "borderRadius": "12px"
        }
    ),

    html.Div([
        html.H3("📍 Filter by Region"),

        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "🌍 All", "value": "all"},
                {"label": "⬆️ North", "value": "north"},
                {"label": "⬇️ South", "value": "south"},
                {"label": "➡️ East", "value": "east"},
                {"label": "⬅️ West", "value": "west"},
            ],
            value="all",
            inline=True,
            inputStyle={
                "marginRight": "6px",
                "marginLeft": "15px",
                "cursor": "pointer"
            },
            labelStyle={
                "display": "inline-block",
                "padding": "10px 18px",
                "margin": "8px",
                "border": "2px solid #3498db",
                "borderRadius": "25px",
                "backgroundColor": "#f8f9fa",
                "fontWeight": "bold",
                "fontSize": "15px",
                "cursor": "pointer",
                "transition": "0.3s"
            }
        )
    ],
    style={
        "backgroundColor": "#ecf0f1",
        "padding": "20px",
        "borderRadius": "10px",
        "marginTop": "20px"
    }),

    dcc.Graph(id="sales-graph")

],
style={
    "width": "85%",
    "margin": "auto",
    "fontFamily": "Segoe UI"
})

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-radio", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)