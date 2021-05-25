"""
    미스코리아 상위 3명을 가려 진선미를 선출한다.
"""
entry = [
    ("김사랑", 70, 75),
    ("이하늬", 60, 65),
    ("이지은", 80, 85),
    ("서윤희", 90, 95),
    ("김은정", 85, 95)]

sum = []

def make_sum(inner_entry, inner_sum) :
    """
        inner_entry {list} : 명단
        inner_sum {list} : 진, 선, 미를 가려 저장할 명단
    """
    if not inner_entry:
        print("entry list is empty")
    else:
        for i in range(0, 5) :
            inner_sum.append(entry[i][1] + entry[i][2])

        inner_sum.sort(reverse = True)

        print("진", list(filter(lambda x : x[1] + x[2] == inner_sum[0], entry)))
        print("선", list(filter(lambda x : x[1] + x[2] == inner_sum[1], entry)))
        print("미", list(filter(lambda x : x[1] + x[2] == inner_sum[2], entry)))

make_sum(entry, sum)
