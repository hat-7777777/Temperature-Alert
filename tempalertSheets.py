import gspread, pprint, random, time
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Temperature Data Thing 3: The Party").sheet1
index = 0
temp = ["Yes", "No"]

while True:
    num = random.randint(0,100)
    index += 1
    
    sheet.update_cell(index, 1, num)
    time.sleep(1)
