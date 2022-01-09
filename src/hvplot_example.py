import panel as pn
import pandas as pd, numpy as np

import hvplot.pandas  # noqa

primary_color="#3E5F8A"
secondary_color="#EA899A"

idx = pd.date_range('1/1/2000', periods=1000)
df1  = pd.DataFrame(np.random.randn(1000, 1), index=idx, columns=list('A')).cumsum()
df2  = pd.DataFrame(np.random.randn(1000, 1), index=idx, columns=list('B')).cumsum()

p1 = df1.hvplot(width=700, line_width=4, color=primary_color)
p2 = df2.hvplot(width=700, line_width=4, color=secondary_color)

overlay = (p1*p2).opts(width=1400)
layout = (p1+p2) 

pn.template.FastListTemplate(
    site="Panel", title="Hvplot Example",
    main=[overlay, layout],
    accent_base_color=primary_color, header_background=secondary_color
).servable()