create schema if not exists jaffle_shop;

create schema if not exists stripe;

create table jaffle_shop.customers 
( id integer,
  first_name varchar,
  last_name varchar
);

create table jaffle_shop.orders
( id integer,
  user_id integer,
  order_date date,
  status varchar,
  _etl_loaded_at timestamp default CURRENT_TIMESTAMP
);

create table stripe.payment 
( id integer,
  orderid integer,
  paymentmethod varchar,
  status varchar,
  amount integer,
  created date,
  _batched_at timestamp default current_timestamp
);
