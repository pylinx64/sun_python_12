from cryptography.fernet import Fernet

# генерируется ключ. Доступ к вашим данным по ключю
key = Fernet.generate_key()
print(key)

text = b'kolbasnii tort + kirpich za 10 grn'
# шифровальщик
crypto = Fernet(key)

# шифруем сообщение
secure_text = crypto.encrypt(text)
print(secure_text)

# расшифровываем сообщения
unsecure_text = crypto.decrypt(secure_text)
print(unsecure_text)


