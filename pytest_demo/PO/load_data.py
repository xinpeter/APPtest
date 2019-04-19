import yaml
import os,sys

def load_data(file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    sys.path.append(base_dir)
    with open('%s/data/%s.yml' %(base_dir,file_name) ,'r') as f:
        data = yaml.safe_load(f)
    return data
