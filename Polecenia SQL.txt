1. Dla tabeli customers stworzyć zapytanie, które wyświetli wszystkie osoby mieszkające w Berlinie lub we Francji.

SELECT * FROM `customers` WHERE Country = 'Berlin' OR Country = 'France';

2. Dla tabeli orders stworzyć zapytanie, które wyświetli tylko 2 pierwsze rekordy należące do przedziału dat od 1996-07-15 do  1996-07-30 posortowane rosnąco po kolumnie ShipperID oraz malejąco po kolumnie OrderID.

SELECT * FROM `orders` WHERE OrderID BETWEEN '1996-07-15' AND '1996-07-30' Order BY ShipperID ASC, OrderID DESC limit 3;

3. Wstawić nowy rekord do tabeli products o nazwie Krzesło, cenie wynoszącej 25, CategoryID równym 1 oraz SupplierID równym 1

INSERT INTO products (ProductName, Price, CategoryID, SupplierID) VALUES ("Krzesło", 25, 1, 1);

4. Zaktualizować w tabeli shippers kolumnę Phone o wartość Brak dla wszystkich rekordów, które nie mają uzupełnionej wartości Phone 

UPDATE shippers SET Phone = 'Brak' Where Phone is null;

5. Usunąć rekordy z tabeli shippers , których ShipperID mieści się w przedziale od 4 do 5

DELETE FROM shippers WHERE ShipperID BETWEEN 4 and 5

6. Dla tabeli suppliers przygotuj zestawienie, które pogrupuje łączną ilość osób należących dla konkretnego Country.

Select Country, Count(ContactName) As Ilośćosób FROM suppliers Group by Country;

7.Wykonaj zapytanie, które połączy dwie tabele: products oraz order_details i przedstawi zwrócone wartości Product name oraz Quantity.

SELECT products.ProductName, order_details.Quantity FROM products INNER JOIN order_details;

8.1.Stworzyć bazę danych o nazwie sklep

Create database sklep

8.2. Stworzyć tabelkę produkty z następującymi typami kolumn:

-ID - klucz główny

-nazwa - varchar z maksymalną ilością znaków 150

- iloscSztuk - int

- price - money


CREATE TABLE produkty(
    ID int,
    nazwa varchar(150),
    iloscSztuk int,
    price decimal(10,2),
    PRIMARY KEY (ID)
);

8.3.Zapełnij tabelkę produkty 5 produktami

Insert INTO produkty VALUES (1, 'krzesło',10, 15.50)
Insert INTO produkty VALUES (2, 'stół',15, 21.99)
Insert INTO produkty VALUES (3, 'biurko',5, 99.99)
Insert INTO produkty VALUES (4, 'lampa',30, 15.99)
Insert INTO produkty VALUES (5, 'szafka',5, 41.99)

8.4. Utwórz kopię bazy sklep

backup DATABASE sklep
TO disk = 'C:\Users\UserTest'

8.5.Usunąć bazę danych sklep
DROP DATABASE sklep

8.6 Zaimportować bazę danych z utworzonej kopii

Create database sklep

Za pomocą phpmyadmin exportujemy wcześniej zrobiony backup.

8.7 Zmodyfikuj dowolną kolumnę w bazie sklep

ALTER TABLE produkty MODIFY COLUMN iloscSztuk varchar(999)

8.8 Usuń tabelę produkty

DROP TABLE produkty

8.9 Usuń bazę danych sklep

drop DATABASE sklep
