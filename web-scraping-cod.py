import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

tabela = pd.read_excel("barcodes.xlsx")
descricoes = []

driver = webdriver.Edge()

for codigo_de_barras in tabela["Barcode"]:
    url = "https://cosmos.bluesoft.com.br/produtos/" + str(codigo_de_barras)

    driver.get(url)

    driver.implicitly_wait(10)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    span = soup.find("span", id="product_description")

    if span:
        descricao = span.text.strip()
        descricoes.append(descricao)
    else:
        descricoes.append("")

driver.close()

tabela["Descrição"] = descricoes
tabela.to_excel("ProdutosAtualizados.xlsx", index=False)