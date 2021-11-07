import os
import time
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
imgdir = "../dataset"
a = "%20".join(input("크롤링할 이미지 입력: ").split())
label = input("레이블 입력: ")
b = int(input("받을 이미지 개수: "))
d = int(input("시작 인덱스 입력: "))
print("시작 중...")
driver = webdriver.Chrome(options=opt)
driver.get(f"https://www.google.com/search?q={a}&tbm=isch")
done = False
elem = driver.find_element(By.TAG_NAME, "body")
print("이미지 스캔 중...", end='')
# for i in range(200):
#     cnt += 1
#     elem.send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.01)
# try:
#     driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
# except:
#     for i in range(50):
#         cnt += 1
#         elem.send_keys(Keys.PAGE_DOWN)
#         time.sleep(0.01)
#     driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
links = []
images = []
cnt = 1
while cnt <= b:
    if cnt % 40 == 0:
        for i in range(10):
            try:
                driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.01)
            except:
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.01)
    if cnt % 25 == 0 or (
            driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{cnt}]/a[1]/div[1]/img').get_attribute(
                    'src') is None):
        b += 1
    else:
        images.append(driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{cnt}]/a[1]/div[1]/img'))
    cnt += 1

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print(f"찾은 이미지 개수: {len(links)}개")
try:
    os.mkdir(f"../datasets/{label}/")
except:
    pass
for k, i in enumerate(links):
    urlretrieve(i, f"../datasets/{label}/{label}_{k + d}.jpg")
    print(f"\r{round((k + 1) * 100 / len(links), 2)}% 완료됨", end='  ')
    print("[" + "=" * ((k + 1) * 30 // len(links)) + "." * (30 - ((k + 1) * 30 // len(links))) + "]", end='')
    if k < 50:
        time.sleep(0.001)
    