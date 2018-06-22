bokeh.plotting

1.basic step for plotting
The basic steps to creating plots with the bokeh.plotting interface are:

1.1 Prepare some data
In this case plain python lists, but could also be NumPy arrays or Pandas series.

1.2 Tell Bokeh where to generate output
In this case using output_file(), with the filename "lines.html".
Another option is output_notebook() for use in Jupyter notebooks.

1.3 Call figure()
This creates a plot with typical default options and easy customization of 
title, tools, and axes labels.


1.4 Add renderers
In this case, we use line() for our data, specifying visual customizations like 
colors, legends and widthss.

1.5 Ask Bokeh to show() or save() the results.
These functions save the plot HTML to a file and 
optionally display it in a browser.



2.
from bokeh.plotting import figure, output_file, show

#prepare some data
x = [i*0.1 for i in range(0,51)]
y = list(map(lambda x:x**2,x))

#output to static HTML file
output_file('plot.html')

#create a new plot
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"
p = figure(
    title='...',height='...',width='...'
    tools=TOOLS,
    y_axis_type='...',y_range=[...,...],y_axis_label='...',
    x_axis_type='...',x_range=[...,...],x_axis_label='...',
)

#add some renderers
p.line(x,y,legend='...',
line_color='...',line_width=...,line_alpha=...,line_dash='...')

p.circle(x,y,legend='...',
line_color='...',line_width=...,fill_color='...',fill_alpha='...',size=...)
p.triangle
p.square

#show the results
show(p)

3.colors

colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*x, 30+2*y)
]
%02x : 格式化无符号十六进制数,两位,不够补零
色号范围 : 0~255

4.关于widget的问题

首先是要有widget
然后把widget打包成widgetbox
再然后把widgetbox放入layout中
最后把layout组装成Panel
最最后由pannel构成Tabs

4.5关于figure的问题
首先是要有一个figure对象
然后用它的各种方法(etc.line,circle)来画图
最后可以用gridplot把多个figure对象合并起来(可选)
from bokeh.layouts import gridplot
show(gridplot([[s1, s2, s3]]))

5.关于跳过某点的问题

nan = float('nan')
x = [1,2,nan,4,5]
y = [1,2,3,4,5]

6.ColumnDataSource的问题
CDS用于高效使用数据,导入figure中的数据会先被转为CDS的格式,然后再显示出来
也可以直接创建CDS格式的数据,并这样可以使数据在多个figure间共享
CDSView用于数据筛选,由CDS和filters参数组成
在调用figure的方法的时候,可以通过source和view参数把CDS和CDSView传递进去

x = list(range(-20, 21))
y0 = [abs(xx) for xx in x]
y1 = [xx**2 for xx in x]
# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))
# create a view of the source for one plot to use
view = CDSView(source=source, filters=[BooleanFilter([True if y > 250 or y < 100 else False for y in y1])])
right = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
right.circle('x', 'y1', size=10, hover_color="firebrick", source=source, view=view)

7.layouts
我们有http://bokeh.pydata.org/en/latest/docs/user_guide/layout.html里的
collumn
row
widgetbox
gridplot
和集大成者
layout

8.这次CSC1002可能会用上的Handling Categorical Data的问题:
http://bokeh.pydata.org/en/latest/docs/user_guide/categorical.html
在Stacked和Hover Tools那节里

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

output_file("colormapped_bars.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

p = figure(x_range=fruits, y_range=(0,9), plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

p.vbar(x='fruits', top='counts', width=0.9, color='color', legend="fruits", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)
