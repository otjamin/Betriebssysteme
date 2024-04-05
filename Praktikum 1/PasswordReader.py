import fileinput

# Open file as read-only
with fileinput.input("etc/passwd") as f:
    # Iterate over lines
    for line in f:
        # Split line by colon
        colons = line.split(":")

        # Print username and UID
        print(f"Benutzername: {colons[0]}")
        print(f"UID: {colons[2]}")  # \n is read from the file, so we don't need to explicitly add a new line here

