# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 입력받고 split으로 구분하여 new_name과 new_price에 저장.
        new_name, new_price = input(append_message).split()
        # 만약 data_dict에 new_name과 같은 key값이 없다면,
        if new_name not in data_dict:
            # data_dict에 new_name을 키 값으로, new_price를 정수로 변하여 value 값으로 추가
            data_dict[new_name] = int(new_price)
            # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
            continue
        # data_dict에 new_name과 같은 key값이 있다면
        else:
            # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 입력받은 수정할 상품명을 name에 저장
        name = input(search_name_message_for_update)
        # 만약 data_dict에 name이 있다면,
        if name in data_dict:
            # 입력받은 새로운 상품명과 가격을 split으로 구분하여 new_name과 new_price에 저장
            new_name, new_price = input(update_message).split()
            # data_dict에 new_name이 없다면,
            if new_name not in data_dict:
                # 기존 상품명으로 data_dict에서 삭제한다.
                del data_dict[name]
                # 새로운 상품명을 key 값으로, 새로운 가격을 value 값으로 추가한다.
                data_dict[new_name] = int(new_price)
                # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
                continue
            # data_dict에 new_name이 있다면,
            else:
                # data_dict[new_name]의 value를 new_price로 수정
                data_dict[new_name] = int(new_price)
        # data_dict에 name이 없다면,
        else:
            # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 입력받은 삭제할 상품명을 name에 저장
        name = input(delete_message)
        # 만약 data_dict에 name이 있다면,
        if name in data_dict:
            # name을 키 값으로 삭제
            del data_dict[name]
            # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
            continue
        # data_dict에 name이 없다면,
        else:
            # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 입력받은 번호를 정수형으로 형변환해서 choice에 저장
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 입력받은 상품명을 keyword에 저장
            keyword = input(search_name_message)
            # 만약 data_dict에 keyword가 있다면,
            if keyword in data_dict:
                # data_dict의 items메소드를 사용하여 나오는 key와 value를 각각 name과 price에 저장하고 반복
                for name, price in data_dict.items():
                    # 만약 keyword와 name이 같다면,
                    if keyword == name:
                        # name과 price를 서식문자로 출력
                        print(f'{name}, {price}')
                # 오류 메시지를 출력하지 않기 위해 다음 반복을 즉시 실행
                continue
            # data_dict에 keyword가 없다면,
            else:
                # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 검색 결과에 따른 반복 진행 및 오류 메시지 출력 유무를 구분하기 위해 선언
            check = False
            # 입력받은 가격을 정수형으로 형변화해서 price_input에 저장
            price_input = int(input(search_price_message))
            #
            min = price_input * 0.5
            #
            max = price_input * 1.5
            #
            for name, price in data_dict.items():
                if min <= price <= max:
                    check = True
                    print(f'{name}, {price}')

            if check:
                continue

            if not check:
                result_message = search_error_message

    # 목록
    elif choice == 5:
        if len(data_dict) == 0:
            result_message = no_item_message
        else:
            for name, price in data_dict.items():
                print(f'{name}, {price}')
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        result_message = error_message

    print(result_message)
    result_message = ""
