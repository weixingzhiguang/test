from rsa_util import RsaUtil


data = "{\"PageIndex\":\"1\",\"PageSize\":\"100\"}"
# data = "{\"PaymentType\":2,\"PaymentSerialNumber\":\"8887836000011111111\",\"PayType\":\"JS01\",\"ExpectTime\":\"2021-03-31 13:58:10\",\"PayerAccount\":\"817041635838\",\"CompanyCode\":\"200200\",\"CompanyName\":\"HONGKONG YUNEXPRESS LOGISTICS LIMITED\",\"PaymentAmount\":1.0,\"Currency\":\"HKD\",\"DebitCurrency\":\"HKD\",\"ReceiverAccount\":\"1067131025\",\"ReceiverName\":\"ETARGET LIMITED\",\"ReceiverBank\":\"CITIHKHBANK\",\"ReceiverBankType\":\"CIT\",\"ReceiverRegion\":\"HK\",\"ReceiverProvince\":\"\",\"ReceiverCity\":\"\",\"CorporateFlag\":1,\"IsUrgent\":1,\"Summary\":\"current account\",\"TradingPurposes\":\"YT007\",\"BankUnionNumber\":\"\",\"SwiftCode\":\"CITIHKHBANK\",\"PayeeRegion\":\"HK\",\"PayeeProvince\":\"\",\"PayeeCity\":\"\",\"PayeeStreetName\":\"\",\"PayeeBuildingNumber\":\"\",\"PayeePostcode\":\"\",\"BsbCode\":\"\",\"ERPRemark1\":\"\",\"ERPRemark2\":\"\"}"
# data = "{\"0\":\"0\",\"1\":\"1\",\"10\":\"10\",\"11\":\"11\",\"12\":\"12\",\"13\":\"13\",\"14\":\"14\",\"15\":\"15\",\"16\":\"16\",\"17\":\"17\",\"18\":\"18\",\"19\":\"19\",\"2\":\"2\",\"3\":\"3\",\"4\":\"4\",\"5\":\"5\",\"6\":\"6\",\"7\":\"7\",\"8\":\"8\",\"9\":\"9\"}"
#
#
pri_key = '''
MIIEpQIBAAKCAQEA73YF3SVgqXSKJ2pvHh3e3VZLdSOBkq8t9pfu0OOIzj1xCPpKK39
tMdj6a+z8cDWzGE/yBlYtpKuJYZF+ZIqGF71IdhEjFmq5Px0a9VWvl8PFpcZeLJsUs2
UBx8RN2wf+BhXU38pkUaUhhatB60z5yrSiTljihOrXP4ANuQ9qHave0IiTRn43EIo1g
RrY4kHGaVwWJhPXdi+Q4j3AdHVmaYGGw02tqzVus8GC8WskKuawd94G9sTzO/6fIlkz
O3dolAyMwWa8Gi6yEb7GPqDcuSH6KAwm4DFr2XBxHDjjAy2ogtLk1l/pK01FI0jMrx7
n1pnlc4JqdCq2MEbMgJuBWwIDAQABAoIBAQCmB68JJmFfHO6tZZ6lwxBDZxHqpjOxAM
VdtPpg22J/nRpCn0fN4QxVA5yeODLPmmwS71tgCWCcTFN00uxPybwvuY4ETt2FLXpDy
GposICPOa5QwrmJM/2mZOJXIETbGS+ICJsQj8P+1//mLlgGTdjkM1pV+EsW3b1gyei5
53YsGydqxriGIOCEdbh/2vzdRFw/9cjUnJuIja+tSxAI5za/LMAowyqaFjNaEHWwP6k
rEBZ+YDDlsbVVkDF4px8Du33u5Jr4flRkeZLlNS/RukBHFh3eECtbmyuJaL5X5s+jf0
WxCVwtdJ1nmNERtxd1DJ++zAS1YNF/pge1aeaRcFgBAoGBAP5mfXMq2Xmt1qHfrmbfp
9JYj0Hi/o2DW3nnUgYoBFHk5v8grWtuVQc9tHy5mMeea4yj/DMnyCH6TMWai2CNId8o
tWjkXBFjLD7Ff9gWClRyPkKzRkVd+uGGlG6hCjQROo8FhZcaamcLGr3a2nGuZ7hJgKo
g3e6vGp7Xfdbf+ljJAoGBAPD3fCS5EQ04Y+jIQTI77I8VYsYkOW8830+d7NMQozNPZp
zJjFGTxJCnbTS6C4xDUxvQVDhfYObZdfTiKrcJaEbWO66EM1aB7ZYZXGDHXAUGOPZCw
YBFPbYbN+jgpuOHf9kJefBmaTAecxxRCeMMDOH3N9wgUBKptTASMhYauz8DAoGBAKMR
3U4qZFbL6K3AbNGCgdeibsnEEHlzfvqIHZrWodZAzRUyxBb+FUDb+8qLSXSDhtsS7oF
3+aBWCkoMA1VzggfC124SGzYGBQGDpaxEjICO7nvg4KVsVXmkw5aaYaj4djnhRz2RcC
z3AEA8fhOqwM9vRitHgBsUYRL6fK50ycuJAoGBAIWkDGLljPJzEt4YqiftGh6k8roHf
x8VeJhUcvMAKDMd10Afe8YGmR7M7IEwqZTqBd7IJN168Gg3tPbStHP9MKsQx9rbEQnq
V1VGzXgTORLER7U0gtLcFAS6hcCPT5+jF6HMYqeUdMQuLxNGUqBsn3x3OrDH7wDaxFV
b0hF2U+D3AoGACahkwfCkLP/1xqqUztMgnKDJEB/W/izLHW+GGg1pQHwlkZ4sOvW0Px
sVT4liNCfaxzwA/q4i1/2oXX/Jgqa2CUL5Xuw5S3xJDzy6Qzg929lJdzhprTW4yN4E7
poegt/Yll+96aGkNtY9l3USxBUux6wwob2mviW8wBaUuTNE92M=
'''


pub_key = '''
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA73YF3SVgqXSKJ2pvHh3e3VZ
LdSOBkq8t9pfu0OOIzj1xCPpKK39tMdj6a+z8cDWzGE/yBlYtpKuJYZF+ZIqGF71Idh
EjFmq5Px0a9VWvl8PFpcZeLJsUs2UBx8RN2wf+BhXU38pkUaUhhatB60z5yrSiTljih
OrXP4ANuQ9qHave0IiTRn43EIo1gRrY4kHGaVwWJhPXdi+Q4j3AdHVmaYGGw02tqzVu
s8GC8WskKuawd94G9sTzO/6fIlkzO3dolAyMwWa8Gi6yEb7GPqDcuSH6KAwm4DFr2XB
xHDjjAy2ogtLk1l/pK01FI0jMrx7n1pnlc4JqdCq2MEbMgJuBWwIDAQAB
'''

# pri_key = '''
# MIICWwIBAAKBgQCQFA4YVQZatJAyO7TsuzkWE8dz17qi8GuOCnegKbKd6alLXkDz
# KhVG3kd3GijouHtlqsm2zFCK7K+I5MUu8Fuk23OEwIVZn9StltjLzJ1hB1AZC1/N
# CoCFZG5T2+AaQolrw8LvPS5jH2TuYQf7oLDHR88BKJgV/tZlr22Jicqm0wIDAQAB
# AoGAMP6A5IlVRdcNCef/2Fi6SuWi96OuleYHzR+GGnLTiJuCtFxy3b27yoOf7cJ5
# ktnZLHNtcLn90aA2+OhCnXmiz+M9PNArzfvtDoAKMlM9UEpBjGW/QYPkcHgnKOs9
# utAr4OnPB9PFdvCuwya4P8AL/7kpjSW+4zQpUT459BlJFxECQQDYUnQQgyR3CZiG
# Pj9vPfmmFmogpZpJTG9zAuOjOCxa5BQvV4iKhk6pkQAaVsjc7WMobEIhLqXn/I8E
# ldsqIPj1AkEAqoFZULpjke8CQm0rmr2UdbhU74KKYzeS2KKKc/2TdQUzTqvBdY2+
# VCyc0Ok6BWctBHfsu4FR6YpDYsg3QwvjpwJAEHeuaDdjhkBPwSBp+dDw+UjJiXSx
# 2xSbg1jb9WfoUH7+XmA+f7UbteLY7ChhIBheLQyYuCfx70gVpxa1WW6rJQJAEahR
# mpWi6CMLZduub1kAvew4B5HKSRohQAQdOIPjOHQwaw5Ie6cRNeBk4RG2K4cS12qf
# /o8W74udDObVKkFZ8wJAPL8bRWv0IWTlvwM14mKxcVf1qCuhkT8GgrG/YP/8fcW8
# SiT+DifcA7BVOgQjgbTchSfaA+YNe7A9qiVmA+G4GQ==
# '''
#
#
# pub_key = '''
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQFA4YVQZatJAyO7TsuzkWE8dz
# 17qi8GuOCnegKbKd6alLXkDzKhVG3kd3GijouHtlqsm2zFCK7K+I5MUu8Fuk23OE
# wIVZn9StltjLzJ1hB1AZC1/NCoCFZG5T2+AaQolrw8LvPS5jH2TuYQf7oLDHR88B
# KJgV/tZlr22Jicqm0wIDAQAB
# '''
rsa_util = RsaUtil(pub_key, pri_key)
print(f'原文: {data}')

encrypt = rsa_util.public_long_encrypt(data)
print(f'加密: {encrypt}')

decrypt_str = rsa_util.private_long_decrypt(encrypt)
print(f'解密: {decrypt_str}')
#
sign = rsa_util.sign(data)
print(f'sign: {sign}')

verify = rsa_util.verify(decrypt_str, sign)
print(f'verify: {verify}')

