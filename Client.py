# coding: cp1251
import UakeyClient
import OpenDataBotObject

class Client():
    def __init__(self, UAKey_client : UakeyClient, OPB_client : OpenDataBotObject):
        try:
            if OPB_client != None:
                self.code = OPB_client.code
            else:
                self.code = UAKey_client.code
        except :
            self.code = UAKey_client.code

        try:
            self.name = OPB_client.name
        except :
            self.name = UAKey_client.name

        self.emails = []

        try:
            self.emails.extend(OPB_client.email)
            self.emails.extend(UAKey_client.emails)
        except :
            self.emails.extend(UAKey_client.emails)


        self.phones = OPB_client.phones

        self.registered = OPB_client.registered



