from os import listdir, environ
import subprocess

for deployment_yaml in [filename for filename in listdir('{}/k8s'.format(environ['HOME'])) if filename.endswith(".yaml")]:
    subprocess.run(["kubectl", "apply", "-f", "{}".format(deployment_yaml)])

