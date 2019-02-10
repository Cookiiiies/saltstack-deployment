from os import listdir, environ
import subprocess

for deployment_yaml in [
    filename for filename in listdir('{dir}/k8s_descriptions'.format(dir=environ['HOME'])) if filename.endswith(".yaml")
]:
    subprocess.run(
        [
            "kubectl",
            "apply",
            "-f",
            "{dir}/k8s/{name}".format(dir=environ['TRAVIS_BUILD_DIR'], name=deployment_yaml)
        ]
    )
