# Настройка параметров Selenium WebDriver
# Для Chrome
# 1. Импорт опций Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 2. Инициализация опций Chrome
chrome_options = Options()

# 3. Добавление желаемых возможностей
chrome_options.add_argument("--disable-extensions")

# 4. Добавление желаемых возможностей сессии
driver = webdriver.Chrome(chrome_options=chrome_options)

# Для Firefox
# 1. Импорт опций Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 2. Инициализация опций Firefox
firefox_options = Options()

# 3. Добавление желаемых возможностей
firefox_options.set_headless()

# 4. Добавление желаемых возможностей сессии
driver = webdriver.Firefox(options=firefox_options)

