import socket
from PIL import Image

from des import des
from convert import hex_to_binary

image = Image.open("C:\\Users\\naksh\\OneDrive\\Desktop\\Extra\\DES_photo\\ladybug.jpeg")

# pixel_array is a list of the pixels
pixel_array = image.convert("RGB")
width, height = image.size
hex_codes_list = []

def rgb_to_hex(rgb):
    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

for y in range(height):
    for x in range(width):
        pixel = pixel_array.getpixel((x, y))
        hex_code = rgb_to_hex(pixel)
        hex_code = hex_code[1:]
        hex_codes_list.append(hex_code)
#hex_codes_list is a list of the hex codes without the hash#

input_hex = "".join(hex_codes_list)
extraToAdd = 64 - (len(input_hex)%64)
#input_hex is the string of hexadecimal inputs
#extraToAdd are the extra white spaces add to ensure the length%64=0
#If the modulus value is 62 then the extraToAdd will be 64-62 = 2

for i in range(extraToAdd):
    input_hex += '0'

print("Length of input hexadecimal string: ",len(input_hex))
input_binary = hex_to_binary(input_hex)
print("Length of input binary string: ",len(input_binary))
#The input hexadecimal string is converted to a binary string

output_binary = ""
iteration_num = int(len(input_binary)/64)
print(iteration_num)
#iteration_num stands for the number of blocks/iterations the image is sent in 

# Split the long string into blocks of length 64
blocks = [input_binary[i:i+64] for i in range(0, len(input_binary), 64)]

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server listening...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address} established.")

# Send the width and height of the picture
width_str = str(width)
height_str = str(height)
client_socket.send(width_str.encode())
client_socket.send(height_str.encode())

# Send each encrypted block to the client
for i in blocks:
    encrypted_block = des(i)
    client_socket.sendall(encrypted_block.encode())

# Close the connection
client_socket.close()
server_socket.close()
