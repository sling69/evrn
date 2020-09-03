import sys, smtplib, ssl

port = 587  # For TLS
smtp_server = "smtp.office365.com"
sender_email = "sye@dqri.net"  # Enter your address
receiver_email = "sye184.c0c83fc@m.evernote.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = "test"
#message = """\
#Subject: Hi there

#This message is sent from Python."""
#
    if len(sys.argv)<2:
        print('evrn.py <note title>')
        sys.exit(2)
    else: 
        message = str(sys.argv)

    #context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
connection = smtplib.SMTP(smtp_server, port)
#with smtplib.SMTP_SSL(smtp_server, port) as server:
connection.starttls(context=context)
connection.login(sender_email, password)
connection.sendmail(sender_email, receiver_email, message)