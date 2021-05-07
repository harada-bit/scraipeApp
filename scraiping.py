import requests
from bs4 import BeautifulSoup


class URL_SCR:
    def __init__(self):
        self.element_list = []
    def url_scraipe(self,load_url,bunrui):
        self.load_url = load_url
        self.bunrui = bunrui
        print(self.bunrui)


        html = requests.get(self.load_url)
        soup = BeautifulSoup(html.content, "html.parser")


        if "class_" in self.bunrui["dai_list"]:
            topic = soup.find(class_=self.bunrui["dai_text"])
        elif "id" in self.bunrui["dai_list"]:
            topic = soup.find(id=self.bunrui["dai_text"])
        elif "href" in self.bunrui["dai*"]:
            topic = soup.find(href=self.bunrui["sho_text"])


        if "class_" in self.bunrui["sho_list"]:
            for element in topic.find_all(class_=self.bunrui["sho_text"]):
                self.element_list.append(element.text)
        elif "id" in self.bunrui["sho_list"]:
            for element in topic.find_all(id=self.bunrui["sho_text"]):
                self.element_list.append(element.text)
        elif "href" in self.bunrui["sho_list"]:
            for element in topic.find_all(href=self.bunrui["sho_text"]):
                self.element_list.append(element.text)
        elif "a" in self.bunrui["sho_list"]:
            for element in topic.find_all("a"):
                self.element_list.append(element.text)
