from time import sleep

#intro txt
def print_some_stuff():
    print("Hello world" +"\r\n" +"wait...")
    sleep(3)
    print("This is python 3.9")
    various_data_types()

def various_data_types():
    some_text = "a string, this is -Yoda"
    a_number = 1
    a_list = [10, 12, 32, 51, a_number]
    print(some_text +", a number: " +str(a_number))
    print(a_list[:])



def main():
    print_some_stuff()

if __name__ == "__main__":
    main()