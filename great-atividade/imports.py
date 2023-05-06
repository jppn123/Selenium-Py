from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.color import Color
from time import sleep

class Imp():
    URL = 'https://testlink.org/'
    TITLE = 'TestLink'
    BTAGTEXT = '(1.9.20 - Raijin)'
    XPATHIFRAME = '//iframe[@title="Flattr"]'
    IFRAMECONTENT = 'File not found.'
    XPATHROWMARKETING = '//*[@class="col-lg-6"]'
    XPATHGITHUBANCHOR = '//a[@href="https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/"]'
    GITHUBANCHORTITLE = 'GitHub - TestLinkOpenSourceTRMS/testlink-code at testlink_1_9_20_fixed'
    BEFOREXPATHINPUTGITHUB = '//input[@class="form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field is-clearable"]'
    AFTERXPATHINPUTGITHUB = '//input[@class="form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field"]'
    LISTAXPATHSGITHUT = ['//span[@data-search-type="Code"]',
                         '//span[@data-search-type="Commits"]',
                         '//span[@data-search-type="Issues"]',
                         '//span[@data-search-type="Discussions"]',
                         '//span[@data-search-type="RegistryPackages"]',
                         '//span[@data-search-type="Wikis"]'
                         ]
   