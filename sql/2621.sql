select
	p.name
from 
	products p, providers pd
where 
	p.id_providers = pd.id
    and p.amount between 10 and 20
    and pd.name like 'P%'