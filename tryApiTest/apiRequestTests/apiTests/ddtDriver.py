#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

from ddt import data,unpack,ddt
import unittest

@ddt
class MyDdtTest(unittest.TestCase):

    @data((1,1),(2,2),(3,3))
    @unpack
    def test_ddt(self,value1,value2):
        print('实际参数{0},预期参数{1}'.format(value1,value2))
        print(self.assertEqual(value1,value2))

if __name__ == '__main__':
    unittest.main(verbosity=2)

# import unittest
# from ddt import ddt,data,unpack
#
# @ddt
# class MyTestCase(unittest.TestCase):
#
#     @data((1,2),(2,3))
#     @unpack
#     def test_something(self,value1,value2):
#         print (value1,value2)
#         self.assertEqual(value2, value1+1)
#
# if __name__ == '__main__':
#     unittest.main()