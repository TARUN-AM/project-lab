contacts = []

while True:
    print("\n1. ADD CONTACTS")
    print("2. VIEW CONTACTS")
    print("3. SEARCH CONTACTS")
    print("4. DELETE CONTACTS")
    print("5. EXIT")

    try:
        choice = int(input("\nENTER YOUR CHOICE: "))
    except ValueError:
        print("PLEASE ENTER A NUMBER FROM 1 TO 5.")
        continue

    if choice == 1:
        name = input("ENTER NAME: ")
        number = input("ENTER NUMBER: ")

        contact = {"name": name, "number": number}
        contacts.append(contact)

        print("CONTACT ADDED SUCCESSFULLY!")

    elif choice == 2:
        if len(contacts) == 0:
            print("NO CONTACTS YET!!")
        else:
            for i in range(len(contacts)):
                print(i + 1, contacts[i]["name"], contacts[i]["number"])

    elif choice == 3:
        search = input("ENTER THE NAME TO SEARCH: ")
        found = False

        for c in contacts:
            if c["name"].lower() == search.lower():
                print(c["name"], "-", c["number"])
                found = True

        if not found:
            print("CONTACT NOT FOUND!!")

    elif choice == 4:
        num = int(input("ENTER CONTACT NUMBER TO DELETE: "))

        if num > 0 and num <= len(contacts):
            removed = contacts.pop(num - 1)
            print("DELETED:", removed["name"])
        else:
            print("INVALID SELECTION!!")

    elif choice == 5:
        print("BYEEE!!")
        break

    else:
        print("INVALID CHOICE, TRY AGAIN...")