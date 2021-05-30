import operator
import unittest
from faker import Faker
import os


class TestMain(unittest.TestCase):
    def test_print_evn(self):
        # env_http_port = os.getenv('ENV_HTTP_PORT')
        # print('env: ENV_HTTP_PORT=%s' % env_http_port)
        # self.assertEqual(True, True)

        # env python3 3.9.2
        a_num = 0x12345678901234567890123456789012345678901234567890123456789012345678901234567890
        b_num = 0x987654431234567890123456789012345678901234567890123456789012345678901234567890
        self.assertGreater(a_num, b_num)
        print(operator.gt(str(a_num), str(b_num)))  # False
        # == python2 cmp(str(a_num), str(b_num)) >> eq <- 0 gt <- 1 lt <- -1
        self.assertLess(id(a_num), id(b_num))

        # self.assertTrue(operator.gt(str(a_num), str(b_num)))
        # self.assertTrue()

    def test_faker(self):
        faker = Faker("zh_CN")
        print('姓名:', faker.name())  # 随机输出中文姓名
        print('联系方式:', faker.phone_number())  # 随机输出电话号码
        print('地址:', faker.address())  # 随机输出地址
        print('公司:', faker.bs())  # 随机输出公司
        print('工作:', faker.job())  # 随机输出工作
        print('邮箱:', faker.company_email())  # 随机输出邮箱
        print('身份证:', faker.ssn(min_age=18, max_age=100))  # 随机输出身份证号码
        print('文本:', faker.text()) # 随机文本


if __name__ == '__main__':
    unittest.main()
