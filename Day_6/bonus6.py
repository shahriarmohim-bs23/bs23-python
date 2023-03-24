contents = ["Mohim","Abed","Wasif"]
filenames = ["doc.txt","report.txt","presentation.txt"]

for content,file in zip(contents,filenames):
    file = open(f"../files/{file}",'w')
    file.write(content)
    
    
    
a = "Mohim" \
    "wasif" \
    "Abed" 
print(a)