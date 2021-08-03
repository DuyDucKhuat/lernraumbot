import account
import lernraum
import time
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pause
from datetime import datetime
from selenium.webdriver.common.keys import Keys


class CheckOutBot:
    def __init__(self, roomselection):
        if roomselection == "bib1vormittags":
            ID = lernraum.bib1vormittags
        elif roomselection == "bib1nachmittags":
            ID = lernraum.bib1nachmittags
        elif roomselection == "bib2vormittags":
            ID = lernraum.bib2vormittags
        elif roomselection == "bib2nachmittags":
            ID = lernraum.bib2nachmittags
        elif roomselection == "semi90nachmittags":
            ID = lernraum.semi90nachmittags
        elif roomselection == "semi90vormittags":
            ID = lernraum.semi90vormittags

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=option)
        self.driver.get("https://buchung.hsz.rwth-aachen.de/angebote/aktueller_zeitraum/_Lernraumbuchung.html")
        self.driver.find_element_by_name(ID).click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_xpath("//*[@id=\"bs_form_main\"]/div/div[2]/div[1]/label/div[2]/input").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_id("bs_pw_anmlink").click()

    def login(self, email, password):
        # time.sleep(2)
        email_input = self.driver.find_element_by_name("pw_email")
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.driver.find_element_by_xpath("//*[@id=\"bs_pw_anm\"]/div[3]/div[2]/input")
        password_input.clear()
        password_input.send_keys(password)
        self.driver.find_element_by_xpath("//*[@id=\"bs_pw_anm\"]/div[5]/div[1]/div[2]/input").click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_xpath("//*[@id=\"bs_bed\"]/label/input").click()
        self.driver.find_element_by_xpath("//*[@id =\"bs_foot\"]/div[3]/div[2]/input").click()
        # self.driver.get_screenshot_as_file('mainbib' + email + ' .png')
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element_by_xpath("//*[@id=\"bs_foot\"]/div[1]/div[2]/input").click()
        # self.driver.get_screenshot_as_file('mainbib1' + email + ' .png')
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.get_screenshot_as_file('mainbib2' + email + ' .png', "confirmations")
        # print("successfull!")
        # time.sleep(2)

    def loginfromdata(self, accnumber):
        if accnumber == "1":
            self.login(account.email, account.password)
        if accnumber == "2":
            self.login(account.email2, account.password2)
        if accnumber == "3":
            self.login(account.email3, account.password3)
        if accnumber == "4":
            self.login(account.email4, account.password4)
        if accnumber == "5":
            self.login(account.email5, account.password5)
        if accnumber == "6":
            self.login(account.email6, account.password6)
        if accnumber == "7":
            self.login(account.email7, account.password7)
        if accnumber == "8":
            self.login(account.email8, account.password8)


if __name__ == "__main__":
    d = datetime.today()
    roomselection = sys.argv[1]
    if roomselection.endswith('vormittags'):
        pause.until(datetime(d.year, d.month, d.day, 7, 59, 59))
    else:
        pause.until(datetime(d.year, d.month, d.day, 13, 59, 59))
    checkout_bot = CheckOutBot(roomselection)
    if len(sys.argv) > 1:
        accnumber = sys.argv[2]
        checkout_bot.loginfromdata(accnumber)
    else:
        checkout_bot.login(account.email, account.password)
        # time.sleep(20)
