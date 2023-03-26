def html(tag):
    def title(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return title

print(__name__)
        """_ When we import a python file at that time the value of __name__ will be file name
         But when we run the file the value of __name__ will be __main__. _
        """
if __name__ == "__main__":
   print("i am from main")