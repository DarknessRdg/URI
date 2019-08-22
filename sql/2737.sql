select name, customers_number from lawyers where customers_number in (select max(customers_number) from lawyers)
union all
select name, customers_number from lawyers where customers_number in (select min(customers_number) from lawyers)
union all
select 'Average', trunc(avg(customers_number), 0) from lawyers