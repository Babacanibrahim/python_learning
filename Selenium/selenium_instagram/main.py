from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome'u gizli modda başlat
chrome_options = Options()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 20)

try:
    browser.get("https://www.instagram.com/")

    # Kullanıcı adı gir
    username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username.send_keys("your_username")

    # Şifre gir
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("your_password")

    # Giriş yap butonuna tıkla
    login_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div'
    )))
    login_button.click()

    # Profil fotoğrafı yüklenene kadar bekle ve tıkla
    profile = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[alt*="profil resmi"]')))
    profile.click()

    # "Takip" linkine tıkla
    followers_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//a[contains(@href, "/following/")]')
    ))
    followers_link.click()

    # Scroll edilebilir alanı bekle (class arayüz değişebilir!)
    scroll_box = wait.until(EC.presence_of_element_located((
        By.XPATH, '//div[@role="dialog"]//div[contains(@class, "_aano")]'
    )))

    # Scroll yaparak tüm kullanıcıları yükle
    last_height, same_count = 0, 0
    max_same = 5

    while True:
        browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
        time.sleep(1)
        new_height = browser.execute_script("return arguments[0].scrollTop", scroll_box)

        if new_height == last_height:
            same_count += 1
            if same_count >= max_same:
                break
        else:
            same_count = 0
            last_height = new_height

    # Kullanıcı adlarını al
    users = scroll_box.find_elements(By.XPATH, './/a[contains(@href, "/") and not(contains(@href, "/following/"))]')
    usernames = [u.text.strip() for u in users if u.text.strip()]

    print(f"\nToplam {len(usernames)} kullanıcı bulundu:")
    for name in usernames:
        print(name)

except Exception as e:
    print("Hata oluştu:", e)
    browser.save_screenshot("hata_ekrani.png")

finally:
    input("\nDevam etmek için Enter'a basın...")
    browser.quit()
