# Expense-Tracker
SmartExpense Tracker është një aplikacion i thjeshtë Python për menaxhimin e shpenzimeve personale, i ndërtuar me metodologjinë TDD (Red/Green/Refactor). Ai lejon shtimin, shfaqjen dhe fshirjen e shpenzimeve, ndërsa të dhënat ruhen në një bazë lokale SQLite. Projekti ndihmon në zhvillimin e aftësive për Python modular, testim me pytest, dhe menaxhim të bazës së të dhënave.

Funksionalitetet kryesore:
•	Shto shpenzim (emër + shumë)
•	Shiko të gjitha shpenzimet
•	Fshi shpenzim sipas ID-së
•	Ruajtje e qëndrueshme në SQLite
•	Testim i kodit për siguri dhe qëndrueshmëri
User Stories: përdoruesi mund të shtojë, shikojë dhe fshijë shpenzime, ndërsa zhvilluesi sigurohet që funksionet të jenë të mbuluara me teste.

Tech Stack:
•	Python 3 – logjika e aplikacionit
•	SQLite3 – ruajtje lokale e dhënash
•	Pytest – testim automatike (TDD)
•	OS & File System – menaxhim i folderave dhe skedarëve

Struktura modulare:
Expense-Tracker/
├── main.py            # File kryesor për ndërfaqen e përdoruesit
├── expenses.py        # Menaxhimi i shpenzimeve dhe lidhja me SQLite
├── utils.py           # Funksione ndihmëse për formatim dhe validim
├── data/
│   └── expenses.db    # Baza e të dhënave SQLite
├── tests/
│   ├── test_utils.py      # Testet për funksionet ndihmëse
│   └── test_expenses.py   # Testet për funksionet e shpenzimeve
├── README.md          # Përshkrimi dhe udhëzimet e projektit
└── .github/
    └── workflows/ └── tests.yml  # Workflow për CI (GitHub Actions) – testet automatike

Raport Javor – TDD
Projekti: Expense Tracker | Java: 2 | Data: 12.11.2025
Këtë javë u krijuan testet fillestare sipas TDD (shtim, fshirje, formatim shpenzimesh), të cilat aktualisht deshtojnë (Red). U organizuan testet me komente dhe emra funksionesh më të qartë. Javën tjetër do të implementohen funksionet kryesore për të kaluar testet dhe do të fillojë interface-i vizual.

Raport Javor – TDD
Projekti: Expense Tracker | Java: 3 | Data: 21.11.2025
Këtë javë u implementuan funksionet kryesore të Expense Tracker në utils.py, expenses.py dhe main.py, duke kaluar shumicën e testeve ekzistuese (Red → Green). U përmirësuan emrat e funksioneve dhe organizimi i kodit për të qenë më i qartë dhe i mirëmbajtshëm. Javën tjetër planifikohet plotësimi i funksioneve të munguar dhe sigurimi që të gjitha testet të kalojnë me sukses.

Raport Javor – TDD
Projekti: Expense Tracker | Java: 4 | Data: 24.11.2025
Këtë javë u shtua konfigurimi CI (tests.yml) dhe u përmirësuan testet në test_expenses.py dhe test_utils.py, duke kaluar në Green. U rregulluan funksionet në expenses.py dhe utils.py sipas TDD dhe u stabilizua procesi i testimit në GitHub Actions. Javën tjetër planifikohet korrigjimi i mungesave, përmirësimi i dizajnit dhe zgjerimi i funksionaliteteve (Feature 3).
