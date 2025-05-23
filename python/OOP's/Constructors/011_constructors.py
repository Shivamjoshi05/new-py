class book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def get_info(self):
        print(f"the title is {self.title} author: {self.author} and size {self.pages} pages")

b=book("Wings","Raj",390)
b.get_info()
