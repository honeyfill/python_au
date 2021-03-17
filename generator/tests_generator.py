import unittest
from generator.generate_md import *


class TestMdFile(unittest.TestCase):

    def test_lnk(self):
        md = MdFile(read_source('test.py'))
        expect_link = '+ [I write random text](#i-write-random-text)'
        self.assertEqual(md.get_link(), expect_link)

    def test_title(self):
        md = MdFile(read_source('test.py'))
        expect_title = '## I wont to do it\n'
        self.assertEqual(md.get_title(), expect_title)

    def test_code(self):
        md = MdFile(read_source('test.py'))
        expect_code = '''python\nreturn str(11 - 12)\n'''
        self.assertEqual(md.get_code(), expect_code)

    def test_task(self):
        md = MdFile(read_source('test.py'))
        expect_task = """## I wont to do it
        '''python
        return str(11 - 12)
        '''\n\n"""
        self.assertEqual(md.get_task(), expect_task)
