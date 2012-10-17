TERMS PL
==============
A set of tools to analyse term frequencies in web documents in polish. Currently, the project is limited to proccessing web data in order to calculate TF/IDF score. Unless it is stated otherwise, everything is distributed under BSD license.

---
TOOLS
---
word_freq.py: as input take a csv file with a column that has text (in polish) in which You want to count word frequencies. As output, print as many lines, as there are unique pairs: rows at the begining - words in the text column. Let's say that your input file looks like this (but must be in polish:) ):
Blogpost_number1;"Hello, world! Hello".
The Output would look like this:
Blogpost_number1;Hello;2
Blogpost_number1;,;1
Blogpost_number1;world;1
Blogpost_number1;!;1

My script takes advantage of a very useful tool written by Marcin Woliński. This is a copyright disclaimer, unfortunatly in polish only. If you dont understand what the heck does it mean, just remember that the code of Morfeusz is distributed under BSD license, but the results of this program is a transformation of corpus data owned by someone.
##############################
Copyright © 2011 Zygmunt Saloni, Włodzimierz Gruszczyński, Marcin Woliński, Robert Wołosz

Wszelkie prawa zastrzeżone.

Redystrybucja i używanie, czy to w formie kodu źródłowego, czy w formie kodu wykonawczego, są dozwolone pod warunkiem spełnienia poniższych warunków:

Redystrybucja kodu źródłowego musi zawierać powyższą notę copyrightową, niniejszą listę warunków oraz poniższe oświadczenie o wyłączeniu odpowiedzialności.

Redystrybucja kodu wykonawczego musi zawierać powyższą notę copyrightową, niniejszą listę warunków oraz poniższe oświadczenie o wyłączeniu odpowiedzialności w dokumentacji i/lub w innych materiałach dostarczanych wraz z kopią oprogramowania.

NINIEJSZE OPROGRAMOWANIE JEST DOSTARCZONE PRZEZ WŁAŚCICIELI PRAW AUTORSKICH „TAKIM, JAKIE JEST”. KAŻDA, DOROZUMIANA LUB BEZPOŚREDNIO WYRAŻONA GWARANCJA, NIE WYŁĄCZAJĄC DOROZUMIANEJ GWARANCJI PRZYDATNOŚCI HANDLOWEJ I PRZYDATNOŚCI DO OKREŚLONEGO ZASTOSOWANIA, JEST WYŁĄCZONA. W ŻADNYM WYPADKU WŁAŚCICIELE PRAW AUTORSKICH NIE MOGĄ BYĆ ODPOWIEDZIALNI ZA JAKIEKOLWIEK BEZPOŚREDNIE, POŚREDNIE, INCYDENTALNE, SPECJALNE, UBOCZNE I WTÓRNE SZKODY (NIE WYŁĄCZAJĄC OBOWIĄZKU DOSTARCZENIA PRODUKTU ZASTĘPCZEGO LUB SERWISU, ODPOWIEDZIALNOŚCI Z TYTUŁU UTRATY WALORÓW UŻYTKOWYCH, UTRATY DANYCH LUB KORZYŚCI, A TAKŻE PRZERW W PRACY PRZEDSIĘBIORSTWA) SPOWODOWANE W JAKIKOLWIEK SPOSÓB I NA PODSTAWIE ISTNIEJĄCEJ W TEORII ODPOWIEDZIALNOŚCI KONTRAKTOWEJ, CAŁKOWITEJ LUB DELIKTOWEJ (WYNIKŁEJ ZARÓWNO Z NIEDBALSTWA JAK INNYCH POSTACI WINY), POWSTAŁE W JAKIKOLWIEK SPOSÓB W WYNIKU UŻYWANIA LUB MAJĄCE ZWIĄZEK Z UŻYWANIEM OPROGRAMOWANIA, NAWET JEŚLI O MOŻLIWOŚCI POWSTANIA TAKICH SZKÓD OSTRZEŻONO.
#############################

---

tfidf.py: calculate tf/idf for a given dataframe.
script calculates TF/IDF value for words in a set of documents
User has to specify: 
1. A csv-formatted file (';' as separator, '"' as quote),
2. The number of a column which contains words
3. The number of a column which contains the sum of term occurances in a document
4. The number of a column that indicates by which column to aggregate ( a document : 'd' in http://en.wikipedia.org/wiki/TFIDF )
This script writes output to STDOUT
