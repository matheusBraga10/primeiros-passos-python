import smtplib
import email.message

def enviar_email():
    corpo_email = '''<p>Olá Fulano, aqui é o Matheus</p>

    <p>O faturamento da loja foi de R$ {faturamento},00</p>
    <p>Vendemos {quantidade_podutos} produtos</p>
    <p>O ticket médio foi e R$ {ticket_medio},00</p>

    <p>Abraços,</p>
    <p>Matheus.</p>''' #'Corpo do E-mail'

    msg = email.message.Message()
    msg['Subject'] = 'Curriculo - TI - Matheus' #'Assunto'
    msg['From'] = 'matheusfbraga10#gmail.com' #'Remetente'
    msg['To'] = '' #'Destinatário
    password = '' #'Senha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Logiin Credentiais for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'])
#Criando integração com o e-mail
outlook = win32.Dispatch('outllok.application')

#criar um e-mail
email = outlook.CreateItem(0)


faturamento = 1500
quantidade_podutos = 10
ticket_medio = faturamento/quantidade_podutos

#configurar as informaçẽos do seu e-mail
email.To = "pythonimpressionador@gmail.com; pythonimpressionador+lira@gmail.com" #'destino'
email.Subject = 'E-mail automático do Python' #'assunto'
email.HTMLBody = f'''
<p>Olá Fulano, aqui é o Matheus</p>

<p>O faturamento da loja foi de R$ {faturamento},00</p>
<p>Vendemos {quantidade_podutos} produtos</p>
<p>O ticket médio foi e R$ {ticket_medio},00</p>

<p>Abraços,</p>
<p>Matheus.</p>''' #'Corpo do E-mail'

anexo1 = 'c://home/matheus/Documentos/MeusProjetos/...'
email.Attachments.Add(anexo1)

email.Send()
print('E-mail enviado')
