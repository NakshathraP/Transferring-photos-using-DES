def binary_to_hex(bin_string): 
    hex_string = ""
    for i in range(0, len(bin_string),4):
        hex_chunk = bin_string[i:i+4]
        hex_decimal = int(hex_chunk, 2)
        hex_decimal = hex(hex_decimal)[2:]
        hex_string += hex_decimal
    return hex_string
