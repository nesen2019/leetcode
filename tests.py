#!/usr/bin/python 
# -*- ecoding=utf-8 -*-
import os
import unittest
from unittest import TestCase
from utils.utils import load_module

PATH_PROJECT = "/root/progs/notebook/edocteel"
PATH_PROJECT = r"D:\Prog\leetcode"


class Test(TestCase):
    my_modules = dict()

    def load_the_module(self, filename):
        module_name = os.path.basename(os.path.splitext(filename)[0])
        if module_name not in self.my_modules:
            module = load_module(filename, module_name=module_name)
            self.my_modules[module_name] = module
        return self.my_modules[module_name]

    def mytest_module(self, filename):
        file_dir, file_name = os.path.split(filename)
        module_test = load_module(file_path=filename)
        if "_t" in file_name:
            filename_val = os.path.join(file_dir, f"{file_name.split('_t')[0]}.py")
            module_val = load_module(file_path=filename_val)
        else:
            module_val = module_test
        module_val.Solution.check_class(module_test.Solution)
        return True, file_name

    def test_all_file(self):

        path = os.path.join(PATH_PROJECT, "lecode100")
        path_list = os.listdir(path)

        for i in path_list:
            if i.startswith("__"):
                continue
            filename = os.path.join(os.path.abspath(path), i)
            if os.path.isfile(filename):
                self.mytest_module(filename)

    def test_one_file(self):
        filename = os.path.join(PATH_PROJECT, "lecode100", "I0001_L0001_t01.py")
        self.mytest_module(filename=os.path.abspath(filename))


if __name__ == "__main__":
    unittest.main()
