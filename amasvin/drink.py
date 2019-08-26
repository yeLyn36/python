class Drink :
  _cups = ["레귤러", "점보"]
  _ice = ["0%", "50%", "100%", "150%"] 
  _sugar = ["0%", "50%", "100%", "150%"]

  def __init__ (self, name, price) :
    self.name = name
    self.price = price
    self.cup = 0 # 0 레귤러 1 점보
    self.ice = 2 # 0 0% 1 50% 2 100% 3 150%
    self.sugar = 2 # 0 0% 1 50% 2 100% 3 150%

  def set_cup (self) :
    self.cup = input("컵사이즈를 선택하세요 (0:레귤러 1:점보) : ")
    if self.cup == "":
      self.cup = 0
    else :
      self.cup = int(self.cup)
      if self.cup == 1 :
        self.price += 500

  def set_ice (self) :
    self.ice = input("얼음 양을 선택하세요 (0:0% 1:50% 2:100% 3:150%) : ")
    if self.ice == "":
      self.ice = 2
    else :
      self.ice = int(self.ice)
  
  def set_sugar (self) :
    self.sugar = input("당도를 선택하세요 (0:0% 1:50% 2:100% 3:150%) : ")
    if self.sugar == "":
      self.sugar = 2
    else :
      self.sugar = int(self.sugar)

  def __str__ (self) : 
    return "주문내역 : 제품명 " + self.name + ", 가격 " + str(self.price) + ", 컵사이즈 " + Drink._cups[self.cup] + ", 얼음량 " + Drink._ice[self.ice] + ",당도 " + Drink._sugar[self.sugar]

  def order(self) :
    self.set_cup()
    self.set_ice()
    self.set_sugar()
