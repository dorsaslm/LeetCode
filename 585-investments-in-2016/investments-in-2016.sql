# Write your MySQL query statement below
with cte as(
    select pid,tiv_2015,tiv_2016,lat,lon
    from Insurance
),
cte1 as(
    select * from cte
    where not exists (SELECT 1 
        FROM Insurance AS i 
        WHERE i.pid != cte.pid AND i.lat = cte.lat AND i.lon = cte.lon)
    and exists (select 1 from Insurance AS ii where ii.pid != cte.pid and ii.tiv_2015 = cte.tiv_2015 )
)
select round(sum(tiv_2016),2) as tiv_2016  from cte1


