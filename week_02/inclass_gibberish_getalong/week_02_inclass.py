# %% codecell
x = 2
type(x)

# %% codecell
color_list = ["pink", "blue", "yellow", "purple", "violet"]
print(color_list[1:4])

# %% codecell
x = True

if not x:
    print("x is False")
else:
    print("x is True")

# %% codecell
x = 5
print(x != 5)
print(x > 3 or x < 10)

# %% codecell
x = 40

if x > 10:
    print("x is above 10.")
    if x > 20:
        print("x is also above 20.")
    else:
        print("x is not above 20.")

# %% codecell
for color in color_list:
    print(color)

# %% codecell
x = 0
while x < 6:
    print(x)
    x += 1

# %% codecell
x = 1
while x != 9 and x < 23:
    print(x)
    x += 1

# %% codecell


def greeting():
    print('Hello World!\n')


for x in range(5):
    print(x)
    greeting()

# %% codecell


def slacker(fred, bomp):
    print(fred)
    print(bomp)


slacker("uuu", "aaaa")

oh = "ooooohhhh"
hihi = "hiiiihiiii"
slacker(oh, hihi)
