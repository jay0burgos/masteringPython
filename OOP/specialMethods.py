

class Sample():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    #following are special methods
    def __str__(self) -> str: #if theres a used function such as print() that requires the string representation of class it will class this function
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print("book object deleted")

myBook = Sample("myLife", "jose", 23)

print(myBook)

print(len(myBook))

del(myBook)




