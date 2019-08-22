select round(AVG(price), 2) from products;

-- other option
select round(sum(price) / count(price), 2) from products;