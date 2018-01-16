from html.parser import HTMLParser

# create a subclass and overried the handler methods
class MyHTMLParser(HTMLParser):

    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print('Encountered comment:', data)
        pos = self.getpos()
        print('At line: ', pos[0], " position ", pos[1])

    # function to handle the ending tag
    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])

    # function to handle character and text data (tag contents)
    def handle_data(self, data):
        print("Encountered some data:", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])



def main():
    # instantiate the parser and feet it some HTML
    parser = MyHTMLParser()



    # open the sample HTML file and read it
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read() # read the entire file
        parser.feed(contents)


main()