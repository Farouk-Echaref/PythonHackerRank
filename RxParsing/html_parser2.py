#!/usr/bin/python3

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

if __name__ == "__main__":
    html_str = ""
    my_parser = MyHTMLParser()
    N = int(input())
    while N:
        html_str += input()
        html_str += '\n'
        N -= 1
    my_parser.feed(html_str)
    my_parser.close()