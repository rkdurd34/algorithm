from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
# 1. 다른 컴퓨터에서 매크로 돌릴 시 크롬 드라이버 다운 받은 뒤 경로 수정, 다수 아이디 사용시 아이디,비번 변경
# 2. 예비 수강신청에서 실제 수강 신청으로 홈페이지 주소 바꾸기
print('asda')
driver = webdriver.Chrome('/Users/kang/Downloads/chromedriver')
driver.implicitly_wait(0.05)
print('asdasd')

# driver.get("http://builder.hufs.ac.kr/user/hufs/basket_intro/basket.html")
# sugang_button = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/a/div")
# sugang_button.click()

# # 수강 신청 홈페이지
# window_after = driver.window_handles[1]
# driver.switch_to_window(window_after)
driver.get('http://vsugang2.hufs.ac.kr:8080/sugang/jsp/basket/s_login_go.jsp')
while True:
    login_input_id = driver.find_element_by_name('user_id')
    login_input_password = driver.find_element_by_name('password')
    login_input_id.send_keys('201602809')
    login_input_password.send_keys('970609')
    login_but = driver.find_element_by_xpath("/html/body/div[1]/form/div/div/div[2]/div[1]/p[3]/a[1]")
    login_but.click()
    #  로그인
    driver.switch_to_frame("fra1")
    whole = driver.find_element_by_css_selector('html > body > div:nth-child(5)')
    whole.click()
    
    # print(table)
    count=0
    while count != 15:
        # 장바구니 클릭
        driver.switch_to.default_content()
        driver.switch_to_frame("fra2")
        driver.switch_to_frame("fra2_1")
        button = driver.find_element_by_css_selector('body > center > div > form > table > thead > tr > th:nth-child(5) > button')
        button.click()
        time.sleep(0.01)

    
        driver.switch_to.default_content()
        driver.switch_to_frame("fra2")
        driver.switch_to_frame('fra2_2')
        table = driver.find_elements_by_css_selector("body > center > div > form > table > tbody > tr > td:nth-child(2) > a >img" )
        for i in table:
            # button = i.find_element_by_css_selector("td:nth-child(2) > a > img")
            button = i 
            button.click()  
            da = Alert(driver)
            da.accept()
            time.sleep(0.3)
            try:
                db  = Alert(driver)
            except:
                time.sleep(0.1)
                db = Alert(driver)
            
            db.dismiss()
        count+=1
    # 로그아웃
    driver.switch_to.default_content()
    driver.switch_to_frame("fra1")
    whole = driver.find_element_by_css_selector('html > body > div:nth-child(3)')
    whole.click()
    alert = Alert(driver)
    time.sleep(0.02)
    alert.accept()
    time.sleep(0.02)
    
    


    
driver.quit()
time.sleep(3)








# from selenium import webdriver
# driver = webdriver.Chrome('/Users/kang/Downloads/chromedriver')
# driver.implicitly_wait(1)
# driver.get("file:///Users/kang/Downloads/test_/card.html")
# driver.implicitly_wait(3)
# element1 = driver.find_element_by_class_name('cardContainer') 
# element_png = element1.screenshot_as_png 
# with open("/Users/kang/Downloads/test_/test1.png", "wb") as file: 
#     file.write(element_png)
# driver.quit()