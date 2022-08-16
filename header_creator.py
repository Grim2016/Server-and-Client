def header_creator(header_type:str,input_string:str):
    """
    Creates header based on input
    """
    hex_len = hex(len(bytes(input_string,"utf-8")))
    if len(hex_len) < 7:
        difference = 7 - len(hex_len)
        hex_split = hex_len.split("x")
        for _ in range(difference):
            hex_split[1] = "0"+hex_split[1]
            hex_len = "x".join(hex_split)
    return bytes(f"{header_type}|{hex_len}","utf-8")
