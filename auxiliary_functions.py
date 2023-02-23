### The function to convert the network portion of a given IP (as a string) into decimal
def net_ip_str_to_int(ip : str):
    ### We are extracting the octets
    octets = ip.split('/')[0].split('.')
    ### Converting into decimal
    ip_dec = int(octets[0]) * (2 ** 24) + int(octets[1])  * (2 ** 16) + int(octets[2])  * (2 ** 8) + int(octets[3]) 
    ### For the network portion
    net_ip_dec = ip_dec - ip_dec % (2 ** (32 - int(ip.split('/')[1])))
    return net_ip_dec

### The function to convert a given decimal into an IP address as a string
def ip_int_to_str(n : int):
    ### Finding the decimal value of each octets
    octet_1 = n // (2 ** 24)
    octet_2 = (n % (2 ** 24)) // (2 ** 16)
    octet_3 = (n % (2 ** 16)) // (2 ** 8)
    octet_4 = n % (2 ** 8)
    ### Converting each octet into 8 bits and merging them for the final ip address
    ip = bin(octet_1)[2 : ].zfill(8) + '.' + bin(octet_2)[2 : ].zfill(8) + '.' + bin(octet_3)[2 : ].zfill(8) + '.' + bin(octet_4)[2 : ].zfill(8)
    return ip

### The function to convert an IP address in bits as a string into an IP address in decimal as string
def ip_bits_to_dec(ip: str):
    return str(int(ip[0 : 8] , 2)) + '.' + str(int(ip[9 : 17] , 2)) + '.' + str(int(ip[18 : 26] , 2)) + '.' + str(int(ip[27 : 35] , 2))

### The function converting decimal value of 32 bits into an IP address in decimal as string
def ip_int_to_octets(n: int):
    return ip_bits_to_dec(ip_int_to_str(n))

### The function to check if an IP address is valid
def is_ip_valid(ip: str):
    ### There has to be minimum 9 characters, one of them must be '/' and three of them dots.
    if len(ip) < 9 or ip.count('/') != 1 or ip.count('.') != 3:
        return False
    ### suffix must be composed of numbers
    elif not ip.split('/')[1].isnumeric():
        return False
    ### suffix must be between 1 and 32
    elif int(ip.split('/')[1]) > 32 or int(ip.split('/')[1]) <= 0:
        return False
    else:
        octets = ip.split('/')[0].split('.')
        for x in octets:
            ### each octet must be numeric
            if not x.isnumeric():
                return False
            ### The values must be between 0 and 255
            elif int(x) < 0 or int(x) > 255:
                return False
        return True