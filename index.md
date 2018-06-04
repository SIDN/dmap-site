# [Domain Name Ecosystem Mapper (Dmap)](http://Dmap.sidnlabs.nl)



Dmap is multi-application crawler that *reduces the complexity* in both executing and analyzing measurement data. Taking as input a list of domain names (entire DNS zones even), it does:
   1. *Crawls* the domain for DNS, HTTP, HTTPS, TLS, SMTP and a screenshot (if they are available)
   1. *Converts* the raw measurement data and store into a 166-features unified SQL data model
   3. *Provides a SQL interface* to  the analysis, so analysts do not have to worry about different raw measurement formats
   
More details on our [research paper](paper.pdf).

## Check our [demo page](demo/)

 We have a database dump from Alexa 1M domains, which we cover  our [research paper](paper.pdf).

Please check our [demo page](demo/), which provides both data and data model.

 

## Open for researchers, code and binaries
 
We have developed [Dmap](http://Dmap.sidnlabs.nl) as a project with [SIDN Labs](https://sidnlabs.nl), the research arm of [SIDN](https://sidn.nl), the .nl top-level domain registry.

We are more than happy to make Dmap availble for researchers, both code and binaries. We just would not like to be used commercially. 

Therefore, if you are a reseracher, just do the following:
  1. Send a request to sidnlabs at sidn .nl stating how you intend to use Dmap *using your university/resarch institution* e-mail address. 
  1. We will send you our academic license agreement (Modified Apache 2 License)
  1. Once you send us back, we will quickly process that and give it access to our  [GitHub Repository](https://github.com/SIDN/emap), so you can clone, improve, and use as you want.
     * It includes the complete documentation as well
 
## Why Dmap?
  
  Very often, researchers spend an awful lot of time planning and executing measurements. The complexity of different data formats and issues that may emerge drain energy that could be otherwise be spent on reserach questions.
  
  Dmap is intended to be an enabling platform that free researchers from the complexity of measurements and parsing complex data formats; rather, it automates the measurements and provides a SQL interface o the data. 
  
  
##  More information
For a full description, please [download our research paper (PDF).](paper.pdf)

```
Wullink, M., Moura, G.C. M., Hesselman, C.: Dmap: Automating Domain Name 
Ecosystem Measurements and Applications. In: IFIP/IEEE  Network 
Traffic Measurement and Analysis Conference (TMA 2018).
Vienna, Austria, 26-29 June  2018.
``` 

Copyright (C) 2018  SIDN Labs ![alt text][logo]

[logo]: http://entrada.sidnlabs.nl/assets/logo-sidn-labs-50px.png "Copyright (C) 2018  SIDN Labs"