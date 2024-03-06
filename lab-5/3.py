import re

txt = "FJKJKffffJJKfda zzz-zzz, usernameblablabla_krutoi 899898 fdfdfdfd_fdfdfdf"

x = re.findall(r'[a-z]+_[a-z]*', txt)

print(x)

