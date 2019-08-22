select
	c.name, o.id
from 
	customers c, orders o
where 
	c.id = o.id_customers
	and
    	o.orders_date between '2016-1-1' and '2016-6-30'