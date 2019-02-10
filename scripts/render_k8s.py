from jinja2 import Template
from os import environ, listdir



for jinja_template in [filename for filename in listdir('{}/k8s'.format(environ['TRAVIS_BUILD_DIR'])) if filename.endswith(".jinja2")]:
    
    path = "{dir}/k8s/{name}".format(dir=environ['TRAVIS_BUILD_DIR'], name=jinja_template)
    print("openfile: {}\n".format(path))
    with open(path) as file:
        
        print("render file")
        template = Template(file.readlines())
        output_filename = jinja_template.replace(".jinja2")
        
        path = "{dir}/k8s_descriptions/{name}".format(dir=environ['HOME'], name=output_filename)
        print("output to: {}\n".format(path))
        with open(path, "w") as output_file:
            output_file.write(template.render(environ))
