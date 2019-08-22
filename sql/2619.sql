select 
    p.name, f.name, p.price     
from 
    providers f, products p, categories c 
where
    p.id_providers = f.id and c.id = p.id_categories
    and p.price > 1000 and c.name = 'Super Luxury'