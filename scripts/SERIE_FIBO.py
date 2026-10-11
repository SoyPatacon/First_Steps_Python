a: int = 0
b: int = 1
sig:int
print ("")
print ("SERIE FIBONACCI")
print ("")

for i in range(0, 30):
    print(f"{a:,}".replace(",", ".")) 
    sig = a + b
    a = b
    b = sig