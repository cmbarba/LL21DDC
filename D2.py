## Day 1 Challenge ##

# Provided

name = '  Dot  '

# Work

sname = name.strip()
uname = sname.upper()
print("#" + uname + "!")

#Alternative way, chaining methods together

name2 = '  Dot  '

name2 = name2.upper().strip()
print(f"#{name2}!")
