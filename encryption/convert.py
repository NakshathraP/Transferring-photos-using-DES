def hex_to_binary(hex_string):
    decimal_integer = int(hex_string, 16)
    binary_string = bin(decimal_integer)

    binary_string = binary_string[2:] # Remove the 0b prefix

    # Add the appropriate zeroes at the beginning of the string
    remainder = len(binary_string)%4
    if remainder != 0:
        binary_string = ("0" *(4-remainder))+binary_string 

    return binary_string