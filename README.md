1. Cele ćwiczenia:
- Utrwalenie składni w GiT
- Zapoznanie się ze standardami przechowywania danych w plikach 
tekstowych
- Utworzenie projektu informatycznego i zarządzanie jego wersją w GiT - 
- Zapoznanie się z Github Actions
- Język programowania dowolny, preferowany Python

2. Opis projektu:
<p>
Program do konwersji danych obsługujący formaty: .xml, .json i .yml (.yaml)
Sposób użycia: program.exe pathFile1.x pathFile2.y
gdzie x i y to jeden z formatów .xml, .json i .yml (.yaml).
Powyższe wywołanie programu powinno prawidłowo rozpoznać format, pobrać dane z pathFile1.x, a 
następnie utworzyć nowy plik pathFile2.y i przekonwertować dane zgodnie z nowym formatem.
</p>
<p>
W przypadku tworzenia oprogramowania w pythonie, z projektu należy wygenerować plik .exe przy pomocy
pyinstaller.exe (dostępny do instalacji przez pip). Aby uniknąć powstania wielu .dll trzeba wykorzystać flagę
--onefile:
pyinstaller.exe --onefile project.py
</p>
<p>
Dodatkowo można dołączyć do projektu prosty UI (User Interface), sugerowany jest PyQt (dostępny przez 
pip).
Przy uruchomieniu programu posiadającego własny UI, dodatkowo zostanie uruchomione okno wiersza 
poleceń. Aby uniknąć takiego zachowania, trzeba wygenerować plik .exe komendą:
pyinstaller.exe --onefile --noconsole project.py
</p>
