def input_error(func):
    """Handle input errors in command handlers."""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."

        except IndexError:
            return "Enter user name"

        except KeyError:
            return "Contact not found."

    return inner


def parse_input(user_input):
    """
    Parse user input into a command and arguments.
    Command names are case-insensitive.
    """
    parts = user_input.strip().split()

    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]

    return command, args


@input_error
def add_contact(args, contacts):
    """Add a new contact or update an existing one."""
    if len(args) != 2:
        raise ValueError("Expected name and phone")

    name, phone = args
    contacts[name.lower()] = phone

    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Change the phone number of an existing contact."""
    if len(args) != 2:
        raise ValueError("Expected name and phone")

    name, phone = args
    name = name.lower()

    if name not in contacts:
        raise KeyError(name)

    contacts[name] = phone

    return "Contact updated."


@input_error
def show_phone(args, contacts):
    """Return the phone number for a given contact."""
    if not args:
        raise IndexError("Missing user name")

    if len(args) != 1:
        return "Invalid command."

    name = args[0].lower()

    return contacts[name]


@input_error
def show_all(contacts):
    """Return all saved contacts as a formatted string."""
    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    """Run the main command-line assistant loop."""
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)

        if command in ["close", "exit"] and not args:
            print("Good bye!")
            break

        elif command == "hello" and not args:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all" and not args:
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
