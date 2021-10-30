from time import sleep

from networking_bot.utilities import (
    load_invite_sent_to_urls,
    update_invite_sent_to,
    load_config,
    load_or_create_status,
    update_status,
    get_driver
)
from networking_bot.alumni_url_scrapping import get_alumnis_url
from networking_bot.requesting_connection import request_connections, remove_alumnis_in_pending

# fix case where all alumnis on a given page are pending

NB_LAUNCHS = 8


def main() -> None:

    for _ in range(NB_LAUNCHS):

        config = load_config()

        invite_sent_to_urls = load_invite_sent_to_urls()
        status, job_id = load_or_create_status(config["query"])

        driver = get_driver(cookie=config['cookie'])

        alumnis_url, job_done = get_alumnis_url(
            driver,
            status['last_page_scrapped'],
            **config['query']
        )
        alumnis_url = remove_alumnis_in_pending(alumnis_url, invite_sent_to_urls)   
        status['last_page_scrapped'] += 1    

        if not job_done:

            request_connections(driver, alumnis_url)
            update_status(status, job_id, job_done)
            invite_sent_to_urls += alumnis_url
            update_invite_sent_to(invite_sent_to_urls)
            
            driver.quit()
            sleep(60*60)

        else:

            driver.quit()
            break



if __name__ == "__main__":
    main()