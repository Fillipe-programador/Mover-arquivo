from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import shutil
from pathlib import Path

pasta = Path(r"C:\Users\Usuario\Downloads")
pasta_mover = Path(r"C:\Users\Usuario\OneDrive\Área de Trabalho\testes\arquivos")
pasta_antes = set(pasta.iterdir())

options = Options()

options.add_argument(r"--user-data-dir=C:\seleniumprofile")
options.add_argument("--profile-directory=Default")

nav = webdriver.Chrome(options=options)
nav.maximize_window()
nav.get("https://brackeysgames.itch.io/brackeys-platformer-bundle")
butao = nav.find_element("class name", "button.buy_btn")
butao.click()
sleep(2)
thanks = nav.find_element("class name", "direct_download_btn")
thanks.click()
sleep(2)
dowload = nav.find_element("class name", "button.download_btn")
dowload.click() # Quero mover esse dowload aqui

sleep(2)
pasta_atual = set(pasta.iterdir())
nova_pasta = pasta_atual - pasta_antes

for i in nova_pasta:
    shutil.move(i, pasta_mover)

sleep(100)
