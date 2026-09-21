select 'hello world!';


select 'hello world!' as "Greeting";

show schemas;

show databases;

show schemas in account;

show tables in account;

insert into root_depth 
values
(
    3,
    'D',
    'Deep',
    'cm',
    60,
    90
);

select * from root_depth;


--To add more than one row at a time
insert into root_depth (root_depth_id, root_depth_code
     , root_depth_name, unit_of_measure
     , range_min, range_max)  
values
     (5,'X','short','in',66,77)
     ,(8,'Y','tall','cm',98,99)
;


-- To remove a row you do not want in the table
delete from root_depth
where root_depth_id = 6;


--To change a value in a column for one particular row
update root_depth
set root_depth_id = 6
where root_depth_id = 8;


--To remove all the rows and start over
truncate table root_depth;

use role accountadmin;

create or replace api integration dora_api_integration
api_provider = aws_api_gateway
api_aws_role_arn = 'arn:aws:iam::321463406630:role/snowflakeLearnerAssumedRole'
enabled = true
api_allowed_prefixes = ('https://awy6hshxy4.execute-api.us-west-2.amazonaws.com/dev/edu_dora');


use role accountadmin;  

-- Create the missing database
CREATE DATABASE IF NOT EXISTS UTIL_DB;

create or replace external function util_db.public.grader(
      step varchar
    , passed boolean
    , actual integer
    , expected integer
    , description varchar)
returns variant
api_integration = dora_api_integration 
context_headers = (current_timestamp, current_account, current_statement, current_account_name) 
as 'https://awy6hshxy4.execute-api.us-west-2.amazonaws.com/dev/edu_dora/grader'
; 


use role accountadmin;
use database util_db; 
use schema public; 

select grader(step, (actual = expected), actual, expected, description) as graded_results from
(SELECT 
 'DORA_IS_WORKING' as step
 ,(select 123) as actual
 ,123 as expected
 ,'Dora is working!' as description
); 


show functions in account; 


-- ALTER FUNCTION GARDEN_PLANTS.VEGGIE.GRADER RENAME TO UTIL_DB.PUBLIC.GRADER;


select * 
from garden_plants.information_schema.schemata;


SELECT * 
FROM GARDEN_PLANTS.INFORMATION_SCHEMA.SCHEMATA
where schema_name in ('FLOWERS','FRUITS','VEGGIES'); 


select count(*) as schemas_found, '3' as schemas_expected 
from GARDEN_PLANTS.INFORMATION_SCHEMA.SCHEMATA
where schema_name in ('FLOWERS','FRUITS','VEGGIES'); 


select * from garden_plants.veggies.vegetable_details;

select * from garden_plants.veggies.vegetable_details
where plant_name = 'Spinach' and root_depth_code = 'D';


delete from garden_plants.veggies.vegetable_details
where plant_name = 'Spinach' and root_depth_code = 'D';



-- copy into my_table_name
-- from @my_internal_stage
-- files = ( 'IF_I_HAD_A_FILE_LIKE_THIS.txt')
-- file_format = ( format_name='EXAMPLE_FILEFORMAT' );


copy into garden_plants.veggies.vegetable_details_soil_type
from @util_db.public.my_internal_stage
files = ( 'VEG_NAME_TO_SOIL_TYPE_PIPE.txt')
file_format = ( format_name=GARDEN_PLANTS.VEGGIES.PIPECOLSEP_ONEHEADROW );



--The data in the file, with no FILE FORMAT specified
select $1
from @util_db.public.my_internal_stage/LU_SOIL_TYPE.tsv;

--Same file but with one of the file formats we created earlier  
select $1, $2, $3
from @util_db.public.my_internal_stage/LU_SOIL_TYPE.tsv
(file_format => garden_plants.veggies.COMMASEP_DBLQUOT_ONEHEADROW);

--Same file but with the other file format we created earlier
select $1, $2, $3
from @util_db.public.my_internal_stage/LU_SOIL_TYPE.tsv
(file_format => garden_plants.veggies.PIPECOLSEP_ONEHEADROW );


select $1, $2, $3
from @util_db.public.my_internal_stage/LU_SOIL_TYPE.tsv
(file_format => garden_plants.veggies.l9_challenge_ff);



copy into garden_plants.veggies.LU_SOIL_TYPE
from @util_db.public.my_internal_stage
files = ( 'LU_SOIL_TYPE.tsv')
file_format = ( format_name=garden_plants.veggies.l9_challenge_ff );


select * from garden_plants.veggies.lu_soil_type;


select $1, $2, $3, $4
from @util_db.public.my_internal_stage/veg_plant_height.csv
(file_format => garden_plants.veggies.COMMASEP_DBLQUOT_ONEHEADROW);


copy into garden_plants.veggies.vegetable_details_plant_height
from @util_db.public.my_internal_stage
files = ( 'veg_plant_height.csv' )
file_format = ( format_name=garden_plants.veggies.COMMASEP_DBLQUOT_ONEHEADROW );


select * from garden_plants.veggies.vegetable_details_plant_height;





