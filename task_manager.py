# ===== Importing external modules ===========
'''This is the section where you will import modules'''
from datetime import datetime

# ==== Login Section ====
# TODO: Implement the following functionality
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and passwords from the user.txt file
    - You can use a list or dictionary to store a list of usernames and
       passwords from the file.
    - Use a while loop to validate your user name and password.
'''
# Create an empty dictionary to store usernames and passwords
users = {}

# Open user.txt and read usernames and passwords
with open("user.txt", "r") as user_file:
    for line in user_file:
        username, password = line.strip().split(", ")
        users[username] = password

# Keep asking the user to log in until correct details are entered
while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Check if username exists
    if username_input not in users:
        print("That username does not exist. Please try again.\n")

    # Check if password is correct
    elif users[username_input] != password_input:
        print("Incorrect password. Please try again.\n")

    else:
        print(f"\nWelcome, {username_input}!\n")
        break

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input(
        '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
    ).lower()

    if menu == 'r':
        # TODO: Implement the following functionality
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        # Ask for new username
        new_username = input("Enter new username: ")

        # Check if username already exists
        if new_username in users:
            print("Username already exists. Please try a different one.\n")

        else:
            # Ask for password
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm password: ")

            # Check if passwords match
            if new_password == confirm_password:
                # Save to file
                with open("user.txt", "a") as user_file:
                    user_file.write(f"\n{new_username}, {new_password}")

                # Add to dictionary (so it works immediately without restarting)
                users[new_username] = new_password
                print("User registered successfully!\n")

            else:
                print("Passwords do not match. Please try again.\n")    

    elif menu == 'a':
        # TODO: Implement the following functionality
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not
              complete.
        '''
        # Ask for task details
        assigned_to = input("Enter the username of the person assigned to this task: ")

        if assigned_to not in users:
            print("That user does not exist. Please register the user first.\n")

        else:
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (e.g. 25 Oct 2025): ")
        
            # Get today's date
            date_assigned = datetime.today().strftime("%d %b %Y")
            # New tasks are always incomplete at first
            task_completed = "No"

            # Write the task to tasks.txt
            with open("tasks.txt", "a") as task_file:
                task_file.write(
                    f"\n{assigned_to}, {task_title}, {task_description}, "
                    f"{date_assigned}, {due_date}, {task_completed}"
        )
            
            print("Task added successfully!\n")
        
    elif menu == 'va':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in
              the PDF
            - It is much easier to read a file using a for loop.'''
        # Open tasks.txt and read all tasks
        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                # Split each line into parts
                assigned_to, task_title, task_description, date_assigned, due_date, task_completed = line.strip().split(", ")

                # Display each task in a readable format
                print("\n" + "-" * 40)
                print(f"Task:               {task_title}")
                print(f"Assigned to:        {assigned_to}")
                print(f"Date assigned:      {date_assigned}")
                print(f"Due date:           {due_date}")
                print(f"Task complete?      {task_completed}")
                print(f"Task description:   {task_description}")
                print("-" * 40)

    elif menu == 'vm':
        # TODO: Implement the following functionality
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        # Open tasks.txt and read all tasks
        with open("tasks.txt", "r") as task_file:
            found_task = False

            for line in task_file:
                # Split each line into parts
                assigned_to, task_title, task_description, date_assigned, due_date, task_completed = line.strip().split(", ")

                # Only show tasks for the logged-in user
                if assigned_to == username_input:
                    found_task = True

                    print("\n" + "-" * 40)
                    print(f"Task:               {task_title}")
                    print(f"Assigned to:        {assigned_to}")
                    print(f"Date assigned:      {date_assigned}")
                    print(f"Due date:           {due_date}")
                    print(f"Task complete?      {task_completed}")
                    print(f"Task description:   {task_description}")
                    print("-" * 40)

            # If no tasks were found for this user
            if not found_task:
                print("You have no tasks assigned to you.\n")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")