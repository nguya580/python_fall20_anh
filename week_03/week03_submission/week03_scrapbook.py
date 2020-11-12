# %% codecell
import random

guestList = ("Anh", "Paras", "Linh", "Chi", "Thy", "Sven", "Sohee")
objects = ["Cheestos", "spinach dip", "tortilla chips", "Coke", "popcorn"]

def invitation_template(guestList, eventName, location, objects, date, time):
    ''' the function store template for the invitation '''
    location = location[::- 1]

    for guest in guestList:
        print(f''' Hello {guest},
        I invite you to join {eventName} with me and Teddy at {location}.
        Please come on time at {time} on the date of {date}.
        Please bring {random_object(objects)} to the movie night

        See you all,
        Anh and Teddy the shibe.

        ********\n''')

# %% codecell
def random_object(list):
    """ this function returns random object that participants will bring """

    return random.choice(list)

random_object(objects)

# %% codecell
def all_objects(list):
    """ this function returns all the objects within the object[list] """

    return ', '.join(list[0:-1]) + ', and %s' %(list[-1]) #[::-1] is anything before the last index in list, [0:-1] is from the 1st index to the second to last index

all_objects(objects)

# %%codecell
#invitation_template(guestList, eventName, location, objects, date, time)
invitation_template(guestList, 'horror movie night', '123 Spinach st, apt 6F, 11102', objects, 'Nov 20, 2021', '7 PM')





# %% codecell
def checkPalindrome():
    ''' this f tests where a sentence is a Palindrome. '''

    txt = input("Please type your sentence: ")

    unwanted = ['?', ':', ',', '!', ';']

    #remove unwanted characters
    new_txt = txt
    for char in unwanted:
        new_txt = new_txt.replace(char, "")

    print(new_txt)

    txt_lower = new_txt.lower()
    txt_spaceClear = txt_lower.replace(' ', '')

    txt_Palindrome = txt_spaceClear[::-1]

    if txt_Palindrome == txt_spaceClear:
        print(f'True. "{txt}" is a Palindrome.')
    else:
        print(f'False. "{txt}" is not a Palindrome.')

    checkP_again()

def checkP_again():
    choice = input("""\nDo you want to check another phrase?
Enter 'y' to continue, or 'n' to exit.""")

    if choice == 'y':
        checkPalindrome()
    elif choice == 'n':
        print("\nBye bye.")

checkPalindrome()





# %% codecell
import matplotlib.pyplot as plt

data = {'Youtube': 6, 'Instagram': 3, 'Facebook': 2, 'Chrome': 1}

plt.plot(range(len(data)), list(data.values()), color = '#F3872F')
plt.ylabel('Hours')

plt.xticks(range(len(data)), list(data.keys()), rotation = 45,)

plt.suptitle('Most used apps screen time of Anh')

plt.show()
