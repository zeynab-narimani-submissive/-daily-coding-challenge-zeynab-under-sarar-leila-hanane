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
    def editNameByIndex(self,index,name):
        self.bookName[index-1] = name
    def editNamebyValue(self,currentName,newName):
        for i in range(len(self.bookName)):
            if self.bookName[i] == currentName:
                self.bookName[i] = newName
    def editYearByIndex(self,index,year):
        self.publishYear[index-1] = year
    def editYearByValue(self,currentYear,newYear):
        for i in range(len(self.publishYear)):
            if self.publishYear[i] == currentYear:
                self.publishYear[i] = newYear
    def editAuthorByIndex(self,index,author):
        self.bookAuthor[index-1] = author
    def editAuthorbyValue(self,currentAuthor,newAuthor):
        for i in range(len(self.bookAuthor)):
            if self.bookAuthor[i] == currentAuthor:
                self.bookAuthor[i] = newAuthor
    def editPublisherByIndex(self,index,publisher):
        self.bookPublisher[index-1] = publisher
    def editPublisherbyValue(self,currentPublisher,newPublisher):
        for i in range(len(self.bookPublisher)):
            if self.bookPublisher[i] == currentPublisher:
                self.bookPublisher[i] = newPublisher
    def editSubjectByIndex(self,index,subject):
        self.bookSubject[index-1] = subject
    def editSubjectByValue(self,currentSubject,newSubject):
        for i in range(len(self.bookSubject)):
            if self.bookSubject[i] == currentSubject:
                self.bookSubject[i] = newSubject
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
#l1.deleteBookByIndex(5)
#l1.searchBookByname("FLR in Education")
l1.editNameByIndex(4,"FLR in Education for Everyone")
l1.searchBookByIndex(4)
l1.editNamebyValue("FLR in Education for Everyone","FLR in Education")
l1.searchBookByname("FLR in Education")
l1.editYearByIndex(4,2025)
l1.searchBookByIndex(4)
l1.editYearByValue(2025,2026)
l1.searchBookByname("FLR in Education")
l1.editAuthorByIndex(4,"Miss Sara & Miss Tara lala")
l1.searchBookByname("FLR in Education")
