from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = '/home/wallison/projetos-python/materiais-wfm/chromedriver'


def main():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              options=options
                              )
    driver.get("https://google.com.br")
    print(driver.title)
    driver.close()


if __name__ == '__main__':
    start = datetime.now()
    main()
    print(datetime.now() - start)
