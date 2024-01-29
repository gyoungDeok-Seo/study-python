from s_mysql.task.mysql_with_api.service_module import *
from random import randint

if __name__ == '__main__':
    # while True:
        # service_choice = input('1. 회원가입\n2. 로그인 및 비밀번호 변경\n3. 한국어 번역')
        # 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
        # 아이디(이메일) 중복검사
        # insert_query = "insert into tbl_member(email, password, name) values (%s, %s, %s)"
        #
        # email = input("이메일: ")
        # password = input("비밀번호: ")
        # name = input('이름: ')
        #
        # if check_email(email):
        #     print('이미 사용 중인 이메일입니다.')
        #     continue
        #
        # else:
        #     phone = input('전화번호: ')
        #     authentication = send_sms(phone)
        #     if authentication == input('인증번호: '):
        #         insert_params = email, pw_encryption(password), name
        #         save(insert_query, insert_params)
        #         print('회원가입이 완료되었습니다.')
        #         break
        #
        #     else:
        #         print('인증번호를 다시 확인해주세요.')



        # 로그인 후 마이페이지로 이동
        # 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사
        # message = "이메일: "
        # member_email = input(message)
        # find_by_id_query = "select email, password, name from tbl_member where email = %s"
        # find_by_id_params = member_email,
        # member = find_by_id(find_by_id_query, find_by_id_params)
        #
        # if member:
        #     message = "비밀번호: "
        #     member_password = input(message)
        #     encryption = hashlib.sha256()
        #     encryption.update(member_password.encode('utf-8'))
        #     member_password = encryption.hexdigest()
        #
        #     if member.get("password") == member_password:
        #         print(f"{member.get('name')}님 환영합니다~!")
        #         for key in member:
        #             if key == 'password':
        #                 continue
        #             print(member.get(key))
        #
        #         message = "비밀번호 변경 [Y/n]: "
        #         check = input(message)
        #
        #         if check == 'Y':
        #             code = [chr(i + 65) for i in range(0, 26)] + [f'{i}' for i in range(0, 10)]
        #             certification_number = ""
        #
        #             for i in range(10):
        #                 certification_number += code[randint(0, len(code))]
        #
        #             send_email(member.get("email"), certification_number)
        #             message = f"{member.get('email')}로 인증코드를 전송했습니다.\n10자리 인증번호: "
        #             certification_number_input = input(message)
        #
        #             if certification_number_input == certification_number:
        #                 while True:
        #                     message = '새로운 비밀번호: '
        #                     new_password = input(message)
        #                     encryption = hashlib.sha256()
        #                     encryption.update(new_password.encode('utf-8'))
        #                     new_password = encryption.hexdigest()
        #
        #                     if not new_password == member.get("password"):
        #                         update_query = "update tbl_member set password = %s where %s"
        #                         update_params = new_password, member.get("password"),
        #                         update(update_query, update_params)
        #                         print('비밀번호가 변경되었습니다. 다른 비밀번호를 입력해주세요.')
        #                         break
        #
        #                     else:
        #                         print('기존 비밀번호와 동일합니다.')
        #
        #     else:
        #         print('비밀번호를 다시 확인해주세요.')
        #
        # else:
        #     print('이메일을 다시 확인해주세요.')

        # 사용자가 입력한 한국어를 영어로 번역
        # 한국어와 번역된 문장을 DBMS에 저장
        # 번역 내역 전체 조회
        # while True:
        #     message = '1. 번역\n2. 번역 내역 전체 조회\n3. 나가기\n'
        #     choice = input(message)
        #     if choice == '1':
        #         message = '한국어: '
        #         korean = input(message)
        #         english = papago(korean)
        #         print(f"{korean} -> {english}")
        #
        #         insert_query = "insert into tbl_translation(korean, english) values (%s, %s)"
        #         insert_params = korean, english
        #
        #         save(insert_query, insert_params)
        #         continue
        #
        #     elif choice == '2':
        #         find_all_query = "select * from tbl_translation"
        #         translation_all = find_all(find_all_query)
        #         for translation in translation_all:
        #             print(f"{translation.get('korean')} -> {translation.get('english')}")
        #
        #         break
        #
        #     elif choice == '3':
        #         print('안녕히 가세요.')
        #         break
        #
        #     else:
        #         print('다시 입력하세요.')
        #         continue

        # 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
        # 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
        # 경로와 추출한 텍스트 전체 조회
        message = '이미지 경로: '
        image_directory = input(message)
        content = ocr(image_directory)['ParsedResults'][0]['ParsedText']

        insert_query = "insert into tbl_ocr(image_directory, content) values (%s, %s)"
        insert_params = image_directory, content

        save(insert_query, insert_params)

        find_all_query = "select * from tbl_ocr"
        ocr_list = find_all(find_all_query)
        for ocr in ocr_list:
            print(f"{ocr.get('image_directory')},\n{ocr.get('content')}")