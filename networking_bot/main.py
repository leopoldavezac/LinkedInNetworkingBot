from time import sleep

from networking_bot.utilities import (
load_config,
load_or_create_status,
update_status_f,
get_driver
)
from networking_bot.alumni_url_scrapping import get_alumnis_url
from networking_bot.login import login
from networking_bot.requesting_connection import request_connections

NB_LAUNCHS = 8

def main() -> None:

    for _ in range(NB_LAUNCHS):

        config = load_config()
        status, status_file_nm = load_or_create_status(config["query"])

        driver = get_driver()
        login(driver, **config["login"])

        alumnis_url, job_state = get_alumnis_url(
            driver,
            **config['query'],
            page_index=status['last_page_scrapped']+1
        )
        update_status_f(status, status_file_nm, job_state)
        
        if job_state == False:
            break

        request_connections(driver, alumnis_url)

        driver.quit()

        sleep(60*60)



if __name__ == "__main__":
    main()