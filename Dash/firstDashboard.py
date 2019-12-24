import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.layout = html.Div(children = [
            html.H1('Hello Dash')
])

if __name__ == "__main__":
    app.run_server()