def check_email(string):
    spaces = (" " not in string)
    sign = "@" in string
    dot = string.rfind(".") != -1
    dot_sign = "@." not in string
    return spaces and sign and dot and dot_sign

