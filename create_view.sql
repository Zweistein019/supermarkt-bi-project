CREATE OR REPLACE VIEW vw_umsatz AS
SELECT city AS Stadt,
datetime AS Verkaufszeit,
ROUND(quantity * unit_cost,2) AS Kosten,
customer_type AS Kundentyp,
quantity AS Bestellungen, 
ROUND(revenue,2) AS Umsatz,
rating AS Bewertung,
payment_method AS Zahlungsmethode,
product_line AS Produktkategorie
FROM supermarkt_sales;


