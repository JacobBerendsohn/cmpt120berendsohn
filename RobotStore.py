# RobotStore.py
# Jacob Berendsohn


class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self, count):
        if(self.quantity - count >= 0):
            return True
        else:
            return False

    def finalPrice(self, count):
        endPrice = self.price * count
        return endPrice

    def setStock(self, numBought):
        self.quantity = self.quantity - numBought


productList = [Product("Ultrasonic range finder", 2.50, 4), Product("Servo motor", 14.99, 10),
               Product("Servo controller", 44.95, 5), Product("Microcontroller Board", 34.95, 7),
               Product("Laser range finder", 149.99, 2), Product("Lithium polymer battery", 8.99, 8)]


def printStock():
    i = 1
    print()
    print("Available Products")
    print("------------------")
    for product in productList:
        if product.inStock(1) is True:
            print(str(i)+")", product.name, "$", product.price)
            i = i+1
        else:
            print(str(i)+")", "Sold Out")
            i = i + 1
    print()
    i = 1


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        vals[0] = (int(vals[0]) - 1)

        if vals[0] == "quit":
            break

        prodId = int(vals[0])
        count = int(vals[1])

        if productList[prodId].inStock(count) is True:
            if cash >= productList[prodId].price:
                productList[prodId].setStock(count)
                cash -= productList[prodId].finalPrice(count)
                print("You purchased", count, productList[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productList[prodId].name)

        print("There are", productList[prodId].quantity, productList[prodId].name, "left.")
main()