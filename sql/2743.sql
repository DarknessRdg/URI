select * from (select name, length(name) from people) a order by length desc