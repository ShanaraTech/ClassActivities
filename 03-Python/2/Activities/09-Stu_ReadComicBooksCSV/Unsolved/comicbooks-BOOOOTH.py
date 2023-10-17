# Modules
import os
import csv

# Prompt user for title lookup
title = input("What comic book are you looking for? ")

# Set path for file
# csvpath = os.path.join("..", "Resources", "comic_books.csv")
csvpath = "09-Stu_ReadComicBooksCSV\Resources\comic_books.csv"

# Set variable to check if we found the comic book
book_found = False

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Loop through looking for the video
        for row in csvreader:
                # Set variable to confirm we have found the video

                row_title = row[0]
                if row_title == title:
                        # extract cols we care about
                        publisher = row[8]
                        pub_date = row[9]

                        # craft return text
                        text = f"{row_title} was published by {publisher} in the year {pub_date}."
                        print(text)

                        # exit for
                        book_found = True
                        break

        # If the book is never found, alert the user
        if book_found == False:
                print(f"Sorry :( The comic {title} was not found in the data set.")
