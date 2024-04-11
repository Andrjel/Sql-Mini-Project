-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2024-03-15 17:35:55.691

-- foreign keys
ALTER TABLE Currency_Quotes DROP CONSTRAINT Currency_Quotes_Currency;

ALTER TABLE Quotes DROP CONSTRAINT Quotes_Stock;

ALTER TABLE Stock_Exchange DROP CONSTRAINT Stock_Exchange_Country;

ALTER TABLE Stock DROP CONSTRAINT Stock_Information_Country;

ALTER TABLE Stock DROP CONSTRAINT Stock_Information_Currency;

ALTER TABLE Stock DROP CONSTRAINT Stock_Stock_Exchange;

ALTER TABLE Stock DROP CONSTRAINT Stock_Stock_Type;

-- tables
DROP TABLE Country;

DROP TABLE Currency;

DROP TABLE Currency_Quotes;

DROP TABLE Quotes;

DROP TABLE Stock;

DROP TABLE Stock_Exchange;

DROP TABLE Stock_Type;

-- End of file.

