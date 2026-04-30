"""
Flatmate billing: split a bill proportionally by days stayed.
"""
from dataclasses import dataclass, field


@dataclass
class Bill:
    name: str
    amount: float


@dataclass
class FlatMate:
    name: str
    days: int

    def share(self, bill: Bill, mates: list["FlatMate"]) -> float:
        """Pay proportional to days stayed vs total occupancy days."""
        total_days = sum(m.days for m in mates)
        return bill.amount * (self.days / total_days)


def print_summary(bill: Bill, mates: list[FlatMate]) -> None:
    print(f"Bill: {bill.name} — Total: £{bill.amount:.2f}\n")
    for mate in mates:
        print(f"  {mate.name} ({mate.days} days): £{mate.share(bill, mates):.2f}")


def main() -> None:
    bill = Bill("April 2026", 200)
    mates = [FlatMate("John", 30), FlatMate("Jenny", 20)]
    print_summary(bill, mates)


if __name__ == "__main__":
    main()
