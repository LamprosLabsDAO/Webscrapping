# Webscrapping
A standard webscrapping tool to fetch the html contents from the websites 

This folder consist of two sub folders and other file : 
Create a input_datas and output_data folders to current directory.
1.get_links   : fetch all the links of topics and sub topics present in the give url docs and sotes in input datas 
2.input_datas : stores all href links in give html page in csv formate 
3.main2.py    : using all the href links which are fetched main2.py outpst the csv data having the url,heading,text,links,code in output.csv file in outut folder  
4.output_datas: stores the webscraped data which is fetched from the web page
5.script.py   : combinly runs the all codes automatically in serial order with given input filename as argumnet. 

you can manually insert the url for required page inside get_link code along with its class name.

note : all the relative href links are included in the follwing code other then that are links of third party websites who data is not need to be fetched 

currently the data of tron docs is stored inside the output_datas folder
