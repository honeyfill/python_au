class MdFile:
    def __init__(self, title, link, code):
        self.title = title
        self.link = link
        self.code = code

        def get_title(self):
            return "## " + self.title.slpit(". ")[1].strip("\n")

        def get_link(self):
            title = self.title.slpit(". ")[1].strip("\n")
            link_tale = self.link.split("/")[-2]
            return f"+ [{title}](#{link_tale})"

        def get_code(self):
            return f"```python\n{self.code}\n```\n"

        def get_task(self):
            return f"{self.get_title()}\n\n{self.link}\n\n{self.get_code()}\n"


def read_source(filename):
    data = filename.readlines()
    res = [data[0], data[1].strip("\n"), "".join(map(lambda x: x[8::], data[6::]))]
    return res


def read_old(filename):
    data = []
    file = open(f"leetcode/{filename})")
    data = file.read()
    file.close()
    return data


def prepare_to_write(md, data):
    links = ''
    tasks = ''
    if (len(data) != 0):
        links, tasks = data.split("<!---->\n")  # i found, that it isn't shows at md files, amazing
    links += md.get_link()
    tasks += md.get_task()
    tasks.strip('\n')
    return [links, tasks]


def write_to_file(filename, data):
    title = f"# {filename.split('.')[0].upper()}\n\n"
    file = open(f"leetcode/{filename}", "w")
    if title not in data[0]:
        file.write(title)
    file.write(f"{data[0]}")
    file.write("\n<!---->\n")  # i found, that it isn't shows at md files, amazing
    file.write(data[1])


def main(source, lol):
    txt_file = MdFile(read_sourсe(source))
    md_file = read_old(lol)
    md_file = prepare_to_write(txt_file, md_file)
    write_to_file(lol, md_file)


source = input()
lol = input()
