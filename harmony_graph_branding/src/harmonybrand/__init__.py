__version__ = "0.3.0"

# Brand a Plotly graph with Harmony theme
def harmonydark(fig):
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/harmonydata/brand/main/logomark/PNG/Logomark-04.png",
            xref="paper", yref="paper",
            x=1.05, y=1.05,
            sizex=0.25, sizey=0.25,
            xanchor="right", yanchor="bottom"
        )
    )

    fig.update_layout(
    #     font_family="Montserrat-Regular",
        title_font_family="Montserrat",
        xaxis_title="Date",
        yaxis_title="Postings per million",
        font=dict(
            family="Pragmatica",
            size=24,
            color="rgb(255,255,255)"
        ),
        title_font=dict(
            family="Montserrat",
            size=48,
            color="rgb(99,230,178)"
        ),
        paper_bgcolor='rgb(17,30,84)',
        plot_bgcolor='rgb(17,30,84)',
        width=1080,
        height=1080,
        margin=dict(l=150, r=100, t=200, b=150),
    )

    fig.update_xaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')

    fig.update_traces(line_color='#80ed99')

def harmonylight(fig):
    fig.add_layout_image(
        dict(
            source="https://raw.githubusercontent.com/harmonydata/brand/main/logomark/PNG/Logomark-04.png",
            xref="paper", yref="paper",
            x=1.05, y=1.05,
            sizex=0.25, sizey=0.25,
            xanchor="right", yanchor="bottom"
        )
    )

    fig.update_layout(
    #     font_family="Montserrat-Regular",
        title_font_family="Montserrat",
        xaxis_title="Date",
        yaxis_title="Postings per million",
        font=dict(
            family="Pragmatica",
            size=24,
            color="rgb(0,0,0)"
        ),
        title_font=dict(
            family="Montserrat",
            size=48,
            color="rgb(54,99,237)"
        ),
        paper_bgcolor='rgb(255,255,255)',
        plot_bgcolor='rgb(255,255,255)',
        width=1080,
        height=1080,
        margin=dict(l=150, r=100, t=200, b=150),
    )

    fig.update_xaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='#cccccc', gridcolor='#cccccc')

    fig.update_traces(line_color="rgb(54,99,237)")
