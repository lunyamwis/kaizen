-- data setup
create table tt(
X int,
Y int
);

insert into tt(X,Y)
with n8(N) as (
    select 1 N
    union all 
    select 2
    union all
    select 3
    union all
    select 4
)
select t1.N,t2.N
from n8 t1, n8 t2

-- find solutions

select t1.X, t1.Y, t2.X, t2.Y , t3.X, t3.Y, t4.X, t4.Y --, t5.X, t5.Y, t6.X, t6.Y, t7.X, t7.Y, t8.X, t8.Y 
from tt t1
join tt t2 on t1.X <> t2.X and t1.Y <> t2.Y and abs (t1.X - t2.X) <> abs (t1.Y - t2.Y)
join tt t3 on t1.X <> t3.X and t1.Y <> t3.Y and abs (t1.X - t3.X) <> abs (t1.Y - t3.Y)
          and t2.X <> t3.X and t2.Y <> t3.Y and abs (t2.X - t3.X) <> abs (t2.Y - t3.Y)
join tt t4 on t1.X <> t4.X and t1.Y <> t4.Y and abs (t1.X - t4.X) <> abs (t1.Y - t4.Y)
          and t2.X <> t4.X and t2.Y <> t4.Y and abs (t2.X - t4.X) <> abs (t2.Y - t4.Y)
          and t3.X <> t4.X and t3.Y <> t4.Y and abs (t3.X - t4.X) <> abs (t3.Y - t4.Y);