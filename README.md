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

Red-Green-Refactor Cycle – SmartExpense Tracker
1️⃣ Red Phase (Testet që dështojnë)
•	Qëllimi: Shkrimi i testeve për funksionet kryesore: add_expense(), get_all_expenses(), delete_expense() dhe funksionet ndihmëse në utils.py.
•	Aktivitetet:
o	Krijova testet në tests/test_expenses.py dhe tests/test_utils.py.
o	Testet për add_expense() dhe delete_expense() dështuan, sepse funksionaliteti nuk ishte implementuar ende.
2️⃣ Green Phase (Kod që kalon testet)
•	Qëllimi: Implementimi i kodit minimal që bën testet të kalojnë.
•	Aktivitetet:
o	Implementova add_expense(), get_all_expenses(), delete_expense() në expenses.py.
o	Implementova format_currency() dhe validate_amount() në utils.py.
•	Rezultati: Të gjitha testet kaluan me sukses.
3️⃣ Refactor Phase (Përmirësimi i kodit pa ndryshuar funksionalitetin)
•	Qëllimi: Përmirësimi i strukturës, modularitetit dhe lexueshmërisë së kodit.
•	Aktivitetet:
o	Funksionet e shpenzimeve u grumbulluan në expenses.py.
o	Funksionet ndihmëse u vendosën në utils.py.
o	Testet u ruajtën për të garantuar që ndryshimet nuk prishin funksionalitetin.
•	Rezultati: Kodi është modular, i testueshëm dhe i qëndrueshëm.

Përditësimi i Arkitekturës – SmartExpense Tracker
Arkitektura Modulare:
•	main.py – Ndërfaqe CLI me përdoruesin.
•	expenses.py – Menaxhimi i shpenzimeve:
o	add_expense() – shton shpenzime në SQLite
o	get_all_expenses() – lexon të gjitha shpenzimet
o	delete_expense() – fshin shpenzime sipas ID-së
o	init_db() – inicializon bazën e të dhënave
•	utils.py – Funksione ndihmëse:
o	format_currency() – formaton shumën në monedhë
o	validate_amount() – kontrollon vlefshmërinë e shumave
•	data/expenses.db – Baza lokale SQLite
•	tests/ – Testet automatike me pytest, sipas modulit dhe funksionalitetit
•	.github/workflows/tests.yml – CI workflow për ekzekutimin automatik të testeve
Përfitimet e dizajnit modular:
•	Modularizim i qartë i logjikës dhe funksioneve ndihmëse
•	Testueshmëri e lartë për secilin modul
•	Ruajtje e qëndrueshme e të dhënave dhe integrim i thjeshtë me CI/CD
Test Coverage Snapshot (pytest + pytest-cov):
Name                    Stmts   Miss  Cover
-------------------------------------------
expenses.py                 33      0   100%
tests/test_expenses.py      34      0   100%
tests/test_utils.py         22      0   100%
utils.py                    11      2    82%
-------------------------------------------
TOTAL                      100      2    98%

Shpjegimi i “tests.yml” per CI passing
•  Trigger – Aktivizohet kur bëhet push ose pull_request në branch-in main.
•  Jobs → test – Përdor Ubuntu si mjedis për testim.
•  Steps:
•	Checkout repository – Klonon kodin nga GitHub.
•	Set up Python – Instalimi i Python 3.11.
•	Install dependencies – Instalohen pytest dhe pytest--cov për testim dhe mbulim kodi.
•	Run tests with coverage – Ekzekutohen testet dhe krijohet raporti i mbulimit (coverage.xml).
•	Upload test coverage report – Ngarkon raportin si artifact në GitHub për ta shkarkuar.


Shpjegimi i test_expenses.py per Feature 1 dhe 2
•  setup_function() – Pastron bazën e të dhënave para çdo testi që testet të jenë të izoluar (TDD).
•  Feature 1 (Shtimi i shpenzimeve)
•	test_add_expense() – Kontrollon që një shpenzim i vetëm shtohet.
•	test_add_multiple_expenses() – Kontrollon që disa shpenzime shtohen njëherësh.
•	test_add_invalid_expense() – Kontrollon që shtimi i të dhënave të pavlefshme hedh gabim (ValueError).
•	
•  Feature 2 (Fshirja e shpenzimeve)
•	test_delete_expense() – Kontrollon që një shpenzim mund të fshihet.
•  Extra validation
•	test_database_initialization() – Kontrollon që funksioni get_all_expenses() kthen një listë pas inicializimit të DB.


Shpjegimi i test_utils.py per  Feature 1 dhe 2
•  Testet për format_currency()
•	test_format_currency() – Kontrollon që një numër i thjeshtë formatizohet si "5.00 €".
•	test_format_currency_large_number() – Kontrollon që numrat shumë të mëdhenj formatizohen si duhet.
•	test_format_currency_with_float() – Rrotullon numrat me dhjetore tek 2 shifra pas presjes.
•  Testet për validate_amount()
•	test_validate_amount_valid() – Numrat pozitivë pranohen.
•	test_validate_amount_invalid() – Numrat negativë ose jo-numerikë refuzohen.
•	test_validate_amount_zero() – 0 nuk konsiderohet i vlefshëm.
•	test_validate_amount_none() – None refuzohet.
•	test_validate_amount_empty_string() – String i zbrazët refuzohet.

Raport Javor – TDD
Projekti: Expense Tracker | Java: 2 | Data: 12.11.2025
Këtë javë u krijuan testet fillestare sipas TDD (shtim, fshirje, formatim shpenzimesh), të cilat aktualisht deshtojnë (Red). U organizuan testet me komente dhe emra funksionesh më të qartë. Javën tjetër do të implementohen funksionet kryesore për të kaluar testet dhe do të fillojë interface-i vizual.

Raport Javor – TDD
Projekti: Expense Tracker | Java: 3 | Data: 21.11.2025
Këtë javë u implementuan funksionet kryesore të Expense Tracker në utils.py, expenses.py dhe main.py, duke kaluar shumicën e testeve ekzistuese (Red → Green). U përmirësuan emrat e funksioneve dhe organizimi i kodit për të qenë më i qartë dhe i mirëmbajtshëm. Javën tjetër planifikohet plotësimi i funksioneve të munguar dhe sigurimi që të gjitha testet të kalojnë me sukses.

Raport Javor – TDD
Projekti: Expense Tracker | Java: 4 | Data: 24.11.2025
Këtë javë u shtua konfigurimi CI (tests.yml) dhe u përmirësuan testet në test_expenses.py dhe test_utils.py, duke kaluar në Green. U rregulluan funksionet në expenses.py dhe utils.py sipas TDD dhe u stabilizua procesi i testimit në GitHub Actions. Javën tjetër planifikohet korrigjimi i mungesave, përmirësimi i dizajnit dhe zgjerimi i funksionaliteteve (Feature 3).
