"""Envia mensagem por e-mail aos participantes da capacitação a patir de um arquivo csv.

    Dado que: os dados dos participantes na capacitação são inseridos na planilha de controle 
        e a aba 'csv_mensagem' é formatada com os dados da mensagem com email|assunto|corpo|tabela
    Quando: for gerado o arquivo 'mensagem_capacitacao.csv'
    Então: enviar e-mail para cada participante encontrado no arquivo 'mensagem_capacitacao.csv'
"""

from enviar_mensagem import enviar_emails


if __name__ == "__main__":
    print("Enviando e-mails ...")
    enviar_emails("mensagem_capacitacao.csv")
    print("e-mails envidados ...")
