from order import Order
from file_manager import filemanager

file_manager = filemanager("history.bin")
history = []
try:
    history = file_manager.load()
    if history != None:
        for d in history:
            print(d)
            sum += d.price
        print("아마스빈에서 내가 쓴 돈은 " + str(sum) + "원입니다.")
except FileNotFoundError:
    print("저장 내역이 존재하지 않습니다.")
print("-"*80)


#저장 내역 출력

o = Order()
o.order_drink()

file_manager.save(o.order_menu)