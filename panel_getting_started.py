# pip install panel pandas matplotlib
import numpy as np
import pandas as pd
from matplotlib.figure import Figure

data_url = "https://cdn.jsdelivr.net/gh/holoviz/panel@master/examples/assets/occupancy.csv"
data = pd.read_csv(data_url, parse_dates=["date"]).set_index("date")

primary_color = "#0072B5"
secondary_color = "#94EA84"


def mpl_plot(avg, highlight):
    fig = Figure(figsize=(10,5))
    ax = fig.add_subplot()
    avg.plot(ax=ax, c=primary_color)
    if len(highlight):
        highlight.plot(style="o", ax=ax, c=secondary_color)
    return fig


def find_outliers(variable="Temperature", window=20, sigma=10, view_fn=mpl_plot):
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = np.abs(residual) > std * sigma
    return view_fn(avg, avg[outliers])


# Panel
import panel as pn

pn.extension(sizing_mode="stretch_width")

# Widgets
variable = pn.widgets.RadioBoxGroup(
    name="Variable", value="Temperature", options=list(data.columns), margin=(-10, 5, 10, 10)
)
window = pn.widgets.IntSlider(name="Window", value=20, start=1, end=60)

# Reactive Function(s). I.e. functions that are rerun when the widget values changes
reactive_outliers = pn.bind(find_outliers, variable, window, 10)

# Layout(s)
settings = pn.Column(pn.pane.Markdown("Variable", margin=(10, 5, 5, -5)), variable, window)

# Template

pn.template.FastListTemplate(
    site="Panel",
    title="Getting Started Example",
    sidebar=[settings],
    main=[pn.panel(reactive_outliers, sizing_mode="scale_both")],
    accent_base_color=primary_color,
    header_background=primary_color,
).servable()