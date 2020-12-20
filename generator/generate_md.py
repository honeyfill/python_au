class Task:
    def __init__(self, file):
        title = file.readline()
        title = title[:-1]
        self.title = "## {} \n".format(title)
        link = file.readline()
        self.link = "{}".format(link)
        self.menulink = "+ [{0}](#{1})".format(title, link.split('/')[-2])
        self.code = []
        self.code.append('```python\n')
        for i in file.readlines():
            self.code.append(i)
        self.code.append('\n')
        self.code.append('```\n')

class MdFile:
    def __init__(self, file):
        self.title = file.readline()
        self.menu = []
        file.readline()
        cur_line = file.readline()
        while cur_line and cur_line[0] == '+':
            self.menu.append(cur_line)
            cur_line = file.readline()
        self.code = []
        self.code.append(cur_line)
        for i in file.readlines():
            self.code.append(i)

SourceFile = open("source_leetcode_data.txt", 'r')
task = Task(SourceFile)
SourceFile.close()

FileName = input()
fileName = FileName.lower();
MdHolder = open(fileName + ".md", 'r')
mdfile = MdFile(MdHolder)
MdHolder.close()

OutputFile = open("tree.md", 'w')
OutputFile.write('# ' + FileName + '\n\n')
for i in range(len(mdfile.menu)):
    OutputFile.write(mdfile.menu[i])
OutputFile.write(task.menulink + '\n')
for i in range(len(mdfile.code)):
    OutputFile.write(mdfile.code[i])
OutputFile.write(task.title + '\n')
OutputFile.write(task.link + '\n')
for i in task.code:
    OutputFile.write(i)
OutputFile.close()
