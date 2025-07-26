from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Şifreni buraya yaz (dikkatli ol, kod içinde şifre saklamak güvenlik riski)
PASSWORD = "password"

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 20)

try:
    browser.get("https://x.com/")

    # Giriş butonuna tıklama
    login_form = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Giriş yap" or text()="Log in"]')))
    login_form.click()

    # Kullanıcı adı girme
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
    username_input.send_keys("username")

    # "İleri" butonunu tıklama
    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[.//span[text()="İleri"]]')))
    print("İleri butonu bulundu ve tıklanıyor...")
    next_button.click()

    # Şifre alanının yüklenmesini bekle
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    print("Şifre alanı bulundu.")

    # Şifreyi otomatik gir
    password_input.send_keys(PASSWORD)

    # Giriş yap butonuna tıklama
    login_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//div[@role="button"]//span[text()="Giriş yap" or text()="Log in"]'
    )))
    login_button.click()
    print("Giriş butonuna tıklandı.")

    # Giriş sonrası kısa bekleme
    time.sleep(5)

except Exception as e:
    print("Hata oluştu:", e)
    browser.save_screenshot("hata_ekrani.png")
    with open("hata_sayfa_kaynagi.html", "w", encoding="utf-8") as f:
        f.write(browser.page_source)
    sys.exit()

finally:
    browser.quit()
