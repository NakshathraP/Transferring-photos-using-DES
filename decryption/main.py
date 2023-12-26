import socket
from PIL import Image, ImageDraw

from des import des_decryption
from convert import binary_to_hex

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Receive the width and height of the picture from the server
width = int(client_socket.recv(1024).decode())
height = int(client_socket.recv(1024).decode())
print(width, height)

# Receive blocks and perform decryption
received_blocks = []
while True:
    block = client_socket.recv(64).decode()
    if not block:
        break
    decrypted_block = des_decryption(block)
    received_blocks.append(decrypted_block)

# Close the connection
client_socket.close()

# Reconstruct the full string
received_string = ''.join(received_blocks)
output_binary = received_string
output_hex = binary_to_hex(output_binary)

whiteSpace = 64 - (len(output_hex)%64)
#whiteSpaces were previously added to make the block size = 64

output_hex = output_hex[:-whiteSpace]

hex_list = ['#' + output_hex[i:i+6] for i in range(0, len(output_hex), 6)]

# Create a new image with RGB mode
image = Image.new('RGB', (width, height))

# Create a draw object
draw = ImageDraw.Draw(image)

# Calculate the width and height of each cell
cell_width = image.width // width
cell_height = image.height // height

# Loop through the hex color codes and fill the cells with colors
for i, hex_code in enumerate(hex_list):
    x0 = i % width * cell_width
    y0 = i // width * cell_height
    x1 = x0 + cell_width
    y1 = y0 + cell_height
    draw.rectangle([x0, y0, x1, y1], fill=hex_code)

# Save the image
image.save('output_image.png')
image.show()
