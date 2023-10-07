# Import librarie
import pandas as pd
from jinja2 import Environment, FileSystemLoader
# Load the data 
OTU = pd.read_csv('OTU_table.csv',header=(0))


# load the env where the template is present 
env = Environment(loader=FileSystemLoader('template_format'))

# Load the template file
template = env.get_template('template.html')

# Render the template with variables
html = template.render(page_title_text='Report',
                       content_1='Content 1',
                       content_2= 'Content 2',
                       otu_table=OTU)

# Write the template to an HTML file
with open('html_report_output.html', 'w') as f:
    f.write(html)