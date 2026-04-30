from dataclasses import dataclass

@dataclass
class BillSharing:
    name: str
    amount: float


@dataclass
class FlatMate:
    name: str
    days: int

    def pay(self, bill: BillSharing, mate:int, total_day: int)-> float:
        return (bill.amount / mate / total_day) * self.days

def print_summary(bill: BillSharing, mates: list[FlatMate]):
    total_mates = len(mates)
    total_day = sum(m.days for m in mates)
    print(f"Total: {total_mates} with {total_day} days in total: {bill.amount}")
    for mate in mates:
        print(f"{mate.name} in {mate.days} days: {mate.pay(bill, total_mates, total_day)}")

def main():
    total_bill = BillSharing(
        "Aprils, 2026",
        200.0
    )
    mates = [FlatMate('John', 20), FlatMate('Jenny', 30)]
    print_summary(total_bill, mates)

if __name__ == '__main__':
    main()