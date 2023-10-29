import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from pages import home, details, search
from components import navbar

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, "assets/style.css",
                          'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

# To override the default favicon, you just need to put a 'favicon.ico' file in the 'assets' folder.
app.title = "IOWA LIQUOR SALES DASHBOARD"

content = html.Div(id="page-content", className='mt-0 mb-0')
app.layout = html.Div([dcc.Location(id="url"), navbar.header, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/details":
        return details.layout
    elif pathname == "/search":
        return search.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ], className="p-3 bg-light rounded-3",
    )


@app.callback(
    Output("offcanvas-scrollable", "is_open"),
    Input("open-offcanvas-scrollable", "n_clicks"),
    State("offcanvas-scrollable", "is_open"),
)
def toggle_offcanvas_scrollable(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server()
