from os import listdir, environ
from subprocess import check_call


dir = '{dir}/k8s_descriptions'.format(dir=environ['HOME'])

for deployment_yaml in sorted([
    filename for filename in listdir(dir) if filename.endswith(".yaml")
]):
    
    check_call(
        [
            "kubectl",
            "apply",
            "-f",
            "{dir}/{name}".format(dir=dir, name=deployment_yaml)
        ]
    )
