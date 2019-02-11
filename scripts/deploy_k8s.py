from os import listdir, environ
from subprocess import check_call, STDOUT


dir = '{dir}/k8s_descriptions'.format(dir=environ['HOME'])

for deployment_yaml in sorted([
    filename for filename in listdir(dir) if filename.endswith(".yaml")
]):
    path = "{dir}/{name}".format(dir=dir, name=deployment_yaml)
    print("Deploy yaml from: {}\n".format(path))
    check_call(
        [
            "kubectl",
            "apply",
            "-f",
            path
        ],
        stdout=STDOUT,
        stderr=STDOUT
    )
