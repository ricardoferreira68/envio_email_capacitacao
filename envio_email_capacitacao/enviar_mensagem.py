"""Envia mensagem por e-mail a partir do arquivo csv.
"""

import pandas as pd  # Usado para ler arquivo .csv
import smtplib
from email.message import Message
import os


def enviar_emails(arquvio_csv: str) -> None:
    """Envia mensagem por email a partir dos dados contidos no arquivo_csv.

    Args:
        arquvio_csv (str): nome do arquivo em disco contendo os dados para envio da mensagem.
    """

    dados_das_mensagens  = le_arquivo_com_dados_das_mensagens(arquvio_csv)  # Ex:mensagem_capacitacao.csv


    for dads_de_uma_mensagem in dados_das_mensagens.itertuples():

        # Validar o campo "email"
        if not(dads_de_uma_mensagem[1] is None or dads_de_uma_mensagem[1] == "" or dads_de_uma_mensagem[1] == "\n"):
            enviar_email(   email=dads_de_uma_mensagem[1], 
                            assunto=dads_de_uma_mensagem[2], 
                            corpo=dads_de_uma_mensagem[3])


def le_arquivo_com_dados_das_mensagens(arquivo: str)  -> pd.core.frame.DataFrame:
    """ Ler o arquivo com as mensagens a serem enviadas
        Linha de mensagem finalizada com | (para aceitar enter no meio da mensagem).

    Args:
        arquivo (str): nome do arquivo .csv gravado em disco.

    Returns:
        pd.core.frame.DataFrame: dataframe pandas contendo as mensagens lidas do arquivo.
    """

    dataframe_com_dados_das_mensagens = pd.read_csv(arquivo, sep='|', header=[0])

    return dataframe_com_dados_das_mensagens


def enviar_email(email: str, assunto: str, corpo: str) -> None:
    """Envia um única mensagem.

    Args:
        email (str): endereço de e-mail para onde a mensagem deve ser enviada.
        assunto (str): Subject da mensagem a ser enviada.
        corpo (str): Texto da mensagem a ser enviada.
    """

    msg = Message()
    msg['From'] = "joseferreira@lampp-it.com.br"
    msg['To'] = email
    msg['Bcc'] = "joseferreira@lampp-it.com.br"
    msg['Subject'] = assunto
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg['From'], os.environ["PASSWORD"])
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode("utf-8"))
