from time import sleep

from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

def request_connection(driver: webdriver.Chrome, person_url: str) -> None:

    PROFILE_ACTIONS_WEB_EL_CLASS_NM = 'pvs-profile-actions'
    MODAL_SEND_INVITE_WEB_EL_CLASS_NM = 'ml1'

    driver.get(person_url)

    profile_actions_web_el = WebDriverWait(driver, 20).until(
        lambda x: x.find_element(By.CLASS_NAME, PROFILE_ACTIONS_WEB_EL_CLASS_NM)
    )

    request_connections_web_el = profile_actions_web_el.find_element_by_tag_name("button")
    request_connections_web_el.click()

    modal_send_invite_web_el = WebDriverWait(driver, 20).until(
        lambda x: x.find_element(By.CLASS_NAME, MODAL_SEND_INVITE_WEB_EL_CLASS_NM)
    )
    try:
        modal_send_invite_web_el.click()
    except ElementClickInterceptedException:
        pass #case where alumni is 'influencer'


def request_connections(driver:webdriver.Chrome, persons_url: List[str]) -> None:

    for person_url in persons_url:
        request_connection(driver, person_url)
        sleep(30)


def remove_alumnis_in_pending(
    alumnis_url:List[str],
    alumnis_networked_url:List[str]
    ) -> List[str]:

    return [
        alumni_url for alumni_url in alumnis_url
        if alumni_url not in alumnis_networked_url
        ]

