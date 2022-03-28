from typing import Optional


class Item:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price 

    def __getId(self):
        return self.id

    def __getName(self):
        return self.name

    def __getPrice(self):
        return self.price


class VendingMachine:
    def __init__(self):
        self.inventory = {
            'A': [],
            'B': [],
            'C': []
        }
        self.defaultInventoryLevel = 5
        self.changeAvailable = 100.00

    def printInventory(self):
        print(self.inventory)

    def printToCustomer(self):
        print('---- Please Select an Item ----\n')
        for key, val in self.inventory.items():
            for itemIdx in range(len(val)):
                itemDescription = val[itemIdx][0]
                itemPrice = val[itemIdx][2]
                print(f'-- Press {key}{itemIdx} for {itemDescription}: ${itemPrice}\n')

    def insertItem(self, item: Item, shelf: str):
        # Insert item with a defualt inventory level
        self.inventory[shelf].append([item, self.defaultInventoryLevel])
        self.printInventory()

    def __dispenseItem(self, shelfId: str, itemIdx: int) -> bool:
        item = self.inventory[shelfId][itemIdx]
        item[1] -= 1
        return True

    def __dispenseChange(self, amountPaid: float, itemPrice: float):
        """If enough change available, proceed. Else flag transaction."""
        change = amountPaid - itemPrice
        if self.changeAvailable >= change:
            print(f'Dispensing item with change of: {change:.2f}')
            self.changeAvailable - change
        else:
            # Some logging function or API call to notify for refill.
            print(
                """
                Insufficient change available in machine. 
                Please try another item.
                """)

    # Place Order Method
    def placeOrder(self, selection: str, amountPaid: float) -> Optional[float]:
        """Place order and return change due"""
        # Clean input
        if len(selection) != 2:
            print('Please enter two valid characters for selection.')
            return
        elif not selection[0].isalpha():
            print('Invalid input for first character.')
            return 
        elif not selection[1].isdigit():
            print('Invalid input for second character.')
            return
        selection = selection.upper()
        shelfId, itemIdx = selection[0], int(selection[1])
        # Access the selection
        item = self.inventory[shelfId][itemIdx]

        # Check for available inventory
        availableInventory = item[1]
        if availableInventory < 1:
            print('Out of Stock. Please select another item.')
            return

        # Check for correct payment
        itemPrice = item[0].price
        if amountPaid < itemPrice:
            print('Insufficient funds. Please try again.')
            return

        # Dispense item
        if self.__dispenseItem(shelfId, itemIdx):
            # Calculate change and return
            self.__dispenseChange(amountPaid, itemPrice)


if __name__ == '__main__':
    vm = VendingMachine()
    vm.printInventory()

    # Create items
    snickers = Item(1, 'Snickers', 2.00)
    reeses = Item(2, 'Reeses', 2.00)
    chips = Item(3, 'Chips', 3.00)
    protein = Item(4, 'Protein', 3.00)
    energy1 = Item(5, '5 Hour Energy', 4.00)
    energy2 = Item(6, 'Monster Energy', 4.00)

    vm.insertItem(snickers, 'A')
    vm.insertItem(reeses, 'A')
    vm.insertItem(chips, 'B')
    vm.insertItem(protein, 'B')
    vm.insertItem(energy1, 'C')
    vm.insertItem(energy2, 'C')

    vm.placeOrder('A1', 5.00)
