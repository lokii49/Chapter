class Chapter:
    """Chapter class with contains the details"""
    def __init__(self, subject, name, pages, marks):
        self.subject = subject
        self.name = name
        self.pages = pages
        self.marks = marks


class Exam:
    """This is exam class."""
    def __init__(self, examName, chapterList):
        self.examName = examName
        self.chapterList = chapterList

    def findMaximumChapterByPage(self):
        page = []
        for i in self.chapterList:
            page.append(i.pages)
        for item in self.chapterList:
            if max(page) == item.pages:
                return (item.subject, item.pages, item.marks, item.name)

    def sortChapterByMarks(self):
        mark = []
        for i in self.chapterList:
            mark.append(i.marks)
        sm = sorted(mark)
        return sm

if __name__=='__main__':
    num = int(input())
    chapterList=[]
    for i in range(num):
        subject = input()
        pages = int(input())
        marks = int(input())
        name = input()
        chapterList.append(Chapter(subject, name, pages, marks))
        examName = None
    obj = Exam(examName, chapterList)
    result1 = obj.findMaximumChapterByPage()
    for i in result1:
        print(i)
    result2 = obj.sortChapterByMarks()
    for i in result2:
        print(i)