import urllib
import json
from bs4 import BeautifulSoup

# this program parses program codes and rankings 
# of universities from yok tercih sihirbazi

# i used this parser to get program codes 
# and minimum rankings info for 2017
# TODO make it more modular to extract other info

# the page returns json
# TODO make start and puan_turu variables parametric
url_base = "https://yokatlas.yok.gov.tr/server_side/server_processing-atlas2016-TS-t4.php?draw=2&columns[0][data]=0&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=1&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=2&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=3&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=4&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=false&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=5&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=6&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=false&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=7&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=false&columns[7][search][value]=&columns[7][search][regex]=false&columns[8][data]=8&columns[8][name]=&columns[8][searchable]=true&columns[8][orderable]=false&columns[8][search][value]=&columns[8][search][regex]=false&columns[9][data]=9&columns[9][name]=&columns[9][searchable]=true&columns[9][orderable]=false&columns[9][search][value]=&columns[9][search][regex]=false&columns[10][data]=10&columns[10][name]=&columns[10][searchable]=true&columns[10][orderable]=false&columns[10][search][value]=&columns[10][search][regex]=false&columns[11][data]=11&columns[11][name]=&columns[11][searchable]=true&columns[11][orderable]=true&columns[11][search][value]=&columns[11][search][regex]=false&columns[12][data]=12&columns[12][name]=&columns[12][searchable]=true&columns[12][orderable]=true&columns[12][search][value]=&columns[12][search][regex]=false&columns[13][data]=13&columns[13][name]=&columns[13][searchable]=true&columns[13][orderable]=true&columns[13][search][value]=&columns[13][search][regex]=false&columns[14][data]=14&columns[14][name]=&columns[14][searchable]=true&columns[14][orderable]=false&columns[14][search][value]=&columns[14][search][regex]=false&columns[15][data]=15&columns[15][name]=&columns[15][searchable]=true&columns[15][orderable]=false&columns[15][search][value]=&columns[15][search][regex]=false&columns[16][data]=16&columns[16][name]=&columns[16][searchable]=true&columns[16][orderable]=true&columns[16][search][value]=&columns[16][search][regex]=false&columns[17][data]=17&columns[17][name]=&columns[17][searchable]=true&columns[17][orderable]=true&columns[17][search][value]=&columns[17][search][regex]=false&columns[18][data]=18&columns[18][name]=&columns[18][searchable]=true&columns[18][orderable]=true&columns[18][search][value]=&columns[18][search][regex]=false&columns[19][data]=19&columns[19][name]=&columns[19][searchable]=true&columns[19][orderable]=true&columns[19][search][value]=&columns[19][search][regex]=false&columns[20][data]=20&columns[20][name]=&columns[20][searchable]=true&columns[20][orderable]=true&columns[20][search][value]=&columns[20][search][regex]=false&columns[21][data]=21&columns[21][name]=&columns[21][searchable]=true&columns[21][orderable]=true&columns[21][search][value]=&columns[21][search][regex]=false&columns[22][data]=22&columns[22][name]=&columns[22][searchable]=true&columns[22][orderable]=true&columns[22][search][value]=&columns[22][search][regex]=false&columns[23][data]=23&columns[23][name]=&columns[23][searchable]=true&columns[23][orderable]=true&columns[23][search][value]=&columns[23][search][regex]=false&columns[24][data]=24&columns[24][name]=&columns[24][searchable]=true&columns[24][orderable]=true&columns[24][search][value]=&columns[24][search][regex]=false&columns[25][data]=25&columns[25][name]=&columns[25][searchable]=true&columns[25][orderable]=true&columns[25][search][value]=&columns[25][search][regex]=false&columns[26][data]=26&columns[26][name]=&columns[26][searchable]=true&columns[26][orderable]=true&columns[26][search][value]=&columns[26][search][regex]=false&columns[27][data]=27&columns[27][name]=&columns[27][searchable]=true&columns[27][orderable]=false&columns[27][search][value]=&columns[27][search][regex]=false&columns[28][data]=28&columns[28][name]=&columns[28][searchable]=true&columns[28][orderable]=true&columns[28][search][value]=&columns[28][search][regex]=false&columns[29][data]=29&columns[29][name]=&columns[29][searchable]=true&columns[29][orderable]=true&columns[29][search][value]=&columns[29][search][regex]=false&columns[30][data]=30&columns[30][name]=&columns[30][searchable]=true&columns[30][orderable]=true&columns[30][search][value]=&columns[30][search][regex]=false&columns[31][data]=31&columns[31][name]=&columns[31][searchable]=true&columns[31][orderable]=true&columns[31][search][value]=&columns[31][search][regex]=false&columns[32][data]=32&columns[32][name]=&columns[32][searchable]=true&columns[32][orderable]=true&columns[32][search][value]=&columns[32][search][regex]=false&columns[33][data]=33&columns[33][name]=&columns[33][searchable]=true&columns[33][orderable]=true&columns[33][search][value]=&columns[33][search][regex]=false&columns[34][data]=34&columns[34][name]=&columns[34][searchable]=true&columns[34][orderable]=true&columns[34][search][value]=&columns[34][search][regex]=false&order[0][column]=34&order[0][dir]=desc&length=100&search[value]=&search[regex]=false&ust_bs=0&alt_bs=3000000&_=1518169234334&puan_turu=mf4&start=0"


# get the response json page
content = urllib.request.urlopen(url_base)
data = content.read()

# parse it as json
jsonData = json.loads(data.decode('utf-8-sig'))

# for every element 
# print the program code and ranking info
# TODO print info to a csv file
arr_len = len(jsonData['data'])
for i in range(arr_len):
	soup = BeautifulSoup(jsonData['data'][i][1], "html.parser")
	progCode = soup.find("a")
	soup = BeautifulSoup(jsonData['data'][i][19], "html.parser")
	ranking = soup.find("font")
	print("%s:%s" % (progCode.text, ranking.text))


