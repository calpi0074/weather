import requests
import time

current_date = time.strftime('%Y%m%d')

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params = {
    'serviceKey': 'qfJEhWmlC3B5Q/f44N5F1LV+/EyWYTh4SkFwMQoaNsV3se26CAiwuGfD42mT7O8vRe+/DkwTgG5OAB7wJAFx6A==',
    'pageNo': '1',
    'numOfRows': '1000',
    'dataType': 'JSON',
    'base_date': current_date,
    'base_time': '0600',
    'nx': '61',
    'ny': '127'
}

response = requests.get(url, params=params)
data = response.json()

if data['response']['header']['resultCode'] == "00":
    items = data['response']['body']['items']['item']

    weather_data = {}
    for item in items:
        category = item['category']
        if category in ['PTY', 'UUU', 'VVV', 'VEC', 'WSD']:
            weather_data[category] = item['obsrValue']
    print("PTY (강수 형태):", weather_data.get('PTY'))
    print("UUU (동서 바람 성분):", weather_data.get('UUU'), "m/s")
    print("VVV (남북 바람 성분):", weather_data.get('VVV'), "m/s")
    print("VEC (풍향):", weather_data.get('VEC'), "도 (북측 기준 시계방향)")
    print("WSD (풍속):", weather_data.get('WSD'), "m/s")
else:
    print("Error: ", data['response']['header']['resultMsg'])

                                                                  
