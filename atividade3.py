import requests
import struct

url = "https://callback-iot.onrender.com/data"

def decode_hexdata(hex_str):
    data_bytes = bytes.fromhex(hex_str[:24])  
    
    temperature, humidity, pressure = struct.unpack('<fff', data_bytes)
    return temperature, humidity, pressure

def main():
    response = requests.get(url)
    data = response.json()
    
    print("Decodificando dados do endpoint:")
    for item in data:
        if 'hexData' in item:
            hexdata = item['hexData']
            temp, hum, pres = decode_hexdata(hexdata)
            print(f"Temperatura: {temp:.2f} °C")
            print(f"Umidade: {hum:.2f} %")
            print(f"Pressão: {pres:.2f} hPa")
            print("-" * 30)

if __name__ == "__main__":
    main()
