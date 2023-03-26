import glob
import csv
import shutil
import webbrowser

# myfiles = glob.glob("./files/*.txt")


# for filepath in myfiles:
#     with open(filepath,'r') as file:
#          print(file.read().upper())


# with open("./files/weather.csv","r") as file:
#      data = list(csv.reader(file))
# city = input("Enter a city: ")

# for row in data[1:]:
#     if row[0] == city:
#        print(row[1])

#shutil.make_archive("output","zip","files")
user_term = input("Enter a search team: ")
webbrowser.open("https://google.com/search?q="+user_term)
