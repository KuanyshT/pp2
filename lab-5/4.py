import re

txt = 'aasdfdjksalFjfJJJjjjJjjJsGcDjJnB, AOaoAoAoAoAo'

x = re.findall('[A-Z][a-z]', txt)

print(x)