import gspread, random, time, board, adafruit_dht
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
    bruh = "No data"
    try:
        temperature_c = dhtDevice.temperature

        sheet.update_cell(index, 1, temperature_c)
    except RuntimeError as error:
        print(error.args[0])
        sheet.update_cell(index, 1, "-")

    index += 1
    print("index =", index)

while True:
    main()
    time.sleep(10)
