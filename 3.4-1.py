import hashlib

m1 = hashlib.md5()
m2 = hashlib.sha1()
m3 = hashlib.sha256()
m1.update("Hello, world!")
m2.update("Hello, world!")
m3.update("Hello, world!")
m1.hexdigest()
m2.hexdigest()
m3.hexdigest()
print(m1.hexdigest())
print(m2.hexdigest())
print(m3.hexdigest())
