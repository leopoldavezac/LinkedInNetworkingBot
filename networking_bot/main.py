from time import sleep

from networking_bot.utilities import (
load_config,
load_or_create_status,
update_status,
get_driver
)
from networking_bot.alumni_url_scrapping import get_alumnis_url
from networking_bot.requesting_connection import request_connections, remove_alumnis_in_pending

NB_LAUNCHS = 8

def main() -> None:

    for _ in range(NB_LAUNCHS):

        config = load_config()
        status, job_id = load_or_create_status(config["query"])

        driver = get_driver(cookie=config['cookie'])

        alumnis_url, job_done = get_alumnis_url(
            driver,
            **config['query']
        )
        alumnis_url = remove_alumnis_in_pending(alumnis_url, status['invite_sent_to_urls'])

        if not job_done:

            request_connections(driver, alumnis_url)
            status['invite_sent_to_urls'] += alumnis_url
            update_status(status, job_id, job_done)
            
            driver.quit()
            sleep(60*60)

        driver.quit()



if __name__ == "__main__":
    main()