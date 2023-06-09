from senha import senha
import smtplib
import email.message

def enviar_email():
    faturamento = 1500
    quantidade_podutos = 10
    ticket_medio = faturamento/quantidade_podutos

    corpo_email = f'''
    <p>Olá Fulano, aqui é o Matheus</p>

    <p>O faturamento da loja foi de R$ {faturamento:.2f}</p>
    <p>Vendemos {quantidade_podutos} produtos</p>
    <p>O ticket médio foi e R$ {ticket_medio:.2f}</p>

    <p>Abraços,</p>
    <p>Matheus.</p>''' #'Corpo do E-mail'


    msg = email.message.Message()
    msg['Subject'] = 'Curriculo - TI - Matheus' #'Assunto'
    msg['From'] = 'matheusfbraga10@gmail.com' #'Remetente'
    msg['To'] = 'matheuscervejeiro@gmail.com; ' #'Destinatário
    password = senha #'Senha'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

     #To attach a file to the email (optional):
    #attachment  = ''
    #email.Attachments.Add(attachment)
    
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Logiin Credentiais for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('UTF-8'))
    print('Email enviado')

enviar_email()