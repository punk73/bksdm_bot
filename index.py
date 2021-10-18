from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from telegram import sendMessage, getUpdates

def getLatestInfo():
    s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)
    # driver.maximize_window()
    link = "https://bkpsdm.karawangkab.go.id/category/pengumuman/"
    # browser = webdriver.Chrome("C:/Program Files/Google/Chrome/Application/chrome.exe")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(service=s, chrome_options=chrome_options)

    browser.get(link)
    page = browser.page_source

    soup = BeautifulSoup(page, features="lxml")

    a = soup.select('.blog_lists header.entry-header h4 a')
    content = a[0]['href']
    oldLink = "https://bkpsdm.karawangkab.go.id/pengumuman-penjadwalan-ulang-seleksi-kompetensi-dasar-cpns-khusus-peserta-terkonfirmasi-positiv-covid-19-di-lingkungan-pemerintah-kabupaten-karawang-tahun-anggaran-2021/"

    return content

res = getUpdates()
if(res['ok']):
    results = res['result']
    chat_ids = []
    chatDict = {}
    for res in results :
        k = res['message']['chat']['id']
        if(not k in chatDict ):
            chatDict[k] = True
            chat_ids.append(k)

    content = getLatestInfo()

    for chat_id in chat_ids:
        sendMessage(chat_id, content)
