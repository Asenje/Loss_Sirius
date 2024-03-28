from seleniumbase import Driver
from selenium.webdriver.common.by import By
import json

browser = Driver(uc=True)
browser.get('https://www.vbr.ru/banki/tin_koff-kreditnie-sistemi/otzivy/')

result_data = []

try:

    for page in range(1, 120):
        browser.get(f'https://www.vbr.ru/banki/tin_koff-kreditnie-sistemi/otzivy/{page}/')

        all_text = browser.find_elements(By.CLASS_NAME, "teaser")
        full_all_text = browser.find_elements(By.CLASS_NAME, 'full hidden')


        for i in all_text:
            text = i.text

            result_data.append({
            'text': text
        })

except Exception as ex:
    print(f'Твоя ошибка: {ex}')

finally:
    with open('result_vbr.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file)
