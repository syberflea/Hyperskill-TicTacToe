ind = email.find("@")
local_part = "".join(email[:ind])
print(local_part)