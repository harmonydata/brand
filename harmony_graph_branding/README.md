# Usage

```
import harmonybrand

import plotly.express as px
fig = px.line(x=[1,2,3], y=[3,1,2],
                title="<b>Receiver operating characteristic</b>")

harmonybrand.harmonydark(fig)

fig.show(renderer="png")
```

or

```
import harmonybrand

import plotly.express as px
fig = px.line(x=[1,2,3], y=[3,1,2],
                title="<b>Receiver operating characteristic</b>")

harmonybrand.harmonylight(fig)

fig.show(renderer="png")
```

You need TTF files in same folder: `Montserrat-ExtraBold.ttf` and `Pragmatica-Regular.ttf`.
