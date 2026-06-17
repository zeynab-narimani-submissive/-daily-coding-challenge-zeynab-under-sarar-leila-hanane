class library:
    def __init__(self,bookName,publishYear,bookAuthor,bookPublisher,bookSubject):
        self.bookName = bookName
        self.publishYear = publishYear
        self.bookAuthor = bookAuthor
        self.bookPublisher = bookPublisher
        self.bookSubject = bookSubject
    def searchSubject(self,key):
        flag = False
        for i in range(len(self.bookSubject)):
            if self.bookSubject[i] == key:
                flag = True
                print(self.bookName[i],self.publishYear[i],self.bookAuthor[i],self.bookPublisher[i])

        if flag == False:
            print("not found")
bookName = ["harry potter","the little prince","oliver twist"]
publishYear = [1399,1395,1393]
bookAuthor = ["J.k rowling","antonie de saint","charles dickens"]
bookPublisher = ["Penguin","Cherry","Alba"]
bookSubject = ["magic","fantasy","adventure"]
l1 = library(bookName,publishYear,bookAuthor,bookPublisher,bookSubject)
print(l1.bookName)
print(l1.publishYear)
print(l1.bookAuthor)
print(l1.bookPublisher)
print(l1.bookSubject)
l1.searchSubject("magic")   