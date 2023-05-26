import requests
import json


def get_data():


    cookies = {
        '__lhash_': '8796cbf2af22642b3b5e6b2e2c84281c',
        'MVID_ACTOR_API_AVAILABILITY': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_COOKIE': '2500',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLC': 'true',
        'MVID_GLP': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        '_gid': 'GA1.2.1551530942.1683288469',
        '_ym_uid': '1683288469980926888',
        '_ym_d': '1683288469',
        '__SourceTracker': 'yandex.ru__organic',
        'admitad_deduplication_cookie': 'yandex.ru__organic',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '68ee7eeaf4af3a4f2c050e05d8545840',
        'tmr_lvidTS': '1683288472086',
        'advcake_track_id': '69ba190f-f769-cfba-14ce-96b4d450a6e5',
        'advcake_session_id': '2300280c-86f1-05fd-9c80-e13f901e9021',
        'uxs_uid': '75ecd0a0-eb3d-11ed-8297-4bfb23a170e9',
        'adrcid': 'AQdCpX5c4LrEiK6cNNqE63A',
        'flocktory-uuid': '59282af3-193f-4783-8fcd-e9f351929499-2',
        'afUserId': '84332e30-9958-4575-919e-4374f24ff693-p',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1225055242.20480.0000',
        'bIPs': '1081167284',
        'AF_SYNC': '1683288472794',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '50a91038-6029-4176-b337-45b43be1abb1',
        '_ym_isad': '2',
        '__hash_': '90616e5fcffc2baf575f05afeb71134c',
        'mindboxDeviceUUID': '75bfd537-7481-40eb-a6f5-3382eaf4e23b',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2275bfd537-7481-40eb-a6f5-3382eaf4e23b%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_sp_ses.d61c': '*',
        '_sp_id.d61c': '40312e38-96e7-4808-9f8e-3c036a47c1dc.1683288469.6.1683395021.1683372999.eff2cc1d-0176-4ad2-9517-162569e099cc.db6916e4-c388-42ba-b382-73f58d3f88c7.8cd92360-12c3-4abe-b217-e76549d6b43e.1683395018256.7',
        '_ga': 'GA1.2.1000008493.1683288469',
        '_dc_gtm_UA-1873769-37': '1',
        'tmr_detect': '0%7C1683395024119',
        '_ga_BNX5WPP3YK': 'GS1.1.1683395018.5.0.1683395048.30.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1683395018.5.0.1683395048.0.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1c8b91648e28448dbd0e3b5ed9f12514,sentry-sample_rate=0.5',
        # 'cookie': '__lhash_=8796cbf2af22642b3b5e6b2e2c84281c; MVID_ACTOR_API_AVAILABILITY=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CART_AVAILABILITY=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_COOKIE=2500; MVID_CREDIT_AVAILABILITY=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; _gid=GA1.2.1551530942.1683288469; _ym_uid=1683288469980926888; _ym_d=1683288469; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; SMSError=; authError=; tmr_lvid=68ee7eeaf4af3a4f2c050e05d8545840; tmr_lvidTS=1683288472086; advcake_track_id=69ba190f-f769-cfba-14ce-96b4d450a6e5; advcake_session_id=2300280c-86f1-05fd-9c80-e13f901e9021; uxs_uid=75ecd0a0-eb3d-11ed-8297-4bfb23a170e9; adrcid=AQdCpX5c4LrEiK6cNNqE63A; flocktory-uuid=59282af3-193f-4783-8fcd-e9f351929499-2; afUserId=84332e30-9958-4575-919e-4374f24ff693-p; flacktory=no; BIGipServeratg-ps-prod_tcp80=1225055242.20480.0000; bIPs=1081167284; AF_SYNC=1683288472794; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=50a91038-6029-4176-b337-45b43be1abb1; _ym_isad=2; __hash_=90616e5fcffc2baf575f05afeb71134c; mindboxDeviceUUID=75bfd537-7481-40eb-a6f5-3382eaf4e23b; directCrm-session=%7B%22deviceGuid%22%3A%2275bfd537-7481-40eb-a6f5-3382eaf4e23b%22%7D; _dc_gtm_UA-1873769-1=1; _sp_ses.d61c=*; _sp_id.d61c=40312e38-96e7-4808-9f8e-3c036a47c1dc.1683288469.6.1683395021.1683372999.eff2cc1d-0176-4ad2-9517-162569e099cc.db6916e4-c388-42ba-b382-73f58d3f88c7.8cd92360-12c3-4abe-b217-e76549d6b43e.1683395018256.7; _ga=GA1.2.1000008493.1683288469; _dc_gtm_UA-1873769-37=1; tmr_detect=0%7C1683395024119; _ga_BNX5WPP3YK=GS1.1.1683395018.5.0.1683395048.30.0.0; _ga_CFMZTSS5FM=GS1.1.1683395018.5.0.1683395048.0.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?f_category=noutbuki-987&f_brand=lenovo&f_skidka=da&f_tolko-v-nalichii=da',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '1c8b91648e28448dbd0e3b5ed9f12514-ba8b88adc656d548-0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.751 Yowser/2.5 Safari/537.36',
        'x-set-application-id': '6452d179-428b-4a2f-ad67-d3ac9015e10b',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJjYXRlZ29yeSIsIiIsIm5vdXRidWtpLTk4NyJd',
            'WyJicmFuZCIsIiIsImxlbm92byJd',
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()

    products_ids = response.get('body').get('products')
    
    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
        
    # print(len(response.get('body').get('products')))
    
    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': '30066789,30065399,30064660,30065769,30065694,30066706,30066705,30066574,30065988,30064625,30055123,30057546,30060110,30054781,30065297,30065908,30066485,30065767,30066486,30065398,30065279,30065620,30065290,30066090',
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    
    items_prices = {}
    
    material_prices = response.get('body').get('materialPrices')
    
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')
        
        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
        
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)
    
    
def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)
        
    products_data = products_data.get('body').get('products')
    
    for item in products_data:
        product_id = item.get('productId')
        
        if product_id in products_prices:
            prices = products_prices[product_id]
            
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
        
    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)
    

def main():
    get_data()
    get_result()
    
    
if __name__ == '__main__':
    main()