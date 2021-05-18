from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import requests
from Crypto import Random

def gen_sign(private_key, unsign_data):
    rsaKey = RSA.importKey(base64.b64decode(private_key))
    signer = Signature_pkcs1_v1_5.new(rsaKey)
    digest = SHA256.new()
    digest.update(unsign_data.encode('utf8'))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    return signature


def gen_encipher(publicKey, unsign_data):
    rsaKey = RSA.importKey(base64.b64decode(publicKey))
    encipher = Cipher_pkcs1_v1_5.new(rsaKey)
    encipher =encipher.encrypt(unsign_data.encode('utf=8'))
    encipherture = base64.b64encode(encipher)
    return encipherture


def gen_decipher(private_key, unsign_data,sentinel=b'decrypt error'):
    rsaKey = RSA.importKey(base64.b64decode(private_key))
    decipher = Cipher_pkcs1_v1_5.new(rsaKey)
    decipherture=decipher.decrypt(base64.b64decode(unsign_data.encode('utf-8')),sentinel)
    return decipherture


def request_bank():
    content1 = "appKey=aiguAae0b9&charset=UTF-8&sign_type=RSA2&timeStamp=1589279314"
    content2 = "{\"PageIndex\":2,\"PageSize\":172}"
    privateKey = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5rwTUDHtHh1lBSFvXvEge6mBx91yuEVhA8TCL9va8Tt5NwD8Chfd+qbak00ihbg55ld+e/tVEwnvqxRRRg3aDimWb0ddKBGJyvAaABT+OFMojC9lK6detMPScAn4JTPwvWtu3DYthOsGFqXyg56X5v0sQr6c/2noQrmSdJm8ux+9py/YIOiaE9gfNOoFSwzxvrlxvrGVLYMWk6BEh5rgRrtWE2CVZgdTrJntE9MqvZgOa3nT+qatwgSM94pNCRR7n2ELyB16vE2huTJjdh4P8LnkZ579dHRmL6c7hIKwgUcV6jyQHk2VhresWQLr8aNelNmJVqXwTCf3x9tQoaHavAgMBAAECggEAfkXfarTyQTpyIEss6hFImn2ZCOfHRzjUY5WiBgz0zip0Uzuhnf2syZ5wbragded6QIUDhgSW1CPOUWGk56oXNm0vnD+fwN4qdQwY/4aSKfVJYXv1UVSlL0pTjqTDQV/xP+Lx+BJl7sEeSd9wuZvO64CDc92AR5Qz3pQ6KASzJ4P3Ph5OInLNXqhl7VoMbFa9uAqApsiUT/try5J+dggt6deXX7dO01I1b9vNvulrL1gUeXyaBBL+mYd43d7OOGgKhDigQAhqfCZEtDkhxi+uON1VnCwWft/UbDYN2hGMGkl8F+y/VhfcAzszkM5Ivrekmw0db9dAMt1Si/BIt9kaAQKBgQDhoK34o12qoBha35p0oe1Q06R7CyWnIag2VqQdEMKb2KiXABOXvkkyaZatkGJTJFURjOKkyFnqpt1R7Wn9fOkd5+i7WhbMMW034oOhL5BHVmHteTcNXkMIZlEv5C4xq+fHz9B0tIDkixK4n4tOaU5XT/K81Vem+vUMZ2LBZIh3IQKBgQDSrdXpic0u0t2OqJrkiaqHlBZr4qh//IFlOCBUJmy8874jXWTvVOiJIOrBvf9FFVFZQR9QdgS+X0WChYB3IBRBcj8vaEiOa7k1fpvyH40nXl5oGRNLIynpvhj0Ls8PRaYDim+DbH0N8J6mhB26ET1/ccpr8MiqKZqWaSelKxLDzwKBgGwJeWRGLXKnKCJTUW0poC4EuYylYMkvh5FFWV4FiXoAe3Gaesc9OWVnQ9wl977h9c3qjRfkS5HdhrpVGVxktGc6hak4URRDUo3g67CByu8twMRqN18yVJywCY4KD8h/DQQTUTiguds1cKhw1M6eBAIw6QVcjpUJM89Vreb2kZWhAoGBAMzcSqin3cQNOXHSE6PtFcx2PIM1yKGDeJNjS1RodM4buaUL2O08xE0rm/s+9G1JuGuw/nEwAZbYb2/mvy+XGvs0y6oenocWyubwsVV0Rr6kbeqNj4w9qjDnL76pkaCJGlBRGfRS1xtqAetrhrh6sTEvBiWF4qpMgEyH/gwG4V1TAoGAInqQ6QnMJtHFFdRSUzixNXAALHgPnn9EMuA4w+CmnhwXz15jTW24R6YJni6zRiCylqTPXZGz5uqO+tvKMaTQqFmiJ++KGtcpyug81HNSWEaG5Bpsn1IeGscWWkBZJvMqqCmBWWIVw4127o6lPGXz5AHONJ1VO0wA/IifNUb1Cvc="
    publicKey = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv7s9h0rjs6WMvpc9NntRm8qg6afOc+upbLcj2h8z4cRDuyMpjmPgZa5WuArrl596QfmHs3OwfBsGPu/9XiwNhlS5xwoC+XKaPOdbhLQr3YMygmcvAvZD8XiHo7qfBCnBxDjKyCZru4G9zAPivsjbp/f+MtlxOHXZ3pnYpeS8IvKDmKmix1lqA6h3gtwdHXnRIMC7i+jQt9LfXbCJkBnkMHGkYBJm1mz/gwjwg1ktBh8Apx9dMVcNXF17OiwncOnyhVHoIxAPq0vM/p7IRoZmDeoD1XrHbERNwnNwOUziaPdUIHtM+YYEKFfIvNLhX07rSxxGzllHrHb3SzULuoGuEQIDAQAB"
    privateKey1 = "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5rwTUDHtHh1lBSFvXvEge6mBx91yuEVhA8TCL9va8Tt5NwD8Chfd+qbak00ihbg55ld+e/tVEwnvqxRRRg3aDimWb0ddKBGJyvAaABT+OFMojC9lK6detMPScAn4JTPwvWtu3DYthOsGFqXyg56X5v0sQr6c/2noQrmSdJm8ux+9py/YIOiaE9gfNOoFSwzxvrlxvrGVLYMWk6BEh5rgRrtWE2CVZgdTrJntE9MqvZgOa3nT+qatwgSM94pNCRR7n2ELyB16vE2huTJjdh4P8LnkZ579dHRmL6c7hIKwgUcV6jyQHk2VhresWQLr8aNelNmJVqXwTCf3x9tQoaHavAgMBAAECggEAfkXfarTyQTpyIEss6hFImn2ZCOfHRzjUY5WiBgz0zip0Uzuhnf2syZ5wbragded6QIUDhgSW1CPOUWGk56oXNm0vnD+fwN4qdQwY/4aSKfVJYXv1UVSlL0pTjqTDQV/xP+Lx+BJl7sEeSd9wuZvO64CDc92AR5Qz3pQ6KASzJ4P3Ph5OInLNXqhl7VoMbFa9uAqApsiUT/try5J+dggt6deXX7dO01I1b9vNvulrL1gUeXyaBBL+mYd43d7OOGgKhDigQAhqfCZEtDkhxi+uON1VnCwWft/UbDYN2hGMGkl8F+y/VhfcAzszkM5Ivrekmw0db9dAMt1Si/BIt9kaAQKBgQDhoK34o12qoBha35p0oe1Q06R7CyWnIag2VqQdEMKb2KiXABOXvkkyaZatkGJTJFURjOKkyFnqpt1R7Wn9fOkd5+i7WhbMMW034oOhL5BHVmHteTcNXkMIZlEv5C4xq+fHz9B0tIDkixK4n4tOaU5XT/K81Vem+vUMZ2LBZIh3IQKBgQDSrdXpic0u0t2OqJrkiaqHlBZr4qh//IFlOCBUJmy8874jXWTvVOiJIOrBvf9FFVFZQR9QdgS+X0WChYB3IBRBcj8vaEiOa7k1fpvyH40nXl5oGRNLIynpvhj0Ls8PRaYDim+DbH0N8J6mhB26ET1/ccpr8MiqKZqWaSelKxLDzwKBgGwJeWRGLXKnKCJTUW0poC4EuYylYMkvh5FFWV4FiXoAe3Gaesc9OWVnQ9wl977h9c3qjRfkS5HdhrpVGVxktGc6hak4URRDUo3g67CByu8twMRqN18yVJywCY4KD8h/DQQTUTiguds1cKhw1M6eBAIw6QVcjpUJM89Vreb2kZWhAoGBAMzcSqin3cQNOXHSE6PtFcx2PIM1yKGDeJNjS1RodM4buaUL2O08xE0rm/s+9G1JuGuw/nEwAZbYb2/mvy+XGvs0y6oenocWyubwsVV0Rr6kbeqNj4w9qjDnL76pkaCJGlBRGfRS1xtqAetrhrh6sTEvBiWF4qpMgEyH/gwG4V1TAoGAInqQ6QnMJtHFFdRSUzixNXAALHgPnn9EMuA4w+CmnhwXz15jTW24R6YJni6zRiCylqTPXZGz5uqO+tvKMaTQqFmiJ++KGtcpyug81HNSWEaG5Bpsn1IeGscWWkBZJvMqqCmBWWIVw4127o6lPGXz5AHONJ1VO0wA/IifNUb1Cvc="
    # 设置URL
    sign = str(gen_sign(privateKey, content1), encoding="utf-8")
    print(sign)
    url = "http://192.168.87.135:5001/api/v1/entrance/bankTypePageQuery"
    # 设置消息头
    headers = {
        "charset": "UTF-8",
        "Content-Type":"text/plain",
        "appKey": "aiguAae0b9",
        "timeStamp":"1589279314",
        "sign":sign
    }
    data =str(gen_encipher(publicKey, content2), encoding="utf-8")
    response = requests.post(url, headers=headers, data=data)
    data1= str(response.text)
    print("Status code:", response.status_code)
    print(response.text)
    data1 = str(gen_decipher(privateKey1, data1), encoding="utf-8")
    print(data1)

if __name__ == '__main__':
    request_bank()

