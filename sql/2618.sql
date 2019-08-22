select 
    p.name, f.name, c.name 
from
    providers f, products p, categories c 
where
    p.id_providers = f.id and c.id = p.id_categories
    and f.name = 'Sansul SA' and c.name = 'Imported'