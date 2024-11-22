import random
import math
def isPrime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
def generatePrime():
    while True:
        num=random.randint(100,1000000)
        if isPrime(num):
            return num
        

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def multInverse(e,phi):
    def extendedGcd(a,b):
        if a==0:
            return b, 0 ,1
        else:
            gcd,x,y = extendedGcd(b%a,a)
            return gcd, y - (b//a)*x, x
        
    gcd,x,y= extendedGcd(e, phi)
    if gcd != 1:
        return None
    else:
        return x%phi
    
def encrypt(publicKey,message):
    n,e=publicKey
    encryptedMessage=[pow(ord(char),e,n) for char in message]
    return encryptedMessage

def decrypt(privateKey,encryptedMessage):
    n,d=privateKey
    decryptedMessage=[chr(pow(char,d,n)) for char in encryptedMessage]
    return ''.join(decryptedMessage)

def generateKeys():
    p = generatePrime()
    q = generatePrime()

    n = p*q

    phi = (p-1)*(q-1)

    e = random.randint(2,phi)
    while gcd(e,phi)!=1:
        e = random.randint(2,phi)
    
    d = multInverse(e,phi)

    publicKey=(n,e)
    privateKey=(n,d)

    return publicKey,privateKey

public_key,private_key=generateKeys()
print("public key:",public_key)
print("private key:",private_key)
message = "helloWorld"
encryptedMessage = encrypt(public_key,message)
print("enc:",encryptedMessage)
decryptedMessage = decrypt(private_key,encryptedMessage)
print("dec:", decryptedMessage)