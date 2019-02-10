from jinja2 import Environment, FileSystemLoader
from os import environ, listdir
from base64 import b64decode

# custom jinja filter
def base64_decode(value):
    return b64decode(value)


# init jinja
template_dir = '{dir}/k8s'.format(
    dir=environ['TRAVIS_BUILD_DIR']
)

jinja_env = Environment(
    loader=FileSystemLoader(template_dir),
    trim_blocks=True
)
jinja_env.filters['base64_decode'] = base64_decode

# start rendering
for jinja_template in [filename for filename in listdir(template_dir) if filename.endswith(".jinja2")]:
    print("render file: {}".format(jinja_template))
    rendered_file = jinja_env.get_template(jinja_template).render(
        environ
    )
    
    path = "{dir}/k8s_descriptions/{name}".format(
        dir=environ['HOME'],
        name=jinja_template.replace(".jinja2", "")
    )
    
    print("output to: {}\n".format(path))
    with open(path, "w") as output_file:
        output_file.write(rendered_file)


