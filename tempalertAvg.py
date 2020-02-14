import gspread, random, time, board, adafruit_dht, statistics
from oauth2client.service_account import ServiceAccountCredentials

global dhtDevice

index = 1
scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Temperature Data Thing 3: The Party").sheet1
dhtDevice = adafruit_dht.DHT11(board.D17)

def main():
    global index
    global out
    global temp
    temp = []
    for x in range(0,5):
        try:
            temperature_c = dhtDevice.temperature
            temp.append(temperature_c)
        except RuntimeError as error:
            print(error.args[0])
            ## temp.append(None)
        time.sleep(10)

while True:
    main()
    out = statistics.mean(temp)
    sheet.update_cell(index, 1, out)
    index += 1
    print("index =", index)
