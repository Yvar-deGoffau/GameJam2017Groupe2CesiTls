import pygame,random,math,sys

class Entity:
 def __init__(self,app,*args):
  self.app=app
  self.redraw=True
  self.vision=0
  self.init(*args)
 def init(self):
  pass
 def update(self):
  pass
 def render(self):
  if self.redraw:
   self.surface=pygame.Surface((self.width,self.height))
   self.draw()
   self.redraw=False
  return self.surface


class Nazi(Entity):
 def init(self,x,y):
  self.x=x
  self.y=y
  self.dx=self.dy=0
  self.dir=random.random()*math.pi*2
  self.width=self.height=16
  self.awake=False
  self.vision=128
 def update(self):
  if not self.awake:
   distance=(self.x-self.app.player.x)**2+(self.y-self.app.player.y)**2
   if distance<self.vision**2:
    self.awake=True
    self.redraw=True
   else:
    self.dir+=(random.random()*2-1)/4
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
   
   
class Bullet(Entity):
 def init(self,x,y,dx,dy):
  self.width=self.height=8
  self.x=x
  self.y=y
  self.dx=dx
  self.dy=dy
 def update(self):
  self.x+=self.dx
  self.y+=self.dy
 def draw(self):
  self.surface.fill((127,127,127))
   

class Player(Entity):
 def init(self):
  self.x=320
  self.y=240
  self.dx=0
  self.dy=0
  self.width=self.height=16
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
   

class Application:
 def __init__(self):
  self.entities=[]
  self.display=pygame.display.set_mode((640,480))
  self.clock=pygame.time.Clock()
 def init(self):
  self.player=Player(self)
  self.entities=[self.player,Nazi(self,160,120)]
 def update(self):
  for event in pygame.event.get():
   if event.type==pygame.QUIT:
    pygame.quit()
    sys.exit()
   if event.type==pygame.KEYDOWN:
    if event.key==pygame.K_ESCAPE:
     pygame.quit()
     sys.exit()
   if event.type==pygame.MOUSEBUTTONDOWN:
    px=(self.player.x)
    py=(self.player.y)
    x=event.pos[0]-px
    y=event.pos[1]-py
    dir=math.atan2(y,x)
    dx=math.cos(dir)*16
    dy=math.sin(dir)*16
    self.entities.append(Bullet(self,px,py,dx,dy))
  for entity in self.entities:
   entity.update()
 def render(self):
  self.display.fill((0,0,0))
  for entity in self.entities:
   if entity.vision:
    pygame.draw.circle(self.display,(127,127,0),(int(entity.x),int(entity.y)),128,0)
  for entity in self.entities:
   surface=entity.render()
   self.display.blit(surface,(entity.x-entity.width/2,entity.y-entity.height/2))
  pygame.display.flip()
  self.clock.tick(60)
 def run(self):
  self.init()
  while 1:
   self.update()
   self.render()
   
   
if __name__=="__main__":
 Application().run()
 
