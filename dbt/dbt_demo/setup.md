# uv instructions
# install uv (reopen terminal after install)
pip install uv

# go to project dir
cd demo_dbt

# initialize uv env
uv init .

# install dbt packages (try to use up to same minor version release)
uv add dbt-core dbt-postgres

# check if dbt is installed properly
uv run dbt --version

# initialize dbt project
uv run dbt init


# venv instructions (Windows)
# go to project dir
cd dbt_demo

# activate venv
venv\Scripts\activate

# install dbt packages (try to use up to same minor version release)
python -m pip install dbt-core dbt-postgres pip_system_certs

# check if dbt is installed properly
dbt --version

# download data files
aws s3 cp --no-verify-ssl 's3://dbt-tutorial-public/jaffle_shop_customers.csv' .

aws s3 cp --no-verify-ssl 's3://dbt-tutorial-public/jaffle_shop_orders.csv' .

aws s3 cp --no-verify-ssl 's3://dbt-tutorial-public/stripe_payments.csv' .

# populate tables (run in psql raw db)
\copy jaffle_shop.customers FROM 'jaffle_shop_customers.csv' CSV HEADER;

\copy jaffle_shop.orders (id, user_id, order_date, status) FROM 'jaffle_shop_orders.csv' CSV HEADER;

\copy stripe.payment (id, orderid, paymentmethod, status, amount, created) FROM 'stripe_payments.csv' CSV HEADER;

# clone initial project state and cd to it
git clone https://github.com/dbt-labs/dbt-learn-gt-init.git
cd dbt-learn-gt-init

# or initialize a new dbt project
dbt init

# compile data models to see if there are any errors
dbt compile

# execute code to transform data in dw
dbt run

# run model and its upsteam dependencies before hand
dbt run --select +models/fact_customers_orders.sql

# compile a specific model
dbt compile --select stg_jaffle_shop__customers

# run freshness test of sources data
dbt source freshness

# add packages, which are custom macros, from https://hub.getdbt.com/
# example, create a packages.yml in the dbt project dir and add:
packages:
  - package: dbt-labs/codegen
    version: 0.14.1

# download and install packages
dbt deps

# use generate_source macro from code_gen package (cmd):
dbt run-operation generate_source --args "{\"schema_name\": \"jaffle_shop\", \"database_name\": \"raw\"}"

# sample output:
sources:
  - name: jaffle_shop
    tables:
      - name: customers
      - name: dim_customers
      - name: fct_orders
      - name: orders
      - name: stg_jaffle_shop__customers
      - name: stg_jaffle_shop__orders
      - name: stg_stripe__payments

# use generate_base_model (for staging models):
dbt run-operation generate_base_model --args "{\"source_name\": \"jaffle_shop\", \"table_name\": \"customers\"}"

# output
with source as (
    select * from {{ source('jaffle_shop', 'customers') }}
),
renamed as (
    select
        id,
        first_name,
        last_name
    from source
)
select * from renamed

# save to a file the output of generate_base_model using pipes
dbt --quiet run-operation generate_base_model --args "{\"source_name\": \"jaffle_shop\", \"table_name\": \"customers\"}" > models\staging\jaffle_shop\stg_jaffle_shop__customers.sql

# run tests
dbt test

# execute generic tests only
dbt test --select test_type:generic

# execute singular tests only
dbt test --select test_type:singular

# run tests on a specific source name
dbt test --select source:jaffle_shop

# run tests on all sources
dbt test --select source:*

# use build to run models and tests them safetly
# build combines run and test but stops downstream models 
# from running if a test upstream fails or error occurs
dbt build