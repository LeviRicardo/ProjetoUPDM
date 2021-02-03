from twython import Twython
from random import randint as rd
from dotenv import load_dotenv
import os
import time


def rd_frase():
	o = open('UPDM frases.txt','r',encoding = 'utf8')
	lista = o.readlines()
	final = rd(0,len(lista)-1)
	o.close()
	while '<Ep ' in lista[final]:
		final = rd(0,len(lista)-1)
	return str((lista[final]).rstrip('\n'))


load_dotenv()

ConsumerKey = os.getenv('TCONSUMER')
SecretKey = os.getenv('TCSECRET')
Token = os.getenv('TTOKEN')
SecretToken = os.getenv('TTSECRET')

account = Twython(ConsumerKey,SecretKey,Token,SecretToken)

while True:
	text = rd_frase()
	if text == True:
		continue
		
	account.update_status(status = text)

	time.sleep(6300)
