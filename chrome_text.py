from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 自动下载并匹配正确的 ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get('https://accounts.douban.com/passport/login')
# time.sleep(1)
# driver.switch_to_frame(driver.find_elements_by_tag_name('iframe')[0])
# btm1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/ul[1]/li[2]')
# btm1.click()
# time.sleep(5)
# print(driver.title)
# driver.quit()


# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()  # 确保 chromedriver.exe 在 Python 目录或系统 PATH 中
# driver.get("https://www.baidu.com")
# time.sleep(3)  # 停留3秒，确认浏览器正常打开
# driver.quit()
try:
    # 2. 打开网页
    print("正在打开百度...")
    driver.get("https://accounts.douban.com/passport/login")
    driver.maximize_window()  # 最大化窗口，防止元素被遮挡

    # 2. 【核心步骤 1】定位到 iframe 元素
    # 假设页面上只有一个 iframe，或者你知道它的 ID 是 "login_frame"
    # 建议用 WebDriverWait 等待 iframe 加载完成
    # iframe = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    # )
    #
    # # 3. 【核心步骤 2】切换上下文到 iframe
    # driver.switch_to.frame(iframe)
    # print("已切换到 Iframe 内部")

    # 3. 定位搜索框并输入内容
    # 等待搜索框加载完成（显式等待，比 time.sleep 更智能）
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/ul[1]/li[2]'))
    )
    search_box.click()
    print('转成密码登录')
    # # 输入关键词
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div/input'))
    )
    search_box.send_keys("18144024290")
    print('账号输入成功')

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "app"] / div / div[2] / div / div[2] / div[1] / div[3] / div / input'))
    )
    search_box.send_keys("Jiuyue@11360")
    print('密码输入成功')



    # 4. 点击搜索按钮 (方式一：标准点击)
    # 等待搜索按钮出现
    search_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[4]/a'))
    )


    # 执行点击
    search_btn.click()
    print("搜索按钮已点击 (标准方式)")
    # --- 等待搜索结果加载 ---
    time.sleep(100)
except Exception as e:
    print(f"发生错误: {e}")

# finally:
#     # 6. 关闭浏览器，释放资源
#     driver.quit()
#     print("浏览器已关闭")