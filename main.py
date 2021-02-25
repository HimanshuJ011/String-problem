import string
def abc(s):
  keyboard = string.ascii_lowercase
  a=keyboard.index(s[0])
  c=a
  for i in range(1,len(s)):
    c+=abs(keyboard.index(s[i])-a)
    a=keyboard.index(s[i])
  return c

print(abc("cba"))
