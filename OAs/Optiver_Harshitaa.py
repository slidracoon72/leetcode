class OrderState:
    def __init__(self):
        self.number_of_stores = 0
        self.number_of_orders = 0
        self.number_of_different_beverages = 0
        self.number_of_beverages = 0
        self.numberOfStores_limit = 0
        self.perBeverageTotal_limit = 0
        self.store_orders = {}

    def UpdateLimit(self, numberOfStores: int, perBeverageTotal: int) -> None:
        self.numberOfStores_limit = numberOfStores
        self.perBeverageTotal_limit = perBeverageTotal

        # Check if limits are violated after updating
        if (self.number_of_stores > numberOfStores or
                any(beverage_total > perBeverageTotal for beverage_total in self.get_beverage_totals().values())):
            self.close_all_stores()

    def ProcessOrder(self, uniqueId: int, storeId: int, beverageName: str, quantity: int) -> None:
        # Reject order if quantity exceeds per-beverage total limit
        if quantity > self.perBeverageTotal_limit:
            print(f"reject_order: {uniqueId}")
            return

        # Calculate total for the specified beverage
        current_beverage_total = self.get_beverage_totals().get(beverageName, 0)
        if current_beverage_total + quantity > self.perBeverageTotal_limit:
            print(f"reject_order: {uniqueId}")
            return

        # Add new store if it doesn't exist and check store limit
        if storeId not in self.store_orders:
            if self.number_of_stores >= self.numberOfStores_limit:
                print(f"reject_order: {uniqueId}")
                return
            self.store_orders[storeId] = {}
            self.number_of_stores += 1

        # Update beverage quantity in store
        if beverageName in self.store_orders[storeId]:
            self.number_of_beverages -= self.store_orders[storeId][beverageName]
            self.number_of_orders -= 1

        self.store_orders[storeId][beverageName] = quantity
        self.number_of_beverages += quantity
        self.number_of_orders += 1

        # Update count of different beverages
        self.update_beverage_count()

        # Close store if it has no orders
        if not any(self.store_orders[storeId].values()):
            self.CloseStore(storeId)

    def CloseStore(self, storeId: int) -> None:
        if storeId in self.store_orders:
            self.number_of_beverages -= sum(self.store_orders[storeId].values())
            self.number_of_orders -= len(self.store_orders[storeId])
            del self.store_orders[storeId]
            self.number_of_stores -= 1
            self.update_beverage_count()

    def PrintState(self) -> None:
        print(f"number_of_stores: {self.number_of_stores}, number_of_orders: {self.number_of_orders}, "
              f"number_of_different_beverages: {self.number_of_different_beverages}, number_of_beverages: {self.number_of_beverages}")

    def get_beverage_totals(self) -> dict:
        beverage_totals = {}
        for orders in self.store_orders.values():
            for beverage, qty in orders.items():
                beverage_totals[beverage] = beverage_totals.get(beverage, 0) + qty
        return beverage_totals

    def update_beverage_count(self):
        all_beverages = {beverage for orders in self.store_orders.values() for beverage in orders}
        self.number_of_different_beverages = len(all_beverages)

    def close_all_stores(self):
        self.store_orders.clear()
        self.number_of_stores = 0
        self.number_of_orders = 0
        self.number_of_beverages = 0
        self.number_of_different_beverages = 0


# Create an instance of OrderState
order_state = OrderState()

# Test Case 1: Set the limit and process some orders within the limit
print("Test Case 1")
order_state.UpdateLimit(100, 1000)  # Set limit for stores and per beverage total
order_state.ProcessOrder(1, 1, "lemonade", 100)  # Store 1 orders 100 lemonade
order_state.ProcessOrder(2, 2, "hot_chocolate", 50)  # Store 2 orders 50 hot chocolate
order_state.PrintState()
# Expected output:
# number_of_stores: 2, number_of_orders: 2, number_of_different_beverages: 2, number_of_beverages: 150

# Test Case 2: Add more orders, and update an existing order
print("\nTest Case 2")
order_state.ProcessOrder(3, 3, "lemonade", 75)  # Store 3 orders 75 lemonade
order_state.ProcessOrder(4, 1, "lemonade", 150)  # Update Store 1's lemonade order to 150
order_state.ProcessOrder(5, 1, "water", 50)  # Store 1 orders 50 water
order_state.PrintState()
# Expected output:
# number_of_stores: 3, number_of_orders: 4, number_of_different_beverages: 3, number_of_beverages: 325

# Test Case 3: Exceeding per beverage total limit
print("\nTest Case 3")
order_state.ProcessOrder(6, 2, "lemonade", 900)  # Store 2 tries to order 900 lemonade (should be rejected)
# Expected output:
# reject_order: 6
order_state.PrintState()
# Expected output (unchanged from previous state):
# number_of_stores: 3, number_of_orders: 4, number_of_different_beverages: 3, number_of_beverages: 325

# Test Case 4: Exceeding store limit
print("\nTest Case 4")
order_state.UpdateLimit(2, 1000)  # Lower store limit to 2 (should reset all stores if exceeded)
# Expected output:
# number_of_stores: 0, number_of_orders: 0, number_of_different_beverages: 0, number_of_beverages: 0
order_state.PrintState()

# Test Case 5: Closing a specific store
print("\nTest Case 5")
order_state.UpdateLimit(100, 1000)  # Increase limits to allow more orders
order_state.ProcessOrder(7, 1, "lemonade", 100)  # Store 1 orders 100 lemonade
order_state.ProcessOrder(8, 2, "iced_tea", 150)  # Store 2 orders 150 iced tea
order_state.CloseStore(1)  # Close Store 1
order_state.PrintState()
# Expected output:
# number_of_stores: 1, number_of_orders: 1, number_of_different_beverages: 1, number_of_beverages: 150

# Test Case 6: Edge case - Zero quantity order
print("\nTest Case 6")
order_state.ProcessOrder(9, 2, "iced_tea", 0)  # Store 2 sets iced tea order to 0 (should remove it)
order_state.PrintState()
# Expected output:
# number_of_stores: 0, number_of_orders: 0, number_of_different_beverages: 0, number_of_beverages: 0
