#!/usr/bin/python3

from html.parser import HTMLParser

# overide the original HTMLParser parent class

class myHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if len(attrs) != 0:
            for att in attrs:
                print("->",att[0], ">", att[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if len(attrs) != 0:
            for att in attrs:
                print("->",att[0], ">", att[1])
    # def handle_data(self, data):
    #     print("Found data: ", data)

# my_parser = myHTMLParser()
# my_parser.feed("<html><head><title>HTML Parser - I</title></head>"
# +"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")

if __name__ == "__main__":
    html_str = ""
    my_parser = myHTMLParser()
    N = int(input())
    while N:
        html_str += input()
        N -= 1
    my_parser.feed(html_str)