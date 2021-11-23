from bs4 import BeautifulSoup
import requests


def find_stocks():
    html_text = requests.get('https://finance.yahoo.com/screener/predefined/day_losers').text      #retrieve the sites html code in text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find_all('tr', class_='simpTblRow')                            #creating a variable for the table. match the label 'tr' accordingly and the class.
    for stock_pick in table:                                                    #going through each row in the table
        ticker = stock_pick.find('a', class_='Fw(600) C($linkColor)').text      #creating a variable for the ticker symbol since the class id different than the column
        columns = stock_pick.find_all('span', class_='Trsdu(0.3s)')             #creating a variable slot for the price, % change and the volume
        element_list = []                                                       #creating a shell list to input the column elements
        for elements in columns:                                                #going through each column that matches the ids specified in columns
            element_list.append(elements)                                       #adding each element that matches the columns specified criteria to the element_list
            if len(element_list) == 5:                                          #since the elements in the list are added 1 by 1, i wait until the list retrieves all the elements from the row then I manipulate accordingly
                price = float(element_list[0].text)                             #pulls the price variable from the list
                percent_change = float(element_list[2].text.replace('%', ''))   #pulls the price % change from the list
                volume = element_list[3].text                                   #pulls the price volume from the list, this was tricky because i had millions which had the M and . , then less than 1M it only had a ,

                def convert_volume(vol):                                        #the purpose of this function is to intake the volume from the site and spit out an integer
                    if 'M' in vol:                                              #checking if the volume is in the millions
                        vol = vol.replace('.', '')                              #removing the period, because you cant have an integer with a .
                        vol = vol.replace('M', '')                              #removing the M, because you cant have an integer with a M
                        vol = int(vol) * 1000                                   #since the volume was missing 3 zeros, i added them here. and i converted the vol to int because you cant do math on a string
                        return vol                                              #spits out volume if in millions
                    else:
                        vol = vol.replace(',', '')                              #removing the M, because you cant have an integer with a ,
                        return int(vol)                                         #returning the value, i converted the vol to int because you cant do math on a string

                if price > 50 and percent_change < -5 and convert_volume(volume) > 500000:      #specify what you want to see
                    print('Stock: ' + str(ticker) + '\nPrice: ' + str(price) + '\n% Change: ' + str(
                        percent_change) + '\nVolume: ' + str(convert_volume(volume)) + '\n')


find_stocks()



