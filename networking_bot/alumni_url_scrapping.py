from time import sleep

from typing import List, Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


BASE_QUERY_URL = 'https://www.linkedin.com/search/results/people/?origin=FACETED_SEARCH'
ALUMNI_NM_SPAN_CLASS_NM = 'entity-result__title-line'
ALUMNI_NM_LINK_CLASS_NM = 'app-aware-link'

def get_alumnis_url(
    driver: webdriver.Chrome,
    page_to_scrapped:int,
    school_code: str,
    job_title_nm: str
    ) -> List[Union[List[str], bool]]:

    alumnis_url = []

    school_query_url = BASE_QUERY_URL + '&network=%s&schoolFilter=%s&title=%s&page=%d' % (
        '%5B"S"%5D',
        '%5B"'+school_code+'"%5D',
        "%20".join(job_title_nm.split(" ")),
        page_to_scrapped
    )

    driver.get(school_query_url)

    try:
        alumni_nm_spans = WebDriverWait(driver, 10).until(
            lambda x: x.find_elements(By.CLASS_NAME, ALUMNI_NM_SPAN_CLASS_NM)
        )
    except TimeoutException:

        return [], True

    for alumni_nm_span in alumni_nm_spans:

        a = alumni_nm_span.find_element_by_class_name(ALUMNI_NM_LINK_CLASS_NM)
        url = a.get_attribute('href')
        url = url.split('?')[0]
        alumnis_url.append(url)

    sleep(10)

    return alumnis_url, False


