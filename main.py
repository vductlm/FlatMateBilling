from dataclasses import dataclass
from fpdf import FPDF

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
    fpdf = FPDF()
    total_mates = len(mates)
    total_day = sum(m.days for m in mates)

    fpdf.set_font('Times','B', 24)
    fpdf.add_page()
    fpdf.cell(w=0, align='C', ln=1, txt='Bill Sharing')
    fpdf.cell(w=100, h = 40, txt='Total: ', align='C')
    fpdf.cell(w=100, h=40, txt=str(bill.amount), align='L', ln=1)

    print(f"Total: {total_mates} with {total_day} days in total: {bill.amount}")

    for mate in mates:
        print(f"{mate.name} in {mate.days} days: {mate.pay(bill, total_mates, total_day)}")
        fpdf.cell(w=100, h=40, txt=mate.name, align='C')
        fpdf.cell(w=50, h=40, txt=str(mate.days), align='L')
        fpdf.cell(w=100, h=40, txt=str(mate.pay(bill, total_mates, total_day)), align='L', ln=1)
    fpdf.output('bill.pdf')


def main():
    total_bill = BillSharing(
        "Aprils, 2026",
        200.0
    )
    mates = [FlatMate('John', 20), FlatMate('Jenny', 30)]
    print_summary(total_bill, mates)

if __name__ == '__main__':
    main()