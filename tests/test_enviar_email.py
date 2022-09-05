from envio_email_capacitacao import enviar_mensagem


def test_enviar_email():
    assert enviar_mensagem.enviar_email("mensagem_capacitacao.csv") == None
