def bubble_chart(input_file,output_file):
    '''Creates a bubble chart from input data, for a specific example. Will be made more generic soon.
       Input is a csv file, outputs an html file'''

    from bokeh.io import output_file,save
    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource,HoverTool,tools
    import bokeh.palettes as bp
    import pandas as pd

    # Read in data from a csv file to a dataframe
    
    mydata = pd.read_csv(filename)

    mycolors = bp.Blues7
    # Use ColumnDataSource to configure data
    
    source = ColumnDataSource(data = dict(names = mydata['Researcher Name'],fap = mydata['First Author Publications'],
                                           cap = mydata['Corresponding Author Publication'],tp = mydata['Total Publications'],
                                           ia = mydata['iclikval annotations'], coun = mydata['Country']))

    output_file(output_file) # output filename
    
    hover  = HoverTool(tooltips = [("Name","@names"),("Country","@coun"),("No: first author papers", "@fap"),
                                   ("No: corresponding author publications","@cap")])


    myplot = figure(plot_width = 600,plot_height = 600,tools = [hover,"pan","reset","box_zoom","wheel_zoom"])


    myplot.xaxis.axis_label = "Total number of peer-reviewed publications"
    myplot.yaxis.axis_label = "Number of iCLiKVAL annotations"
    myplot.circle('tp','ia',
                  size =  'fap',line_color = "navy",fill_color = mycolors,source = source)

    # Write out the bubble chart as html file
    save(myplot)




