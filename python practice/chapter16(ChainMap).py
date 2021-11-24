from collections import ChainMap

class Shop:

    total = 0
    menu_list = [{'떡볶이':3000}, {'순대':3000}, {'튀김':500}, {'김밥':2000}]

    @classmethod
    def sales(cls, menu, cnt):
        dic = ChainMap(*cls.menu_list)
        total = dic[menu] * cnt
        cls.total += total

Shop.sales('떡볶이', 1)
Shop.sales('튀김', 5)
Shop.sales('김밥', 2)

print(f'매출 : {Shop.total}원')
