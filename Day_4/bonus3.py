filenames = ["1.Raw Data.txt", "2.Repository Data.txt", "3.Presentation Data.txt"]


for filename in filenames:
    filename = filename.replace(".txt",".py")
    filename = filename.replace(".","-",1) #Specify the which dot have to be replaced
    print(filename)