import os
from chromosome import Chromosome
from classify_hands import join_dirs
from jinja2 import Environment, FileSystemLoader

path = os.path.dirname(os.path.abspath(__file__))
path = join_dirs(path, "templates")
print path
	
c = Chromosome()
c.generate_genes(10, 5, 0)

with open('classifier_test.py', 'w') as f:
	context = {
		'function_name':'yoyo',
		'chromosome':c
	}
	rendering = Environment(loader=FileSystemLoader(path)).get_template('classifier_template.py').render(context)
	f.write(rendering)