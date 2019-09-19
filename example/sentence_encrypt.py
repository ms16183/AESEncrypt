chipher import *

sentence = 'Puella magi madoka magica'
key = 'You are not alone.'

encrypted_sentence = encrypt(sentence.encode(), key.encode())
decrypted_sentence = decrypt(encrypted_sentence, key.encode())

print(sentence)
print(encrypted_sentence)
print(decrypted_sentence)
