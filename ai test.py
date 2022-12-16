import os

# Ask the user for their username and password
print("Enter your username:")
username = input()
print("Enter your password:")
password = input()

# Open the credentials file
with open("credentials.txt", "r") as f:
  # Read the contents of the file
  contents = f.read()
  
  # Check if the provided username and password are in the file
  if f"{username}:{password}" in contents:
    # Print the menu
    print("Menu:")
    print("1. New flight")
    print("2. Delete flight")
    print("3. Total fuel")
    
    # Ask the user to select an option
    print("Enter your choice:")
    choice = int(input())
    
    if choice == 1:
      # Ask the user for the flight number, duration, and type
      print("Enter the flight number:")
      flight_number = input()
      print("Enter the duration:")
      duration = input()
      print("Enter the type (takeoff or landing):")
      flight_type = input()
      
      # Create the file and write the flight information to it
      with open(f"c:\\flights\\{flight_type}-{flight_number}.txt", "w") as flight_file:
        flight_file.write(f"flight number: {flight_number}\n")
        flight_file.write(f"duration: {duration}\n")
        flight_file.write(f"type: {flight_type}\n")
    elif choice == 3:
      # Initialize the total fuel variable
      total_fuel = 0
      
      # Search for all takeoff files in the c:\flights directory
      for root, dirs, files in os.walk("c:\\flights"):
        for file in files:
          if file.startswith("takeoff-"):
            # Open the file and read the third line (which should contain the fuel value)
            with open(os.path.join(root, file), "r") as flight_file:
              second_line = int(flight_file.readlines()[2])
              
              # Add the fuel value to the total fuel
              total_fuel += second_line.split()[1]
      
      # Print the total fuel value
      print(f"Total fuel: {total_fuel}")
  else:
    print("Username and password do not match")