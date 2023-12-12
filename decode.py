#Import the cryptography Library
from cryptography.fernet import Fernet

#Generate a Fernet Key
key = input("Açarınızı daxil edin...\n")

#Create a Fernet object with that key
f = Fernet(key)

#Input string to be decrypted
input_string = input("Zəhmət olmasa kodlaşdırılmış mətini daxil edin...\n")

#Decrypt the string
decrypted_string = f.decrypt(input_string)

#Print our decrypted string
print("Deşifrələnmiş Mətn...\n", decrypted_string.decode())