from expense import init_db, add_expense, get_all_expenses, delete_expense
from utils import format_currency

def main():
    init_db()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Shto shpenzim")
        print("2. Shiko të gjitha")
        print("3. Fshij shpenzim")
        print("4. Dil")

        choice = input("Zgjedhja: ")

        if choice == "1":
            desc = input("Përshkrimi: ")
            amount = float(input("Shuma: "))
            add_expense(desc, amount)
            print("✅ Shpenzimi u shtua me sukses.")
        elif choice == "2":
            expenses = get_all_expenses()
            for e in expenses:
                print(f"[{e[0]}] {e[1]} - {format_currency(e[2])} - {e[3]}")
        elif choice == "3":
            exp_id = int(input("ID për fshirje: "))
            delete_expense(exp_id)
            print("🗑️  U fshi me sukses.")
        elif choice == "4":
            break
        else:
            print("Zgjedhje e pavlefshme!")

if __name__ == "__main__":
    main()