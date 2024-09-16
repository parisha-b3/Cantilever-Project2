import finance as fin 

while True:
    fin.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        fin.add_transactions()
    elif choice == '2':
        fin.view_transactions()
    elif choice == '3':
        fin.view_summary()
    elif choice == '4':
        fin.search_transactions()
    elif choice == '5':
        fin.save_data()
    elif choice == '6':
        fin.load_data()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose a valid option.")