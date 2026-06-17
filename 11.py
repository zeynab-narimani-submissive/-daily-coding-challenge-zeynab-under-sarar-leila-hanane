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
    def searchBookByname(self,key):
        flag = False
        for i in range(len(self.bookName)):
            if self.bookName[i] == key:
                flag = True
                print(self.publishYear[i],self.bookAuthor[i],self.bookPublisher[i],self.bookSubject[i])

        if flag == False:
            print("not found")
    def searchBookByIndex(self,index):
        if index > len(self.bookName) or index <= 0:
            print("index out of bounds")
        else:
            print(self.bookName[index-1],self.publishYear[index-1],self.bookAuthor[index-1],self.bookPublisher[index-1],self.bookSubject[index-1])
    def addBook(self,bookName,publishYear,bookAuthor,bookPublisher,bookSubject):
        self.bookName.append(bookName)
        self.publishYear.append(publishYear)
        self.bookAuthor.append(bookAuthor)
        self.bookPublisher.append(bookPublisher)
        self.bookSubject.append(bookSubject)
    def addBookByIndex(self,index,bookName,publishYear,bookAuthor,bookPublisher,bookSubject):
        self.bookName.insert(index-1,bookName)
        self.publishYear.insert(index-1,publishYear)
        self.bookAuthor.insert(index-1,bookAuthor)
        self.bookPublisher.insert(index-1,bookPublisher)
        self.bookSubject.insert(index-1,bookSubject)  
    def deleteBookByname(self,name):
        for i in range(len(self.bookName)):
            if self.bookName[i] == name:
                del self.bookName[i]
                del self.publishYear[i]
                del self.bookAuthor[i]
                del self.bookPublisher[i]
                del self.bookSubject[i]
                break
    def deleteBookByIndex(self,index):
        if index > len(self.bookName):
            print("not found")
        else:
            del self.bookName[index-1]
            del self.publishYear[index-1]
            del self.bookAuthor[index-1]
            del self.bookPublisher[index-1]
            del self.bookSubject[index-1]
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
l1.searchBookByname("oliver twist")
l1.searchBookByIndex(2)
l1.addBook("the alchemist",1988,"paulo coelho","harperone","philosophical")
l1.addBook("Tom Sawyer",1876,"mark twain","penguin","adventure")
l1.searchBookByname("the alchemist")
l1.searchBookByname("Tom Sawyer")
l1.addBookByIndex(66,"FLR in Education","2026","Miss Sara & Miss Leila","OWK","Life Style")
l1.deleteBookByname("the alchemist")
l1.deleteBookByIndex(5)
l1.searchBookByname("FLR in Education")