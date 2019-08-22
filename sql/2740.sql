select * from (select 'Podium: ' || team as "name" from league order by position limit 3) d
union all
select * from (select 'Demoted: ' || team as "name" from (select * from league order by position desc limit 2) a order by position) r
