"""
Implementa encriptación y desencriptación usando RSA.
"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

llave = RSA.generate(2048)
cifrado = PKCS1_OAEP.new(llave.publickey())
descifrado = PKCS1_OAEP.new(llave)

mensaje = "Secreto".encode()
mensaje_cifrado = cifrado.encrypt(mensaje)
mensaje_descifrado = descifrado.decrypt(mensaje_cifrado)

print("Mensaje original:", mensaje.decode())
print("Mensaje descifrado:", mensaje_descifrado.decode())
