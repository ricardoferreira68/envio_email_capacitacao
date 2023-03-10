"""Envia mensagem por e-mail a partir do arquivo csv.
"""


import smtplib
from email import encoders
from email.message import Message
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from pandas import read_csv
from pandas.core.frame import DataFrame


def enviar_emails(arquvio_csv: str) -> None:
    """Envia mensagem por email a partir dos dados contidos no arquivo_csv.

    Args:
        arquvio_csv (str): nome do arquivo em disco contendo os dados para envio da mensagem.
    """

    dados_das_mensagens = le_arquivo_com_dados_das_mensagens(
        arquvio_csv)  # Ex:mensagem_capacitacao.csv

    contador: int = 0
    for dads_de_uma_mensagem in dados_das_mensagens.itertuples():

        # Validar o campo "email"
        if not (dads_de_uma_mensagem[1] is None or dads_de_uma_mensagem[1] == "" or dads_de_uma_mensagem[1] == "\n"):

            enviar_email(email=dads_de_uma_mensagem[1],
                         assunto=dads_de_uma_mensagem[2],
                         corpo=dads_de_uma_mensagem[3],
                         anexos= [] if dads_de_uma_mensagem[4]==["Sem anexo"] else dads_de_uma_mensagem[4].split(","))
            contador += 1
            print(f"{contador}, ")


def le_arquivo_com_dados_das_mensagens(arquivo: str) -> DataFrame:
    """ Ler o arquivo com as mensagens a serem enviadas
        Linha de mensagem finalizada com | (para aceitar enter no meio da mensagem).

    Args:
        arquivo (str): nome do arquivo .csv gravado em disco.

    Returns:
        DataFrame: dataframe pandas contendo as mensagens lidas do arquivo.
    """

    dataframe_com_dados_das_mensagens = read_csv(
        arquivo, sep='|', header=[0])

    return dataframe_com_dados_das_mensagens


def enviar_email(email: str, assunto: str, corpo: str, anexos: list) -> None:
    """Envia um única mensagem.

    Args:
        email (str): endereço de e-mail para onde a mensagem deve ser enviada.
        assunto (str): Subject da mensagem a ser enviada.
        corpo (str): Texto da mensagem a ser enviada.
        anexos (list): Relação de nomes, com caminho, dos arquivos anexos.
    """

    # cria o servidor SMTP
    # context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server = smtplib.SMTP("smtp.gmail.com: 587")
    # server.starttls()
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Definição do cabeçalho da mensagem.
    msg = MIMEMultipart() 
    msg['From'] = "joseferreira@lampp-it.com.br"
    msg['To'] = email
    msg['Cc'] = ""  # "dp@lampp-it.com.br"
    msg['Cc2'] = "joseferreira@lampp-it.com.br"  # Cópia oculta.
    msg['Subject'] = assunto
    msg.add_header("Content-Type", "Content-Transfer-Encoding")
    

    # Arquivo Anexo
    # anexos = ["/home/ricardo/Documentos/Trabalho em casa/git cheat sheet.pdf"]
    # anexos = ["/home/ricardo/Documentos/Trabalho em casa/git cheat sheet.pdf", 
    #          "/home/ricardo/Documentos/Trabalho em casa/git - book.pdf",
    #          "/home/ricardo/Documentos/Trabalho em casa/Book Pro Git.pdf", 
    #          "/home/ricardo/Documentos/Trabalho em casa/github-git-cheat-sheet.pdf"]
    if anexos != ['Sem anexo']:
        for anexo in anexos:
            filename = anexo.rsplit("/", 1)[1].strip()
            attachment = MIMEBase('application', 'octet-stream')
            with open(anexo.strip(), 'rb') as f:
                attachment.set_payload(f.read())
            encoders.encode_base64(attachment)
            attachment.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
            msg.attach(attachment)
  
    msg.attach(MIMEText(corpo, 'html')) 
    server.login(msg['From'], "lA2021,.aL&uk")  # os.environ["PASSWORD"])
    to_receivers = [msg['To']]
    if msg['Cc'] != "" and msg['Cc'] is not None: to_receivers.append(msg['Cc'])
    if msg['Cc2'] != "" and msg['Cc2'] is not None: to_receivers.append(msg['Cc2'])
    server.sendmail(msg['From'], to_receivers, msg.as_string().encode("utf-8"))
