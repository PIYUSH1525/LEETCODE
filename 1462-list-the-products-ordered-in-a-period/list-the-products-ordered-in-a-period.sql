select product_name, sum(unit) unit
from products p
join orders o on p.product_id = o.product_id
where o.order_date like '2020-02%'
group by product_name
having sum(unit) >= 100