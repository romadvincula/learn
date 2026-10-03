with payments as (
    select * from {{ ref('stg_stripe__payments') }}
), 

paid_orders as (
    select
        order_id,
        sum(amount) as amount
    from payments
    where payment_status = 'success'
    group by 1
),

final as (
    select 
        ord.order_id,
        ord.customer_id,
        ord.order_date,
        coalesce(pord.amount, 0) as amount
    from {{ ref('stg_jaffle_shop__orders') }} as ord
    left join paid_orders as pord on ord.order_id = pord.order_id
)
select * from final