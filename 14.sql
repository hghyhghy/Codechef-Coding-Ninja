 create  table  product(

     pid int primary key ,
     pname varchar(30),
     price decimal(10,2)
 );


 create  table sales(

     sid int primary key ,
     pid int,
     quantity int,
     sales date,
     foreign key (pid) references  product(pid)
 );

 insert into  product(pid, pname, price) VALUES
                                             (1, 'Laptop', 1200.00),
 (2, 'Smartphone', 800.00),
 (3, 'Tablet', 400.00);

 insert into sales(sid, pid, quantity, sales) VALUES
                                                  (1, 1, 2, '2023-01-15'),
 (2, 2, 5, '2023-02-20'),
(3, 3, 3, '2023-03-05');
-- #

-- 1. Find the total revenue generated by each product.

select  product.pname,sum(sales.quantity*product.price) as revenue
from product
join sales
on product.pid = sales.pid
group by product.pname ;

-- 2. Retrieve the name and price of the most expensive product sold.

select  product.pname,product.price
from  product
join sales
on product.pid = sales.pid
order by  price desc
limit 1;

-- 3. Calculate the total quantity of products sold on each sale date.

select  sales.sales,sum(sales.quantity) as total
from sales
group by sales.sales;

-- 4. Find products that were never sold.

select  product.pname
from product
where pid not in (select  pid from sales);

-- 5. List the top 2 best-selling products based on quantity.

select  product.pname,sum(sales.quantity) as total

from product
join sales
on product.pid = sales.pid
group by product.pname
order by total desc
limit 2;

-- 6. Find the average price of products sold after January 2023.

select avg(product.price) as avgprice
from product
join sales
on product.pid = sales.pid
where sales >'2023-01-31';


-- 8. Find the earliest sale date for each product.

select  product.pname, min(sales.sales) as minimumsale
from product
join sales
on product.pid = sales.pid
group by product.pname ;

-- 9. Retrieve the product name and total revenue for products with revenue greater than 2000.

select  product.pname,sum(sales.quantity*product.price) as revenue
from product
join sales
on product.pid = sales.pid
group by product.pname
having  revenue>2000;

SELECT COUNT(DISTINCT Sales.ProductID) AS unique
FROM Sales;
