import requests #this library was used to get the data from a site and at the end it was used to post the result
import json #this library was used to read the data
import hashlib #this one was used to write the result in sha1
import string #this library was used to translate the caesear cypher
import collections #this one was used to create the strings 

r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=TOKEN')
r_dict = r.json()

num = r_dict['numero_casas']
chave = int(num)
cifra = r_dict["cifrado"]
mensagem = cifra.lower()
decifra = r_dict["decifrado"]

def cesar(rotate_string, number_to_rotate_by):

    lower = collections.deque(string.ascii_lowercase)

    lower.rotate(chave)

    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_lowercase, lower))

decifrado = cesar(mensagem, chave)
rs = hashlib.sha1(decifrado.encode())
resumo = rs.hexdigest()
ans = {"numero_casas":(chave), "token":"%s" %(r_dict['token']), "cifrado":"%s" %mensagem, "decifrado":"%s" %decifrado, "resumo_criptografico":"%s" %resumo}
    
with open('answer.json', 'w') as write_file:
    json.dump(ans, write_file)

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=TOKEN'

result = requests.post(url, files={"answer": open("answer.json", "rb")})

print(result.status_code)
print(result.text)