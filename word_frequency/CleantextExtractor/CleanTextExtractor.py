import re
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

chromeAdBlockPath = os.path.join(os.path.dirname(__file__), '', 'chrome_adblock_rules.crx')
optionsChrome = webdriver.ChromeOptions()
optionsChrome.add_argument('user-agent={0}'.format(user_agent))
optionsChrome.add_argument('--headless')
optionsChrome.add_extension(chromeAdBlockPath)
optionsChrome.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})

firefoxAdBlockPath = os.path.join(os.path.dirname(__file__), '', 'firefox_adblock_rules.xpi')
optionsFirefox = webdriver.FirefoxOptions()
optionsFirefox.add_argument('user-agent={0}'.format(user_agent))
optionsFirefox.add_argument('--headless')
optionsFirefox.set_preference("network.cookie.cookieBehavior", 2)


class CleanTextExtractor:
    def __init__(self, firefox=False, chrome=False):
        if chrome:
            self.chrome_browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                                   options=optionsChrome)
        elif firefox:
            self.firefox_browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                                     options=optionsFirefox)
            self.firefox_browser.install_addon(firefoxAdBlockPath, temporary=True)
        else:
            exit('Driver non selezionato')

    def getPageChrome(self, url):
        self.chrome_browser.get(url)
        source = self.chrome_browser.page_source
        return self.extract_meaningfull_text(source)

    def getPageFirefox(self, url):
        self.firefox_browser.get(url)
        source = self.firefox_browser.page_source
        return self.extract_meaningfull_text(source)

    def remove_emojis(self, data):
        emoji = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", re.UNICODE)
        return re.sub(emoji, '', data)

    def extract_meaningfull_text(self, content):
        soup = BeautifulSoup(content, 'html.parser')  # lxml
        for data in soup.findAll([
            'script',
            'style',
            'noscript',
            'footer',
            'header',
            'img',
            'aside',
            'svg',
            'nav',
            'button',
            'form',
            'head',
            'figure',
            'img',
            'ins',
            'link',
            'table',
            'meta'
        ]):
            data.decompose()
        final = re.sub('\n', '', ' '.join(soup.stripped_strings))
        return self.remove_emojis(final)
