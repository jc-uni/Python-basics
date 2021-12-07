from time import sleep
from bear import Bear
from cat import Cat
from dog import Dog

#intro txt
def print_some_stuff():
    """prints some stuff
    """
    print("Hello world" +"\r\n" +"wait...")
    sleep(1)
    print("This is python 3.9")

    various_data_types()


def various_data_types():
    some_text = "\'a string, this is\' -Yoda"
    a_number = 1

    a_list = [some_text, 10, 28, 10, 51, a_number, True, False] #ordered, mutable, allows duplicates
    a_set = {some_text, 10, 28, 10, 51, a_number, True, False} #unordered, immutable (add/remove ok), disallows duplicates
    a_tuple = (some_text, 10, 28, 10, 51, a_number, True, False) #ordered, immutable, allows duplicates
    a_dictionary = {"brand": "Volvo", "model": "XC60", "year": 2019, "operable": True} #ordered(pr. python 3.7), mutable, disallows duplicates
   
    print(type(a_list))
    print(a_list[:])
    print(type(a_set))
    print(a_set)
    print(type(a_tuple))
    print(a_tuple)
    print(type(a_dictionary))
    print(a_dictionary)
    for key, value in a_dictionary.items():
        print(f'{key:10} --> {value:1}') #formatted string literal


def animals():
    a_bear = Bear()
    a_cat = Cat()
    a_dog = Dog()
    a_bear.make_sound()
    a_cat.make_sound()
    a_dog.make_sound()


def main():
    print_some_stuff()
    animals()

if __name__ == "__main__":
    main()