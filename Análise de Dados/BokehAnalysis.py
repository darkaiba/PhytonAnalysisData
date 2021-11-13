# Importando o módulo Bokeh
import bokeh
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.sampledata.iris import flowers

from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson

from bokeh.io import show
from bokeh.models import (ColumnDataSource, HoverTool, LogColorMapper)
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

# Carregando o Bokeh
output_notebook()
# Arquivo gerado pela visualização
output_file("Bokeh-Grafico-Interativo.html")

p = figure()
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width = 2)
show(p)

#### ---> Grafico Barras

# Criando um novo gráfico
output_file("Bokeh-Grafico-Barras.html")

fruits = ['Maças', 'Peras', 'Tangerinas', 'Uvas', 'Melancias', 'Morangos']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

p = figure(x_range=fruits, plot_height=350, toolbar_location=None, title="Contagem de Frutas")

p.vbar(x='fruits',
       top='counts',
       width=0.9,
       source=source,
       legend_label="fruits",
       line_color='white',
       fill_color=factor_cmap('fruits', palette=Spectral6, factors=fruits))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 9
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

####### ---> ScatterPlot

# Construindo um ScatterPlot
colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"], color=colors, fill_alpha=0.2, size=10)

output_file("Bokeh_grafico_Iris.html", title="iris.py example")

show(p)

######## ---> Grafico Circulos
# Outuput
output_file("Bokeh-Grafico-Circulos.html")

p = figure(plot_width = 400, plot_height = 400)

# Adicionando círculos ao gráfico
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size = 20, color = "navy", alpha = 0.5)

# Mostrando o resultado
show(p)

#### --->Dados GeoFísicos
geo_source = GeoJSONDataSource(geojson=geojson)

p = figure()
p.circle(x = 'x', y = 'y', alpha = 0.9, source = geo_source)
output_file("Bokeh-GeoJSON.html")
show(p)

# palette.reverse()

counties = {code: county for code, county in counties.items() if county["state"] == "tx"}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

source = ColumnDataSource(data = dict(x = county_xs,
                                      y = county_ys,
                                      name = county_names,
                                      rate = county_rates,))

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(title = "Texas Unemployment, 2009",
           tools = TOOLS,
           x_axis_location = None,
           y_axis_location = None)

p.grid.grid_line_color = None

p.patches('x', 'y', source = source,
          fill_color = {'field': 'rate', 'transform': color_mapper},
          fill_alpha = 0.7, line_color = "white", line_width = 0.5)

hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Unemployment rate)", "@rate%"),
    ("(Long, Lat)", "($x, $y)"),
]

show(p)
