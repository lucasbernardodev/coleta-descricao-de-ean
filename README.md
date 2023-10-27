# Web Scraping de Produtos

<p> O projeto é um script em Python que faz web scraping no site Cosmos da bluesoft para coletar as descrições dos produtos a partir de uma lista de códigos de barras em Excel. O script usa as bibliotecas pandas, BeautifulSoup e selenium para fazer a requisição, o parseamento e a extração dos dados da página web. O script gera uma nova planilha Excel com os códigos de barras e as descrições dos produtos e não utiliza nenhuma API.</p>

## Requisitos
<p>Para executar este projeto, você precisa ter instalado no seu sistema operacional:</p>

- Python 3.9 ou superior
- Microsoft Edge
- Microsoft Edge Driver
- Bliblioteca pandas
- Biblioteca BeautifulSoup
- Selenium

## Instalação
<p>Instação das bibliotecas usando o gerenciador de pacotes do Python, o pip:</p>
- pip install pandas 
- pip install beautifulsoup4 
- pip install selenium

## Como usar
<p>Para usar este projeto, você precisa seguir os seguintes passos:</p>

1. Clone ou baixe este repositório para o seu computador.
2. Crie uma planilha Excel chamada “barcodes.xlsx” com uma coluna chamada “Barcode” contendo os códigos de barras dos produtos que você quer pesquisar. Salve a planilha na mesma pasta do projeto.
3. Abra o terminal ou o prompt de comando e navegue até a pasta do projeto.
4. Execute o script com o seguinte comando: python web-scraping.py
5. Aguarde alguns minutos até o script terminar de fazer o web scraping.
6. Abra a planilha “ProdutosAtualizados.xlsx” que foi gerada na mesma pasta do projeto. Ela vai conter os códigos de barras e as descrições dos produtos.
