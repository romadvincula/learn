// Create a database named SOCIAL_MEDIA_FLOODGATES
use role sysadmin;
// Create a new database and set the context to use the new database
create database SOCIAL_MEDIA_FLOODGATES comment = 'DWW Lesson 12 Nested Semi-structured data';
//Set the worksheet context to use the new database
use database social_media_floodgates;


use database social_media_floodgates;
use role sysadmin;

create or replace table social_media_floodgates.public.tweet_ingest
(
    raw_status variant
);


create file format social_media_floodgates.public.json_file_format
type = 'JSON' 
compression = 'AUTO' 
enable_octal = FALSE
allow_duplicate = FALSE
strip_outer_array = TRUE
strip_null_values = FALSE
ignore_utf8_errors = FALSE;


// preview staged file
select $1
from @util_db.public.my_internal_stage/nutrition_tweets.json
(file_format => social_media_floodgates.public.json_file_format);


copy into social_media_floodgates.public.tweet_ingest
from @util_db.public.my_internal_stage
files = ( 'nutrition_tweets.json' )
file_format = ( format_name=social_media_floodgates.public.json_file_format );

select * from social_media_floodgates.public.tweet_ingest;



//simple select statements -- are you seeing 9 rows?
select raw_status
from tweet_ingest;

select raw_status:entities
from tweet_ingest;

select raw_status:entities:hashtags
from tweet_ingest;

//Explore looking at specific hashtags by adding bracketed numbers
//This query returns just the first hashtag in each tweet
select raw_status:entities:hashtags[0].text
from tweet_ingest;

//This version adds a WHERE clause to get rid of any tweet that 
//doesn't include any hashtags
select raw_status:entities:hashtags[0].text
from tweet_ingest
where raw_status:entities:hashtags[0].text is not null;

//Perform a simple CAST on the created_at key
//Add an ORDER BY clause to sort by the tweet's creation date
select raw_status:created_at::date
from tweet_ingest
order by raw_status:created_at::date;


with cleaned as (
select 
    raw_status:id::numeric as tweet_id,
    raw_status:created_at::date as created_at,
from tweet_ingest
)
select
    created_at,
    count(tweet_id)
from cleaned
group by created_at
order by created_at;


//Flatten statements can return nested entities only (and ignore the higher level objects)
select value
from tweet_ingest
,lateral flatten
(input => raw_status:entities:urls);

select value
from tweet_ingest
,table(flatten(raw_status:entities:urls));



//Flatten and return just the hashtag text, CAST the text as VARCHAR
select value:text::varchar as hashtag_used
from tweet_ingest
,lateral flatten
(input => raw_status:entities:hashtags);

//Add the Tweet ID and User ID to the returned table so we could join the hashtag back to it's source tweet
select raw_status:user:name::text as user_name
,raw_status:id as tweet_id
,value:text::varchar as hashtag_used
from tweet_ingest
,lateral flatten
(input => raw_status:entities:hashtags);


create or replace view social_media_floodgates.public.urls_normalized as
(select raw_status:user:name::text as user_name
,raw_status:id as tweet_id
,value:display_url::text as url_used
from tweet_ingest
,lateral flatten
(input => raw_status:entities:urls)
);


create or replace view social_media_floodgates.public.hashtags_normalized as
(
    select raw_status:user:name::text as user_name
    ,raw_status:id as tweet_id
    ,value:text::varchar as hashtag_used
    from tweet_ingest
    ,lateral flatten
    (input => raw_status:entities:hashtags)
);


