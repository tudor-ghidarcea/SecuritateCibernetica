#laboratorul 6 exercitiul 2
#a
#from Crypto.Cipher import AES
#key = b'O cheie parecare'
#data = b'testtesttesttesttesttesttesttesttesttesttesttest'
#cipher = AES.new(key, AES.MODE_ECB)
#print(cipher.encrypt(data))
#b
#ce mod de criptare este folosit?
#blocul criptat se repeta de trei ori

#c nu as recomanda utilizarea acestui mod de criptare, deoarece avem acelasi bloc de date criptat
#la fel de mai multe ori

#d care este dimensiunea cheii si a blocului de text?
#dimensiulea cheii este de 128 de biti, iar a blocului de 384

#e modificati codul astfel incat sa functioneze cu cheia b'test'
#from Crypto.Cipher import AES
#from Crypto.Util.Padding import pad
#key = b'O cheie oarecare'
#data = b'test'
#cipher = AES.new(key, AES.MODE_ECB)
#print(cipher.encrypt(pad(data, 16)))

#f refaceti codul, folosind un mod de operare care vi se pare mai potrivit

#from Crypto.Cipher import AES
#from Crypto.Random import get_random_bytes
#key = b'O cheie parecare'
#data = b'testtesttesttesttesttesttesttesttesttesttesttest'
#iv = get_random_bytes(16)
#cipher = AES.new(key, AES.MODE_CBC, iv)
#print(cipher.encrypt(data))
