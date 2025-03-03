import pandas as pd
import matplotlib.pyplot as plt

users_data = pd.read_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv", sep=",", header=0)
users_data.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv", index=False)
bookings_df = pd.read_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", header=0)
df=None
email=None
password=None


while True:
    print("Welcome to ABC Hotel.")
    print("Choose a number:")
    print("1. Book rooms")
    print("2. View existing bookings")
    print("3. Cancel Bookings")
    print("4. Admin Login")
    main=input("How would you like to proceed?: ")

    if main=="1":
        print("Where would you like to stay for your holidays?")
        location=input("Please enter City, Property Name or Location: ")

        date_ar = input("Please enter the Check-In Date (DD/MM): ")
        date_dep = input("Please enter the Check-Out Date (DD/MM): ")
        
        num_rooms = int(input("Please enter the number of Rooms to be booked: "))
        num_people = int(input("Please enter the number of Guests staying in the room: "))
        
        print("Please choose a Price Range:")
        print("1. Rs 0 - Rs 1500")
        print("2. Rs 1500 - Rs 2500")
        print("3. Rs 2500 - Rs 5000")
        print("4. Rs 5000 +")
        
        price_range = int(input("Choose a number: "))
        if price_range==1:
            price_selec = "Rs 0 - Rs 1500"
        elif price_range==2:
            price_selec = "Rs 1500 - Rs 2500"
        elif price_range==3:
            price_selec = "Rs 2500 - Rs 5000"
        elif price_range==4:
            price_selec = "Rs 5000 +"
        else:
            print("Please choose a valid number")
            print("-----------------------")
            continue
        
        print("Looking for rooms under the Price Range ",price_selec, "...")
        
        print("Rooms found!")

        print("-----------------------")

        print("Showing Properties in ", location, "under the Price Range", price_selec)
        print("1. Radisson Blu")
        print("- Rating: Excellent [5 stars]")
        print("2. The Imperial")
        print("- Rating: Excellent [4.5 stars]")
        print("3. Taj")
        print("- Rating: Very Good [4 stars] ")
        print("4. Hard Rock Hotel")
        print("- Rating: Very Good [3.8 stars]")
        print("5. Pattaya Beach Resort")
        print("- Rating: Very Good [4 stars]")

        print("-----------------------")
        hotel = int(input("Please choose a number: "))
        if hotel == 1:
            print("Hotel Chosen: Radisson Blu")
            hotel_ch = "Radisson Blu"
        elif hotel == 2:
            print("Hotel Chosen: The Imperial")
            hotel_ch = "The Imperial"
        elif hotel == 3:
            print("Hotel Chosen: Taj")
            hotel_ch = "Taj"
        elif hotel == 4:
            print("Hotel Chosen: Hard Rock Hotel")
            hotel_ch = "Hard Rock Hotel"
        elif hotel == 5:
            print("Hotel Chosen: Pattaya Beach Resort")
            hotel_ch = "Pattaya Beach Resort"
        else:
            print("Please enter a valid number.")
            continue


        while True:
            print("Booking a room!")
            print("Choose a room type:")
            print("1. Suite")
            print("2. Executive Suite")
            print("3. Deluxe")
            print("4. Villa")
            print("5. Penthouse")
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

            print("Choose your room location:")
            print("1. Poolside")
            print("2. Beachside")
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

            print("Choose facilities to be included:")
            print("1. Breakfast included")
            print("2. Buffet")
            print("3. Gym membership")
            print("4. All")
            print("5. None")
            roomFac=int(input("Choose a number: "))
            if roomFac==1:
                print("Breakfast will be included.")
                roomFacCh="Breakfast"
            elif roomFac==2:
                print("Buffet selected.")
                roomFacCh="Buffet"
            elif roomFac==3:
                print("Gym membership selected.")
                roomFacCh="Gym Membership"
            elif roomFac==4:
                print("All facilities will be provided!")
                roomFacCh="All Facilities"
            elif roomFac==5:
                print("No facilities selected.")
                roomFacCh="None"
            else:
                print("Please enter a valid number.")
                continue

            print("-----------------------")

            d={'Email':email, 'Hotel':hotel_ch, 'Location':location, 'Room type':[roomTypeCh], 'Room loc.':[roomLocCh], 'No. of People':[num_people], 'Facilities':[roomFacCh], 'Price Range':price_selec}
            user_bookings=pd.DataFrame(d)

            bookings_df.loc[bookings_df.shape[0]] = [email,hotel_ch,location,roomTypeCh,roomLocCh,num_people,roomFacCh,price_selec]
            bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

            print("Confirming your bookings!")

            booking_confirm=input("Confirm? (Y/N): ")
            if booking_confirm=="Y" or booking_confirm=="y":
                print("Ok! To confirm your booking, you may have to log in first!")

                while True:
                    print("1. Register")
                    print("2. Login")
                    print("3. Exit")
                    
                    choice = input("Choose a number: ")

                    if choice=="1":
                        reg_email = input("Enter email: ")

                        existing_user = users_data.loc[(users_data["email"] == reg_email)]

                        if not existing_user.empty:
                            print("A user with that email already exists. Please use a different email.")

                            login=input("Do you want to log in instead? (Y/N): ")

                            if login=="y" or login=="Y":
                                log_email = input("Enter email: ")
                                password = input("Enter Password: ")

                                users_data = pd.read_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv")

                                match = users_data.loc[(users_data["email"] == reg_email) & (users_data["password"] == password)]

                                if not match.empty:
                                    print("Login successful!")
                                    bookings_df["Email"] == log_email

                                    bookings_df=bookings_df.where(pd.notna(bookings_df), log_email)

                                    bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                                    print(bookings_df[bookings_df["Email"] == log_email].tail(1))

                                    exit()
                                else:
                                    print("Incorrect email or Password. Please run the prompt again.")
                                    continue

                            elif login=="n" or login=="N":
                                print("Please choose a different email.")

                                reg_email = input("Enter new email: ")

                                match = users_data.loc[(users_data["email"] == reg_email)]

                                if match.empty:
                                    password = input("Enter Password: ")

                                    existing_user = users_data.loc[(users_data["email"] == reg_email) & (users_data["password"] == password)]
                                
                                    print("Registered successfully!")

                                    users_data.loc[users_data.shape[0]] = [reg_email,password]
                                    users_data.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv",sep=",",index=False)

                                else:
                                    print("Please try again.")
                                    exit()

                            else:
                                print("Please enter a valid input (Y/N).")
                        else:
                            password = input("Enter password: ")
                            
                            print("Registered successfully!")

                            users_data.loc[users_data.shape[0]] = [reg_email,password]
                            users_data.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv",sep=",",index=False)

                        print("You may have to Log in now...")

                        log_email = input("Enter email: ")

                        existing_user = users_data.loc[(users_data["email"] == log_email)]
                        
                        if existing_user.empty:
                            print("No account found. You can register instead.")
                            continue
                        else:
                            password = input("Enter Password: ")

                        match = users_data.loc[(users_data["email"]==log_email) & (users_data["password"]==password)]

                        if not match.empty:
                            print("Login successful!")
                            print("Here is your booking: ")

                            bookings_df=bookings_df.where(pd.notna(bookings_df), log_email)

                            bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                            print(bookings_df[bookings_df["Email"] == log_email])
                            exit()

                        else:
                            print("Incorrect email or password")
                        continue

                    elif choice=="2":
                        log_email = input("Enter email: ")

                        existing_user = users_data.loc[(users_data["email"] == log_email)]
                        
                        if existing_user.empty:
                            print("No account found. You can register instead.")
                            continue
                        else:
                            password = input("Enter Password: ")

                        match = users_data.loc[(users_data["email"]==log_email) & (users_data["password"]==password)]

                        if not match.empty:
                            print("Login successful!")
                            print("Here is your booking: ")

                            bookings_df=bookings_df.where(pd.notna(bookings_df), log_email)

                            bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                            print(bookings_df[bookings_df["Email"] == log_email].tail(1))

                            print("Moving on to Payment. Kindl Pay using UPI or Pay at Reception.")
                            print("Thank you for booking with us! Have a nice day")
                            exit()


                        else:
                            print("Incorrect email or password")
                        continue
                        
                    elif choice=="3":
                        print("Exiting...")
                        exit()

                    else:
                        print("Please enter a valid number.")

            elif booking_confirm=="N" or booking_confirm=="n":
                print("Ok! Please run the prompt again to restart!")
                exit()
            else:
                print("Please enter a valid input (Y/N).")
                continue

    elif main=="2":
        print("You may have to log in first!")
        while True:
            log_email = input("Enter email: ")

            existing_user = users_data.loc[(users_data["email"] == log_email)]
            
            if existing_user.empty:
                print("No account found.")
                print("Would you like to register instead?")
                b=input("Y/N: ")
                if b=="Y" or b=="y":
                    print("Ok! Please run the prompt again to restart.")
                    exit()
                if b=="N" or b=="n":
                    print("Redirecting...")
                    continue
            else:
                password = input("Enter Password: ")

            match = users_data.loc[(users_data["email"]==log_email) & (users_data["password"]==password)]

            if not match.empty:
                print("Login successful!")

                bookings_df=bookings_df.where(pd.notna(bookings_df), log_email)

                bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                print(bookings_df[bookings_df["Email"] == log_email])

                print("Moving on to Payment. Kindl Pay using UPI or Pay at Reception.")
                print("Thank you for booking with us! Have a nice day")                
                exit()

            else:
                print("Incorrect email or password")
                continue

    elif main=="3":
        print("Please Log in first.")
        log_email = input("Enter email: ")

        existing_user = users_data.loc[(users_data["email"] == log_email)]
        
        if existing_user.empty:
            print("No account found. Redirecting...")

            print("-----------------------")

            continue
        else:
            password = input("Enter Password: ")

        match = users_data.loc[(users_data["email"]==log_email) & (users_data["password"]==password)]

        if not match.empty:
            print("Login successful!")
            print("Here are your bookings: ")
            print(bookings_df[bookings_df["Email"] == log_email])
            
            print("-----------------------")

            bookings_cancel = input("Would you like to cancel your booking? (Y/N): ")
            if bookings_cancel == "Y" or bookings_cancel == "y":
                print("Cancelling Booking...")
                
                filtered_df = bookings_df[bookings_df['Email'] == log_email]
                
                drop_bookings_df = filtered_df.tail(1)

                bookings_df = bookings_df.drop(drop_bookings_df.index)

                bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                print("Booking cancelled. Restarting the prompt...")
                print("-----------------------")

            
            elif bookings_cancel == "N" or bookings_cancel == "n":
                print("Ok. Please restart the prompt to try again.")

        else:
            print("Incorrect email or password")
        continue

    elif main=="4":
        admin_email = input("Enter email: ")

        existing_user = users_data.loc[(users_data["email"] == admin_email)]
        
        if existing_user.empty:
            print("No account found. Please try again.")
            print("-----------------------")
            continue
        else:
            password = input("Enter Password: ")

        match = users_data.loc[(users_data["email"]==admin_email) & (users_data["password"]==password)]

        if not match.empty:
            print("Login successful!")

            print(bookings_df)

            print("-----------------------")

            print("1. Most Popular Hotels.")
            print("2. Most Popular Location")
            print("3. Most Popular Room type.")
            print("4. Most Popular Facility chosen.")
            print("5. Manage Bookings.")
            print("6. Manage Users.")

            admin_panel = int(input("Choose a number: "))

            if admin_panel == 1:

                value_counts = bookings_df.value_counts(bookings_df["Hotel"])

                bookings_df['Hotel'].value_counts().plot(x="Hotel", y="Popularity", kind="bar")
                plt.show()

                continue
            
            elif admin_panel == 2:

                value_counts = bookings_df.value_counts(bookings_df["Location"])

                bookings_df['Location'].value_counts().plot(x="Location", y="Popularity", kind="bar")
                plt.show()

                continue

            elif admin_panel == 3:

                value_counts = bookings_df.value_counts(bookings_df["Room type"])

                bookings_df['Room type'].value_counts().plot(x="Room Types", y="Popularity", kind="bar")
                plt.show()         

                continue       

            elif admin_panel == 4:
                
                value_counts = bookings_df.value_counts(bookings_df["Facilities"])

                bookings_df['Facilities'].value_counts().plot(x="Facilities", y="Popularity", kind="bar")
                plt.show()

                continue

            elif admin_panel == 5:
                print(bookings_df)

                print("-----------------------")

                print("1. Add a new booking")
                print("2. Delete a booking")
                
                bookings_manage = int(input("Choose a number: "))
                
                if bookings_manage == 1:
                    print("Please Start the Prompt from the beginning and Book a room to add new bookings")

                elif bookings_manage == 2:
                    admin_drop_booking = input("Please enter the email of the booking you want to cancel (Case sensitive): ")

                    if admin_drop_booking in bookings_df.values:
                        print("Ok")

                        bookings_df = bookings_df[ bookings_df['Email'] != admin_drop_booking ]
                        bookings_df.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\bookings.csv", sep=",", index=False)

                        print("User Bookings Updated.")

                    else:
                        print("Please enter a valid email.")
                        print("-----------------------")
                        
                        continue
                
                else:
                    print("Please enter a valid Number. Please restart the prompt to try again.")
                    exit()

            elif admin_panel == 6:
                print(users_data)
                
                print("-----------------------")

                print("1. Add a new User")
                print("2. Delete a User")

                users_manage = int(input("Choose a number: "))
                
                if users_manage == 1:
                    print("Adding a new user...")
                    new_user = input("Please enter email: ")
                    new_password = input("Please enter password: ")
                    users_data.loc[users_data.shape[0]] = [new_user,new_password]
                    users_data.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv",sep=",",index=False)

                    print("User successfully added! Please restart the prompt to Refresh the page.")
                    exit()

                elif users_manage == 2:
                    print("Deleting a user...")
                    admin_drop_user = input("Please enter the email of the booking you want to cancel (Case sensitive): ")
                    if admin_drop_user in users_data.values:
                        print("Ok")

                        users_data = users_data[users_data['email'] != admin_drop_user]
                        users_data.to_csv("C:\\Users\\Gopvasud\\Desktop\\Aarav\\Python\\users_data.csv", sep=",", index=False)

                        print("Users Updated.")
                        print("User successfully added! Please restart the prompt to Refresh the page.")
                        print("-----------------------")
                        exit()

                    else:
                        print("Please enter a valid email. Please restart the prompt to try again.")
                        print("-----------------------")
                        exit()


            else:
                print("Please enter a valid Number")
                continue

            exit()

        else:
            print("Incorrect email or password")
        continue

    else:
        print("Please enter a valid Number.")
        exit()
