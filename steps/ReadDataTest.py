import csv


class readDatatest:
    #Tra ra du lieu user, pass cua tinh nang login
    def getLoginInfo(self, action):
        links = self.getLink('../linkFile.csv')
        for item in links:  # item is dong

            if item[0] == action:  # item0 la phan tu dau tien cua 1 dong
                _dataTestAll = self.dataTestLogin(item[1])#login là item 0, link file datatest la iteam 1. gan datatest all=gia tri tra ve cua ham datatestlogin
                #gan _dataTestAll = gia tri return datas

                #_dataTest = _dataTestAll[0]
        return _dataTestAll

    #Doc cau hinh va tra ra noi dung file cau hinh
    def getLink(self, link):
        linkFile = []
        with open(link, 'r') as f:
            csv_reader = csv.DictReader(f)
            rows = []
            for row in csv_reader:
                _action = row['Action']
                _link = row['LinkData']
                linkFile.append([_action, _link])
        return linkFile

    #Doc datatest tu link o file cau hinh
    def dataTestLogin(self, linkFile):
        with open(linkFile, 'r', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            print(csv_reader)

            datas = []
            for row in csv_reader:
                _account = row['Account']
                _pass = row['Pass']
                _url = row["url"]
                _title = row["title"]
                datas.append([_account, _pass, _url, _title])
        return datas

