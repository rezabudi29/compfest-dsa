import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('data_join.csv')

app.layout = html.Div([
    dcc.Graph(
        id='Posisi Karyawan',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['divisi'] == i]['tanggal'],
                    y=df[df['divisi'] == i]['lokasi_dominan'],
                    text=df[df['divisi'] == i]['jenis_kelamin'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 10,
                        'line': {'width': 2.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.divisi.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'divisi'},
                yaxis={'title': 'tanggal'},
                margin={'l': 200, 'b': 20, 't': 20, 'r': 100},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()


## http://127.0.0.1:8050/