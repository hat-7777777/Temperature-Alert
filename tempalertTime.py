import gspread, random, time, board, adafruit_dht, statistics
from datetime import datetime
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
        except:
            ## print(error.args[0])
            print("Sensor exception (This is normal, don't panic)")

        time.sleep(2)

while True:
    main()
    if len(temp) == 0:
        out = "-"
    else:
        out = statistics.mean(temp)
    try:
        sheet.update_cell(index, 1, out)
    except:
        print("Something went wrong with updating sheet (Blame Google)")
    moment = datetime.now().strftime('%H:%M:%S')
    sheet.update_cell(index, 2, str(moment))
    index += 1
    print("index =", index)
