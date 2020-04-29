from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get('https://instagram.com')
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(6)
    

        self.driver.find_element_by_xpath("//button[contains(text(), 'Enviar código de segurança')]").click()
        sleep(5)
        sleep(60)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        sleep(5)

        # if self.driver.find_element_by_xpath("//a[contains(text(), 'Conecte-se')]"):
        #     self.driver.find_element_by_xpath("//a[contains(text(), 'Conecte-se')]").click()
        #     sleep(2)
            
        #     self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
        #         .send_keys(username)
        #     self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
        #         .send_keys(pw)
        #     self.driver.find_element_by_xpath('//button[@type="submit"]')\
        #         .click()
        #     sleep(4)
        #     self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        #     sleep(5)
        # else:

            
    def unfollow(self, user):
        print('Unfollowing->', user)
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')\
            .send_keys(user)
        sleep(5)
        print('Clicando no perfil ->', user)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(user))\
            .click()
        sleep(5)
        print('Deixando de seguir: ', user)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
    
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
        print('Deixou de seguir: ', user)


    def get_unfollowers(self):
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}/')]".format(self.username))\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        print("Following: ", following)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        print("Followers: ", followers)
        not_following_back = [user for user in following if user not in followers]
        print("Não estão me seguindo de volta:", not_following_back)
        for user2 in not_following_back:
            print(user)
            # sleep(2)
            # self.unfollow(user)
            # sleep(2)
        print("Processo finalizado com sucesso!")

    

    
    # private method
    def _get_names(self):
        sleep(3)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Sugestões)]')
        self.driver.execute_script('arguments[0].scrollIntoView()',sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        #close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names


        

print ("Insira seu username de login (Nao pode ser o email)")
username = input("login: ")
pw = input("Agora sua senha: ")
bot = InstaBot(username,pw)
bot.get_unfollowers()