# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add dependencies
import csv
import os

# Import data from the file /Resources/election_results.csv
# Assign a variable to load a file from a path:
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path:
file_to_save = os.path.join("Resources", "election_analysis.txt")

# Open the election file and read the file
with open(file_to_load) as election_data:

    # Perform Analysis:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)
    



    # print(election_data)


# Create a filename variable to a direct or indirect path to a file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the open statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello Again!")

# Close the file.









