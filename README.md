# 📰WebScraping de Notícias

Este código consegue capturar de forma automática, até as 10 últimas notícias de um dos seguintes sites: G1, UOL, Folha de São Paulo, CNN e Jovem Pan e exibi-las em um arquivo PDF

[![Link](https://img.shields.io/badge/Clique%20Aqui%20%20para%20baixar%20%20o%20%20execut%C3%A1vel-808080?style=for-the-badge)](https://pedrolima.tech/assets/UltimasNoticias.rar)

## Ferramentas 🛠️
 - Pytyhon
 - Tkinter
 - BeatifulSoup
 - urllib
 - reportlab

## Instruções 📄
 - Descompacte o arquivo UltimasNoticias.rar
 - Primeiro faça o Download do arquivo .exe clicando no botão que esta acima ou na seguinte URL: https://pedrolima.tech/assets/UltimasNoticias.rar
 - Execute o programa main.exe
 - Informe a quantidade de notícias que deseja
 - Aperte no botão Gerar PDF
 - Os arquivos PDFs vão ser gerados dentro da pasta projeto (Pasta onde está localizado o arquivo main.exe)
 - As notícias coletadas vão ser sempre as mais recentes, pois a cada novo pedido de geração de PDF, o programa acessa os sites e coleta as informações mais recentes

## Em caso de erro ⚠
![Erro](https://github.com/Pedro101520/WebScraping_de_Noticias/assets/105872928/a508c8df-4351-48ea-9690-1cdaae4fc6e7)

Se aparecer uma mensagem igual a da foto acima quando você executar o main.exe, você terá que instalar o Microsoft Visual C++ Redistributable for Visual Studio, que poderá ser baixado pela seguinte URL: https://aka.ms/vs/16/release/vc_redist.x64.exe
Esse erro geralmente ocorre devido à falta de algumas bibliotecas ou DLLs necessárias no sistema onde o executável está sendo executado. No caso específico do erro mencionado ("api-ms-win-crt-stdio-l1-1-0.dll"), ele está relacionado à ausência de uma atualização do Visual C++ redistribuível no sistema.
