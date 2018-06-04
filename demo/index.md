# DMap Alexa 1M dataset and analysis
  
## Notice:

  * Commit date: Tue Feb 27 11:45:47 UTC 2018

## Goal: 
  * [DMap][1] is our multi-application measurement tool.
  * In this document, we present the results produced by [Dmap][1] after crawling Alexa 1M domains.
  * In this way, users can reproduce Table III from our [DMap paper](../paper.pdf) , and understand how to do measurement analysis using simple SQL code.

  
  
## Requirements:
  * [PostgreSQL DB][3]
  * Any SQL client that can connect to postgresql

## 1. Download the data and set it up 

   * You can download the 1 million scan results from [this link](https://dmap.sidnlabs.nl/demo/pg_dump_export_20180227.zip).
   * Then install it at your already configured [PostgreSQL DB][3] using the following command:
   

```bash
# unzip file
$ unzip  pg_dump_export_20180227.zip

# create database
$ createdb -T template0 DMapdb

# import the data
$ psql DMapdb < pg_dump_export_20180227
```

## 2. DNS
 
   * From this point onwards, we show the results of Table III in the paper, and which queries/python code we use to obtain these numbers
   

#### 2.1 DNS results from Table III in [DMap paper][2]:

|*Metric* |*IPv4* |*IPv6* |*IPv6/IPv4*|
| --------| ------|-------| ----------|
|# Domains (OK) |972,155|153,485|0.16|
|# Unique NSes |289,014|26,127|0.09|
|# Unique IP |210,650|19,754|0.09|
|# Unique ASes |18,418|3,178 |0.17|
|# CDN Cloudflare |117,538|115,396 |0.98|

#### 2.2 SQL queries to obtain these results


*IMPORTANT:*  crawl_run=67 is a ID of this entire measurment, and it' s a fixed value in all queries here.

```sqlite-psql
--Domains (OK)

--IPv4(crawl_status=0 means no error during crawling)
select count(1) from crawl_result_dns  
where crawl_run=67 and ip_version=4 and crawl_status=0

--IPv6 (crawl_status=0 no error)
select count(1) from crawl_result_dns   
where crawl_run=67 and ip_version=6 and crawl_status=0


-- unique IPs (IPv4)

select count( distinct uq_ip)
from (select json_array_elements((jsonb_array_elements(dns_ns)->>'addresses')::json)->>'address' as uq_ip
from crawl_result_dns
where dns_ns is not null 
and ip_version = 4
and crawl_status = 0
and crawl_run = 67)as ips

  
-- unique IPs (IPv6)

select count( distinct uq_ip)
from (select json_array_elements((jsonb_array_elements(dns_ns)->>'addresses')::json)->>'address' as uq_ip
from crawl_result_dns
where dns_ns is not null 
and ip_version = 4
and crawl_status = 0
and crawl_run = 67)as ips

--unique NSes (IPv4)

select count( distinct lower(ns_name))
from (select jsonb_array_elements(dns_ns)->>'name' as ns_name
from crawl_result_dns
where dns_ns is not null
and ip_version = 6
and crawl_status = 0
and crawl_run = 67)as ns_names

-- unique NSes (IPV6)

select count( distinct lower(ns_name))
from (select jsonb_array_elements(dns_ns)->>'name' as ns_name
from crawl_result_dns
where dns_ns is not null
and ip_version = 6
and crawl_status = 0
and crawl_run = 67)as ns_names

--- unique ASes (Ipv4)

select count( distinct uq_as)
from (select json_array_elements((jsonb_array_elements(dns_ns)->>'addresses')::json)->>'asn' as uq_as
from crawl_result_dns
where dns_ns is not null 
and ip_version = 4
and crawl_status = 0
and crawl_run = 67)as ases

--- unique ASes (ipv6)

select count( distinct uq_as)
from (select json_array_elements((jsonb_array_elements(dns_ns)->>'addresses')::json)->>'asn' as uq_as
from crawl_result_dns
where dns_ns is not null 
and ip_version = 6
and crawl_status = 0
and crawl_run = 67)as ases

---cloudflare

select count(domainname) from  crawl_result_dns   
where crawl_run=67 and ip_version=4 and crawl_status=0 
and dns_cdn_cloudflare=true

select count(domainname) from  crawl_result_dns 
  where crawl_run=67 and ip_version=6 and crawl_status=0 
 and dns_cdn_cloudflare=true

```


## 3. HTTP

### 3.1 HTTP results from Table III in [DMap paper][2]:

|*Metric* |*IPv4* |*IPv6* |*IPv6/IPv4*|
| --------| ------|-------| ----------|
|# Domains (OK) |968,338|153,485 |0.16|
|#HTML 5 |681,757|116,066|0.17|
|Bytes (median) |53,889|64,735| 1.20|
|External links (median) |7|8|1.14|
|Internal links (median) |67 |75|1.12|
|Cookies (median) |1|1|1.00|



### 3.3 HTTP SQL queries
```sqlite-psql

--IPv4(crawl_status=0 no error)
select count(1) from crawl_result_http 
 where crawl_run=67 and ip_version=4
 and crawl_status=0

--IPv6 (crawl_status=0 no error)
select count(1) from crawl_result_http 
where crawl_run=67 and ip_version=6 
and crawl_status=0

---- html 5 (ipv4)

select html_version, count(1) as df from crawl_result_http 
where crawl_run=67 and ip_version=4  and http_status=200
 and crawl_status=0 group by html_version

---- html 5 (ipv6)
select html_version, count(1) as df from crawl_result_http
 where crawl_run=67 and ip_version=6  and crawl_status=0 
 and http_status=200  group by html_version


---median bytes len (IPv4/IPV6)

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by http_bytes_len)
 FROM crawl_result_http   where crawl_run=67 and ip_version=4 
 and crawl_status=0  and http_status=200 

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by http_bytes_len) 
FROM crawl_result_http   where crawl_run=67 and ip_version=6 
and crawl_status=0  and http_status=200  


---internal links  (IPv4/IPV6)

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by html_links_int) 
FROM crawl_result_http   where crawl_run=67 and ip_version=4 and 
crawl_status=0  and http_status=200 

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by html_links_int) 
FROM crawl_result_http   where crawl_run=67 and ip_version=6 
sand crawl_status=0  and http_status=200 

--- external links  (IPv4/IPV6)

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by html_links_ext) 
FROM crawl_result_http   where crawl_run=67 and ip_version=4 
and crawl_status=0  and http_status=200 

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by html_links_ext) 
FROM crawl_result_http   where crawl_run=67 and ip_version=6 
and crawl_status=0  and http_status=200 


---cookie count (IPv4/IPV6)

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by cookie_count) 
FROM crawl_result_http   where crawl_run=67 and ip_version=4
 and crawl_status=0

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER by cookie_count) 
FROM crawl_result_http   where crawl_run=67 and ip_version=6
 and crawl_status=0 
```

## 4.TLS


### 4.1 DNS results from Table III in [DMap paper][2]:

|*Metric* |*IPv4* |*IPv6* |*IPv6/IPv4*|
| --------| ------|-------| ----------|
|#Domains (OK) |772,455 |129,443|0.17|
|# Let’s Encrypt |165,526|10,466|0.06|
    

### 4.2 TLS SQL queries



```sqlite-psql
---Domains (OK) (IPV4/IPV60

select count(1)  from  crawl_result_tls   where
 crawl_run=67 and ip_version=4 and crawl_status=0 
 and tls_avail=true
 
select count(1)  from  crawl_result_tls   where 
crawl_run=67 and ip_version=6 and crawl_status=0 
and tls_avail=true

--- Let's Encrypt  (IPV4/IPV60

select count(1)  from  crawl_result_tls   where crawl_run=67 
and ip_version=4 and tls_letsencrypt=True

select count(1)  from  crawl_result_tls   where crawl_run=67 
and ip_version=6 and tls_letsencrypt=True
```

## 5. SMTP

### 5.1 SMTP results from Table III in [DMap paper][2]:
 
 
|*Metric* |*IPv4* |*IPv6* |*IPv6/IPv4*|
| --------| ------|-------| ----------|
|# Domains (OK) |843,126|190,736|0.23|
|# Unique SMTP |501,848 |24,311|0.05|
|# Unique IP |286,504|10,113|0.04|
|# Unique StartTLS |302,871 |8,016|0.03|



### 5.2 STMP SQL queries

  * For  StartTLS query support, we did not write the JSON queries, but a python script. Please [download it here][4] and run it, and obtain all results for SMTP.
   
   * Here is part of the queries, for the remaining see the [smtpstats.py][4].


 ```sqlite-psql  
 --domains (OK), IPv4 and IPv6:
 
  select count(domainname) from crawl_result_smtp 
    where crawl_run=67 and ip_version=4 and
    crawl_status=0 and smtp_count>0

   select count(domainname) from crawl_result_smtp
      where crawl_run=67 and ip_version=6 and
      crawl_status=0 and smtp_count>0
  
 --unique SMTP (Ipv4, IPv6):
 
WITH smtp_hosts AS (
   select lower(json_array_elements(smtp_hosts::json)->>'name') as host
   from crawl_result_smtp
   where ip_version = 4
   and crawl_status = 0
   and crawl_run = 67
)

select count(distinct host)
from smtp_hosts

 --unique SMTP (Ipv6):
 
WITH smtp_hosts AS (
   select lower(json_array_elements(smtp_hosts::json)->>'name') as host
   from crawl_result_smtp
   where ip_version = 6
   and crawl_status = 0
   and crawl_run = 67
)
select count(distinct host)
from smtp_hosts

   
   
-- unique IP (IPv4):
   
WITH smtp_hosts AS (
   select lower(json_array_elements((json_array_elements(smtp_hosts::json)->>'smtpHostIPs')::json)->>'ip') as addr
   from crawl_result_smtp
   where ip_version = 4
   and crawl_status = 0
   and crawl_run = 67
)
select count(distinct addr)
from smtp_hosts

-- unique IP (IPv6):
   
WITH smtp_hosts AS (
   select lower(json_array_elements((json_array_elements(smtp_hosts::json)->>'smtpHostIPs')::json)->>'ip') as addr
   from crawl_result_smtp
   where ip_version = 6
   and crawl_status = 0
   and crawl_run = 67
)
select count(distinct addr)
from smtp_hosts
```



[1]: https://dmap.sidnlabs.nl
[2]: https://www.sidnlabs.nl/downloads/papers-reports/dmap-tma2018.pdf
[3]: https://www.postgresql.org/
[4]: https:///dmap.sidnlabs.nl/demo/smtp-stats.py



Copyright (C) 2018  SIDN Labs ![alt text][logo]

[logo]: http://entrada.sidnlabs.nl/assets/logo-sidn-labs-50px.png "Copyright (C) 2018  