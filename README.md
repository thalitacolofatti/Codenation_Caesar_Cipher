Caesar Cipher Challenge
Codenation AceleraDev Challenge: Solutions, Explanations & References.

This repository includes some useful information about the latest Codenation AceleraDev Challenge: the Caesar Cipher Algorithm. Solving this Challenge is the first step to apply to the Acceleration programs in C#, React, ReactNative, and others available between March 31rd and April 20th, 2020.

About the Algorithm:
The Caesar Cipher Algorithm is an example of a Substitution Cipher. Each letter of a text is switched by another and this change is made using a designated number of steps downward the alphabet sequence. This algorithm is named after Caesar because of its use in communications between the Roman Emperor and his Generals.

**Examples:**

Normal:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphered: DEFGHIJKLMNOPQRSTUVWXYZABC, with a designated number of 3

Normal:  a ligeira raposa marrom saltou sobre o cachorro cansado
Ciphered: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR, with a designated number of 3

References on Wikipedia:
https://pt.wikipedia.org/wiki/Cifra_de_César

About the Challenge:
The current Challenge requests the prospective student to perform three steps, described below:

1st Step: Write a program, in any programming language, that performs an HTTP Request to the URL below and captures a JSON object to be processed further.

URL: https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

Obs: You must personalize the URL with your TOKEN, available at the Codenation website's profile page.

2nd Step: Decipher the ciphered text snippet and evaluate its Hash Value using any SHA-1 or library available in yout target programming language. Update the JSON object with the obtained results and save it in a file named "answer.json".

Example: JSON object received on 1st Step

{ "numero_casas": 10, "token":"token_do_usuario", "cifrado": "texto criptografado", "decifrado": "aqui vai o texto decifrado", "resumo_criptografico": "aqui vai o resumo" }

3rd Step: Submit your answer.json file to the Challenge API, located in a target URL, using a POST Request.

Target URL: https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN

Obs: You must personalize the URL with your TOKEN, available at the Codenation website's profile page.

About the API:

The API is waiting for a file to be sent as a "multipart/form-data", as if it was sent by an "HTML form", with a "type file" field named "answer". Consider this while sending the file.

References on Codenation Website:
https://www.codenation.dev/aceleradev/csharp-sp-4/challenge/dev-ps

About my Solution:
My solution was written using Python and five libraries: requests, json, string, collections and hashlib.

Requests made the entry (using get) and the result delivery(using post).

Json interpreted the entry and it was used to obtain the variables and at the end to make the file to be sent.

String and Collections were used to decrypt the message by Caesar Cipher. I discovered this method by watching John Hammond's Youtube Channel after something in my algorithm was ruined. I had to altered some codes as debug didn't recognize some parts of his commands (for example: string.maketrans(), Python 3.8 didn't recognize this command, so I had to change it and I have found that it accepts str.maketrans())

Finally, Hashlib encodes the message translated into sha1. 


Step 01: Python - imported all the libraries necessary.

Step 02: Getting the initial JSON String:

The GET Request was made to the URL using the requests module.

If not previously installed, run cmd on the directory that python was installed and use the code execution: pip install requests

requests.get('url')
var = r.json()

With this command it is possible to declare the key to decipher the message and the ciphered message, after this it is possible to use them to process the result message and the sha1 digest.

Step 03: Deciphering the Ciphered Message:

The Deciphering function was based on the positions of the letters on the ASCII lowercase string.

The string with the alphabet in the correct order is provided by the command: collections.deque(string.ascii_lowercase)

The string with the alphabet is rotated respecting the key and the order.

As the string only contains letters, all numers and characters that aren't letter are maintained. This was a premise os the Challenge.

After both strings were declared, the traslation was processed using the return:
rotate_string.translate(str.maketrans(string.ascii_lowercase, lower))

Only lower case was declared because the challenge asked this way.

Step 04: Evaluating the SHA-1 HASHLIB function:

Hashlib library already came with Python installation.

With the previous result in hands, it was executed the command hashlib.sha1() but it was necessary to transform the string into byte using: .encode(), because that the only format hashlib.sha1 accepts.

To finish the digest, the command .hexdigest() gives the last result to make the answer.

Step 05: Saving the final JSON into an answer.json File

To create the file Json with the answer, first, it was declared a python dictionary to collect all the results processed:

ans = {"numero_casas":(chave), "token":"%s" %(r_dict['token']), "cifrado":"%s" %mensagem, "decifrado":"%s" %decifrado, "resumo_criptografico":"%s" %resumo}

Then the open('answer.json', 'w') prepared to write a file with the command json.dump(ans, write_file), that saved a file on the directory.

Final Aspect of "answer.json" file:

  {
  	"numero_casas":11,
  	"token":"MY_TOKEN",
  	"cifrado":"lww jzf yppo td wzgp. mfe l yph altc zq dszpd ypgpc sfce lyjmzoj. fyvyzhy",
  	"decifrado":"all you need is love. but a new pair of shoes never hurt anybody. unknown",
  	"resumo_criptografico":"a90cb2b12cf5c2f2a49c71be430156b19c211648"
  }
  
Step 06: Posting the result where is required:

In order to properly communicate with the API, the HTML form has to be configured in a specific manner, embracing all the guidelines priorly stated:

result = requests.post(url, files={"answer": open("answer.json", "rb")})

Finally, the print(result.status_code) to test and print(result.text) to send.

More Information:
Target & Obtained Score:
Challenge Completion and Target Score of 100% are mandatory to proceed to the interviews.

My Obtained Score: 100%

Contacts:
Thalita Colofatti thalitacolofatti@gmail.com

Codenation Website:
https://www.codenation.dev

AceleraDev - Open Sessions:
https://www.codenation.dev/aceleradev

Community:
https://comunidade.codenation.dev/

Further Informations:
websitecontato@codenation.dev