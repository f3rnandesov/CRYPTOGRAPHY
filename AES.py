
# Importa a classe Fernet, que implementa criptografia simétrica AES (AES+128 CBC + HMAC)
from cryptography.fernet import Fernet
#... AES - (Advanced Enccryption Standard) que é um algoritmo de criptografia simétrica. A mesma chave usada para encryptar é a mesma para descryptar.
#... AES - Trabalha com blocos de 128 bits (16 bytes). A mensagem é dividida em blocos de 16 bytes e cada bloco é transformado com base a chave secreta.
#... AES-128 - O 128 se refere ao tamanho da chave, quanto maior a quantidade de bits maior a segurança e menor a velocidade.
# CBC - (Cipher Block Chaining) o AES puro só sabe criptografar um bloco de 16 bytes por vez. Mas mensagens reais são muito maiores e é preciso um modo de operação.
#... Mais clássico é o CBC (Cipher Block Chaining).
#... COMO FUNCIONA O CBC:
#... É um modo de operação usado em criptografia de dados como o AES, DES, etc. Ele define como cada bloco será cifrado e encadeado com o 
#... anterior. Usamos o CBC para ligar vários blocos de dados de forma segura.
#...
#...[M1] [M2] [M3] [M4]
#... 1. O primeiro bloco é combinado (via XOR) com um IV (vetor de inicialização) aleatório. Depois, é criptografado com AES.
#... 2. Cada bloco seguinte é combinado com o resultado do bloco anterior cifrado, e só então é criptografado.
#... ESQUEMA: 
#   C1 = AES( M1 ⊕ IV )
#   C2 = AES( M2 ⊕ C1 )
#   C3 = AES( M3 ⊕ C2 )
#   ...
#... NA DESCRIPTOGRAFIA:
#...M1 = AES⁻¹(C1) ⊕ IV
#   M2 = AES⁻¹(C2) ⊕ C1
#   ...
#... processo inverso do AES
# HMAC - (Hach-based Message Authentication Code) Como o AES-CBC só garante confidencialidade, precisamos de algo que garanta integridade (ou seja, detectar se alguém alterou o texto cifrado).
#... Conceito: HMAC = usa uma função de hash (ex: SHA-256) + uma chave secreta para gerar um código de autenticação
#... HMAC = hash(chave + mensagem)
#... Quando alguém recebe a mensagem: Ele recalcula o HMAC com a mesma chave. Se o resultado for diferente a mensagem foi alterada
# O Fernet faz tudo isso citado automaticamente: 1. Criptografa os dados com AES-128 em modo CBC | 2. Gera um HMAC-SHA-256| 3. junta tudo (IV + dados + HMAC).
#Confidencialidade → ninguém lê sem a chave

#Integridade → ninguém altera sem ser detectado

#Autenticidade → garante que veio de quem tem a chave


##AES	- Algoritmo de criptografia simétrica - Transformar dados em formato ilegível
##AES-128	- Versão do AES com chave de 128 bits - Segurança + desempenho
##CBC	- Modo de operação por blocos encadeados - Evita padrões repetidos
##HMAC - Código de autenticação baseado em hash - Detecta alterações (integridade)


# Gerar Chave
key = Fernet.generate_key() #Gera uma chave secreta aleatória (única e segura) que será usada para criptografar e descriptografar
print("Chave gerada: ", key)

# Criar um objeto Fernet com essa chave
f = Fernet(key) #Vai usar essa chave para criptografar e descriptografar mensagens.

# Definir mensagem (em bytes)
msg = b"hello world"

# Criptografar a mensagem
msg_cifrada = f.encrypt(msg) # Usa o método .encrypt() para criptografar a mensagem. Retorna um texto cifrado (também em base64).
print("Mensagem cryptografada: ", msg_cifrada)

# Descriptografar a mensagem
msg_original = f.decrypt(msg_cifrada) # Usa a mesma chave e o método .decrypt() para descriptografar o texto e recuperar a mensagem original.
print("Mensagem original: ", msg_original.decode())

