from typing import Dict, List, Union

import yaml

from selenium import webdriver


def load_config() -> Dict:
    
    with open('./config.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return config


def load_or_create_status(query:Dict) -> List[Union[Dict, str]]:

    job_id = get_job_id(query['school_code'], query['job_title_nm'])

    try:
        status = load_status(job_id)
    except FileNotFoundError:
        status = {'job_done':False, 'invite_sent_to_urls':[]}
        save_status(status, job_id)
    
    return [status, job_id]


def get_job_id(school_code:str, job_title_nm:str) -> str:

    job_title_nm = replace_space_by_underscore(job_title_nm)

    return '{}_{}'.format(school_code, job_title_nm)


def replace_space_by_underscore(text:str) -> str:

    return text.replace(' ', '_')


def load_status(job_id:str) -> Dict:

    with open('status/{}.yaml'.format(job_id), 'r') as f:
        status = yaml.load(f, Loader=yaml.FullLoader)

    return status


def save_status(status:Dict, job_id:str) -> None:

    with open('status/{}.yaml'.format(job_id), 'w') as f:
        yaml.dump(status, f)


def update_status(status:Dict, job_id:str, job_done:bool) -> None:

    if job_done:
        status['job_done'] = True
    else:
        status['job_done'] = False

    save_status(status, job_id)
    

def get_driver() -> webdriver.Chrome:

    options = webdriver.ChromeOptions()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome(executable_path= "./chromedriver.exe", chrome_options=options)

    return driver