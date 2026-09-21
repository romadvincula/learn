create table garden_plants.veggies.vegetable_details
(
plant_name varchar(25)
, root_depth_code varchar(1)    
);


create table garden_plants.flowers.flower_details
(
plant_name varchar(25)
, root_depth_code varchar(1)    
);


create table garden_plants.veggies.vegetable_details_soil_type
(
plant_name varchar(25)
, root_depth_code varchar(1)    
);


create file format garden_plants.veggies.PIPECOLSEP_ONEHEADROW 
    type = 'CSV'--csv is used for any flat file (tsv, pipe-separated, etc)
    field_delimiter = '|' --pipes as column separators
    skip_header = 1 --one header row to skip
    ;


create file format garden_plants.veggies.COMMASEP_DBLQUOT_ONEHEADROW 
    TYPE = 'CSV'--csv for comma separated files
    FIELD_DELIMITER = ',' --commas as column separators
    SKIP_HEADER = 1 --one header row  
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
--this means that some values will be wrapped in double-quotes bc they have commas in them
    ;


create or replace file format garden_plants.veggies.L9_CHALLENGE_FF
    TYPE = 'CSV'
    FIELD_DELIMITER = '\t'
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    ;


create or replace table garden_plants.veggies.LU_SOIL_TYPE(
SOIL_TYPE_ID number,	
SOIL_TYPE varchar(15),
SOIL_DESCRIPTION varchar(75)
);



create or replace table garden_plants.veggies.VEGETABLE_DETAILS_PLANT_HEIGHT(
plant_name VARCHAR(30),	
UOM varchar(1),
Low_End_of_Range number,
High_End_of_Range number
);