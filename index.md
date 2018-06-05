# [Dmap: Domain Name Ecosystem Mapper](http://dmap.sidnlabs.nl)

![Orbis Terrarum Nova et Accuratissima Tabula by Nicolaes Visscher, 1658, https://en.wikipedia.org/wiki/File:Orbis_Terrarum_Nova_et_Accuratissima_Tabula_by_Nicolaes_Visscher,_1658.jpg](img/map2.jpg)


Dmap is multi-application crawler that *reduces the complexity* in both executing Internet measurements and analyzing their results.

Dmap takes as input a list domain names (entire DNS zones even), and:
   1. *Crawls* domains for DNS, HTTP, HTTPS, TLS, SMTP and a generates a screenshot of a webpage (if it's available)
   1. *Converts* the raw measurement data and store into a 166-features unified SQL data model, so users can easily and convienlty analyze the results using SQL.
 

Just run it and query it. More details on our [research paper](paper.pdf).

## [Demo data page](demo/)

 We have a database dump from Alexa 1M domains, which we cover  our [research paper](paper.pdf).
Please check our [demo data page](demo/), which provides both data and data model.


## How to get it
 
We have developed [Dmap](http://dmap.sidnlabs.nl) as a project with [SIDN Labs](https://sidnlabs.nl), the research arm of [SIDN](https://sidn.nl), the .nl top-level domain registry.

We are more than happy to make Dmap availble for researchers, both code and binaries. We just would not like it to be used commercially. 

Therefore, if you are a reseracher, just do the following:
  1. Send a request to sidnlabs at sidn .nl with the following information:
     * Name
     * University/Research Center/Research Group
     * Your e-mail address (from your University/Research Center) 
        * No Gmail, Yahoo  and similar please.
     * Github account name (for activation)
  1. We will send you our academic license agreement (Modified Apache 2 License)
  1. Once you send it back to us, we will quickly process that and give you full access to our  [GitHub Repository](https://github.com/SIDN/emap).
 
 
##  [Data Model (from raw data to SQL)](datamodel/)
  Very often, researchers spend an awful lot of time planning and executing measurements. The complexity of different data formats and issues that may emerge drain energy that could be otherwise be spent on research questions.
  
  Dmap is intended to be an enabling platform that free researchers from the complexity of measurements and parsing complex data formats; rather, it automates the measurements and provides a SQL interface o the data. 
  
  Want to give at try? Check our [data demo](demo/) page and the  [our data model page](datamodel/) data shows how the results are stored in the SQL database.
  
##  [Research paper](paper.pdf)

For a full description, please [download our research paper (PDF).](paper.pdf)

```
Wullink, M., Moura, G.C. M., Hesselman, C.: Dmap: Automating Domain Name
Ecosystem Measurements and Applications. In: IFIP/IEEE  Network Traffic 
Measurement and Analysis Conference (TMA 2018). 
Vienna, Austria, 26-29 June  2018.
``` 

Copyright (C) 2018  SIDN Labs ![alt text][logo]

[logo]: http://entrada.sidnlabs.nl/assets/logo-sidn-labs-50px.png "Copyright (C) 2018  SIDN Labs"