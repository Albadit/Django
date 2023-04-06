import os, sys

if __name__ == "__main__":
    run = True

    while run:
        print("Press 1: to run server")
        print("Press 2: to make migrations")
        print("Press 3: to migrate")
        print("Press 4: to create super user")
        user_input = input("Select option: ").lower()

        if user_input == "1":
            file = os.path.join(sys.path[0], "manage.py")
            os.system(f"python {file} runserver")

        if user_input == "2":
            file = os.path.join(sys.path[0], "manage.py")
            os.system(f"python {file} makemigrations")
        
        if user_input == "3":
            file = os.path.join(sys.path[0], "manage.py")
            os.system(f"python {file} migrate")
        
        if user_input == "4":
            file = os.path.join(sys.path[0], "manage.py")
            os.system(f"python {file} createsuperuser")