# Python library to produce Harmony branded graphs in Plotly

## Installation

```
python setup.py install
```

## Usage

### Dark theme

```
import harmonybrand

import plotly.express as px
fig = px.line(x=[1,2,3], y=[3,1,2],
                title="<b>Receiver operating characteristic</b>")

harmonybrand.harmonydark(fig)

fig.show()

fig.write_image("harmony_dark.svg")

!convert harmony_dark.svg harmony_dark.png
```

![light](harmony_dark.png)

or

### Light theme

```
import harmonybrand

import plotly.express as px
fig = px.line(x=[1,2,3], y=[3,1,2],
                title="<b>Receiver operating characteristic</b>")

harmonybrand.harmonylight(fig)

fig.show()

fig.write_image("harmony_light.svg")

!convert harmony_light.svg harmony_light.png
```

![light](harmony_light.png)
