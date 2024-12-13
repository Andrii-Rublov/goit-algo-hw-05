def input_error(func): #decorator, function for errors handling
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Give me name and phone number please." 
        except KeyError:                            
            return "Enter the right name please."
        
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts): # adding name and phone number to dictionare contacts
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts): # rewriting phone number for specified contact
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact with name {name} not found. Enter the right name please."

@input_error
def show_phone(args, contacts):# getting phone number for specified contact
    name = args[0]
    return contacts[name]
    

def show_all(_, contacts):# shows all items in dictionary contacts
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(None, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

