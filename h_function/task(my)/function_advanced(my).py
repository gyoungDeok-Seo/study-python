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


# 추가
def insert(**kwargs):
    """
    새로운 상품을 추가하는 메소드
    :param kwargs: {'name': 상품명, 'price': 가격}
    """
    # 전달받은 name과 price의 value값을 이용해 딕셔너리에 추가
    # price는 input함수로 입력받은 값으로 str타입에서 int함수로 형변환
    data_dict[kwargs['name']] = int(kwargs['price'])


# 수정
def update(**kwargs):
    """
    전달 받은 기존 이름을 딕셔너리에서 삭제하고 새로운 이름과 가격으로 추가
    :param kwargs: {'name': 기존 이름, 'new_name': 새로운 이름, 'new_price': 새로운 가격}
    """
    # 전달받은 name의 value 값으로 딕셔너리에서 삭제
    del data_dict[kwargs['name']]
    # 전달받은 new_name과 new_price로 딕셔너리에 추가
    # new_price는 input함수로 입력받은 값이기 때문에 int함수로 형변환
    data_dict[kwargs['new_name']] = int(kwargs['new_price'])


# 상품명으로 검색
def select_by_name(keyword):
    """
    전달받은 keyword가 data_dict에 있는지 검사하고 있다면 key값과 value값을 딕셔너리로 return하는 함수
    :param keyword: 상품명
    :return: 검색결과(dict)
    """
    # 리턴값을 담기 위해 선언
    result = {}
    # 만약 전달 받은 keyword가 data_dict에 있다면,
    if keyword in data_dict:
        # keyword와 data_dict[keyword]를 value 값으로 하는 딕셔너리를 만들어 result에 저장
        result = {'name': keyword, 'price': data_dict[keyword]}

    # 만약 위 조건식에 해당하지 않는다면, 비어있는 상태로 return하고
    # 위 조건식에 해당한다면, 위에서 저장된 값이 return 된다.
    return result


# 가격으로 검색
def select_by_price(price, range=50):
    """
    전달받은 가격과 오차율을 기준으로 해당되는 모든 상품과 가격을 딕셔너리 형식으로 list에 담아 return하는 함수
    :param price: 검색 가격
    :param range: 오차 범위(default=50)
    :return: 오차 범위에 해당되는 상품들의 이름과 가격(dict형식의 값들을 담은 list)
    """
    # 여러개의 상품들이 검색될 경우 담아서 보내기 위해 선언
    result = []
    # 오차 범위의 최소값을 검색 가격과 오차율로 계산하여 min에 저장
    min = price * range * 0.01
    # 오차 범위의 최대값을 검색 가격과 오차율로 계산하여 max에 저장
    max = price * (range * 0.01 + 1)
    # data_dict에 있는 모든 값들을 key 값은 name, value 값은 price에 저장하고 반복을 진행한다
    for name, price in data_dict.items():
        # 만약 검색 가격이 오차 최소 범위 보다 크거나 같으면서 최대 범위 보다 작거나 같다면,
        if min <= price <= max:
            # 위에 선언한 result에 {'name': name, 'price': price} 형식으로 추가
            result.append({'name': name, 'price': price})
    # 만약 한번이라도 위에 해당되지 않는다면 초기값 빈 list가,
    # 한번이라도 위에 해당 한다면 dict형식의 값이 추가된 list가 return된다.
    return result


# 목록
def select_all():
    """
    모든 data_dict의 값들을 return 한다.
    :return: data_dict
    """
    return data_dict

# 삭제
def delete(name):
    """
    전달 받은 상품명을 data_dict에서 삭제한다.
    :param name: 삭제할 상품명
    """
    # data_dict에서 name을 key 값으로 사용하는 value를 삭제한다.
    del data_dict[name]

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        # 사용자에게 상품명과 가격을 입력받고 split으로 구분하여 new_name과 new_price에 저장.
        new_name, new_price = input(append_message).split()
        # 만약 data_dict에 new_name과 같은 key값이 없다면,
        if new_name not in data_dict:
            # inser함수를 사용(함수 용도는 함수내 여러줄 주석 내용 참조)
            insert(name=new_name, price=new_price)
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
        # 만약 select_by_name(name)함수 resturn 값의 length가 0이 아니라면(검색 결과가 있다면),
        if len(select_by_name(name)) != 0:
            # 입력받은 새로운 상품명과 가격을 split으로 구분하여 new_name과 new_price에 저장
            new_name, new_price = input(update_message).split()
            # select_by_name(new_name)함수 resturn 값의 length가 0이라면(검색 결과가 없다면),
            if len(select_by_name(new_name)) == 0: # 이름 가격 둘다 수정
                # update함수를 사용(함수 용도는 함수내 여러줄 주석 내용 참조)
                update(name=name, new_name=new_name, new_price=new_price)
                # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
                continue
                # select_by_name(new_name)함수 resturn 값의 length가 0이 아니라면(검색 결과가 있다면),
            else: # 가격만 수정
                # data_dict에 'new_name'을 key 값으로 갖고있는 value 값을 수정
                data_dict[new_name] = int(new_price)
                # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
                continue
        # 만약 select_by_name(name)함수 resturn 값의 length가 0라면(검색 결과가 없다면),
        else:
            # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        # 입력받은 삭제할 상품명을 name에 저장
        name = input(delete_message)
        # 만약 data_dict에 name이 있다면,
        if name in data_dict:
            # delete(name)함수 사용(함수 용도는 함수내 여러줄 주석 내용 참조)
            delete(name)
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
            # elect_by_name(keyword)함수 사용(함수 용도는 함수내 여러줄 주석 내용 참조)하여 return 값을 product에 저장
            product = select_by_name(keyword)
            # product length가 0이 아니라면(검색 결과가 있다면),
            if len(product) != 0:
                # key값으로 각 value값을 가져오고 서식문자를 사용하여 출력
                print(f"{product['name']}, {product['price']}")
                # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
                continue
                # product length가 0이라면(검색 결과가 없다면),
            else:
                # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            # 입력받은 가격을 정수형으로 형변화해서 price에 저장
            price = int(input(search_price_message))
            # select_by_price(price)함수 사용(함수 용도는 함수내 여러줄 주석 내용 참조)하여 return 값을 result에 저장
            result = select_by_price(price)
            # result의 length가 0이 아니라면(검색 결과가 있다면)
            if len(result) != 0:
                # result를 반복하여 값들을 출력
                for product in result:
                    print(f"{product['name']}, {product['price']}")
            # result의 length가 0라면(검색 결과가 없다면)
            else:
                # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
                result_message = search_error_message

    # 목록
    elif choice == 5:
        # select_all()함수 return 값의 length가 0이라면(검색 결과가 없다면)
        if len(select_all()) == 0:
            # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
            result_message = no_item_message
        # select_all()함수 return 값의 length가 0이 아니면(검색 결과가 있다면)
        else:
            # data_dict의 Key, value를 분리하여 name, price에 각각 저장하고 반복 진행
            for name, price in data_dict.items():
                # 서식 문자를 사용하여 name, price출력
                print(f'{name}, {price}')
                # 오류 메시지를 출력하지 않기 위해 다음 반복 즉시 실행
                continue

    # 나가기
    elif choice == 6:
        # 반복 종료
        break

    # 그 외
    else:
        # 알맞은 메시지를 result_message에 담아서 소스코드 하단의 일괄처리로 보내기
        result_message = error_message
    # 일괄처리된 메시지를 출력
    print(result_message)
    # 다음 반복 시 잘못된 오류메시지가 담겨져 출력되는것을 막기 위해 초기화
    result_message = ""
