from sales_dashboard import app

def test_header(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("#header")

    assert header is not None


def test_graph(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")

    assert graph is not None


def test_region_picker(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-radio")

    assert radio is not None