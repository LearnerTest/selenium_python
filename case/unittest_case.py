#coding:utf-8

import unittest

class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case的前置')

    @classmethod
    def tearDownClass(self):
        print('所有case的后置')

    def setUp(self):
        print('case前置条件')

    def tearDown(self):
        print('case后置条件')
    def testcase01(self):
        print('第一个case')

    def testcase02(self):
        print('第二个case')



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('testcase01'))
    runner = unittest.TextTestRunner()
    runner.run(suite)