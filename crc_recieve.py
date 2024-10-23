import socket

def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(1, len(b)))

def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[:pick]
    while pick < len(divident):
        tmp = xor(divisor, tmp) + divident[pick] if tmp[0] == '1' else xor('0'*pick, tmp) + divident[pick]
        pick += 1
    return xor(divisor, tmp) if tmp[0] == '1' else xor('0'*pick, tmp)

def decodeData(data, key):
    return mod2div(data, key)

# Server code
s = socket.socket()
s.bind(("", 1240))
s.listen(5)
print("Listening on port 1240")

while True:
    c, addr = s.accept()
    print('Connected to', addr)

    data = c.recv(1024).decode()
  
    data, key = data.split(",")


    ans = decodeData(data, key)
    print("Remainder after decoding ->", ans)

   
    msg = ''.join(chr(int(data[i:i+7], 2)) for i in range(0, len(data[:-(len(key)-1)]), 7))
    print("Decoded message:", msg)
    c.send(("Data -> " + data + " Received, No error found").encode())

    c.close()
