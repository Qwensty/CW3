from utils import get_data, get_sorted_data, get_last_values, get_formatted_data


def main():
    """
    Основная функция которая выводит на экран список из 5 последний выполненных клиентом операций

    :return: <дата перевода> <описание перевода>
             <откуда> -> <куда>
             <сумма перевода> <валюта>
    """
    LINK_DATA = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230206T155109Z&X-Amz-Expires=86400&X-Amz-Signature=a59d8cc04376bfcf88a8dc9a53d50e82331944c725365cc8fec75643de451ae9&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"
    MISSING_SENDER = True
    COUNT_LAST_VALUES = 5

    data, info = get_data(LINK_DATA)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_sorted_data(data, missing_sander=MISSING_SENDER)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for row in data:
        print(row, end='\n\n')

if __name__ == "__main__":
    main()
