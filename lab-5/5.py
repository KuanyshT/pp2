import re

txt = 'aaandndnfb dsjdjfdjsdfafjdksfkdjb aaab ab'

x = re.findall(r'a\w*b', txt)

print(x)