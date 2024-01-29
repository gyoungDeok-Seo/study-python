from s_mysql.task.mysql_with_api.crud_module import *
from o_api.external.sms import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.parse
import urllib.request
import smtplib
import ssl
import hashlib
import json
import random
import requests


# 아이디(이메일) 중복검사
def check_email(email):
    find_by_id_query = "select email from tbl_member where email = %s"
    find_by_id_param = email,
    member_info = find_by_id(find_by_id_query, find_by_id_param)

    return member_info


def pw_encryption(password):
    encryption = hashlib.sha256()
    encryption.update(password.encode('utf-8'))

    return encryption.hexdigest()


def create_number():
    numbers = "0123456789"
    result = ""

    for i in range(6):
        result += numbers[random.randint(0, 9)]

    return result


def send_sms(phone):
    result = create_number()

    data = {
        'messages': [
            {
                'to': phone,
                'from': '01049124083',
                'text': f'{result}'
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    return result


def send_email(member_email, certification_number):
    port = 587
    smtp_server = 'smtp.gmail.com'
    sender_email = 'kjkj0724@gmail.com'
    receiver_email = member_email
    password = 'lxyh lrsc byoc xdln'
    message = f"[사이트명 인증번호]\n{certification_number}"

    msg = MIMEText(message, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, data.as_string())
        # server.sendmail(sender_email, receiver_email, message.encode('utf-8'))


def papago(korean):
    client_id = "w58H9rKvOAjhIjLLcAiE"
    client_secret = "XAfQKAdK5V"
    encoding_text = urllib.parse.quote(korean)
    data = f"source=ko&target=en&text={encoding_text}"
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    # -H
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response = json.loads(response.read().decode("utf-8"))
        result = response['message']['result']['translatedText']

        return result


def ocr(image_directory):
    url = f'https://api.ocr.space/parse/imageurl?apikey=K82432867788957&url={image_directory}&language=kor&isOverlayRequired=true'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()
    # print(type(result))
    # print(result['ParsedResults'][0]['ParsedText'])