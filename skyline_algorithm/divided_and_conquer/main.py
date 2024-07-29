import plotly.graph_objects as go
from src.data.point import Points
from src.skyline.divide_and_conquer import m_partitioning_dnc, dnc


def main():
    datas = Points(size=(2, 1000))
    skyline = m_partitioning_dnc(datas.data)
    # skyline = dnc(datas.data)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=[data[0] for data in datas.data],
            y=[data[1] for data in datas.data],
            mode='markers',
            name='points',
            marker=dict(size=15)
            )
        )
    fig.add_trace(
        go.Scatter(x=[data[0] for data in skyline],
                   y=[data[1] for data in skyline],
                   mode='markers',
                   name='skyline',
                   marker=dict(size=15)
                   )
                   )
    fig.show()


if __name__ == '__main__':
    main()
