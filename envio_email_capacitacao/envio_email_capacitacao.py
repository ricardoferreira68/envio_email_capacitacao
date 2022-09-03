"""Envia mensagem por e-mail aos participantes da capacitação a patir de um arquivo csv.

    Dado que: os dados dos participantes na capacitação são inseridos na planilha de controle 
        e a aba "csv_mensagem" é formatada com os dados da mensagem com email|assunto|corpo|
    Quando: for gerado o arquivo "mensagem_capacitacao.csv" é gerado com a opção "Salvar Como"
    Então: enviar e-mail para cada participante encontrado no arquivo "mensagem_capacitacao.csv"
"""

from enviar_mensagem import enviar_email


if __name__ == '__main__':
    print("Enviando e-mail ...")
    enviar_email("mensagem_capacitacao.csv")
