# Transferring-photos-using-DES

This application is run on a virtual environment. To run this application either in a venv or your local system, the sockets and PIL python packages are required.

```
pip install sockets
pip install PIL
```

The main.py file in the encryption folder also serves as the server application. The server converts the image into a list og rgb values. The rgb values are converted to thier respective hex codes. These hex odes are converted to binnary and every block of 64 bits each is encrypted using the Data Encryption Standard and sent through the socket.

The main.py file in the decryption folder serves as the client application. This client connects to the server and when the connection is established the client begins sending each block. Each block(64 bits) is decrypted separately using the Data Encryption Standard algorithm. The resulting string of bits is converted to hexadecimal values which are further converted to rgb values. These rgb values are used to build the image back pixel-by-pixel.

To run the application, open two terminals. Run the main.py of the encryption folder followed by the main.py of the decryption folder in a separate terminal tab.

