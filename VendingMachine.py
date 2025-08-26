items_data = [
   {
      "itemId": 0,
      "itemName": "Aquarius",
      'itemPrice': 120,
   },{
      "itemId": 1,
      "itemName": "Water",
      'itemPrice': 30,
   },{
      "itemId": 2,
      "itemName": "Coca-Cola",
      'itemPrice': 50,
   },{
      "itemId": 3,
      "itemName": "Fanta Orange",
      'itemPrice': 200,
   },{
      "itemId": 4,
      "itemName": "Fanta Lemon",
      'itemPrice': 300,
   },{
      "itemId": 5,
      "itemName": "Sprite",
      'itemPrice': 300,
   },{
      "itemId": 6,
      "itemName": "Nestea",
      'itemPrice': 300,
   },
]
item = []
reciept = """
\t\tPRODUCT NAME -- COST
"""
sum = 0
run = True

print("------- Vending Machine Program with Python-------\n\n")
print("----------The Items In Stock Are----------\n\n")


for i in items_data:
   print(
      f"Item: {i['itemName']} --- Price: {i['itemPrice']} --- Item ID: {i['itemId']}")


def vendingMachine(items_data, run, item):
   while run:
      buyItem = int(
         input("\n\nEnter the item ID for the item you want to buy: "))
      if buyItem < len(items_data):
         item.append(items_data[buyItem])
      else:
         print("THE PRODUCT ID IS WRONG!")
      moreItems = str(
         input("type any key to add more things, and type q to stop:  "))
      if moreItems == "q":
         run = False
   receiptValue = int(
      input(("1. Print the bill? 2. Only print the total sum: ")))
   if receiptValue == 1:
      print(createReceipt(item, reciept))
   elif receiptValue == 2:
      print(sumItem(item))
   else:
      print("INVALID")


def sumItem(item):
   sumItems = 0
   for i in item:
      sumItems += i["itemPrice"]
   return sumItems


def createReceipt(item, reciept):
   for i in item:
      reciept += f"""
      \t{i["itemName"]} -- {i['itemPrice']}
      """
   reciept += f"""
      \tTotal --- {sumItem(item)}
      """
   return reciept


# Main Code
vendingMachine(items_data, run, item)