# Imprime-Auto
Este projeto foi realizado para auxiliar teste de Impressões  em "Etiquetas e Pulseiras" 

Gerenciador de Impressão - Interface Gráfica com Tkinter
Este projeto é uma aplicação simples em Python que utiliza a biblioteca Tkinter para criar uma interface gráfica (GUI) para selecionar e imprimir arquivos. O usuário pode escolher o arquivo, definir o número de cópias e ajustar as opções de impressão, como a largura e a altura.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
Funcionalidades
Seleção de Arquivo: O usuário pode escolher arquivos com as extensões .docx, .xlsx, .pdf e .btw para imprimir.
Número de Cópias: Permite ao usuário definir o número de cópias que deseja imprimir.
Opções de Largura e Altura: O usuário pode configurar manualmente a largura e a altura da impressão (em centímetros).
Envio para Impressão: Os arquivos são enviados para a fila de impressão usando os comandos do sistema.
Requisitos
Python 3.x
Bibliotecas necessárias:
tkinter: para criar a interface gráfica.
win32print e win32api: para interagir com a impressora e enviar os arquivos para a fila de impressão (somente para Windows).
Instalando Dependências
Você pode instalar as dependências necessárias usando o comando abaixo:

pip install pywin32
-----------------------------------------------------------------------------------------
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
--------------------------------------------------------------------------------------------
python gerenciador_impressao.py
-------------------------------------------------------------------------------------------
3. Funcionalidades da Interface
Selecionar Arquivo: Clique no botão "Selecionar Arquivo" e escolha o arquivo que deseja enviar para a impressora.
Número de Cópias: Digite o número de cópias que deseja imprimir no campo correspondente.
Mais Opções: Clique no botão "Mais Opções" para definir a largura e a altura de impressão (em centímetros). Essas opções são opcionais.
Imprimir Arquivo: Após configurar as opções desejadas, clique no botão "Imprimir Arquivo" para enviar o documento à impressora.
4. Tratamento de Erros
O sistema exibe mensagens de erro caso nenhum arquivo seja selecionado ou se o número de cópias for inválido.
Valores incorretos de largura e altura também geram mensagens de erro para evitar impressões mal configuradas.

