with max_high as 
(SELECT name,SUBSTRING(ts, 12, 2) AS hour, max(high) max_high from project03.sta9760ff2020stream1 group by name, SUBSTRING(ts, 12, 2))
select sh.name, high, ts, SUBSTRING(ts, 12, 2) AS hour from project03.sta9760ff2020stream1 sh join max_high mh on sh.name=mh.name and sh.high = mh.max_high and SUBSTRING(sh.ts, 12, 2) = mh.hour
order by sh.name, SUBSTRING(ts, 12, 2);