from s_mysql.study.my_product_module import *

if __name__ == '__main__':
    # 상품 추가
    insert_query = "insert into tbl_product(name, price, created_date) \
                    values(%s, %s, %s)"

    insert_params = ['사과', '1500', '2024-01-17T18:20:00']
    # save(insert_query, insert_params)

    # 전체 상품 조회
    # find_all_query = "select id, name, price, created_date from tbl_product"
    # products = find_all(find_all_query)
    # print(products)
    # for product in products:
    #     print(f'상품명: {product["name"]}')

    # 상품 정보 중 가격이 3000원 이상인 상품은 10% 할인해준다.
    # discount = 10
    # find_all_query = "select id, price from tbl_product where price >= 3000"
    # products = find_all(find_all_query)
    # print(products)
    #
    # update_query = f"update tbl_product \
    #                     set price = %s * (1 - {discount} * 0.01) \
    #                     where id = %s"
    #
    # for product in products:
    #     update_params = [product.get('price'), product.get('id')]
    # print(update_params)
    # update(update_query, update_params)

    # find_all_query = "select id, name, price, created_date from tbl_product"
    # products = find_all(find_all_query)
    # print(products)

    # 평균 가격보다 높은 상품은 모두 삭제한다.
    # find_avg_query = "select round(avg(price)) average from tbl_product"
    # print(find_all(find_avg_query)[0].get('average'))
    # print(find_all(find_avg_query))

    # average = find_all(find_avg_query)[0].get('average')
    # delete_params = [average]
    # print(delete_params)
    delete_query = "delete from tbl_product where price > (select avg(price) from tbl_product)"
    delete(delete_query, None)

    # find_all_query = "select id, name, price, created_date from tbl_product"
    # products = find_all(find_all_query)
    # print(products)