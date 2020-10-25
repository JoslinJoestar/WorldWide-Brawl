import pygame
from PIL import Image
import math
import random
pygame.init()
#font = pygame.font.SysFont('comicsans', 30, True)

#walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
#walkRight=[pygame.image.load("jamw11.png"),pygame.image.load("jamw21.png"),pygame.image.load("jamw3.png"),pygame.image.load("jamw3.png"),pygame.image.load("jamw51.png"),pygame.image.load("jamw61.png"),pygame.image.load("jamw71.png")]#
walkRight=[pygame.image.load("lw1.png"),pygame.image.load("lw2.png"),pygame.image.load("lw3.png"),pygame.image.load("lw4.png"),pygame.image.load("lw5.png"),pygame.image.load("lw6.png"),pygame.image.load("lw7.png")]
walkLeft=[pygame.image.load("lwr1.png"),pygame.image.load("lwr2.png"),pygame.image.load("lwr3.png"),pygame.image.load("lwr4.png"),pygame.image.load("lwr5.png"),pygame.image.load("lwr6.png"),pygame.image.load("lwr7.png")]
luffAttack=[pygame.image.load("la12.png"),pygame.image.load("la13.png"),pygame.image.load("la14.png")]
luffAttack2=[pygame.image.load("la21.png"),pygame.image.load("la22.png"),pygame.image.load("la23.png"),pygame.image.load("la24.png"),pygame.image.load("la25.png"),pygame.image.load("la26.png"),pygame.image.load("la27.png"),pygame.image.load("la28.png"),pygame.image.load("la29.png")]
luffAttack3=[pygame.image.load("la31.png"),pygame.image.load("la32.png"),pygame.image.load("la33.png"),pygame.image.load("la34.png"),pygame.image.load("la35.png"),pygame.image.load("la36.png"),pygame.image.load("la37.png"),pygame.image.load("la38.png")]
luffAttack4=[pygame.image.load("la41.png"),pygame.image.load("la42.png"),pygame.image.load("la43.png"),pygame.image.load("la44.png"),pygame.image.load("la45.png"),pygame.image.load("la46.png"),pygame.image.load("la47.png"),pygame.image.load("la48.png"),pygame.image.load("la49.png"),pygame.image.load("la410.png"),pygame.image.load("la411.png"),pygame.image.load("la4111.png"),pygame.image.load("la412.png"),pygame.image.load("la4121.png"),pygame.image.load("la411.png"),pygame.image.load("la4131.png"),pygame.image.load("la413.png"),pygame.image.load("la414.png"),pygame.image.load("la415.png")]
AmwalkRight=[pygame.image.load("amwr1.png"),pygame.image.load("amwr2.png"),pygame.image.load("amwr3.png"),pygame.image.load("amwr4.png"),pygame.image.load("amwr5.png"),pygame.image.load("amwr6.png"),pygame.image.load("amwr7.png"), pygame.image.load("amwr8.png")]
AmwalkLeft=[pygame.image.load("amwl1.png"),pygame.image.load("amwl2.png"),pygame.image.load("amwl3.png"),pygame.image.load("amwl4.png"),pygame.image.load("amwl5.png"),pygame.image.load("amwl6.png"),pygame.image.load("amwl7.png"),pygame.image.load("amwl8.png")]
AmAttack=[pygame.image.load("ama11.png"),pygame.image.load("ama12.png"),pygame.image.load("ama13.png")]
AmAttack2=[pygame.image.load("ama21.png"),pygame.image.load("ama22.png"),pygame.image.load("ama23.png"),pygame.image.load("ama24.png"),pygame.image.load("ama25.png")]
AmAttack3=[pygame.image.load("ama31.png"),pygame.image.load("ama32.png"),pygame.image.load("ama33.png")]
AmAttack4=[pygame.image.load("ama41.png"),pygame.image.load("ama42.png"),pygame.image.load("ama43.png"),pygame.image.load("ama44.png"),pygame.image.load("ama45.png"),pygame.image.load("ama46.png")]
AmrAttack=[pygame.image.load("amar11.png"),pygame.image.load("amar12.png"),pygame.image.load("amar13.png")]
AmrAttack2=[pygame.image.load("amar21.png"),pygame.image.load("amar22.png"),pygame.image.load("amar23.png"),pygame.image.load("amar24.png"),pygame.image.load("amar25.png")]
AmrAttack3=[pygame.image.load("amar31.png"),pygame.image.load("amar32.png"),pygame.image.load("amar33.png")]
AmrAttack4=[pygame.image.load("amar41.png"),pygame.image.load("amar42.png"),pygame.image.load("amar43.png"),pygame.image.load("amar44.png"),pygame.image.load("amar45.png"),pygame.image.load("amar46.png")]
hitEffect1=[pygame.image.load("hit1.png"),pygame.image.load("hit2.png"),pygame.image.load("hit3.png"),pygame.image.load("hit4.png"),pygame.image.load("hit5.png"),pygame.image.load("hit6.png"),pygame.image.load("hit7.png")]
hitEffect2=[pygame.image.load("hit21.png"),pygame.image.load("hit22.png"),pygame.image.load("hit23.png"),pygame.image.load("hit24.png")]
luffAttackL=[pygame.image.load("lal12.png"),pygame.image.load("lal13.png"),pygame.image.load("lal14.png")]
luffAttackL2=[pygame.image.load("lal21.png"),pygame.image.load("lal22.png"),pygame.image.load("lal23.png"),pygame.image.load("lal24.png"),pygame.image.load("lal25.png"),pygame.image.load("lal26.png"),pygame.image.load("lal27.png"),pygame.image.load("lal28.png"),pygame.image.load("lal29.png")]
luffAttackL3=[pygame.image.load("lal31.png"),pygame.image.load("lal32.png"),pygame.image.load("lal33.png"),pygame.image.load("lal34.png"),pygame.image.load("lal35.png"),pygame.image.load("lal36.png"),pygame.image.load("lal37.png"),pygame.image.load("lal38.png")]
luffUlt=[pygame.image.load("lu1.png"),pygame.image.load("lu2.png"),pygame.image.load("lu3.png"),pygame.image.load("lu4.png"),pygame.image.load("lu5.png"),pygame.image.load("lu6.png"),pygame.image.load("lu7.png"),pygame.image.load("lu8.png"),pygame.image.load("lu9.png"),pygame.image.load("lu10.png"),pygame.image.load("lu11.png"),pygame.image.load("lu12.png"),pygame.image.load("lu13.png"),pygame.image.load("lu14.png"),pygame.image.load("lu15.png"),pygame.image.load("lu16.png"),pygame.image.load("lu17.png"),pygame.image.load("lu18.png"),pygame.image.load("lu19.png"),pygame.image.load("lu20.png"),pygame.image.load("lu21.png"),pygame.image.load("lu22.png"),pygame.image.load("lu23.png"),pygame.image.load("lu24.png"),pygame.image.load("lu25.png"),pygame.image.load("lu26.png"),pygame.image.load("lu27.png"),pygame.image.load("lu28.png"),pygame.image.load("lu29.png"),pygame.image.load("lu30.png"),pygame.image.load("lu31.png"),pygame.image.load("lu32.png"),pygame.image.load("lu33.png"),pygame.image.load("lu34.png"),pygame.image.load("lu35.png"),pygame.image.load("lu36.png"),pygame.image.load("lu37.png"),pygame.image.load("lu38.png"),pygame.image.load("lu39.png"),pygame.image.load("lu40.png"),pygame.image.load("lu41.png"),pygame.image.load("lu42.png")]
luffUlt2=luffUlt[14:18]
luffAttackL4=[pygame.image.load("lal41.png"),pygame.image.load("lal42.png"),pygame.image.load("lal43.png"),pygame.image.load("lal44.png"),pygame.image.load("lal45.png"),pygame.image.load("lal46.png"),pygame.image.load("lal47.png"),pygame.image.load("lal48.png"),pygame.image.load("lal49.png"),pygame.image.load("lal410.png"),pygame.image.load("lal411.png"),pygame.image.load("lal4111.png"),pygame.image.load("lal412.png"),pygame.image.load("lal4121.png"),pygame.image.load("lal411.png"),pygame.image.load("lal4131.png"),pygame.image.load("la413.png"),pygame.image.load("lal414.png"),pygame.image.load("lal415.png")]
AmFall=pygame.image.load("AmFd1.png")#,pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd2.png"),pygame.image.load("AmFd2.png")]
AmFalll=pygame.image.load("AmFd1l.png")#,pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd1.png"),pygame.image.load("AmFd2.png"),pygame.image.load("AmFd2.png")]
LuffFall=pygame.image.load("LuffFall.png")
LuffFalll=pygame.image.load("LuffFalll.png")
LuffGetUp=[pygame.image.load("lgu1.png"),pygame.image.load("lgu2.png"),pygame.image.load("lgu3.png"),pygame.image.load("lgu4.png"),pygame.image.load("lgu5.png")]
LuffGetUpR=[pygame.image.load("lgu1r.png"),pygame.image.load("lgu2r.png"),pygame.image.load("lgu3r.png"),pygame.image.load("lgu4r.png"),pygame.image.load("lgu5r.png")]
AmGetUp=[pygame.image.load("amgu1.png"),pygame.image.load("amgu2.png"),pygame.image.load("amgu3.png"),pygame.image.load("amgu4.png"),pygame.image.load("amgu5.png"),pygame.image.load("amgu6.png"),pygame.image.load("amgu7.png"),pygame.image.load("amgu8.png"),pygame.image.load("amgu9.png")]
AmGetUpl=[pygame.image.load("amgu1l.png"),pygame.image.load("amgu2l.png"),pygame.image.load("amgu3l.png"),pygame.image.load("amgu4l.png"),pygame.image.load("amgu5l.png"),pygame.image.load("amgu6l.png"),pygame.image.load("amgu7l.png"),pygame.image.load("amgu8l.png"),pygame.image.load("amgu9l.png")]
fallExp=[pygame.image.load("fallexplosion1.png"),pygame.image.load("fallexplosion2.png"),pygame.image.load("fallexplosion3.png"),pygame.image.load("fallexplosion4.png"),pygame.image.load("fallexplosion5.png"),pygame.image.load("fallexplosion6.png"),pygame.image.load("fallexplosion7.png")]
AmHit=pygame.image.load("Amh.png")
LuBg=pygame.image.load("G4.png")
AmHitL=pygame.image.load("Amhl.png")
LuffHit=pygame.image.load("luffhit.png")
LuffHitR=pygame.image.load("luffhitr.png")
Aml=pygame.image.load("aml.png")
Amr=pygame.image.load("amr.png")
bg=pygame.image.load("opbg.png")
#musicCount=0
#earth=pygame.image.load("earth.png")
Titlemusic=pygame.mixer.music.load('title.mp3')
Amhp=pygame.image.load("amhp.jpg")
lfhp=pygame.image.load("lfhp.jpg")
#char= pygame.image.load('standing.png')
leftImage=pygame.image.load("lsl.png")
#rightImage=pygame.image.load("jamw71.png")#
rightImage=pygame.image.load("lsr.png")
#Gamemusic = pygame.mixer.music.load('music.mp3')
GGpistol=pygame.mixer.Sound("pistol.wav")
KKGun=pygame.mixer.Sound("luaudio.wav")
storm=pygame.mixer.Sound("storm.wav")
egun=pygame.mixer.Sound("egun.wav")
sound3=pygame.mixer.Sound("3.wav")
AmLaugh=pygame.mixer.Sound("AmLaugh.wav")
AmShout=pygame.mixer.Sound("AmShout.wav")
Amsmash=pygame.mixer.Sound("smash.wav")
fallExpSound=pygame.mixer.Sound("fallExp.wav")
punch=pygame.mixer.Sound("punch.wav")
titleScreen=pygame.image.load("Title.png")
#jamMenu=pygame.image.load("JamMenu.png")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


def returnImageSize(image):
    #fileName=image
    width, height = Image.open(image).size
    return width,height
   
        

class player():
    
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=8
        self.Left=False
        self.Right=False
        self.standing=True
        self.wasLeft=False
        self.wasRight=True
        self.walkCount=0
        self.attack=False
        self.attackNum=0
        self.attackCount=0
        self.attackDone=False
        self.justAttacked=False
        self.hit=False
        self.hitCount=0
        self.hitImage=LuffHit
        self.hitSide=None
        self.hitCount=0
        self.fallCount=0
        self.fallYList=[]
        self.fallXList=[]
        self.Fall=False
        self.fallCount=0
        self.backUp=False
        self.backUpCount=0
        self.startFall=False
        self.fallCheck=False
        self.fallExpCount=0
        self.damage=0
        self.health=200
        player.ult=False
        self.audioCount=0
        player.ultDone=True
        player.ultCount=0
        self.ult2Count=0
        player.attackBreak=0
        self.tempBg=bg
    def draw(self,win):
        
        if self.walkCount+1>=21:
            self.walkCount  =0
            
        if self.standing and self.wasLeft and self.attack:
          # if self.standing and self.wasLeft and self.attack and not self.Right and not self.Left:
                
             if self.attackCount<12 and self.attackNum==1 :
                    self.attackBreak=0
                    self.height=luffAttackL[self.attackCount//4].get_height()
                    self.width=luffAttackL[self.attackCount//4].get_width()
                    win.blit(luffAttackL[self.attackCount//4],(self.x,self.y))
               #     if self.attackCount==1:
                       # self.attackCount+=1
                    if self.attackCount==2:
                        channel=pygame.mixer.find_channel()
                        GGpistol.set_volume(1)
                 #       print("heee")
                        GGpistol.play()
                       
                    if self.attackCount==11:
                        self.attackDone=True
                        self.attack=False
                       # self.wasRight=True
                       # self.attackCount=0
             elif self.attackCount<27 and self.attackNum==2:
                    self.height=luffAttackL2[self.attackCount//3].get_height()
                    self.width=luffAttackL2[self.attackCount//3].get_width()
                    win.blit(luffAttackL2[self.attackCount//3],(self.x,self.y))
                    if self.attackCount==6:
                        
                        storm.play()
                    if self.attackCount==26:
                        self.attackDone=True
                      #  self.attackCount=0
                      #  self.attackNum=0
                        self.attack=False
                      #  self.wasRight=True
                        
                   # self.attack=False
             elif self.attackCount <24 and self.attackNum==3:
               #     print("iiiiii",self.attackCount)
                    self.height=luffAttackL3[self.attackCount//3].get_height()
                    self.width=luffAttackL3[self.attackCount//3].get_width()
                    win.blit(luffAttackL3[self.attackCount//3],(self.x,self.y))
                    
                    sound3.play()
                    sound3.set_volume(0.2 )
                    if self.attackCount==23:
                        self.attackDone=True
                    #    self.attackCount=0
                     #   self.attackNum=0
                        self.attack=False
                    #    self.wasRight=True
                       
             elif self.attackCount<57 and self.attackNum==4:
                    
                    if self.attackCount==2:
                        pygame.mixer.stop()
                        channel=pygame.mixer.find_channel()
                        egun.set_volume(1)
                        egun.play()
                        
                    if self.attackCount//3==10:
                        self.x-=40
                    if self.attackCount//3==9:
                        self.x+=20
                    self.height=luffAttackL4[self.attackCount//3].get_height()
                    self.width=luffAttackL4[self.attackCount//3].get_width()
                    win.blit(luffAttackL4[self.attackCount//3],(self.x,self.y))
    #FIXME
                    if self.attackCount==45 and enemy.hit:
                        for x in range(-100,1,10):
                            y=1/enemy.y*x*x+enemy.y
                            tempX=enemy.x+x
                            enemy.fallXList.append(tempX)
                            enemy.fallYList.append(y)
                        enemy.fallXList.reverse()
                        enemy.fallYList.reverse()
                        
                        #for count in range(20):
                           # self.x=enemy.fallXList[count]
                         #   self.y=enemy.fallYList[count]
                         #   win.blit(AmFall,(self.x,self.y))
                          #  pygame.display.update()
                        enemy.Fall=True 
                        enemy.hit=False
                        #    pygame.display.update()
                    if self.attackCount==56:
                        self.attackDone=True
                        self.attackCount=0
                        self.attackNum=0
                        self.attack=False
                        self.attackBreak+=1
                   #     self.wasRight=True
            
        elif self.standing and self.wasRight and self.attack:
        
                
             if self.attackCount<12 and self.attackNum==1 :
                    self.attackBreak=0
                    self.height=luffAttack[self.attackCount//4].get_height()
                    self.width=luffAttack[self.attackCount//4].get_width()
                    win.blit(luffAttack[self.attackCount//4],(self.x,self.y))
               #     if self.attackCount==1:
                       # self.attackCount+=1
                    if self.attackCount==2:
                        channel=pygame.mixer.find_channel()
                        GGpistol.set_volume(1)
                 #       print("heee")
                        GGpistol.play()
                       
                    if self.attackCount==11:
                        self.attackDone=True
                        self.attack=False
                        self.wasRight=True
                        
                       # self.attackCount=0
                     #   print("ay")
             elif self.attackCount<27 and self.attackNum==2:
                    self.height=luffAttack2[self.attackCount//3].get_height()
                    self.width=luffAttack2[self.attackCount//3].get_width()
                    win.blit(luffAttack2[self.attackCount//3],(self.x,self.y))
                    if self.attackCount==6:
                        
                        storm.play()
                    if self.attackCount==26:
                        self.attackDone=True
                      #  self.attackCount=0
                      #  self.attackNum=0
                        self.attack=False
                        self.wasRight=True
                        
                   # self.attack=False
             elif self.attackCount <24 and self.attackNum==3:
              
                    self.height=luffAttack3[self.attackCount//3].get_height()
                    self.width=luffAttack3[self.attackCount//3].get_width()
                    win.blit(luffAttack3[self.attackCount//3],(self.x,self.y))
                    
                    sound3.play()
                    sound3.set_volume(0.2 )
                    if self.attackCount==23:
                        self.attackDone=True
                    #    self.attackCount=0
                     #   self.attackNum=0
                        self.attack=False
                        self.wasRight=True
                       
             elif self.attackCount<57 and self.attackNum==4:
                    
                    if self.attackCount==2:
                        pygame.mixer.stop()
                        channel=pygame.mixer.find_channel()
                        egun.set_volume(1)
                        egun.play()
                        
                    if self.attackCount//3==10:
                        self.x+=40
                    if self.attackCount//3==9:
                        self.x-=20
                    self.height=luffAttack4[self.attackCount//3].get_height()
                    self.width=luffAttack4[self.attackCount//3].get_width()
                    win.blit(luffAttack4[self.attackCount//3],(self.x,self.y))
                    
                    if self.attackCount==45 and enemy.hit:
                        for x in range(0,101,10):
                            y=1/enemy.y*x*x+enemy.y
                            tempX=enemy.x+x
                            enemy.fallXList.append(tempX)
                            enemy.fallYList.append(y)
                       
                        #for count in range(20):
                           # self.x=enemy.fallXList[count]
                         #   self.y=enemy.fallYList[count]
                         #   win.blit(AmFall,(self.x,self.y))
                          #  pygame.display.update()
                        enemy.Fall=True 
                        enemy.hit=False
                        
                    if self.attackCount==56:
                        self.attackDone=True
                        self.attackCount=0
                        self.attackNum=0
                        self.attack=False
                        self.wasRight=True
                        self.attackBreak+=1
        elif self.ult:
            if self.ult2Count==0:
                
                win.blit(luffUlt[self.ultCount//8],(self.x,self.y))
                self.ultCount+=1
                if self.audioCount==0:
                    KKGun.play()
                    self.audioCount+=1
                
                if self.wasRight:
                    if self.ultCount//8>18 and self.ultCount//8<=21:
                        self.x+=5
                    if self.ultCount//8>21 and self.ultCount//8 <=27:
                        self.x+=2
                        self.y-=3
            if self.ultCount==325 :
                
                for x in range(0,101,10):
                    y=1/enemy.y*x*x+enemy.y
                    tempX=enemy.x+x
                    enemy.fallXList.append(tempX)
                    enemy.fallYList.append(y)
                       
                        #for count in range(20):
                           # self.x=enemy.fallXList[count]
                         #   self.y=enemy.fallYList[count]
                         #   win.blit(AmFall,(self.x,self.y))
                          #  pygame.display.update()
                enemy.Fall=True 
                enemy.hit=False
            if self.ultCount==327:
                enemy.damage+=UltAttack
            if self.ultCount>=335:
                win.blit(luffUlt2[self.ult2Count//2],(self.x,self.y))
                self.ult2Count+=1
                if self.ult2Count==7:
                    self.ultCount=0
                    self.ult2Count=0
                    self.audioCount=0
                    self.ultDone=True
                    self.ult=False
                    
                    bg=self.tempBg
                    win.blit(self.tempBg,(0,0))
                    
        else:
            
            if self.hit and not self.Fall:
                win.blit(self.hitImage,(self.x,self.y))
                
                if enemy.attackNum==2:
                    if self.hitCount<21:
                        win.blit(hitEffect1[self.hitCount//3],(self.x-10,self.y-30))
                    if self.hitCount==12:
                            self.damage+=normAttack
                   # if self.hitCount>19:
                    #    self.hitCount=0
                elif enemy.attackNum%2==1:
                    
                    if self.hitCount<16:
                        print(self.hitCount,self.hitCount//4)
                        win.blit(hitEffect2[self.hitCount//4],(self.x-10,self.y-30))
                    if self.hitCount==12:
                            self.damage+=normAttack
                     #   if self.hitCount==15:
                        #    self.hitCount=0
                        #    self.hit=False
                  #      self.hitSide=None
                elif enemy.attackNum ==4:
                    
                    if self.hitCount<16:     
                        win.blit(hitEffect2[self.hitCount//4],(self.x-10,self.y-30))
                    if self.hitCount==12:
                            self.damage+=normAttack
                       # if self.hitCount==15:
                            #self.hitCount=0
                           # self.hit=False
                           # self.hitSide=None
                            
            elif  self.Fall: #'''not self.hit and '''self.Fall:
            
                if self.y>=math.floor(screenWidth-self.width-10) and not self.fallCheck:
                    self.fallCount=11
                    self.fallCheck=True
                if self.fallCount<=10:
                    
                    self.x=self.fallXList[self.fallCount]
                    self.y=self.fallYList[self.fallCount]
                    if self.hitImage==LuffHit:
                        win.blit(LuffFall,(self.x,self.y))
                    elif self.hitImage==LuffHitR:
                        win.blit(LuffFalll,(self.x,self.y))
                    self.fallCount+=1
                elif self.fallCount>10 and self .fallCount<=34:
                    if self.hitImage==LuffHit:
                       win.blit(LuffFall,(self.x,self.y))
                    elif self.hitImage==LuffHitR:
                        win.blit(LuffFalll,(self.x,self.y))
                    self.fallCount+=1
                if self.fallCount==15:
                    self.fallExpCount=1
                if self.fallCount==35:
                    self.backUp=True
                    self.hit=False
                    self.hitSide=None
                              
                if self.backUp :#and self.startFall:
                    if self.hitImage==LuffHitR:
                   
                        if self.backUpCount%2==0:
                            self.x==2
                            self.y-=5
                        win.blit(LuffGetUpR[self.backUpCount//2],(self.x,self.y))
                    elif self.hitImage==LuffHit:
                     
                        if self.backUpCount%2==0:
                            self.x+=2
                            self.y-=5
                        win.blit(LuffGetUp[self.backUpCount//2],(self.x,self.y))
                    self.backUpCount+=1
                    if self.backUpCount==10:
                        self.backUp=False
                        self.Fall=False
                        self.fallXList=[]
                        self.FallYList=[]
                        self.fallCheck=False
                        self.fallCount=0
                        self.backUpCount=0
                if self.fallExpCount>0:
                    win.blit(fallExp[self.fallExpCount//2],(self.x-65,self.y-80))
                    if self.fallExpCount==2:
                        fallExpSound.play()
                    self.fallExpCount+=1
                    if self.fallExpCount==14:
                       self.fallExpCount=0
                       
                       
            elif self.Left==False and self.Right==False:
                if self.wasLeft:
                    self.height=leftImage.get_height()
                    self.width=leftImage.get_width()
                    win.blit(leftImage,(self.x,self.y))
                      
                if self.wasRight:
                    self.height=rightImage.get_height()
                    self.width=rightImage.get_width()
                    win.blit(rightImage,(self.x,self.y))
        if not self.standing:
            if self.Left:
                self.height=walkLeft[self.walkCount//3].get_height()
                self.width=walkLeft[self.walkCount//3].get_width()
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                
                self.walkCount+=1
            if self.Right:
                self.height=walkRight[self.walkCount//3].get_height()
                self.width=walkRight[self.walkCount//3].get_width()
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
               # pygame.display.update()
                
                self.walkCount+=1
            self.standing=True

    def Ishit(self):
        if enemy.attack and (enemy.x+enemy.width>=self.x-5 and enemy.x+enemy.width<self.x+self.width) and self.hitSide!="Left":
            
            self.x=enemy.x+enemy.width
            if enemy.attackNum==2 or enemy.attackNum==1:
                self.x-=15
            if enemy.attackNum==3 and enemy.attackCount==13:
                self.y-=35
                
            self.hit=True
            self.hitImage=LuffHitR
            self.height=LuffHit.get_height()
            self.width=LuffHit.get_width()
      
            punch.play()
            self.hitSide="Right"
        elif enemy.attack and (enemy.x<=self.x+self.width +5  and enemy.x>= self.x) and self.hitSide !="Right" :
            self.x=enemy.x-enemy.width/2
            self.height=LuffHitR.get_height()
            self.width=LuffHitR.get_width()
            self.hitImage=LuffHit
            self.hit=True
           # self.x-=40
            if enemy.attackNum==2 or enemy.attackNum==1:
                self.x+=15
            if enemy.attackNum==3 and enemy.attackCount==13:
                self.y-=35
        
            punch.play()
            self.hitSide="Left"
        if self.hit:
            self.hitCount+=1
        if self.hitCount==30:
            self.hitCount=0
            self.hit=False
            self.hitSide=None
            
            '''
    def Ishit(self):
        if player.attack and (player.x+player.width>=enemy.x-5 and player.x+player.width<=enemy.x+enemy.width/2-10) and self.hitSide!="Right":
            self.x=player.x+player.width
            self.hit=True
            self.hitImage=AmHitL
            self.height=AmHitL.get_height()
            self.width=AmHitL.get_width()
            #self.x-=20
            print("yiiiiiii")
          #  win.blit(AmHitL,(self.x,self.y))
            punch.play()
            print("heeeeee")
            self.hitSide="Left"
        elif player.attack and (player.x<=enemy.x+enemy.width+10 and player.x>= enemy.x) and self.hitSide !="Left" :
            self.x=player.x
           # self.x=player.x+player.width
            self.height=AmHit.get_height()
            self.width=AmHit.get_width()
            self.hitImage=AmHit
            self.hit=True
            self.x-=40
            
           # player.x+=6a
           # win.blit(AmHit,(self.x,self.y))
            print("hooooo")
            punch.play()
            self.hitSide="Right"
        if self.hit:
         #   print("Sekai")
            self.hitCount+=1
        if self.hitCount==20:
            self.hitCount=0
            self.hit=False
            self.hitSide=None       
'''


class enemy():
    
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=10
        self.Left=False
        self.Right=False
        self.standing=True
        self.wasLeft=True
        self.wasRight=False
        self.walkCount=0
        self.attack=False
        self.attackNum=0
        self.attackCount=0
        self.attackDone=False
        self.justAttacked=False
        self.hit=False
        self.hitCount=0
        self.hitImage=AmHitL
        self.hitSide=None
        self.hitCount=0
        self.fallCount=0
        self.fallYList=[]
        self.fallXList=[]
        self.Fall=False
        self.fallCount=0
        self.backUp=False
        self.backUpCount=0
        self.startFall=False
        self.fallCheck=False
        self.fallExpCount=0
        self.damage=0
        self.health=200
        self.action=None
        self.possibleMoves=[None,"a","d","j"]
        self.moveCount= 1
        self.status="Free"
        self.attackBreak=0
       #     self.status
        
    def draw(self,win):
        
        if self.walkCount+1>=24:
            self.walkCount  =0

        if self.standing and self.wasLeft and self.attack and not self.Right and not self.Left:
            tempNum=self.attackNum
            
            if self.attackCount<15 and self.attackNum==1 :
                self.attackBreak=0
                self.height=AmAttack[self.attackCount//5].get_height()
                self.width=AmAttack[self.attackCount//5].get_width()
                win.blit(AmAttack[self.attackCount//5],(self.x,self.y))
                  
                if self.attackCount==2:
                    channel=pygame.mixer.find_channel()
                    AmLaugh.set_volume(0.5)
                    AmLaugh.play()
                           
                if self.attackCount==14:
                    self.attackDone=True
                    self.attack=False
                    self.wasLeft=True
                         
                        
            elif self.attackCount<20 and self.attackNum==2:
                self.height=AmAttack2[self.attackCount//4].get_height()
                self.width=AmAttack2[self.attackCount//4].get_width()
                win.blit(AmAttack2[self.attackCount//4],(self.x,self.y))
                if self.attackCount==2:
                        
                    AmShout.play()
                if self.attackCount==19:
                    self.attackDone=True
                      #  self.attackCount=0
                      #  self.attackNum=0
                    self.attack=False
                       # self.wasRight=True
                        
                   # self.attack=False
            elif self.attackCount <15 and self.attackNum==3:
              
                self.height=AmAttack3[self.attackCount//5].get_height()
                self.width=AmAttack3[self.attackCount//5].get_width()
                win.blit(AmAttack3[self.attackCount//5],(self.x,self.y))
                    
                Amsmash.play()
                Amsmash.set_volume(0.1 )
                if self.attackCount==14:
                    self.attackDone=True
            
                    self.attack=False
                       
            elif self.attackCount<24 and self.attackNum==4:
                 
                        
                if self.attackCount//4==3:
                    tempx=self.x
                    tempy=self.y
                    self.x-=5
                    self.y-=10
                if self.attackCount//4==5:
                    self.y+=8
                if self.attackCount//4==6:
                    self.x-=5
                    self.y+=3
                        
                self.height=AmAttack4[self.attackCount//4].get_height()
                self.width=AmAttack4[self.attackCount//4].get_width()
                win.blit(AmAttack4[self.attackCount//4],(self.x,self.y))
                
                if self.attackCount==20 and player.hit:
                        for x in range(-100,1,10):
                            y=1/player.y*x*x+player.y
                            tempX=player.x+x
                            player.fallXList.append(tempX)
                            player.fallYList.append(y)
                        player.fallXList.reverse()
                        player.fallYList.reverse()
                        
                       
                        player.Fall=True 
                        player.hit=False
                if self.attackCount==23:
                    self.attackDone=True
                    self.attackCount=0
                    self.attackNum=0
                    self.attack=False
                      #  self.wasLeft=True
                    self.wasRight=False
                    pygame.mixer.stop()
                    self.attackBreak+=1
            
        elif self.standing and self.wasRight and self.attack:
        
                
            if self.attackCount<15 and self.attackNum==1 :
                
                self.attackBreak=0
                self.height=AmrAttack[self.attackCount//5].get_height()
                self.width=AmrAttack[self.attackCount//5].get_width()
                win.blit(AmrAttack[self.attackCount//5],(self.x,self.y))
                   #     if self.attackCount==1:
                           # self.attackCount+=1
                if self.attackCount==2:
                    channel=pygame.mixer.find_channel()
                    AmLaugh.set_volume(0.5)
                    AmLaugh.play()
                           
                if self.attackCount==14:
                    self.attackDone=True
                    self.attack=False
                    self.wasRight=True
                           # self.attackCount=0
                
                        
            elif self.attackCount<20 and self.attackNum==2:
                self.height=AmrAttack2[self.attackCount//4].get_height()
                self.width=AmrAttack2[self.attackCount//4].get_width()    
                win.blit(AmrAttack2[self.attackCount//4],(self.x,self.y))
                if self.attackCount==2:
                        
                    AmShout.play()
                       # print("ewrgtyrefw")
                if self.attackCount==19:
                    self.attackDone=True
                      #  self.attackCount=0
                      #  self.attackNum=0
                    self.attack=False
                       # self.wasRight=True
                        
                   # self.attack=False
            elif self.attackCount <15 and self.attackNum==3:
                self.height=AmrAttack3[self.attackCount//5].get_height()
                self.width=AmrAttack3[self.attackCount//5].get_width()
                win.blit(AmrAttack3[self.attackCount//5],(self.x,self.y))
                    
                Amsmash.play()
                Amsmash.set_volume(0.1 )
                if self.attackCount==14:
                    self.attackDone=True
                    #    self.attackCount=0
                     #   self.attackNum=0
                    self.attack=False
                   #     self.wasRight=True
                       
            elif self.attackCount<24 and self.attackNum==4:
                    
                if self.attackCount//4==3:
                    tempx=self.x
                    tempy=self.y
                    self.x+=5
                    self.y-=10
                if self.attackCount//4==5:
                    self.y+=8
                if self.attackCount//4==6:
                    self.x-=5
                    self.y+=3
                        
                self.height=AmrAttack4[self.attackCount//4].get_height()
                self.width=AmrAttack4[self.attackCount//4].get_width()       
                win.blit(AmrAttack4[self.attackCount//4],(self.x,self.y))
                
                if self.attackCount==20 and player.hit:
                        for x in range(0,101,10):
                            y=1/player.y*x*x+player.y
                            tempX=player.x+x
                            player.fallXList.append(tempX)
                            player.fallYList.append(y)
                        #for count in range(20):
                           # self.x=enemy.fallXList[count]
                         #   self.y=enemy.fallYList[count]
                         #   win.blit(AmFall,(self.x,self.y))
                          #  pygame.display.update()
                        player.Fall=True 
                        player.hit=False
                        
                if self.attackCount==23:
                    self.attackDone=True
                    self.attackCount=0
                    self.attackNum=0
                    self.attack=False
                    self.attackBreak+=1
                      #  self.wasLeft=True
                        #self.wasRight=False
                    pygame.mixer.stop()
        else:
            if self.hit:
                win.blit(self.hitImage,(self.x,self.y))
                if player.ult and player.ultCount==322:
                    self.damage+=75
                if player.attackNum==2:
                    if self.hitCount<21:
                        
                        win.blit(hitEffect1[self.hitCount//3],(self.x-10,self.y-30))
                        if self.hitCount==12:
                            enemy.damage+=normAttack
                 #   if self.hitCount>19:
                 #       self.hitCount=0
                elif player.attackNum%2==1:
                    
                    if self.hitCount<16:
                        print(self.hitCount,self.hitCount//4)
                        win.blit(hitEffect2[self.hitCount//4],(self.x-10,self.y-30))
                        if self.hitCount==12:
                            enemy.damage+=normAttack
                      #  if self.hitCount==15:
                        #    self.hitCount=0
                        #    self.hit=False
                  #      self.hitSide=None
                elif player.attackNum ==4:
                    
                    if self.hitCount<16:     
                        win.blit(hitEffect2[self.hitCount//4],(self.x-10,self.y-30))
                        if self.hitCount==12:
                            enemy.damage+=normAttack
                        #if self.hitCount==15:
                     #       self.hitCount=0
                         #   self.hit=False
                           # self.hitSide=None
                      #  self.fallCount+=1
                    '''
                    if self.fallCount <16 and player.attackCount>56:
                        self.x-=20
                        win.blit(AmFall[self.fallCount//4],(self.x,self.y))
                     #   status="ok"
                    elif self.fallCount<32:# and self.status=="ok": #and player.attackCount>=40:
                        self.y+=5
                        win.blit(AmFall[self.fallCount//4],(self.x,self.y))
                        if self.fallCount==31:
                            print("yoooooooo")
                            self.fallCount=0
                            self.hitCount==0
                            #self.hit=False
                            self.hitSide=None
                    '''
            elif  self.Fall: #'''not self.hit and '''self.Fall:
            
                       
                if self.y>=math.floor(screenWidth-self.width-10) and not self.fallCheck:
                    self.fallCount=11
                    self.fallCheck=True
                if self.fallCount<=10:
                   
                    self.x=self.fallXList[self.fallCount]
                    self.y=self.fallYList[self.fallCount]
                    if self.hitImage==AmHitL:
                        win.blit(AmFalll,(self.x,self.y))
                    elif self.hitImage==AmHit:
                        win.blit(AmFall,(self.x,self.y))
                    self.fallCount+=1
                elif self.fallCount>10 and self .fallCount<=34:
                    if self.hitImage==AmHitL:
                       win.blit(AmFalll,(self.x,self.y))
                    elif self.hitImage==AmHit:
                        win.blit(AmFall,(self.x,self.y))
                    self.fallCount+=1
                if self.fallCount==15:
                    self.fallExpCount=1
                if self.fallCount==35:
                    self.backUp=True
                    self.hit=False
                    self.hitSide=None
                    #pygame.display.update()
                              
                if self.backUp and self.startFall:
                    if self.hitImage==AmHit:
                        if self.backUpCount%3==0:
                            self.x+=2
                            self.y-=5
                        win.blit(AmGetUp[self.backUpCount//2],(self.x,self.y))
                    elif self.hitImage==AmHitL:
                        if self.backUpCount%3==0:
                            self.x-=2
                            self.y-=5
                        win.blit(AmGetUpl[self.backUpCount//2],(self.x,self.y))
                    self.backUpCount+=1
                    if self.backUpCount==18:
                        self.backUp=False
                        self.Fall=False
                        self.fallXList=[]
                        self.FallYList=[]
                        self.fallCheck=False
                        self.fallCount=0
                        self.backUpCount=0
                if self.fallExpCount>0:
                    win.blit(fallExp[self.fallExpCount//2],(self.x-65,self.y-80))
                    if self.fallExpCount==2:
                        fallExpSound.play()
                    self.fallExpCount+=1
                    if self.fallExpCount==14:
                       self.fallExpCount=0
           
                        
                #self.Fall=False
            elif self.Left==False and self.Right==False:
                if self.wasLeft:
                    self.height=Aml.get_height()
                    self.width=Aml.get_width()
                    win.blit(Aml,(self.x,self.y))
                  #  hitImage=AmHitL
                if self.wasRight:
                    self.height=Amr.get_height()
                    self.width=Amr.get_width()
                    win.blit(Amr,(self.x,self.y))
                   ## hitImage=AmHit
            
        if not self.standing:
            
            if self.Left:
                self.height=AmwalkLeft[self.walkCount//3].get_height()
                self.width=AmwalkLeft[self.walkCount//3].get_width()
                win.blit(AmwalkLeft[self.walkCount//3],(self.x,self.y))
               
                self.walkCount+=1
            elif self.Right:
                self.height=AmwalkRight[self.walkCount//3].get_height()
                self.width=AmwalkRight[self.walkCount//3].get_width()
                win.blit(AmwalkRight[self.walkCount//3],(self.x,self.y))
                
                self.walkCount+=1
            self.standing=True
            
    def Ishit(self):
        if player.attack and (player.x+player.width>=enemy.x-5 and player.x+player.width<enemy.x+enemy.width) and self.hitSide!="Right":
            self.x=player.x+player.width
            if player.attackNum==2 or player.attackNum==3:
                self.x-=self.width/2
            self.hit=True
            self.hitImage=AmHitL
            self.height=AmHitL.get_height()
            self.width=AmHitL.get_width()
            #self.x-=20
          #  win.blit(AmHitL,(self.x,self.y))
            punch.play()
            self.hitSide="Left"
        elif player.attack and (player.x<=enemy.x+enemy.width+5 and player.x>= enemy.x) and self.hitSide !="Left" :
            self.x=player.x-player.width/2
           # self.x=player.x+player.width
            if player.attackNum==3:
                self.x+=10
            self.height=AmHit.get_height()
            self.width=AmHit.get_width()
            self.hitImage=AmHit
            self.hit=True
           # self.x-=40
        elif player.ult and player.ultCount==320 and player.y-player.height<=self.y:
            self.hit=True
           # player.x+=6a
           # win.blit(AmHit,(self.x,self.y))
            punch.play()
            self.hitSide="Right"
        if self.hit:
            self.hitCount+=1
        if self.hitCount==30:
            self.hitCount=0     
            self.hit=False
            self.hitSide=None

    def AIControls(self):
        if abs(player.x-enemy.x)<=99.9999 and self.status != "Done":
            self.status="Alert"
        if abs(player.x-enemy.x)>100 and self.status != "Done":
            self.status="Free"
        choice=random.randint(0,2)
        if abs(player.x-enemy.x)>100 and self.moveCount%10==0 and self.status=="Free":
            self.action=self.possibleMoves[choice]
            self.moveCount=1
        if self.status=="Alert":
            if player.x+player.width<enemy.x:
                if player.x+player.width+10>enemy.x:# and self.attackBreak%10==0:
                    if player.x+player.width+5<enemy.x:
                        enemy.x-=5
                    elif enemy.x+enemy.width+5<player.x:
                        enemy.x+=5
                    self.action="j"
          #          if self.attackNum==4:
          #              self.attackBreak+=1
                else:
                    self.action="a"
            elif player.x>enemy.x+enemy.width:
                if self.x+self.width+10>=player.x:#  and self.attackBreak%10==0:
                    if player.x+player.width+5<enemy.x:
                        enemy.x-=5
                    elif enemy.x+enemy.width+5<player.x:
                        enemy.x+=5
                    self.action="j"
                   # if self.attackNum==4:
                     #   self.attackBreak+=1
                else:
                    self.action="d"
          #  if self.attackBreak>0:
            #   self.attackBreak+=1
            
        #elif math.floor(abs(player.x-enemy.x))==200:
         #   self.action=None
      #  if self.action==None and self.moveCount<7:
      #      self.moveCount=9
        self.moveCount+=1
        #if abs(player.x-enemy.x)>100 and self.wasRight:
         #   self.action="a"
       # enemy.action=Nont
       # print(self.action)
      #  if abs(player.x-enemy.x)>100 and self.wasRight:
        #    self.action="d" 
global musicCount
musicCount=0
titleSoundCount=0
def drawAll():
    #itle=font.render("WorlWide Brawl!",True,(255,255,255))
    global musicCount
    #print(bg)
   # win.blit(bg,(0,0))
    if GameStatus=="Title":
        
       #file=pygame.mixer.music.load('TitleSound..mp3')
        #bg=titleScreen
        #print("heyyyy")
        
        #win.blit(bg,(0,0))
       # win.blit(Title,(75,175))
      #  win.blit(instructionText,(150,420))
       # if musicCount==0:
         #  pygame.mixer.music.load(file)
          # pygame.mixer.music.play(-1)
          #  titleSoundCount+=1
        #   musicCount+=1
        pygame.display.update()
   # print(player.hit,"efjngerlkjflerjflewjelwjrew")
    elif GameStatus=="Menu":
            win.blit(bg,(0,0))
            win.blit(text3,(100,25))
            win.blit(Aml,(50,350))
            win.blit(leftImage,(150,365))
           # win.blit(jamMenu,(180,290))
          #  pygame.draw.polygon(win, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
            pygame.display.update()
    if GameStatus=="Game":
       # bg=pygame.image.load("bg.png")
        win.blit(bg,(0,0))
        if musicCount==0:
            music=pygame.mixer.music.load('music.mp3')
            musicCount+=1
            pygame.mixer.music.play(-1)
            
        player.draw(win)
        if not player.ult:
            player.Ishit()
        enemy.draw(win)
        enemy.Ishit()
        enemy.AIControls()
       # win.blit(Am,(enemy.x,enemy.y))
        win.blit(lfhp,(10,10))
       
        pygame.draw.rect(win,(255,0,0),(84,20,200,30))
        pygame.draw.rect(win,(0,255,0),(84,20,player.health-player.damage,30))
        #pygame.draw.rect(win,(255,255,0),(340+64,20,100,30))
        win.blit(Amhp,(340,10))    
        pygame.draw.rect(win,(255,0,0),(340+64,20,200,30))
        pygame.draw.rect(win,(0,255,0),(340+64,20,player.health-enemy.damage,30))
       # pygame.draw.line(win,(125,125,125),(player.x+player.width,440),(player.x+player.width+5,440),30)
        #player.move()
       # pygame.draw.line(win,(125,125,125),(player.x-20,440),(player.x,440),30)
        player.Left=False
        player.Right=False
        player.standing=True
        enemy.Left=False
        enemy.Right=False
        enemy.standing=True
        
        if enemy.damage==200:
            if player.wasRight:
                for x in range(0,101,10):
                    y=1/enemy.y*x*x+enemy.y
                    tempX=enemy.x+x
                    enemy.fallXList.append(tempX)
                    enemy.fallYList.append(y)
                           
                            #for count in range(20):
                               # self.x=enemy.fallXList[count]
                             #   self.y=enemy.fallYList[count]
                             #   win.blit(AmFall,(self.x,self.y))
                              #  pygame.display.update()
                    enemy.Fall=True 
                    enemy.hit=False
            elif player.wasLeft:
                for x in range(-100,1,10):
                        y=1/enemy.y*x*x+enemy.y
                        tempX=enemy.x+x
                        enemy.fallXList.append(tempX)
                        enemy.fallYList.append(y)
                        enemy.fallXList.reverse()
                        enemy.fallYList.reverse()
                            
                            #for count in range(20):
                               # self.x=enemy.fallXList[count]
                             #   self.y=enemy.fallYList[count]
                             #   win.blit(AmFall,(self.x,self.y))
                              #  pygame.display.update()
                        enemy.Fall=True 
                        enemy.hit=False
            enemy.status="Done1"
            win.blit(text1, (150, 230))
            enemy.Fall=True
           ## player.draw(win)
           # enemy.FallCount=0
        if player.damage==200:
            win.blit(text2, (150, 230))
            if enemy.wasLeft:
                for x in range(-50,1,10):
                    y=1/player.y*x*x+player.y
                    tempX=player.x+x
                    player.fallXList.append(tempX)
                    player.fallYList.append(y)
                player.fallXList.reverse()
                player.fallYList.reverse()
            elif enemy.wasRight:
                for x in range(0,101,10):
                    y=1/player.y*x*x+player.y
                    tempX=player.x+x
                    player.fallXList.append(tempX)
                    player.fallYList.append(y)
                            #prit("DOneeee BIIITCH")
                            #for count in range(20):
                               # self.x=enemy.fallXList[count]
                             #   self.y=enemy.fallYList[count]
                             #   win.blit(AmFall,(self.x,self.y))
                              #  pygame.display.update()
                    #player.Fall=True 
                   # player.hit=False
                            
                            #for count in range(20):
                               # self.x=enemy.fallXList[count]
                             #   self.y=enemy.fallYList[count]
                             #   win.blit(AmFall,(self.x,self.y))
                              #  pygame.display.update()
           # player.Fall=True 
           # player.hit=False
            enemy.status="Done"
            
            player.Fall=True
           # enemy.draw(win)
        if enemy.attackBreak>0:
            enemy.attackBreak+=1
        if player.attackBreak>0:
            player.attackBreak+=1
           
           # player.FallCount=0
        if GameStatus=="Title":
             win.blit(Title,(250,250))
     #   pygame.draw.rect(win,(255,0,0),(player.x,player.y,player.width,player.height),2)
      #  pygame.draw.rect(win,(255,0,0),(enemy.x,enemy.y,enemy.width,enemy.height),2)
        pygame.display.update()
       # enemy.action=None
        if enemy.backUp:
            enemy.startFall=True
#win=pygame.display.set_mode((500,460))
screenLength=610
player.tempBg=bg
screenWidth=460
normAttack=10
UltAttack=75
#FIXME change back to lsr.png
width,height=returnImageSize("lsr.png")
win=pygame.display.set_mode((screenLength,screenWidth))
keys = pygame.key.get_pressed()
player=player(10,screenWidth-height,width,height)
width,height=returnImageSize("aml.png")
enemy=enemy(400,screenWidth-height,width,height)
#font = pygame.font.SysFont(None, 24)
font = pygame.font.SysFont('comicsans', 50, True)
black=(0,0,0)
#endRect=pygame.draw.rect(win,(0,0,0),())
text1 = font.render('Player 1 wins!!', True, (0,200,235))
text2= font.render('Player 2 wins!!', True, (0,200,235))
titleSoundCount=0
#font = pygame.font.SysFont('comicsans', 30, True)
Game=""
GameStatus= "Title"
text3=font.render("Choose Your Character",True,(235,0,235))
Titlefont = pygame.font.SysFont('comicsans', 65, True, True)
Title=Titlefont.render("WorldWide Brawl!",True,(0,0,0))
smallFont=pygame.font.SysFont("comicsans",25,True, True)
instructionText=smallFont.render("Press Spacebar to continue",True,(125,0,100))
#win.blit(Title,(250,450))
run=True

while run:
    keys = pygame.key.get_pressed()
   # if player.walkCount>5:
    #    player.walkCount=5
    if GameStatus=="Title":
       # Title=font.render("WorlWide Brawl!",True,(255,255,255))
        bg=titleScreen
        win.blit(bg,(0,0))
        win.blit(Title,(75,175))
        win.blit(instructionText,(150,420))
      #  music=Title
        for event in pygame.event.get():
            if keys[pygame.K_SPACE]:
                win.fill((0,0,0))
                GameStatus="Game"#Menu
       # drawAll()
    elif GameStatus=="Menu":
        bg=earth
       # win.blit(Title,(0,0))
       # win.blit(earth,(0,0))
        drawAll()
        for event in pygame.event.get():
            if keys[pygame.K_SPACE]:
                GameStatus="Game"
    elif GameStatus=="Game":
        pygame.time.delay(20)
        
        if player.damage>200:
            player.damage=200
        if enemy.damage>200:
            enemy.damage=200
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
    
       # keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and player.x>player.vel and not player.Fall and not player.backUp and  not player.hit:
            if not player.attack:
               # if player.x<=enemy.x +enemy.width:# and player.x>=enemy.x: #and player.y>enemy.y-30:
           
                     player.x-=player.vel 
                     player.Right=False
                     player.Left=True
                     player.wasLeft=True
                     player.wasRight=False
                     player.standing=False
                 
        if keys[pygame.K_RIGHT] and player.x<610-player.width-player.vel and not player.Fall and not player.backUp and not player.hit:
            if not player.attack:
              #  if player.x+player.width>=enemy.x:# and player.x+player.width<=enemy.x+enemy.width:# and player.y>enemy.y-30:
                
                 
                      player.x+=player.vel
                      player.Right=True
                      player.standing=False
                      player.wasRight=True
                      player.wasLeft=False
                      player.Left=False
                     # win.blit(walkRight[player.walkCount//3],(player.x,player.y))
                      
        if keys[pygame.K_UP] and player.y>player.vel:
            player.y-=player.vel
        if keys[pygame.K_DOWN] and player.y<460-player.height-player.vel:
            player.y+=player.vel
        
        if keys[pygame.K_SPACE] and not player.Fall and not player.backUp and not player.hit and player.attackBreak%20==0:
            
            if player.attackDone==True and player.attackNum>0:
                player.attack=True
                player.standing=True
                player.attackDone=False
                player.attackCount=0
                player.attackCount+=1
                player.attackNum+=1
             #   print(enemy.wasLeft,enemy.attack,enemy.standing)
            else:
                player.attack=True
                player.standing=True
               # player.attackCount+=1
                if player.attackNum==0:
                    player.attackNum=1
                    player.attackCount=1
                    player.attack=True
                    player.standing=True
                    player.attackDone=False
                
            enemy.Right=False
            enemy.Left=False 
        if keys[pygame.K_m] and not player.Fall and not player.backUp and not player.hit and player.attackBreak%35==0:
            
            if player.ultDone==True :
                bg=LuBg
                player.ult=True
                player.standing=True
                player.ultDone=False
                player.ultCount=0
                player.ult2Count=0
              #  player.attack=True
               
            
           
        
            
    
     
        if player.attackCount>0:
            player.attackCount+=1
            
        ## Enemey
        
        if (keys[pygame.K_a] or enemy.action=="a") and enemy.x>enemy.vel and not enemy.hit and not enemy.Fall and not enemy.backUp:
            if not enemy.attack:
                
                    enemy.x-=enemy.vel
                    enemy.Right=False
                    enemy.Left=True
                    enemy.wasLeft=True
                    enemy.wasRight=False
                    enemy.standing=False
            
     
        if (keys[pygame.K_d] or enemy.action=="d") and enemy.x<screenLength-enemy.width-enemy.vel and not enemy.hit and not enemy.Fall and not enemy.backUp:
            if not enemy.attack:
                
                    enemy.x+=enemy.vel
                    enemy.Right=True
                    enemy.standing=False
                    enemy.wasRight=True
                    enemy.wasLeft=False
                    enemy.Left=False
                  #  enemy.action=None
       
        if keys[pygame.K_w] and enemy.y>enemy.vel:
            enemy.y-=enemy.vel
        if keys[pygame.K_s] and enemy.y<screenWidth-enemy.height-enemy.vel:
            enemy.y+=enemy.vel
        
        if (keys[pygame.K_j] or enemy.action=="j") and not enemy.hit and not enemy.Fall and not enemy.backUp and enemy.attackBreak%50==0:
           
            #print(player.attackCount,player.attackNum,player.attackDone)
            if enemy.attackDone==True and enemy.attackNum>0:
                
                enemy.attack=True
                enemy.standing=True
                enemy.attackDone=False
                enemy.attackCount=0
                enemy.attackCount+=1
                enemy.attackNum+=1               
            
             
            
            else:
                enemy.attack=True
                enemy.standing=True
               # player.attackCount+=1
              
            enemy.Right=False
            enemy.Left=False
            if enemy.attackNum==0:
                enemy.attackNum=1
                enemy.attackCount=1
                enemy.attack=True
                enemy.standing=True
                enemy.attackDone=False
               # enemy.wasRight=False
                #enemy.wasLeft=False
        if enemy.attackCount>0:
            enemy.attackCount+=1
        print(enemy.damage)
        
    if Game!="Over":
        drawAll()
    if enemy.status=="Done" :
        pygame.time.delay(100)
        if  not enemy.attack:
            pygame.image.save(win,"End.jpg")
            End= pygame.image.load("End.jpg")
            win.blit(End,(0,0))
            Game="Over"
    elif enemy.status=="Done1":
        pygame.time.delay(100)
        if not player.attack:
            pygame.image.save(win,"End.jpg")
            End= pygame.image.load("End.jpg")
            win.blit(End,(0,0))
            Game="Over"
    if player.ultDone==True:
        bg=player.tempBg
  #  drawAll()
pygame.quit()




