import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
r_x = np.linspace(0, 1, 100)
r_y = np.random.randn(100)

trace = go.Scatter(x=r_x, y=r_y+5,
                   mode="markers",
                   name="markers")

trace1 = go.Scatter(x=r_x, y=r_y,
                   mode="lines",
                   name="markers")

data = [trace, trace1]
layout = go.Layout(title="Scatter  Plot",
                   xaxis={'title': 'My x Axis'},
                   yaxis=dict(title="My y axis"))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="line.html")
