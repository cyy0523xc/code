# -*- coding: utf-8 -*-
# python test2.py

from widget import Widget, func
import unittest


# 执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))

    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))


# 对函数进行单元测试
class FuncTestCase(unittest.TestCase):
    def testFunc(self):
        self.assertEqual(func(2), 3)


# 测试
if __name__ == "__main__":
    unittest.main()
