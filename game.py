import pygame,random,math,sys

class Level:
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

class Entity:
 def __init__(self,app,*args):
  self.solid=False
  self.isbullet=False
  self.dx=self.dy=0
  self.app=app     #  keep reference to application
  self.redraw=True #  if we need to redraw the sprite
  self.vision=0    #  the field of vision of the guardians
  self.init(*args) #  send the other arguments for the init
 def init(self):   # run the instance-specific init code
  pass
 def update(self): # do the object housekeeping code
  pass
 def draw(self):
  pass
 def render(self): # executed once per frame to render the sprite
  if self.redraw:  #  if we need to redraw the sprite
   self.surface=pygame.Surface((self.width,self.height)) #   then create a new surface for it
   self.draw()     #  execute the instance-specific drawing code
   self.redraw=False  #   and the redraw is now done
  return self.surface #  return our (newly-drawn or not) sprite


class HGuard(Entity):
 def init(self,x1,y,x2):
  self.x1=min(x1,x2)
  self.x2=max(x1,x2)
  self.x=(x1+x2)/2
  self.y=y
  self.width=self.height=16
  self.vision=128
  self.awake=False
  self.dx=random.randint(0,1)*2-1
  self.dy=0
 def update(self):
  self.walk()
  self.x+=self.dx
  self.y+=self.dy
 def walk(self):
  if self.x<self.x1:
   self.dx=1
  elif self.x>self.x2:
   self.dx=-1
 def shoot(self):
  self.app.entities.append(Bullet(self.app,self.x,self.y,-self.dx*8,-self.dy*8))
 def draw(self):
  if self.awake:
   self.surface.fill((255,0,0))
  else:
   self.surface.fill((127,0,0))

class VGuard(Entity):
 def init(self,x,y1,y2):
  self.y1=min(y1,y2)
  self.y2=max(y1,y2)
  self.y=(y1+y2)/2
  self.x=x
  self.width=self.height=16
  self.vision=128
  self.awake=False
  self.dx=0
  self.dy=random.randint(0,1)*2-1
 def update(self):
  self.walk()
  self.x+=self.dx
  self.y+=self.dy
 def walk(self):
  if self.y<self.y1:
   self.dy=1
  elif self.y>self.y2:
   self.dy=-1
 def shoot(self):
  self.app.entities.append(Bullet(self.app,self.x,self.y,-self.dx*8,-self.dy*8))
 def draw(self):
  if self.awake:
   self.surface.fill((255,0,0))
  else:
   self.surface.fill((127,0,0))


class Nazi(Entity):  # the guardians that goes after you
 def init(self,x,y):  # initialize the nazi
  self.x=x            #  register our start position
  self.y=y
  self.dx=self.dy=0   #  the horizontal and vertical speed
  self.dir=random.random()*math.pi*2  # the direction
  self.width=self.height=16 #  width and height
  self.awake=False    #  if we are chasing a player
  self.vision=144
  self.speedawake=2.0
  self.speedasleep=1.5
  #  the field of vision
  self.lastawake=0    #  the last time that we were awaken
 def update(self):
   # look how far away the player is
  distance=(self.x-self.app.player.x)**2+(self.y-self.app.player.y)**2
   # if we see the player
  if distance<self.vision**2:
    # if we were patrolling
   if self.awake==False:
      #  fire a redraw
    self.redraw=True
    # keep awake
   self.awake=True
   self.lastawake=pygame.time.get_ticks()
    # test if there are any other guards near to awaken
   for entity in self.app.entities:
    if entity.vision>0 and entity.awake==False: # if we have to deal with an asleep guardian
     distance=(self.x-entity.x)**2+(self.y-entity.y)**2
     if distance<(self.vision+entity.vision)**2: # if he is close enough
      entity.awake=True  #  awaken him
      entity.lastawake=self.lastawake
      entity.redraw=True
  elif self.awake:
   if pygame.time.get_ticks()-self.lastawake>3000:
    self.awake=False
    self.redraw=True
  if not self.awake:
   self.dir+=(random.random()*2-1)/8
   for entity in self.app.entities:
    if entity.isbullet: # if a bullet is flying by
     distance=(self.x-entity.x)**2+(self.y-entity.y)**2
     if distance<self.vision**2: # if it is close enough
      self.dir=math.atan2(entity.dy,entity.dx) # look what is happening here
  else:
   x=self.x-self.app.player.x
   y=self.y-self.app.player.y
   self.dir=math.atan2(y,x)
   if not random.randint(0,64):
    self.shoot()
  self.dx=math.cos(self.dir)
  self.dy=math.sin(self.dir)
  if self.awake:
   self.dx*=self.speedawake
   self.dy*=self.speedawake
  else:
   self.dx*=self.speedasleep
   self.dy*=self.speedasleep
  self.x-=self.dx
  self.y-=self.dy
 def shoot(self):
  self.app.entities.append(Bullet(self.app,self.x,self.y,-self.dx*8,-self.dy*8))
 def draw(self):
  if self.awake:
   self.surface.fill((255,0,0))
  else:
   self.surface.fill((127,0,0))


class Wall(Entity):
 def init(self,x,y,width,height):
  self.x=x+width/2
  self.y=y+height/2
  self.width=width
  self.height=height
  self.solid=True
 def update(self):
  for entity in self.app.entities:
   if entity.solid:
    continue
   if self.x-(entity.width+self.width/2)<entity.x<self.x+self.width/2+entity.width:
    if self.y-(entity.height+self.height/2)<entity.y<self.y+self.height/2+entity.height:
     if entity.isbullet:
      self.app.entities.remove(entity)
      return
     if self.width<self.height:
      if entity.x<self.x:
       entity.x=self.x-(entity.width)-8
      if entity.x>self.x:
       entity.x=self.x+(entity.width)+8
     else:
      if entity.y<self.y:
       entity.y=self.y-(entity.height)-8
      if entity.y>self.y:
       entity.y=self.y+(entity.height)+8
 def draw(self):
  self.surface.fill((127,127,127))


class HWall(Entity):
 def init(self,x1,y,x2):
  self.thickness=16
  self.width=abs(x2-x1)+self.thickness
  self.x=min(x1,x2)+self.width/2-self.thickness
  self.y=y-self.thickness/2
  self.height=self.thickness
  self.solid=True
 def update(self):
  for entity in self.app.entities:
   if entity.solid:
    continue
   if self.x-(entity.width+self.width/2)<entity.x<self.x+self.width/2+entity.width:
    if self.y-(entity.height+self.height/2)<entity.y<self.y+self.height/2+entity.height:
     if entity.isbullet:
      self.app.entities.remove(entity)
      return
     if entity.y<self.y:
      entity.y=self.y-(entity.height)-8
     else:
      entity.y=self.y+(entity.height)+8
 def draw(self):
  self.surface.fill((127,127,127))
  
class VWall(Entity):
 def init(self,x,y1,y2):
  self.thickness=16
  self.height=abs(y2-y1)+self.thickness
  self.x=x-self.thickness/2
  self.y=min(y1,y2)+self.height/2-self.thickness
  self.width=self.thickness
  self.solid=True
 def update(self):
  for entity in self.app.entities:
   if entity.solid:
    continue
   if self.x-(entity.width+self.width/2)<entity.x<self.x+self.width/2+entity.width:
    if self.y-(entity.height+self.height/2)<entity.y<self.y+self.height/2+entity.height:
     if entity.isbullet:
      self.app.entities.remove(entity)
      return
     if entity.x<self.x:
      entity.x=self.x-(entity.width)-8
     else:
      entity.x=self.x+(entity.width)+8
 def draw(self):
  self.surface.fill((127,127,127))

class Target(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.width=self.height=32
  self.solid=True
  self.destructionstart=0
  self.destructionmode=False
  self.waittime=5000
  self.killtime=25000
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
  self.surface.fill((0,127,0))
  

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
 def draw(self):
  self.surface.fill((0,127,127))
    
class Bullet(Entity):
 def init(self,x,y,dx,dy):
  self.width=self.height=8
  self.x=x
  self.y=y
  self.dx=dx
  self.dy=dy
  self.isbullet=True
 def update(self):
  self.x+=self.dx
  self.y+=self.dy
  for entity in self.app.entities:
   if entity==self:
    continue
   if not entity.solid:
    if entity.x-entity.width/2<self.x<entity.x+entity.width/2:
     if entity.y-entity.height/2<self.y<entity.y+entity.height/2:
      self.app.entities.remove(entity)
 def draw(self):
  self.surface.fill((127,127,127))

class Box(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.width=self.height=12
 def update(self):
  if self.x-self.width/2-self.app.player.width<self.app.player.x<self.x+self.width/2+self.app.player.width:
   if self.y-self.height/2-self.app.player.height<self.app.player.y<self.y+self.height/2+self.app.player.height:
    self.app.player.bullets+=random.randint(4,8)
    self.app.entities.remove(self) 
 def draw(self):
  self.surface.fill((127,0,255))
  
class Player(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.dx=0
  self.dy=0
  self.width=self.height=16
  self.bullets=0
 def update(self):
  if pygame.key.get_pressed()[pygame.K_LEFT]:
   self.dx=-4
  elif pygame.key.get_pressed()[pygame.K_RIGHT]:
   self.dx=4
  else:
   self.dx=0
  if pygame.key.get_pressed()[pygame.K_UP]:
   self.dy=-4
  elif pygame.key.get_pressed()[pygame.K_DOWN]:
   self.dy=4
  else:
   self.dy=0
  self.x+=self.dx
  self.y+=self.dy
 def draw(self):
  self.surface.fill((255,255,255))

WIDTH=1024
HEIGHT=768

class Application:
 def __init__(self):
  self.entities=[]
  self.display=pygame.display.set_mode((WIDTH,HEIGHT))
  self.clock=pygame.time.Clock()
 def init(self):
  self.scrollx=self.scrolly=0
  self.gameover=False
  self.entities=Level().level1(self)
 def update(self):
  if self.player not in self.entities:
   self.gameover=True
  if self.gameover:
   self.init()
  for event in pygame.event.get():
   if event.type==pygame.QUIT:
    pygame.quit()
    sys.exit()
   if event.type==pygame.KEYDOWN:
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
   self.display.fill((127,0,0),(0,0,int(self.display.get_width()*value),16))
 def render(self):
  self.display.fill((0,0,0))
  for entity in self.entities:
   if entity.vision:
    surface=pygame.Surface((entity.vision*2,entity.vision*2),pygame.SRCALPHA)
    surface.fill((0,0,0,0))
    if entity.awake:
     pygame.draw.circle(surface,(255,255,0,127),(entity.vision,entity.vision),entity.vision,0)
    else:
     pygame.draw.circle(surface,(127,127,0,127),(entity.vision,entity.vision),entity.vision,0)
    self.display.blit(surface,(self.scrollx+int(entity.x-entity.vision),self.scrolly+int(entity.y-entity.vision)))
  for entity in self.entities:
   surface=entity.render()
   self.display.blit(surface,(self.scrollx+(entity.x-entity.width/2),self.scrolly+(entity.y-entity.height/2)))
  self.render_statusbar()
  pygame.display.flip()
  self.clock.tick(60)
  pygame.display.set_caption("bullets left:"+str(self.player.bullets))
 def run(self):
  self.init()
  while 1:
   self.update()
   self.render()
   
   
if __name__=="__main__":
 try:
  Application().run()
 finally:
  pygame.quit()
 
