# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = ['사과','딸기','배','키위','망고']
price_list = [1500, 1800, 2000, 3000, 4000]

title = "이용하실 서비스의 번호를 입력하세요.: \n"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격\n'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격\n'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."
result_message = ''

while True:
    service = int(input(title + menu))
    # 추가
    if service == 1:
        append_name, append_price = input(append_message).split()
        if append_name not in name_list:
            name_list.append(append_name)
            price_list.append(int(append_price))
            result_message = f'{append_name}을 {append_price}원으로 추가했습니다.'
        else:
            result_message = append_error_message
    # 수정
    elif service == 2:
        update_name = input(search_name_message_for_update)
        if update_name not in name_list:
            result_message = update_error_message
        else:
            name_index = name_list.index(update_name)
            name_list[name_index], price_list[name_index] = input(update_message).split()

    # 삭제
    elif service == 3:
        delete_name = input(delete_message)
        if delete_name not in name_list:
            result_message = delete_error_message
        else:
            del price_list[name_list.index(delete_name)]
            del name_list[name_list.index(delete_name)]
    # 검색
    elif service == 4:
        search_number = int(input(search_menu))
        if search_number == 1:
            search_name = input(search_name_message)
            if search_name in name_list:
                find_name = name_list[name_list.index(search_name)]
                find_price = price_list[name_list.index(search_name)]
                result_message = f'{find_name}, {find_price}원'
            else:
                result_message = search_name_error_message
        elif search_number == 2:
            search_price = int(input(search_price_message))
            min = search_price * 0.5
            max = search_price * 1.5
            for price in price_list:
                if min <= price <= max:
                    index = price_list.index(price)
                    result_message = f'{name_list.index(index)}, {price_list.index(index)}'
            else:
                result_message = search_error_message
        else:
            result_message = error_message
    # 목록
    elif service == 5:
        if len(name_list) == 0 and len(price_list) == 0:
            result_message = no_item_message
        else:
            for i in range(len(name_list)):
                result_message += f'{name_list[i]}, {price_list[i]}원\n'
    # 나가기
    elif service == 6:
        print('이용해 주셔서 감사합니다.')
        break
    else:
        result_message = error_message

    print(result_message)

    last_menu = int(input('1.메뉴보기 2.종료하기\n'))

    if last_menu == 2:
        print('이용해 주셔서 감사합니다.')
        break

# 강사님 코드
# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

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
        # 사용자에게 상품명과 가격을 동시에 입력받는다(구분점은 공백문자).
        new_name, new_price = input(append_message).split()
        # 입력한 상품명이 기존 상품과 중복되지 없다면,
        if new_name not in name_list:
            # 이름 list에 추가
            name_list.append(new_name)
            # 가격 list에 추가
            price_list.append(int(new_price))
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue
        else:
            # 입력한 상품명이 기존 상품과 중복되었다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = append_error_message

    # 수정
    elif choice == 2:
        # 사용자에게 수정하려는 상품명을 입력받는다.
        name = input(search_name_message_for_update)
        # 만약 이름 list안에 입력받은 이름이 있다면,
        if name in name_list:
            # 수정할 이름과 가격을 입력받는다.(구분점은 공백문자)
            new_name, new_price = input(update_message).split()
            # 만약 수정할 이름이 이름 list안의 값들과 중복되지 않다면,
            if new_name not in name_list:
                # 수정하고자 하는 상품명의 이름 list안에서 인텍스를 구한다.
                index = name_list.index(name)
                # 상품명과 가격이 인덱스를 공유하기 때문에 해당 해당 인덱스에 수정되는 이름과 가격을 저장한다.
                name_list[index], price_list[index] = new_name, new_price
                # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
                continue
            else:
                # 수정할 이름이 이름 list안의 값들과 중복된 다면,
                # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = update_error_message2
        else:
            # 이름 list안에 입력받은 이름이 없다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 삭제할 상품명을 입력받는다.
        name = input(delete_message)
        # 만약 입력받은 상품명이 이름list안에 있다면
        if name in name_list:
            # 입력받은 이름을 통해 해당 값의 인덱스를 구한다.
            index = name_list.index(name)
            # 인덱스를 통해 이름 list에서 삭제한다.
            del name_list[index]
            # 인덱스를 통해 가격 list에서 삭제한다.
            del price_list[index]
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 skip
            continue

        else:
            # 입력받은 상품명이 이름list안에 없다면,
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        # 사용자에게 검색 메뉴를 보여주고 선택한 번호를 choice에 저장
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            # 사용자가 입력한 상품명을 name에 저장
            name = input(search_name_message)
            # 만약 입력받은 상품명이 이름list에 있다면,
            if name in name_list:
                # 입력받은 상품명을 통해 인덱스를 구하고 index에 저장
                index = name_list.index(name)
                # 서식문자와 index를 사용하여 해당 상품명과 가격을 출력
                print(f'{name_list[index]}, {price_list[index]}')
                # 오류 메시지를 출력하지 않기 위해 즉시 다음 반복 실행
                continue

            else:
                # 입력받은 상품명이 이름list에 없다면,
                # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 사용자가 입력한 가격을 정수형으로 변환하여 price에 저장
            price = int(input(search_price_message))
            # 입력받은 가격으로 오차 최소 금액을 min에 저장
            min = price * 0.5
            # 입력받은 가격으로 오차 최대 금액을 max에 저장
            max = price * 1.5
            # [price for price in price_list if min <= price <= max]
            # 가격list안에서 오차 최소, 최대 금액사이에 포함되는 가격들로 list 생성
            # price_list.index(i) for i in
            # 생성된 list의 가격들을 통해 기존 가격list안의 인덱스를 찾고 해당 list값을 result_index에 저장
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]
            # 만약 result_index의 길이가 0이 아니라면,
            if len(result_index) != 0:
                # result_index list로 반복문을 실행
                for i in result_index:
                    # 각 인덱스에 해당하는 이름, 가격 list의 값들을 서식문자로 출력
                    print(f'{name_list[i]}, {price_list[i]}')
                    # 오류 메시지를 출력하지 않기 위해 즉시 다음 반복 실행
                    continue
            # result_index의 길이가 0이라면,
            else:
                # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = search_error_message
    # 목록
    elif choice == 5:
        # 만약 이름list의 길이가 0이라면,
        if len(name_list) == 0:
            # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = no_item_message
        # 이름 list의 길이가 0이 아니라면,
        else:
            # 이름 list의 길이만큼 range함수를 실행하여 list를 만들고 반복문 실행
            for i in range(len(name_list)):
                # 반복문의 변수 i를 통해 이름 list와 가격 list 전체를 출력
                print(f'{name_list[i]}, {price_list[i]}')
                # 오류 메시지를 출력하지 않기 위해 즉시 다음 반복 실행
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        # 알맞은 메세지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
        result_message = error_message
    # 위에서 일괄처리하여 보냈던 메시지 출력
    print(result_message)
    # while문으로 반복되기 전 result_message 초기화
    result_message = ""

