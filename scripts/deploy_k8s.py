from os import listdir
import subprocess

for deployment_yaml in [filename for filename in listdir('../k8s') if filename.endswith(".yaml")]:
    subprocess.run(["kubectl", "apply", "-f", "{}".format(deployment_yaml)])

