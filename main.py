def input_error(func):
    def inner(user_string):
        try:
            result = func(user_string)
            return result
        except KeyError:
            print('Enter user name:')
        except ValueError:
            print('Enter correct type:')
        except IndexError:
            print('Please enter command, name and phone please:')

    return inner



@input_error
def add_contact(new_contact):
    contacts[new_contact[0]] = new_contact[1]
    return f'A new contact added successfully. Name: "{new_contact[0]}" Number: "{new_contact[1]}"'


@input_error
def change_contact(contact):
    contacts[contact[0]] = contact[1]
    return f'The contact changed successfully. Name: "{contact[0]}" New number: "{contact[1]}"'


@input_error
def get_number(name_contact):
    return f'Name: {name_contact[0]} Number: {contacts[name_contact[0]]}'


@input_error
def quit_func(quit_command):
    return f'Thank you for using our BOT!!'


@input_error
def hello_func(hello_command):
    return f"Hello! How can I help you?"


@input_error
def show_all_func(show_all_command):
    return f'All contacts: \n{contacts}'


def main():

    COMMANDS = {
        'add': add_contact,
        'change': change_contact,
        'phone': get_number,
        'hello': hello_func,
        'show all': show_all_func,
        'good bye': quit_func,
        'close': quit_func,
        'exit': quit_func,
    }

    print('Welcome to BOT >>>')

    while True:

        user_input = input().lower()
        if user_input == '.':
            break

        if user_input.split()[0] in COMMANDS:
            test_none = COMMANDS[user_input.split()[0]](user_input.split()[1:])

            if test_none is not None:
                print(COMMANDS[user_input.split()[0]](user_input.split()[1:]))

                if COMMANDS[user_input.split()[0]](user_input.split()[1:]) == "Thank you for using our BOT!":
                    break

        elif user_input in COMMANDS:
            print(COMMANDS[user_input](user_input))

        else:
            print(
                f"Incorrect input '{user_input}', please, try again:")


if __name__ == "__main__":
    contacts = {}
    main()