import logging
import subprocess
logging.basicConfig(filename='deployment.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
application_name = 'my_app'
try:
    subprocess.run(['kubecl','apply', '-f' f'{application_name}.yaml'], check=True)
    logging.info(f"successfully deployed the applicaton f{application_name} to kubernetes")
except subprocess.CalledProcessError as e:
    logging.ERROR(f'Encountered exception during deployment :{e}')
