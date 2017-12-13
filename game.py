import pygame,random,math,sys

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
 def render(self): # executed once per frame to render the sprite
  if self.redraw:  #  if we need to redraw the sprite
   self.surface=pygame.Surface((self.width,self.height)) #   then create a new surface for it
   self.draw()     #  execute the instance-specific drawing code
   self.redraw=False  #   and the redraw is now done
  return self.surface #  return our (newly-drawn or not) sprite


class Nazi(Entity):  # the guardians that goes after you
 def init(self,x,y):  # initialize the nazi
  self.x=x            #  register our start position
  self.y=y
  self.dx=self.dy=0   #  the horizontal and vertical speed
  self.dir=random.random()*math.pi*2  # the direction
  self.width=self.height=16 #  width and height
  self.awake=False    #  if we are chasing a player
  self.vision=128
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
   if not random.randint(0,128):
    self.shoot()
  self.dx=math.cos(self.dir)*2
  self.dy=math.sin(self.dir)*2
  if self.awake:
   self.dx*=1
   self.dy*=1
  else:
   self.dx*=0.5
   self.dy*=0.5
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

class Target(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.width=self.height=32
  self.solid=True
  self.destructionstart=0
  self.destructionmode=False
 def update(self):
  if not self.destructionmode:
   if self.x-(self.width/2+self.app.player.width)<self.app.player.x<self.x+(self.width/2+self.app.player.width) and self.y-(self.height/2+self.app.player.height)<self.app.player.y<self.y+(self.height/2+self.app.player.height):
    if pygame.key.get_pressed()[pygame.K_SPACE]:
     if self.destructionstart==0:
      self.destructionstart=pygame.time.get_ticks()
     if pygame.time.get_ticks()-self.destructionstart>3000:
      self.destructionmode=True
    else:
     self.destructionstart=0
   else:
    self.destructionstart=0
  else:
   if pygame.time.get_ticks()-self.destructionstart>10000:
    self.app.gameover=True
   self.redraw=True
    
 def draw(self):
  self.surface.fill((0,127,0))
  

class Exit(Entity):
 def init(self,x,y):
  self.width=self.height=32
  self.x=x
  self.y=y
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
 def init(self):
  self.x=320
  self.y=240
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
  self.gameover=False
  self.player=Player(self)
  self.target=Target(self,640,240)
  self.entities=[Exit(self,320,240),self.target]
  for i in range(4):
   x=random.randint(0,self.display.get_width())
   y=random.randint(0,self.display.get_height())
   self.entities.append(Nazi(self,x,y))
  for i in range(4):
   x=random.randint(0,self.display.get_width())
   y=random.randint(0,self.display.get_height())
   self.entities.append(Box(self,x,y))
  for box in ((0,0,WIDTH,16),(0,0,16,HEIGHT),(0,HEIGHT-16,WIDTH,16),(WIDTH-16,0,16,HEIGHT),(WIDTH/2-8,0,16,HEIGHT/2)):
   self.entities.append(Wall(self,*box))
  self.entities.append(self.player)
 def update(self):
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
    x=event.pos[0]-px
    y=event.pos[1]-py
    dir=math.atan2(y,x)
    dx=math.cos(dir)*16
    dy=math.sin(dir)*16
    self.entities.append(Bullet(self,px,py,dx,dy))
    self.player.bullets-=1
  for entity in self.entities:
   entity.update()
 def render_statusbar(self):
  if not self.target.destructionmode:
   if self.target.destructionstart!=0:
    value=(pygame.time.get_ticks()-self.target.destructionstart)/3000.0
    self.display.fill((0,127,0),(0,0,int(self.display.get_width()*value),16))
  else:
   value=(pygame.time.get_ticks()-self.target.destructionstart-3000)/7000.0
   self.display.fill((127,0,0),(0,0,int(self.display.get_width()*value),16))
 def render(self):
  self.display.fill((0,0,0))
  for entity in self.entities:
   if entity.vision:
    surface=pygame.Surface((256,256),pygame.SRCALPHA)
    surface.fill((0,0,0,0))
    if entity.awake:
     pygame.draw.circle(surface,(255,255,0,127),(128,128),128,0)
    else:
     pygame.draw.circle(surface,(127,127,0,127),(128,128),128,0)
    self.display.blit(surface,(int(entity.x-128),int(entity.y-128)))
  for entity in self.entities:
   surface=entity.render()
   self.display.blit(surface,(entity.x-entity.width/2,entity.y-entity.height/2))
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
 
