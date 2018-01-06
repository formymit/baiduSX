#-*-coding:utf-8-*-
with open('iname_cardNum_search_cardNum.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    print(len(lines))

    new_lines = set(lines)
    print(len(new_lines))

