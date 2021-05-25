entry =[
    ("김사랑",70,75),
    ("이하늬",60,65),  
    ("이지은",80,85),
    ("서윤희",90,95),
    ("김은정",85,95)]  
sum = []
def makeSum(entry, # ignore_01 : 괄호 안의 인수는 세로로 정렬되지 않거나 내어 쓰기를 사용하지 않아야 한다
  sum) :
    if not entry:
      print("entry list is empty")
        for i in range(0,5) :
            sum.append(entry[i][1]+entry[i][2])
        sum.sort(reverse=True) # ignore_02 : 연산자 앞뒤 공백이 있어야 한다
        
        print ("진",list(filter(lambda x:x[1]+x[2]==sum[0],entry)))
				# ignore_03 : print문에서 print와 괄호 사이의 공백은 없어야 한다
        print ("선",list(filter(lambda x:x[1]+x[2]==sum[1],entry)))
        print ("미",list(filter(lambda x:x[1]+x[2]==sum[ 2 ],entry)))
				# ignore_04 : 대괄호([]) 안의 공백은 없어야 한다

makeSum(entry,sum)