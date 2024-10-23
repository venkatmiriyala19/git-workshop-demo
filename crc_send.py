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

def encodeData(data, key):
    return data + mod2div(data + '0' * (len(key) - 1), key)

def crcfind():
    encoded_data = encodeData(data, key)
    print("Encoded data to be sent in binary format:", encoded_data)
    s.sendto((encoded_data + "," + key).encode(), ('127.0.0.1', port))
    print("Server feedback:", s.recv(1024).decode())

# Client code
s = socket.socket()
port = 1240
s.connect(('127.0.0.1', port))

input_string = input("Enter data you want to send -> ")
data = ''.join(format(ord(x), 'b').zfill(7) for x in input_string)
print("Data in binary format:", data)

while True:
    n = int(input("Choose CRC Technique:\n1. CRC-12\n2. CRC-16\n3. Exit\n"))
    if n == 1:
        key = input("Enter CRC-12 key (13 digits): ")
        crcfind()
    elif n == 2:
        key = input("Enter CRC-16 key (17 digits): ")
        crcfind()
    else:
        break

s.close()
