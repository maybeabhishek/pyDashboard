import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)
r_x = np.random.randint(1,101,100)
r_y = np.random.randint(1,101,100)

data = [go.Scatter(x=r_x,
                   y = r_y, 
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(23,56,146)',
                       symbol="pentagon",
                       line= {'width':2}
                   )
                )]
layout = go.Layout(title="Scatter  Plot",
                    xaxis={'title':'My x Axis'},
                    yaxis=dict(title= "My y axis"))
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename="scatter.html")