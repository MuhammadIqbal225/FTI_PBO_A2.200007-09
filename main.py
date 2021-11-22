class Hero:

    def __init__(self,name,health,attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    def getName(self):
        return self.__name
        
    def getHealth(self):
        return self.__health

    def diserang(self,serangPower):
        self.__health -= serangPower

earthshaker = Hero("earthshaker",50, 10)

print(earthshaker.getName())
print(earthshaker.getHealth())
earthshaker.diserang(10)
print(earthshaker.getHealth())
      