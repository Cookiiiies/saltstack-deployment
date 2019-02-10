from jinja2 import Template
from os import environ, listdir


for jinja_template in [filename for filename in listdir('{}/k8s'.format(environ['HOME'])) if filename.endswith(".jinja2")]:
    
    print("openfile: {}\n".format(jinja_template))
    with open(jinja_template) as file:
        
        print("render file: {}\n".format(jinja_template))
        template = Template(file.readlines())
        output_filename = jinja_template.replace(".jinja2")
        
        print("output to: {}\n".format(output_filename))
        with open(output_filename, "w") as output_file:
            output_file.write(template.render(environ))
