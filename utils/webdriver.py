from selenium import webdriver
from selenium.webdriver.edge.service import Service

def setup_driver(driver_path):
    options = webdriver.EdgeOptions()
    options.add_argument('--start-maximized')
    service = Service(driver_path)
    return webdriver.Edge(service=service, options=options)
