# -*- coding: cp1252 -*-
import pygame,random,math,os,sys


def find_intersection( p0, p1, p2, p3 ) :
# https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    s10_x = p1[0] - p0[0]
    s10_y = p1[1] - p0[1]
    s32_x = p3[0] - p2[0]
    s32_y = p3[1] - p2[1]

    denom = s10_x * s32_y - s32_x * s10_y

    if denom == 0 : return None # collinear

    denom_is_positive = denom > 0

    s02_x = p0[0] - p2[0]
    s02_y = p0[1] - p2[1]

    s_numer = s10_x * s02_y - s10_y * s02_x

    if (s_numer < 0) == denom_is_positive : return None # no collision

    t_numer = s32_x * s02_y - s32_y * s02_x

    if (t_numer < 0) == denom_is_positive : return None # no collision

    if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive : return None # no collision


    # collision detected

    t = t_numer / denom

    intersection_point = [ p0[0] + (t * s10_x), p0[1] + (t * s10_y) ]
    return intersection_point

class Level:
 def __init__(self):
  self.level=0
  self.levels=[self.level1,self.level2]
 def getNextLevel(self,app):
  return self.levels[self.level%len(self.levels)](app)
 def level1(self,app):
  Z=24
  app.player=Player(app,20*Z,8*Z)
  app.target=Target(app,120*Z,4*Z)
  return [
    #les murs
   HWall(app,  0*Z, 5*Z, 23*Z),
   VWall(app,  0*Z, 5*Z, 50*Z),
   VWall(app, 23*Z, 5*Z, 30*Z),
   HWall(app, 11*Z,14*Z, 23*Z),
   HWall(app, 14*Z,30*Z, 35*Z),
   VWall(app, 14*Z,30*Z, 38*Z),
   VWall(app, 21*Z,30*Z, 38*Z),
   VWall(app, 29*Z,30*Z, 45*Z),
   VWall(app, 14*Z,41*Z, 45*Z),
   HWall(app, 14*Z,45*Z, 29*Z),
   HWall(app,  0*Z,50*Z, 47*Z),
   VWall(app, 47*Z,18*Z, 50*Z),
   VWall(app, 35*Z, 9*Z, 30*Z),
   HWall(app, 35*Z, 9*Z, 91*Z),
   HWall(app, 47*Z,36*Z,115*Z),
   VWall(app, 74*Z, 9*Z, 21*Z),
   HWall(app, 74*Z,18*Z, 85*Z),
   VWall(app, 74*Z,25*Z, 29*Z),
   HWall(app, 74*Z,29*Z, 91*Z),
   VWall(app, 91*Z, 9*Z, 32*Z),
   HWall(app, 91*Z,32*Z,115*Z),
   VWall(app,115*Z, 0*Z, 32*Z),
   HWall(app,115*Z, 0*Z,144*Z),
   VWall(app,115*Z,36*Z, 51*Z),
   HWall(app,115*Z,51*Z,144*Z),
   VWall(app,144*Z, 0*Z, 51*Z),
   HWall(app,115*Z,11*Z,125*Z),
   VWall(app,125*Z, 6*Z, 11*Z),
   HWall(app,125*Z, 8*Z,134*Z),
   VWall(app,140*Z, 0*Z,  5*Z),
   HWall(app,125*Z,20*Z,144*Z),
   VWall(app,133*Z,13*Z, 20*Z),
   VWall(app,138*Z,13*Z, 20*Z),
   HWall(app,132*Z,38*Z,144*Z),
   VWall(app,132*Z,38*Z, 42*Z),
   VWall(app,132*Z,45*Z, 51*Z),
   HWall(app,115*Z,44*Z,126*Z),
   VWall(app,126*Z,47*Z, 51*Z),

    #les guardiens
   VGuard(app,  3*Z, 8*Z, 24*Z),
   VGuard(app,  9*Z,17*Z, 32*Z),
   VGuard(app, 21*Z,16*Z, 27*Z),
   VGuard(app,  9*Z,34*Z, 42*Z),
   VGuard(app, 16*Z,32*Z, 41*Z),
   HGuard(app, 10*Z,47*Z, 19*Z),
   HGuard(app, 48*Z,11*Z, 57*Z),
   VGuard(app, 67*Z,11*Z, 20*Z),
   VGuard(app, 56*Z,15*Z, 27*Z),
   VGuard(app, 50*Z,25*Z, 33*Z),
   VGuard(app, 62*Z,25*Z, 33*Z),
   VGuard(app, 70*Z,27*Z, 32*Z),
   HGuard(app, 80*Z,11*Z, 89*Z),
   HGuard(app, 75*Z,19*Z, 88*Z),
   VGuard(app, 88*Z,20*Z, 27*Z),
   HGuard(app, 75*Z,28*Z, 83*Z),
   HGuard(app, 75*Z,33*Z, 86*Z),
   HGuard(app, 89*Z,33*Z,101*Z),
   HGuard(app,106*Z,33*Z,121*Z),
   HGuard(app,118*Z,27*Z,130*Z),
   HGuard(app,126*Z,23*Z,136*Z),
   VGuard(app,141*Z,23*Z, 35*Z),
   VGuard(app,130*Z,35*Z, 49*Z),
   HGuard(app,116*Z,46*Z,124*Z),
   HGuard(app,135*Z,41*Z,142*Z),
   HGuard(app,135*Z,47*Z,142*Z),
   HGuard(app,127*Z,10*Z,142*Z),
   VGuard(app,136*Z,12*Z, 18*Z),
   VGuard(app,142*Z,12*Z, 18*Z),
   VGuard(app,142*Z, 2*Z,  7*Z),
   HGuard(app,125*Z, 2*Z,137*Z),

    #les boites
   Box(app, 21*Z,29*Z),
   Box(app, 25*Z,32*Z),
   Box(app, 27*Z,32*Z),
   Box(app, 76*Z,11*Z),
   Box(app, 76*Z,13*Z),
   Box(app,117*Z,49*Z),
   Box(app,142*Z,49*Z),
   Box(app,142*Z,40*Z),

    #les autres choses
   Exit(app,20*Z,8*Z),
   app.target,
   app.player,
   ]

 def level2(self,app):
  Z=24
  app.player=Player(app,2*Z,2*Z)
  app.target=Target(app,107*Z,59*Z)
  return [
    #les murs
   HWall(app,  0*Z, 0*Z, 13*Z),
   HWall(app, 25*Z, 0*Z,132*Z),
   VWall(app,  0*Z, 0*Z,  8*Z),
   VWall(app,  0*Z,26*Z, 64*Z),
   VWall(app,132*Z, 0*Z, 64*Z),
   HWall(app,  0*Z,64*Z, 14*Z),
   HWall(app, 40*Z,64*Z, 60*Z),
   HWall(app, 90*Z,64*Z,132*Z),
   HWall(app,  0*Z, 8*Z,  8*Z),
   VWall(app,  8*Z, 8*Z, 26*Z),
   HWall(app,  0*Z,26*Z,  8*Z),
   VWall(app, 13*Z, 0*Z, 18*Z),
   HWall(app, 13*Z,18*Z, 25*Z),
   VWall(app, 25*Z, 0*Z, 18*Z),
   HWall(app, 13*Z,22*Z, 25*Z),
   VWall(app, 13*Z,22*Z, 38*Z),
   VWall(app, 25*Z,22*Z, 38*Z),
   HWall(app, 13*Z,38*Z, 25*Z),
   HWall(app,  0*Z,53*Z, 10*Z),
   VWall(app,  7*Z,58*Z, 64*Z),
   VWall(app, 14*Z,50*Z, 64*Z),
   HWall(app, 14*Z,50*Z, 40*Z),
   VWall(app, 40*Z,50*Z, 64*Z),
   VWall(app, 32*Z, 0*Z, 12*Z),
   HWall(app, 32*Z,12*Z, 36*Z),
   HWall(app, 41*Z,12*Z, 46*Z),
   VWall(app, 46*Z, 0*Z, 12*Z),
   HWall(app, 32*Z,18*Z, 47*Z),
   VWall(app, 32*Z,18*Z, 21*Z),
   VWall(app, 32*Z,26*Z, 33*Z),
   HWall(app, 32*Z,33*Z, 47*Z),
   VWall(app, 47*Z,18*Z, 20*Z),
   VWall(app, 47*Z,24*Z, 33*Z),
   VWall(app, 60*Z,50*Z, 64*Z),
   HWall(app, 60*Z,50*Z, 90*Z),
   VWall(app, 90*Z,50*Z, 64*Z),
   HWall(app, 62*Z,13*Z, 66*Z),
   VWall(app, 62*Z,13*Z, 23*Z),
   HWall(app, 62*Z,23*Z, 66*Z),
   HWall(app, 70*Z,13*Z, 74*Z),
   VWall(app, 74*Z,13*Z, 23*Z),
   HWall(app, 70*Z,23*Z, 74*Z),
   HWall(app, 62*Z,34*Z, 66*Z),
   VWall(app, 62*Z,34*Z, 44*Z),
   HWall(app, 62*Z,44*Z, 66*Z),
   HWall(app, 70*Z,34*Z, 74*Z),
   VWall(app, 74*Z,34*Z, 44*Z),
   HWall(app, 70*Z,44*Z, 74*Z),
   HWall(app, 90*Z,16*Z,103*Z),
   VWall(app, 90*Z,16*Z, 44*Z),
   HWall(app, 90*Z,44*Z,123*Z),
   VWall(app,103*Z,16*Z, 64*Z),
   HWall(app,126*Z,44*Z,132*Z),
   HWall(app,103*Z,53*Z,120*Z),
   VWall(app,124*Z,53*Z, 64*Z),
   VWall(app, 96*Z, 0*Z, 10*Z),
   VWall(app,115*Z, 0*Z,  3*Z),
   VWall(app,115*Z, 6*Z, 12*Z),
   HWall(app,115*Z,12*Z,122*Z),
   HWall(app,126*Z,12*Z,132*Z),

    #les guardiens
   HGuard(app, 13*Z,19*Z, 24*Z),
   VGuard(app,  3*Z,29*Z, 51*Z),
   VGuard(app, 11*Z,47*Z, 61*Z),
   HGuard(app, 13*Z,44*Z, 42*Z),
   VGuard(app, 28*Z, 2*Z, 18*Z),
   VGuard(app, 38*Z, 3*Z, 15*Z),
   HGuard(app, 28*Z,23*Z, 36*Z),
   HGuard(app, 43*Z,21*Z, 53*Z),
   HGuard(app, 41*Z,15*Z, 59*Z),
   VGuard(app, 49*Z,25*Z, 50*Z),
   VGuard(app, 42*Z,45*Z, 61*Z),
   VGuard(app, 55*Z,45*Z, 61*Z),
   VGuard(app, 58*Z,23*Z, 42*Z),
   HGuard(app, 49*Z, 6*Z, 65*Z),
   VGuard(app, 68*Z, 7*Z, 12*Z),
   VGuard(app, 68*Z,21*Z, 35*Z),
   VGuard(app, 68*Z,42*Z, 48*Z),
   VGuard(app, 77*Z,21*Z, 35*Z),
   VGuard(app, 85*Z,21*Z, 35*Z),
   HGuard(app, 84*Z,47*Z, 99*Z),
   VGuard(app, 93*Z,49*Z, 61*Z),
   HGuard(app, 84*Z,13*Z,107*Z),
   HGuard(app,103*Z, 4*Z,117*Z),
   VGuard(app,124*Z, 8*Z, 15*Z),
   HGuard(app,105*Z,23*Z,129*Z),
   HGuard(app,105*Z,27*Z,129*Z),
   HGuard(app,105*Z,31*Z,129*Z),
   HGuard(app,105*Z,35*Z,129*Z),
   HGuard(app,105*Z,39*Z,129*Z),
   HGuard(app,105*Z,42*Z,129*Z),
   HGuard(app,105*Z,47*Z,129*Z),
   HGuard(app,105*Z,50*Z,118*Z),
   VGuard(app,126*Z,50*Z, 61*Z),

    #les boites
   Box(app,  3*Z,62*Z),
   Box(app, 34*Z, 2*Z),
   Box(app, 44*Z, 2*Z),
   Box(app, 45*Z,31*Z),
   Box(app, 64*Z,17*Z),
   Box(app, 64*Z,40*Z),
   Box(app, 96*Z,62*Z),
   Box(app,130*Z, 2*Z),
   Box(app,130*Z,62*Z),

    #les autres choses
   Exit(app,2*Z,2*Z),
   app.target,
   app.player,
   ]

class Entity:
 def __init__(self,app,*args):
  self.iswall=False
  self.solid=False
  self.isbullet=False
  self.dx=self.dy=0
  self.candestroy=True
  self.app=app     #  keep reference to application
  self.redraw=True #  if we need to redraw the sprite
  self.vision=0    #  the field of vision of the guardians
  self.imgwidth=None
  self.imgheight=None

  self.init(*args) #  send the other arguments for the init
 def init(self):   # run the instance-specific init code
  pass
 def update(self): # do the object housekeeping code
  pass
 def draw(self):
  pass
 def in_zone(self,x,y,w,h):
  if self.x<(x-w)-self.width:
   return False
  if self.y<(y-h)-self.height:
   return False
  if self.x>(x+w)+self.width:
   return False
  if self.y>(y+h)+self.height:
   return False
  return True
 def render(self): # executed once per frame to render the sprite
  if self.imgwidth==None:
   self.imgwidth=int(self.width)
  if self.imgheight==None:
   self.imgheight=int(self.height)
  if self.redraw:  #  if we need to redraw the sprite
   self.surface=pygame.Surface((self.imgwidth,self.imgheight)) #   then create a new surface for it
   self.surface.fill((0,0,0))
   self.draw()     #  execute the instance-specific drawing code
   self.surface.set_colorkey((0,0,0))
   self.redraw=False  #   and the redraw is now done
  return self.surface #  return our (newly-drawn or not) sprite


class VGuard(Entity):
 def init(self,x,y1,y2):
  self.width=self.height=16
  self.y1=min(y1,y2)+self.height/2
  self.y2=max(y1,y2)+self.height/2
  self.y=random.randint(self.y1,self.y2)+self.height/2
  self.x=x-self.width/2
  self.startx=x
  self.dx=0
  self.dy=0
  self.imgwidth=self.imgheight=32
  self.vision=128
  self.following=self.app.player
  self.trace=[(self.x,self.y1),]
  self.awake=False
  self.lastdir=0
  self.steptime=0
  self.speeds=[1.5,2.0]
  self.reload=pygame.time.get_ticks()
  self.steptick=pygame.time.get_ticks()
 def dohead(self,tracelist):
  self.awake=True
  if self.trace[0]==(self.startx,self.y2) or self.trace[0]==(self.startx,self.y1):
   self.trace=[(self.x,self.y)]
   self.reload=pygame.time.get_ticks()+random.randint(250,500)
  self.trace.append((self.following.x,self.following.y))
  tracelist.append(self)
  for ele in self.app.entities:
   if ele in tracelist:
    continue
   if not ele.vision:
    continue
   if (self.x-ele.x)**2+(self.y-ele.y)**2<self.vision**2+ele.vision**2 and self.app.can_see(self.x,self.y,ele.x,ele.y):
    ele.dohead(tracelist)

 def followbullet(self,bullet):
  if self.trace[0]==(self.startx,self.y2) or self.trace[0]==(self.startx,self.y1):
   self.trace=[(self.x,self.y)]
   if self.app.difficulty:
    self.trace.append((bullet.startx,bullet.starty))
   else:
    self.trace.append(((bullet.startx+bullet.x)/2,(bullet.starty+bullet.y)/2))
   self.trace.append((bullet.x,bullet.y))

 def update(self):
  if len(self.trace)<2:
   for ele in self.app.entities:
    if ele.isbullet:
     if (self.x-ele.x)**2+(self.y-ele.y)**2<self.vision**2 and self.app.can_see(self.x,self.y,ele.x,ele.y):
      self.followbullet(ele)
  if (self.x-self.following.x)**2+(self.y-self.following.y)**2<self.vision**2 and self.app.can_see(self.x,self.y,self.following.x,self.following.y):
   self.dohead([])
  else:
   while len(self.trace)>3 and self.app.can_see(self.trace[-1][0],self.trace[-1][1],*self.trace[-3]):
    self.trace.pop(-2)
   if (self.x-self.trace[-1][0])**2+(self.y-self.trace[-1][1])**2<self.width*self.height:
    if len(self.trace)>1:
     self.trace.pop(-1)
     self.awake=False
    else:
     if abs(self.y-self.y1)<abs(self.y-self.y2):  #go to the nearest point of our line
      self.trace=[(self.startx,self.y2),]
     else:
      self.trace=[(self.startx,self.y1),]
  self.headingx=self.trace[-1][0]
  self.headingy=self.trace[-1][1]
  angle=math.atan2(self.headingy-self.y,self.headingx-self.x)
  self.dx=math.cos(angle)*self.speeds[self.awake]
  self.dy=math.sin(angle)*self.speeds[self.awake]
  self.x+=self.dx
  self.y+=self.dy
  self.remake_draw()
  if self.awake and pygame.time.get_ticks()-self.reload>500:
   self.shoot()
 def shoot(self):
  self.app.entities.append(Bullet(self.app,self.x,self.y,self.dx*8,self.dy*8))
  self.reload=pygame.time.get_ticks()+random.randint(250,500)
 def remake_draw(self):
  if self.dx==0 and self.dy==0:
   return False
  direction=math.atan2(self.dy,self.dx)
  direction/=math.pi
  direction=int(direction*4)
  direction%=8
  if direction!=self.lastdir:
   self.lastdir=direction
   self.redraw=True
  if pygame.time.get_ticks()-self.steptick>(1.0/(self.dx**2+self.dy**2))*400:
   self.steptime+=1
   self.steptick=pygame.time.get_ticks()
   self.redraw=True
 def draw(self):
  imglist=["guard-e","guard-se","guard-s","guard-sw","guard-w","guard-nw","guard-n","guard-ne"]
  img=self.app.gfx[imglist[self.lastdir]+str((self.steptime%4)+1)]
  pygame.transform.scale(img,self.surface.get_size(),self.surface)


class HGuard(Entity):
 def init(self,x1,y,x2):
  self.width=self.height=16
  self.x1=min(x1,x2)+self.width/2
  self.x2=max(x1,x2)+self.width/2
  self.x=random.randint(self.x1,self.x2)+self.width/2
  self.y=y-self.height/2
  self.starty=y
  self.dx=0
  self.dy=0
  self.imgwidth=self.imgheight=32
  self.vision=128
  self.following=self.app.player
  self.trace=[(self.x1,self.y),]
  self.awake=False
  self.lastdir=0
  self.steptime=0
  self.speeds=[1.5,2.0]
  self.reload=pygame.time.get_ticks()
  self.steptick=pygame.time.get_ticks()
 def dohead(self,tracelist):
  self.awake=True
  if self.trace[0]==(self.x1,self.starty) or self.trace[0]==(self.x2,self.starty):
   self.trace=[(self.x,self.y)]
   self.reload=pygame.time.get_ticks()+random.randint(250,500)
  self.trace.append((self.following.x,self.following.y))
  tracelist.append(self)
  for ele in self.app.entities:
   if ele in tracelist:
    continue
   if not ele.vision:
    continue
   if (self.x-ele.x)**2+(self.y-ele.y)**2<self.vision**2+ele.vision**2 and self.app.can_see(self.x,self.y,ele.x,ele.y):
    ele.dohead(tracelist)

 def followbullet(self,bullet):
  if self.trace[0]==(self.x1,self.starty) or self.trace[0]==(self.x2,self.starty):
   self.trace=[(self.x,self.y)]
   if self.app.difficulty:
    self.trace.append((bullet.startx,bullet.starty))
   else:
    self.trace.append(((bullet.startx+bullet.x)/2,(bullet.starty+bullet.y)/2))
   self.trace.append((bullet.x,bullet.y))

 def update(self):
  if len(self.trace)<2:
   for ele in self.app.entities:
    if ele.isbullet:
     if (self.x-ele.x)**2+(self.y-ele.y)**2<self.vision**2 and self.app.can_see(self.x,self.y,ele.x,ele.y):
      self.followbullet(ele)
  if (self.x-self.following.x)**2+(self.y-self.following.y)**2<self.vision**2 and self.app.can_see(self.x,self.y,self.following.x,self.following.y):
   self.dohead([])
  else:
   while len(self.trace)>3 and self.app.can_see(self.trace[-1][0],self.trace[-1][1],*self.trace[-3]):
    self.trace.pop(-2)
   if (self.x-self.trace[-1][0])**2+(self.y-self.trace[-1][1])**2<self.width*self.height:
    if len(self.trace)>1:
     self.trace.pop(-1)
     self.awake=False
    else:
     if abs(self.x-self.x1)<abs(self.x-self.x2):  #go to the nearest point of our line
      self.trace=[(self.x2,self.starty),]
     else:
      self.trace=[(self.x1,self.starty),]
  self.headingx=self.trace[-1][0]
  self.headingy=self.trace[-1][1]
  angle=math.atan2(self.headingy-self.y,self.headingx-self.x)
  self.dx=math.cos(angle)*self.speeds[self.awake]
  self.dy=math.sin(angle)*self.speeds[self.awake]
  self.x+=self.dx
  self.y+=self.dy
  self.remake_draw()
  if self.awake and pygame.time.get_ticks()-self.reload>500:
   self.shoot()
 def shoot(self):
  self.app.entities.append(Bullet(self.app,self.x,self.y,self.dx*8,self.dy*8))
  self.reload=pygame.time.get_ticks()+random.randint(250,500)
 def remake_draw(self):
  if self.dx==0 and self.dy==0:
   return False
  direction=math.atan2(self.dy,self.dx)
  direction/=math.pi
  direction=int(direction*4)
  direction%=8
  if direction!=self.lastdir:
   self.lastdir=direction
   self.redraw=True
  if pygame.time.get_ticks()-self.steptick>(1.0/(self.dx**2+self.dy**2))*400:
   self.steptime+=1
   self.steptick=pygame.time.get_ticks()
   self.redraw=True
 def draw(self):
  imglist=["guard-e","guard-se","guard-s","guard-sw","guard-w","guard-nw","guard-n","guard-ne"]
  img=self.app.gfx[imglist[self.lastdir]+str((self.steptime%4)+1)]
  pygame.transform.scale(img,self.surface.get_size(),self.surface)

class HWall(Entity):
 def init(self,x1,y,x2):
  self.thickness=16
  self.width=abs(x2-x1)+self.thickness
  self.x=min(x1,x2)+self.width/2-self.thickness/2
  self.x1=min(x1,x2)
  self.x2=max(x1,x2)
  self.candestroy=False
  self.y=y
  self.height=self.thickness
  self.solid=True
  self.iswall=True
 def update(self):
  for entity in self.app.entities:
   if entity.solid:
    continue
   if self.x-(self.width/2)<entity.x<self.x+self.width/2:
    if self.y-(entity.height+self.height/2)<entity.y<self.y+self.height/2+entity.height:
     if entity.isbullet:
      self.app.entities.remove(entity)
      return
     if entity.y<self.y:
      entity.y=self.y-(entity.height)-8
     else:
      entity.y=self.y+(entity.height)+8
     entity.awake=False

 def is_near(self,x,y,vision):
  if self.y<y-vision:
   return False
  if self.y>y+vision:
   return False
  if self.x2<x-vision:
   return False
  if self.x1>x+vision:
   return False
  if y==self.y:
   return False
  return True
 
 def block_vision(self,surface,x,y,vision):
  if self.y<y-vision:
   return
  if self.y>y+vision:
   return
  if self.x2<x-vision:
   return
  if self.x1>x+vision:
   return
  if y-1<self.y<y+1:
   return
  angle1=math.atan2(self.y-y,self.x1-x)
  angle2=math.atan2(self.y-y,self.x2-x)
  dist1=vision/math.sin(angle1)
  dist2=vision/math.sin(angle2)
  x3=math.cos(angle1)*abs(dist1)+x
  x4=math.cos(angle2)*abs(dist2)+x
  if self.y>y:
   pygame.draw.polygon(surface,(0,0,0,0),(
   (int(self.x1-x+vision),int(self.y-y+vision)),
   (int(x3-x+vision),int(vision*2)),
   (int(x4-x+vision),int(vision*2)),
   (int(self.x2-x+vision),int(self.y-y+vision))))
  else:
   pygame.draw.polygon(surface,(0,0,0,0),(
   (int(self.x1-x+vision),int(self.y-y+vision)),
   (int(x3-x+vision),0),
   (int(x4-x+vision),0),
   (int(self.x2-x+vision),int(self.y-y+vision))))

 def draw(self):
  for i in range(self.surface.get_width()/16+1):
   self.surface.blit(self.app.gfx["wall-h"],(i*16,0))
  

class VWall(Entity):
 def init(self,x,y1,y2):
  self.thickness=16
  self.height=abs(y2-y1)
  self.x=x
  self.y=min(y1,y2)+self.height/2
  self.width=self.thickness
  self.candestroy=False
  self.solid=True
  self.iswall=True
  self.y1=min(y1,y2)
  self.y2=max(y1,y2)
 def update(self):
  for entity in self.app.entities:
   if entity.solid:
    continue
   if self.x-(entity.width+self.width/2)<entity.x<self.x+self.width/2+entity.width:
    if self.y-(self.height/2)<entity.y<self.y+self.height/2:
     if entity.isbullet:
      self.app.entities.remove(entity)
      return
     if entity.x<self.x:
      entity.x=self.x-(entity.width)-8
     else:
      entity.x=self.x+(entity.width)+8
     entity.awake=False

 def is_near(self,x,y,vision):
  if self.x<x-vision:
   return False
  if self.x>x+vision:
   return False
  if self.y2<y-vision:
   return False
  if self.y1>y+vision:
   return False
  if x-1<self.x<x+1:
   return False
  return True

 def block_vision(self,surface,x,y,vision):
  angle1=math.atan2(self.y1-y,self.x-x)
  angle2=math.atan2(self.y2-y,self.x-x)
  dist1=vision/math.cos(angle1)
  dist2=vision/math.cos(angle2)
  y3=math.sin(angle1)*abs(dist1)+y
  y4=math.sin(angle2)*abs(dist2)+y
  if self.x>x:
   pygame.draw.polygon(surface,(0,0,0,0),(
   (int(self.x-x+vision),int(self.y1-y+vision)),
   (int(vision*2),int(y3-y+vision)),
   (int(vision*2),int(y4-y+vision)),
   (int(self.x-x+vision),int(self.y2-y+vision))))
  else:
   pygame.draw.polygon(surface,(0,0,0,0),(
   (int(self.x-x+vision),int(self.y1-y+vision)),
   (0,int(y3-y+vision)),
   (0,int(y4-y+vision)),
   (int(self.x-x+vision),int(self.y2-y+vision))))

 def draw(self):
  for i in range(self.surface.get_height()/16+1):
   self.surface.blit(self.app.gfx["wall-v"],(0,i*16))

class Target(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.width=self.height=64
  self.solid=True
  self.candestroy=False
  self.destructionstart=0
  self.destructionmode=False
  self.waittime=5000
  #if self.app.difficulty:
  # self.killtime=25000
  #else:
  self.killtime=35000
 def update(self):
  if not self.destructionmode:
   if self.x-(self.width/2+self.app.player.width)<self.app.player.x<self.x+(self.width/2+self.app.player.width) and self.y-(self.height/2+self.app.player.height)<self.app.player.y<self.y+(self.height/2+self.app.player.height):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
     if self.destructionstart==0:
      self.destructionstart=pygame.time.get_ticks()
     if pygame.time.get_ticks()-self.destructionstart>self.waittime:
      self.destructionmode=True
    else:
     self.destructionstart=0
   else:
    self.destructionstart=0
  else:
   if pygame.time.get_ticks()-self.destructionstart>self.killtime+self.waittime:
    self.app.gameover=True
   self.redraw=True
    
 def draw(self):
  pygame.transform.scale(self.app.gfx["target"],self.surface.get_size(),self.surface)
    
  

class Exit(Entity):
 def init(self,x,y):
  self.width=self.height=32
  self.x=x
  self.y=y
  self.solid=True
 def update(self):
  if self.app.target.destructionmode:
   if self.x-(self.width/2+self.app.player.width)<self.app.player.x<self.x+(self.width/2+self.app.player.width) and self.y-(self.height/2+self.app.player.height)<self.app.player.y<self.y+(self.height/2+self.app.player.height):
    self.app.gameover=True
    self.app.levels.level+=1
 def draw(self):
  pygame.transform.scale(self.app.gfx["exit"],self.surface.get_size(),self.surface)

class Font:
 TABSIZE=8
 def __init__(self,bgcol,fgcol,width=8,height=8):
  self.width=width
  self.height=height
  self.font={}
  font=open(os.path.join("Images","font.bin"),"rb")
  letter=0
  for i in range(96):
   s=pygame.Surface((8,8))
   s.fill((255,0,255))
   s2=pygame.Surface((8,8))
   s2.fill((255,0,255))
   for j in range(8):
    v=font.read(1)
    if len(v)==0:
     break
    byte=ord(v)
    for k in range(8):
     if byte&1:
      s.set_at((7-k,j),fgcol)
      s2.set_at((7-k+1,j+1),(127,127,127))
     byte>>=1
   s2=pygame.transform.scale(s2,(width,height))
   s=pygame.transform.scale(s,(width,height))
   s2.set_colorkey((255,0,255))
   s.set_colorkey((255,0,255))
   s2.blit(s,(0,0))
   self.font[chr(i+32)]=s2
 def draw_text(self,text,surface,x,y):
   xpos=x
   ypos=y
   for letter in text:
    if letter=="\n":
     xpos=x
     ypos+=self.height
    elif letter=="\t":
     xchr=(xpos-x)/self.width
     xpos+=(self.TABSIZE-(xchr%self.TABSIZE))*self.width
    elif letter in self.font:
     surface.blit(self.font[letter],(xpos,ypos))
     xpos+=self.width
     
class Bullet(Entity):
 def init(self,x,y,dx,dy):
  self.width=self.height=8
  self.x=x
  self.y=y
  self.startx=self.x
  self.starty=self.y
  self.dx=dx
  self.dy=dy
  self.isbullet=True
  self.app.snd_shoot.play()
 def update(self):
  self.x+=self.dx
  self.y+=self.dy
  for entity in self.app.entities:
   if entity==self:
    continue
   if not entity.iswall:
    if entity.x-entity.width/2<self.x<entity.x+entity.width/2:
     if entity.y-entity.height/2<self.y<entity.y+entity.height/2:
      self.app.entities.remove(entity)
 def draw(self):
  pygame.draw.circle(self.surface,(127,127,127),(4,4),4)

class Box(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.width=self.height=32
 def update(self):
  if self.x-self.width/2-self.app.player.width<self.app.player.x<self.x+self.width/2+self.app.player.width:
   if self.y-self.height/2-self.app.player.height<self.app.player.y<self.y+self.height/2+self.app.player.height:
    score=random.randint(4,8)
    self.app.player.bullets+=score
    self.app.entities.append(BoxText(self.app,self.x,self.y,"+"+str(score)))
    self.app.entities.remove(self) 
 def draw(self):
  pygame.transform.scale(self.app.gfx["box"],self.surface.get_size(),self.surface)

class BoxText(Entity):
 def init(self,x,y,score):
  self.text=score
  self.width=32*len(self.text)
  self.height=32
  self.x=x
  self.y=y
  self.dx=0
  self.dy=-1
  self.spawntime=pygame.time.get_ticks()
 def update(self):
  self.x+=self.dx
  self.y+=self.dy
  if pygame.time.get_ticks()-self.spawntime>1000:
   self.app.entities.remove(self)
 def draw(self):
  self.app.font.draw_text(self.text,self.surface,0,0)

class Player(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.dx=0
  self.dy=0
  self.width=self.height=16
  self.imgwidth=self.imgheight=32
  self.bullets=0
  self.imgnow="player-w"
  self.steptick=pygame.time.get_ticks()
  self.steptime=0
  self.lastdir=4
 def update(self):
  if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_z] or pygame.key.get_pressed()[pygame.K_w]:
   self.dy=-4
   self.imgnow="player-n"
  elif pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
   self.dy=4
   self.imgnow="player-s"
  else:
   self.dy=0
  if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_q] or pygame.key.get_pressed()[pygame.K_a]:
   self.dx=-4
   self.imgnow="player-w"
  elif pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
   self.dx=4
   self.imgnow="player-e"
  else:
   self.dx=0
  self.x+=self.dx
  self.y+=self.dy
  self.remake_draw()
 def remake_draw(self):
  if self.dx==0 and self.dy==0:
   return
  direction=math.atan2(self.dy,self.dx)
  direction/=math.pi
  direction=int(direction*4)
  direction%=8
  if direction!=self.lastdir:
   self.lastdir=direction
   self.redraw=True
  if pygame.time.get_ticks()-self.steptick>100:
   self.steptime+=1
   self.steptick=pygame.time.get_ticks()
   self.redraw=True
 def draw(self):
  imglist=["player-e","player-se","player-s","player-sw","player-w","player-nw","player-n","player-ne"]
  img=self.app.gfx[imglist[self.lastdir]+str((self.steptime%4)+1)]
  pygame.transform.scale(img,self.surface.get_size(),self.surface)

WIDTH=1024
HEIGHT=768

class Application:
 def __init__(self):
  self.entities=[] 
  pygame.init()
  self.displayinfo=pygame.display.Info()
  self.videowidth=self.displayinfo.current_w
  self.videoheight=self.displayinfo.current_h
  self.olddisplaysize=(WIDTH,HEIGHT)
  self.unset_fullscreen()
  self.clock=pygame.time.Clock()
  self.snd_shoot=pygame.mixer.Sound(os.path.join("Sounds","Shoot.wav"))
  self.levels=Level()
  self.show_splash()
 def init(self):
  self.scrollx=self.scrolly=0
  self.entities=self.levels.getNextLevel(self)
  self.difficulty=self.levels.level/len(self.levels.levels)
  self.gameover=False
 def set_fullscreen(self):
  self.olddisplaysize=self.display.get_size()
  self.display=pygame.display.set_mode((self.videowidth,self.videoheight),pygame.FULLSCREEN)
  self.fullscreen=True
  self.prepare_gfx()
 def unset_fullscreen(self): 
  self.display=pygame.display.set_mode( self.olddisplaysize,pygame.RESIZABLE)
  self.fullscreen=False
  self.prepare_gfx()
 def prepare_gfx(self):
  self.gfx={}
  for f in os.listdir("Images"):
   try:
    img=pygame.image.load(os.path.join("Images",f)).convert()
    self.gfx[f.split(".")[0]]=img
   except pygame.error:
    pass
  floor=self.gfx["floor"]
  self.background=pygame.Surface((self.display.get_width()+floor.get_width(),self.display.get_height()+floor.get_height()))
  for y in range(self.background.get_height()/floor.get_height()):
   for x in range(self.background.get_width()/floor.get_width()):
    self.background.blit(floor,(x*floor.get_width(),y*floor.get_height()))
  self.vision128awake=pygame.Surface((255,255),pygame.SRCALPHA)
  self.vision128asleep=pygame.Surface((255,255),pygame.SRCALPHA)
  self.vision128awake.fill((0,0,0,0))
  self.vision128asleep.fill((0,0,0,0))
  for i in range(128):
   pygame.draw.circle(self.vision128awake,(255,255,0,i*2),(128,128),128-i,0)
   pygame.draw.circle(self.vision128asleep,(255,255,0,i),(128,128),128-i,0)
 def show_splash(self):
  self.font=Font((255,0,255),(255,255,255),24,24)
  texte="""
   AGENT HILLER, BIENVENUE EN FRANCE.
   
   COMME VOUS LE SAVEZ DEJA LE PAYS EST SOUS
    L'OCCUPATION ALLEMANDE DEPUIS 1940.
    
   MAINTENANT LES FRANCAIS FABRIQUENT DES
    HELICES D'AVION POUR LA LUFTWAFFE.
    
   VOTRE PREMIERE MISSION CONSISTERA A VOUS
    INFILTREZ DANS L'USINE RATIER A FIGEAC
    ET DETRUIRE LE PROCHAIN CHARGEMENT.
    
   NOUS VOUS AVONS TROUVE UNE ARME, UN
    LUGER P08, SEULEMENT NOUS N'AVONS PAS
    LES MUNITIONS QUI VONT AVEC.
    
   VOUS DEVREZ EN TROUVER SUR PLACE.
   
   NOUS AVONS PASSE UN BON MOMENT A CREUSER
    UNE GALLERIE AVEC L'AIDE DE
    CERTAINS RESISTANTS,
    
   VOUS ENTREREZ ET SORTIREZ PAR LA LE PLUS
    VITE POSSIBLE AVANT DE FAIRE
    EXPLOSER LES HELICES.


   BIEN VOUS AVEZ COMPRIS,
    ALORS AU BOULOT AGENT HILLER!"""
  scrolly=self.display.get_height()
  showingsplash=True
  while showingsplash:
   self.display.blit(self.background,(0,0))
   self.font.draw_text(texte,self.display,-64,scrolly)
   pygame.display.flip()
   if scrolly<-texte.count("\n")*24-48:
    showingsplash=False
   scrolly-=1
   for event in pygame.event.get():
    if event.type==pygame.QUIT:
     pygame.quit()
     sys.exit()
    if event.type==pygame.KEYDOWN:
     showingsplash=False
    if event.type==pygame.MOUSEBUTTONDOWN:
     showingsplash=False
   if scrolly>24:
    self.clock.tick(60)
   else:
    self.clock.tick(50)
  self.font=Font((255,0,255),(255,255,255),32,32)

 def can_see(self,startx,starty,endx,endy):
  for ele in self.entities:
   if ele.iswall:
    if find_intersection((startx,starty),(endx,endy),(ele.x-ele.width/2,ele.y-ele.height/2),(ele.x+ele.width/2,ele.y+ele.height/2)):
     return False
  return True
   
  
 def update(self):
  if self.player not in self.entities:
   self.gameover=True
  if self.gameover:
   self.init()
  for event in pygame.event.get():
   if event.type==pygame.VIDEORESIZE:
    pygame.display.set_mode(event.size,pygame.RESIZABLE)
    self.prepare_gfx()
   if event.type==pygame.QUIT:
    pygame.quit()
    sys.exit()
   if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_f:
     if self.fullscreen:
      self.unset_fullscreen()
     else:
      self.set_fullscreen()
    if event.key==pygame.K_ESCAPE:
     pygame.quit()
     sys.exit()
    if event.key==pygame.K_RETURN:
     pygame.display.set_caption("PAUSE")
     paused=True
     while paused:
      for event in pygame.event.get():
       if event.type==pygame.KEYDOWN:
        paused=False
       if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
   if event.type==pygame.MOUSEBUTTONDOWN and self.player.bullets>0:
    px=(self.player.x)
    py=(self.player.y)
    x=event.pos[0]-px-self.scrollx
    y=event.pos[1]-py-self.scrolly
    dir=math.atan2(y,x)
    dx=math.cos(dir)*16
    dy=math.sin(dir)*16
    self.entities.append(Bullet(self,px,py,dx,dy))
    self.player.bullets-=1
  for entity in self.entities:
   entity.update()
  self.scrollx=-self.player.x+self.display.get_width()/2
  self.scrolly=-self.player.y+self.display.get_height()/2

 def render_statusbar(self):
  if not self.target.destructionmode:
   if self.target.destructionstart!=0:
    value=float(pygame.time.get_ticks()-self.target.destructionstart)/self.target.waittime
    self.display.fill((0,127,0),(0,0,int(self.display.get_width()*value),16))
  else:
   value=float(pygame.time.get_ticks()-self.target.destructionstart-self.target.waittime)/self.target.killtime
   #self.display.fill((127,0,0),(0,0,int(self.display.get_width()*value),16))
   timebeforedie=self.target.killtime-(pygame.time.get_ticks()-self.target.destructionstart-self.target.waittime)
   timebeforedie=int(timebeforedie/1000)
   self.font.draw_text("EXPLOSION IN "+str(timebeforedie)+" SECONDS",self.display,8,self.display.get_height()-32)
  txt=str(self.player.bullets)
  self.font.draw_text(txt,self.display,8,8)
  if self.difficulty==True:
   txt="HARD MODE ENABLED"
   self.font.draw_text(txt,self.display,self.display.get_width()-len(txt)*32-8,8)
 def render(self):
  self.display.blit(self.background,(self.scrollx%self.gfx["floor"].get_width()-8,self.scrolly%self.gfx["floor"].get_height()-8))
  for entity in self.entities:
   if not entity.in_zone(self.player.x,self.player.y,self.display.get_width(),self.display.get_height()):
    continue
   if entity.vision:
    #surface=pygame.Surface((entity.vision*2,entity.vision*2),pygame.SRCALPHA)
    #surface.fill((0,0,0,0))
    if entity.awake:
     #for i in range(entity.vision):
     # pygame.draw.circle(surface,(255,255,0,i),(entity.vision,entity.vision),128-i,0)
     surface=self.vision128awake.copy()
    else:
     #for i in range(entity.vision):
     # pygame.draw.circle(surface,(127,127,0,i),(entity.vision,entity.vision),128-i,0)
     surface=self.vision128asleep.copy()
    for element in self.entities:
     if element.iswall and element.is_near(entity.x,entity.y,entity.vision):
      element.block_vision(surface,entity.x,entity.y,entity.vision)
    entity.lightning=surface
    self.display.blit(surface,(self.scrollx+int(entity.x-entity.vision),self.scrolly+int(entity.y-entity.vision)))
  for entity in self.entities:
   surface=entity.render()
   self.display.blit(surface,(self.scrollx+(entity.x-entity.imgwidth/2),self.scrolly+(entity.y-entity.imgheight/2)))
  self.render_statusbar()
  pygame.display.flip()
  self.clock.tick(60)
  pygame.display.set_caption("fps:"+str(self.clock.get_fps()))
 def run(self):
  self.init()
  self.gameover=True
  time=1
  while 1:
   oldtime=pygame.time.get_ticks()
   for i in range(int(time)+1):
    self.update()
   self.render()
   newtime=pygame.time.get_ticks()
   time=1000.0/(newtime-oldtime)
   time=60.0/time
   
if __name__=="__main__":
 try:
  Application().run()
 finally:
  pygame.quit()
 
