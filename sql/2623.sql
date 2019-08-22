select 
    p.name, c.name 
from 
    products p, categories c 
where
    c.id = id_categories and
    id_categories in (1,2,3,6, 9) and
    p.amount > 100
