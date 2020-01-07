#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from test11.calculator import Calculator

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        u'表示所有用例开始时'
        print('测试用例开始-----')

    @classmethod
    def tearDownClass(cls):
        u'表示所有用例都执行完后'
        print("测试用例结束")

    def setUp(self):
        u'每条用例开始前设置前置条件'
        print('设置前置条件')

    def tearDown(self):
        u'每条用例结束后设置后置动作'
        print('设置后置动作')

    @unittest.skipIf(True,'如果前面条件为真则跳过执行')#通过该装饰器可以设置如果前面条件为真则跳过用例执行
    def test_add(self):
        c = Calculator(3,5)
        result = c.add()
        self.assertEqual(result,8,msg='加法运算失败')

    @unittest.expectedFailure  #过该装饰器可以设置该测试用例的执行结果都是失败
    def test_sub(self):
        c = Calculator(23,12)
        result = c.sub()
        self.assertEqual(result, 12, msg='减法运算失败')

    @unittest.skipUnless(3>2,'如果条件为真时则执行用例') #通过该装饰器可以设置如果条件为真时则执行用例
    def test_mul(self):
        c = Calculator(1,2)
        result = c.mul()
        self.assertEqual(result, 2, msg='乘法运算失败')

    @unittest.skip("直接跳过测试") #通过该装饰器可以设置直接跳过该用例的执行
    def test_div(self):
        c = Calculator(23,12)
        result = c.div()
        self.assertEqual(result, 1, msg='除法运算失败')

if __name__ == "__main__":
    u'创建测试套件'
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    #创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)

