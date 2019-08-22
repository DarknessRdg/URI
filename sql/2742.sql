select 
    l.name, trunc(omega * 1.618, 3) "Fator N" 
from 
    dimensions d join life_registry l on d.id = dimensions_id 
where (d.name = 'C875' or d.name = 'C774') and l.name like 'Richard%'