# License Monitoring tool for evaluation of concurrent users for aiding  Maximo Application Suite tradeup decisions
## Authored by Tamas Kubicsek, IBM - 2021.04.20

This solution is intended to be used for anyone with an existing IBM Maximo who is planning to evaluate how many Maximo Application Suite points would be needed at a potential MAS Tradeup.

The tool will place a log into a csv (Excel openable) file every 2 minutes about the logged distinct in users, and also if your environment holds in the Maximo users application
the type field filled in with the license you use, it will also give you the points used at each of these 2 minutes. With that in your spreadsheet you can check what was the 
maximum points used, and which time, or you can further analize your usage.

The tool is not impacting your production environment's performance, it is a small footprint code.

