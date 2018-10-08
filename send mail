import smtplib      #library for email service

server = smtplib.SMTP('smtp.gmail.com',576)   #selecting the server
server.starttls()
toid = 'email id of receiver'
fromeid = 'email id of sender' 
server.login('your email id','your email id password')
server.sendmail(fromid,toid,"message")  #here 3rd parameter as your mail body 
server.quit()     #closing the server
