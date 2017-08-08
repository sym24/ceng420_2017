import os
from chromosome import Chromosome
from jinja2 import Environment, FileSystemLoader

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(os.path.sep, os.path.dirname(os.path.abspath(__file__)), '/templates'))
#path += "/templates"
print path
	
c = Chromosome()
c.generate_genes(10, 5, 0)

with open('classifier_test.py', 'w') as f:
	context = {
		'chromosome':c
	}
	rendering = Environment(loader=FileSystemLoader(path)).get_template('classifier_template.py').render(context)
	f.write(rendering)