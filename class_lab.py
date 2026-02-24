class Category:

    def __init__(self,name):
        self.name=name
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
            })

    def withdraw(self,amount,description=""):
        if self.get_balance()>=amount:
            self.ledger.append({
            'amount':-amount,
            'description': description
            })
            return True
        return False

    def get_balance(self):
        total=0
        for items in self.ledger:
            total+=items['amount']
        return total

    def transfer(self,amount,other_category):
        if self.withdraw(amount,f"Transfer to {other_category.name}"):
            other_category.deposit(amount,f"Transfer from {self.name}")
            return True 
        return False

    def check_funds(self,amount):
        return self.get_balance()>=amount
            

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23].ljust(23)
            amt = f"{entry['amount']:.2f}"[:7].rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
        
def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate spending per category
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += abs(item["amount"])
        spent.append(total)

    total_spent = sum(spent)

    percentages = [(int((s / total_spent) * 100) // 10) * 10 for s in spent]

    # Bars
    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"   # ← THIS SPACE IS CRITICAL

    # Horizontal line (must match bar width)
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names (vertical)
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")
