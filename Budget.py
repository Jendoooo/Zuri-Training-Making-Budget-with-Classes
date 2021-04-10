class Budget:
    def __init__(self, name):
        self.name = name
        self.transaction_records = []

    def withdraw(self, ammount, description=""):
        self.transaction_records.append({"ammount": -ammount,
                                         "description": description})

    def deposit(self, ammount, description=""):
        self.transaction_records.append({"ammount": ammount,
                                         "description": description})

    def balance(self):
        total = 0
        # looping through the list
        for item in self.transaction_records:
            total += item["ammount"]
        return total

    def transfer(self, ammount, destination):
        self.withdraw(ammount, f"Transfer to {destination.name}")
        destination.deposit(ammount, f"Transfer from {self.name}")

    def __str__(self):
        font = self.name.center(80, "*") + "\n"

        for item in self.transaction_records:
            font += f"{item['description'][:40].ljust(40)}{format(item['ammount'], '.2f').rjust(40)}\n"
        font += f"Domiciliary Balance:{format(self.balance(), '.2f')}"
        return font


if __name__ == "__main__":
    food = Budget("Food Budget ")
    food.deposit(10000, "Corruption ")
    food.withdraw(500, "Money for chow")
    food.withdraw(1000, "GRE ")
    food.withdraw(1000, "Money for School")
    food.balance()
    gaming = Budget("Gaming")
    Health = Budget("Health")

    food.transfer(5000, gaming)
    gaming.transfer(2000, Health)
    gaming.withdraw(500, "PS5 Purchase")
    Health.withdraw(1000, "Health Insurance")
    print(food)
    print(gaming)
    print(Health)
