import os
import unittest

from faker import Faker


class TestMain(unittest.TestCase):
    def test_faker(self):
        faker = Faker('zh_CN')
        print('姓名:', faker.name())  # 随机输出中文姓名
        print('联系方式:', faker.phone_number())  # 随机输出电话号码
        print('地址:', faker.address())  # 随机输出地址
        print('邮编: ', faker.postcode())  # 邮编# '611854'
        print('公司:', faker.bs())  # 随机输出公司
        print('工作:', faker.job())  # 随机输出工作
        print('邮箱:', faker.company_email())  # 随机输出邮箱
        print('身份证:', faker.ssn(min_age=18, max_age=100))  # 随机输出身份证号码
        print('文本:', faker.text())  # 随机文本
        # 生成地址相关的调用
        print('== 生成地址相关的调用 ==')
        print('楼名: ', faker.building_number())  # 楼名    # 'Q座'
        print('街道名称: ', faker.street_name())  # 街道名称# '重庆路'
        print('街道地址: ', faker.street_address())  # 街道地址# '重庆路A座'
        print('地区: ', faker.district())  # 地区# '金牛'
        print('完整城市名: ', faker.city())  # 完整城市名# '吉林市'
        print('城市名字: ', faker.city_name())  # 城市名字(不带市县)# '长春'
        print('城市后缀名: ', faker.city_suffix())  # 城市后缀名# '市'
        print('省: ', faker.province())  # 省# '吉林省'
        print('国家名称: ', faker.country())  # 国家名称# '俄罗斯'
        print(
            'BZ 国家编号: ', faker.country_code(representation='alpha-2')
        )  # 'BZ'   # 国家编号

    def test_print_evn(self):
        env_http_port = os.getenv('ENV_HTTP_PORT')
        print('env: ENV_HTTP_PORT=%s' % env_http_port)
        self.assertEqual(True, True)

    def test_big_num(self):
        a_num = 0x12345678901234567890123456789012345678901234567890123456789012345678901234567890
        b_num = 0x987654431234567890123456789012345678901234567890123456789012345678901234567890
        # env python3 3.11.+
        self.assertGreater(a_num, b_num)
        # env python3 3.9.2
        # self.assertLess(a_num, b_num)
        # self.assertLess(id(a_num), id(b_num))
        # == python2 cmp(str(a_num), str(b_num)) >> eq <- 0 gt <- 1 lt <- -1


if __name__ == '__main__':
    unittest.main()
