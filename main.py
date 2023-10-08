def input_error(func):
    def inner(user_string):
        try:
            result = func(user_string)
            return result
        except KeyError:
            return 'Enter user name:'
        except ValueError:
            return 'Enter correct type:'
        except IndexError:
            return 'Please enter command, name, and phone:'
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
    contact_list = "\n".join([f'Name: {name}, Number: {number}' for name, number in contacts.items()])
    return f'All contacts: \n{contact_list}'

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
        user_input = input('Enter a command: ').lower()
        
        if user_input == '.':
            break

        if user_input.split()[0] in COMMANDS:
            command = user_input.split()[0]
            arguments = user_input.split()[1:]
            result = COMMANDS[command](arguments)
            if result:
                print(result)

        elif user_input in COMMANDS:
            result = COMMANDS[user_input](user_input)
            if result:
                print(result)

        else:
            print(f"Incorrect input '{user_input}', please, try again:")

if __name__ == "__main__":
    contacts = {}
    main()
