class Target:
    def __init__(self,targetNum):
        self.targetNum = targetNum
        self.tergetANum = 0
        if targetNum < 10:
            self.targetANum = '0' + str(targetNum)
        else:
            self.targetANum = str(targetNum)
        self.latitude = 0
        self.longitude = 0
        self.orientation = 0
        self.shape = ''
        self.targetColor = ''
        self.alpha = ''
        self.alphaColor = ''
        self.img = ''
        print 'Target: ' + str(self.targetNum)

    def getPos(self):
        return self.latitude, self.longitude

    def setPos(self, cx,cy):
        self.latitude = cx
        self.longitude = cy

    def setTargetColor(self, color):
        self.targetColor = color

    def setImg(self, name):
        self.img = name

    def printObj(self):
        print ' ' + str(self.targetANum)
        print ' Lat:' + str(self.latitude) + ' Lon:' + str(self.longitude)
        print ' Color:' + str(self.targetColor)
        print ' File:' + str(self.img)

    def saveObj(self):
        return True
