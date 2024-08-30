import pandas as pd

users_data = pd.read_csv("School project work\\users_data.csv", sep=",", header=0)
users_data.to_csv("School project work\\users_data.csv", index=False)
df=None
email=None
password=None

while True:
    print("Welcome to ABC Hotel.")
    print("""
        Choose a number:
        1. Book rooms
        2. View existing bookings
        3. Cancel bookings""")
    main=input("How would you like to proceed?: ")
    date_ar = input("Please enter the date of arrival (DD/MM/YYYY): ")
    date_dep = input("Please enter the date of departure (DD/MM/YYY):  ")
    if main=="1":
        print("Where would you like to stay for your holidays?")
        location=input("Where would you like to spend your vacation?: ")
        if location=="Dubai" or location=="USA" or location=="India":
            print("Hotels available in", location)
        else:
            print("No hotels available in", location, "Please try again.")
            continue
        print("Now on to bookings!")

        while True:
            print("Booking a room!")
            print("""
            Choose a room type:
            1. Suite
            2. Executive Suite
            3. Deluxe
            4. Villa
            5. Penthouse""")
            roomType=int(input("Choose a number: "))
            if roomType==1:
                print("Suite selected.")
                roomTypeCh="Suite"
            elif roomType==2:
                print("Executive Suite selected.")
                roomTypeCh="Executive Suite"
            elif roomType==3:
                print("Deluxe selected.")
                roomTypeCh="Deluxe"
            elif roomType==4:
                print("Villa selected.")
                roomTypeCh="Villa"
            elif roomType==5:
                print("Penthouse selected.")
                roomTypeCh="Penthouse"
            else:
                print("Please enter a valid number!")
                continue

            print("Rooms available!")

            print("-----------------------")

            num_people=int(input("Please enter the number of people staying in the room: "))

            print("-----------------------")

            print("""
                Choose your room location:
                1. Poolside
                2. Beachside""")
            roomLoc=int(input("Choose a number: "))
            if roomLoc==1:
                print("Poolside selected.")
                roomLocCh="Poolside"
            elif roomLoc==2:
                print("Beachside selected.")
                roomLocCh="Beachside"
            else:
                print("Please choose a valid number.")
                continue

            print("Room available!")

            print("-----------------------")

            print("""
                Choose facilities to be included:
                1. Breakfast included
                2. Buffet
                3. Gym membership
                4. All
                5. None""")
            roomFac=int(input("Choose a number: "))
            if roomFac==1:
                print("Breakfast will be included.")
                roomFacCH="Breakfast"
            elif roomFac==2:
                print("Buffet selected.")
                roomFacCH="Buffet"
            elif roomFac==3:
                print("Gym membership selected.")
                roomFacCH="Gym Membership"
            elif roomFac==4:
                print("All facilities will be provided!")
                roomFacCH="All Facilities"
            elif roomFac==5:
                print("No facilities selected.")
                roomFacCH="None"
            else:
                print("Please enter a valid number.")
                continue

            print("-----------------------")

            d={'Location':location, 'Room type':[roomTypeCh], 'Room loc.':[roomLocCh], 'No. of People':[num_people], 'Facilities':[roomFacCH]}
            bookings_df=pd.DataFrame(d)

            print("Confirming your bookings!")
            print(bookings_df)
            booking_confirm=input("Confirm? (Y/N): ")
            if booking_confirm=="Y" or booking_confirm=="y":
                print("Ok! Moving on to the Payment details. You may have to Log in first!")
            elif booking_confirm=="N" or booking_confirm=="n":
                print("Ok! Please run the prompt again to restart!")
                break
            else:
                print("Please enter a valid input (Y/N).")
                continue


            #User Login/Register
            while True:
                print("""
                    1. Register
                    2. Login
                    3. Exit""")
               
                choice = input("Choose a number: ")

                if choice=="1":
                    email = input("Enter email: ")

                    existing_user = users_data.loc[(users_data["email"] == email)]

                    if not existing_user.empty:
                        print("A user with that email already exists. Please use a different email.")

                        login=input("Do you want to log in instead? (Y/N): ")

                        if login=="y" or "Y":
                            email = input("Enter email: ")
                            password = input("Enter Password: ")

                            users_data = pd.read_csv("School project work\\users_data.csv")

                            match = users_data.loc[(users_data["email"] == email) & (users_data["password"] == password)]

                            admin_username = "admin"
                            admin_password = "adminpass"

                            # Admin Login
                            if email == admin_username and password == admin_password:
                                print("Welcome to the Admin Dashboard!")
                                admin_dash = input("Would you like to view all bookings? (Y/N: ")
                                if admin_dash=="Y" or admin_dash=="y":
                                    print(bookings_df)
                                    break
                                elif admin_dash=="N" or admin_dash=="n":
                                    print("Ok! For booking your own room as a member of the staff of ABC Hotel, head over to your nearest hotel!")
                                    break
                                else:
                                    print("Please enter a valid input.")
                                    continue

                            if not match.empty:
                                print("Login successful!")
                                print(bookings_df)
                            else:
                                print("Incorrect email or Password.")

                        elif login=="n" or "N":
                            print("Please choose a different email.")

                            email = input("Enter new email: ")
                            password = input("Enter Password: ")

                            existing_user = users_data.loc[(users_data["email"] == email) & (users_data["password"] == password)]

                        else:
                            print("Please enter a valid input. (Y/N)")
                    else:
                        password = input("Enter password: ")
                       
                        print("Registered successfully!")

                        users_data.loc[users_data.shape[0]] = [email,password]
                        users_data.to_csv("School project work\\users_data.csv",sep=",",index=False)

                elif choice=="2":
                    email = input("Enter email: ")

                    existing_user = users_data.loc[(users_data["email"] == email)]
                   
                    if existing_user.empty:
                        print("No account found. You can register instead.")
                        continue
                    else:
                        password = input("Enter Password: ")

                    match = users_data.loc[(users_data["email"]==email) & (users_data["password"]==password)]

                    if not match.empty:
                        print("Login successful!")
                        print("Here is your booking: ")
                        print(bookings_df)
                        break

                    else:
                        print("Incorrect email or password")
                    continue
                   
                elif choice=="3":
                    print("Exiting...")
                    break
                   

                else:
                    print("Please enter a valid number.")
            break
        break
   

    elif main=="2":
        print("You may have to log in first!")
        while True:
            email = input("Enter email: ")

            existing_user = users_data.loc[(users_data["email"] == email)]
           
            if existing_user.empty:
                print("No account found. You can register instead.")
                continue
            else:
                password = input("Enter Password: ")

            match = users_data.loc[(users_data["email"]==email) & (users_data["password"]==password)]

            if not match.empty:
                print("Login successful!")
                print("Here is your booking: ")
                print(bookings_df)
                break

            else:
                print("Incorrect email or password")
                continue

    elif main=="3":
        print("Ok! Which booking would you like to cancel?")
