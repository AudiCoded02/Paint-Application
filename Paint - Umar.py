#paintassignment.py
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog
init()
root=Tk()
root.withdraw()

font.init()
timesFont=font.SysFont("Times New Roman",30)
timeFont=font.SysFont("Times New Roman", 30)
timeColFont=font.SysFont("Times New Roman", 20)
subFont=font.SysFont("Times New Roman", 25)
size=width,height=1024,768
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)


#initialize variables
col=BLACK
col2=BLACK
polyMid=0
polyEnd=0
polyStart=0
polyButton=0
thickEraser=5
thickBrush=5
thickPoly=1
thickRect=6
thickCircle=5
fill=1              #815,755
thick=5
sprayThick=20
tool="no tool"
r,g,b,a=0,0,0,5
alp=10 
rad=25
negRad=-25
title="Assassin's Creed Paint"
text="Start Painting!"
subText="Select a Tool"
widthText="Width"
action="nothing"
sepiafilt="Sepia"
grayfilt="Grayscale"
rgbfilt="RGB"


            
        






################for stamps and backgrounds
stamps=["stamps/altairAssassin.png","stamps/bayekAssassin.png","stamps/edwardAssassin.png","stamps/evieAssassin.png","stamps/ezioAssassin.png","stamps/haythamAssassin.png","stamps/jacobAssassin.png","stamps/ratonAssassin.png"]
assassins=[]
for creed in stamps:
    pic=image.load(creed)


    assassinPic=transform.scale(pic, (200,170))
    assassins.append(assassinPic)

######loading ALL images (before while running loop) in the images folder
palPic=image.load("images/rgb color wheel.png")
pencilPic=image.load("images/penciltool.png")
erasePic=image.load("images/eraser.png")
clearPic=image.load("images/clearTrash.png")
brushPic=image.load("images/brush.png")
highlightPic=image.load("images/highlighter.png")
backPic=image.load("images/assassin.png")
sprayPic=image.load("images/spraypaint.png")
linePic=image.load("images/line.png")
rectPic=image.load("images/rectangle.png")
circPic=image.load("images/circle.png")
sPic=image.load("images/save.png")
lPic=image.load("images/load.png")
pPic=image.load("images/fillPaint.png")
poPic=image.load("images/polygon.png")
dropPic=image.load("images/dropper.png")
rdPic=image.load("images/redo.png")
udPic=image.load("images/undo.png")
logoPic=image.load("images/logo.jpg")

fillPic=image.load("images/filled.png")
unfillPic=image.load("images/unfilled.png")
#altairPic=image.load("stamps/altairAssassin.png")
#########making adjustments to some pics
highsizePic=transform.scale(highlightPic, (50,50))
smallsprayPic=transform.scale(sprayPic, (50,50))
linevertPic=transform.scale(linePic, (50,50))
rectsmallPic=transform.scale(rectPic, (50,50))
circlePic=transform.scale(circPic, (50,50))
filledPic=transform.scale(fillPic, (150,75))
unfilledPic=transform.scale(unfillPic, (75,75))
colourPic=transform.scale(palPic, (200,200))
savePic=transform.scale(sPic, (50,50))
loadPic=transform.scale(lPic, (50,50))
paintPic=transform.scale(pPic, (50,50))
polyPic=transform.scale(poPic, (50,50))
dropperPic=transform.scale(dropPic, (50,50))
undoPic=transform.scale(udPic, (50,50))
redoPic=transform.scale(rdPic, (50,50))
logoFilterPic=transform.scale(logoPic, (120,100))
######loading ALL stamps (before while running loop) in the stamps folder
#######defining ALL rects
pencilRect=Rect(20,80,50,50)
eraserRect=Rect(80,80,50,50)
canvasRect=Rect(140,80,675,515)
palRect=Rect(824,360,200,200)
clearRect=Rect(20,140,50,50)
highlightRect=Rect(80,140,50,50)
brushRect=Rect(20,200,50,50)
lineRect=Rect(20,260,50,50)
sprayRect=Rect(80,200,50,50)
rectangleRect=Rect(80,260,50,50)
circleRect=Rect(20,320,50,50)
fillPRect=Rect(20,380,50,50)
assassinRect=Rect(820,80,200,170)
fillRect=Rect(815,595,107,183)
unfillRect=Rect(922,595,101,183)
locateRect=Rect(140,596,408,172)
saveRect=Rect(20,20,50,50)
loadRect=Rect(80,20,50,50)
polyRect=Rect(80,320,50,50)
dropperRect=Rect(80,380,50,50)
undoRect=Rect(820,20,50,50)
redoRect=Rect(880,20,50,50)
sepiaRect=Rect(10,650,120,100)
grayRect=Rect(10,540,120,100)
rgbRect=Rect(10,435,120,100)
#########showing the picture
screen.blit(backPic,(0,0))
screen.blit(colourPic,(823,360))
screen.blit(pencilPic,(20,80))
screen.blit(erasePic, (80,80))
screen.blit(clearPic, (20,140))
screen.blit(brushPic, (20,200))
screen.blit(highsizePic,(80,140))
screen.blit(smallsprayPic,(80,200))
screen.blit(linevertPic, (20,260))
screen.blit(rectsmallPic, (80,260))
screen.blit(circlePic, (20,320))
#screen.blit(altairPic,(800,100))
screen.blit(filledPic, (790,626))
screen.blit(unfilledPic, (930,626))
screen.blit(savePic, (20,20))
screen.blit(loadPic, (80,20))
screen.blit(paintPic, (20,380))
screen.blit(polyPic, (80,320))
screen.blit(dropperPic, (80,380))
screen.blit(undoPic, (820,20))
screen.blit(redoPic, (880,20))
screen.blit(logoFilterPic, (10,650))
screen.blit(logoFilterPic, (10,540))
screen.blit(logoFilterPic, (10,435))
#######canvas
draw.rect(screen,WHITE,canvasRect)


######show the stamps and background
backgrounds=["stamps/island.jpg","stamps/odyssey.jpg","stamps/origins.jpg","stamps/city.jpg","stamps/syndicate.jpg","stamps/nexus.jpg","stamps/whiteCanvas.jpg"]
locations=[]
big=[]
for land in backgrounds:
    
    back=image.load(land)
    bigPic=transform.scale(back, (675,515))
    big.append(bigPic)
    canvasBack=transform.scale(back, (408,172))
    locations.append(canvasBack)
pos=0
posB=0

b=len(locations)
n=len(assassins)

running=True
undoList=[screen.subsurface(canvasRect).copy()]
redoList=[]
drawn=False
while running:
    click=False
    
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            click=True
            copy=screen.subsurface(canvasRect).copy()
            polyButton=1
            sx,sy=mouse.get_pos()#starting position of the y
            screenShot=screen.copy()###screen capture
            if evt.button==4:#scrolling up
        ############when a tool is selected, only the thickness level of that specific tool will change
                polyButton=2
                if thickEraser<20 and tool=="eraser":
                    thickEraser+=5
                if thickBrush<20 and tool=="brush":
                    thickBrush+=5
                if thickPoly<6:
                    thickPoly+=1
                if thickRect<40 and tool=="rect":
                    thickRect+=2
                if thickCircle<40 and tool=="circle":
                    thickCircle+=2
                if thick<40 and tool=="line":
                    thick+=5
                if alp<20 and tool=="highlighter":
                    alp+=2
                if sprayThick<50:
                    sprayThick+=5
                if rad<75 and tool=="spray":
                    rad+=5
                if negRad>-75 and tool=="spray":
                    negRad-=5
                if tool=="assassin":
                    pos=(pos+1)%n
                if tool=="background" or tool=="no tool":
                    posB=(posB+1)%7
            if evt.button==5:#scrolling down
                #same as the first one
                if thickEraser>5 and tool=="eraser":
                    thickEraser-=5
                if thickBrush>5 and tool=="brush":
                    thickBrush-=5
                if thickPoly>1:
                    thickPoly-=1
                if thickRect>2 and tool=="rect":
                    thickRect-=2
                if thickCircle>2 and tool=="circle":
                    thickCircle-=2
                if thick>5 and tool=="line":
                    thick-=5
                if alp>2 and tool=="highlighter":
                    alp-=2
                if sprayThick>5:
                    sprayThick-=5
                if rad>25 and tool=="spray":
                    rad-=5
                if negRad<-25 and tool=="spray":
                    negRad+=5
                if tool=="assassin":
                    pos=(pos-1)%n
                if tool=="background" or tool=="no tool":
                    posB=(posB-1)%7
        if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
    ############when the mouse is not pressed, it will take a screenshot of the canvas in its current state and append it to the undoList
            ucopy=screen.subsurface(canvasRect).copy()
            undoList.append(ucopy)
           ####end
            polyButton=0
        
    mb=mouse.get_pressed()
    mx,my=mouse.get_pos()
    
    #######drawing the shapes
    draw.rect(screen,WHITE,pencilRect,2)
    draw.rect(screen,WHITE,eraserRect,2)
    draw.rect(screen,WHITE,clearRect,2)
    draw.rect(screen,WHITE,lineRect,2)
    draw.rect(screen,WHITE,brushRect,2)
    draw.rect(screen,WHITE,highlightRect,2)
    draw.rect(screen,WHITE,sprayRect,2)
    draw.rect(screen,WHITE,rectangleRect,2)
    draw.rect(screen,WHITE,circleRect,2)
    draw.rect(screen,BLACK,fillRect,2)
    draw.rect(screen,BLACK,locateRect,3)
    draw.rect(screen,BLACK,unfillRect,2)
##    draw.rect(screen,BLACK,(927,590,100,175),1)
    draw.rect(screen,BLACK, loadRect,2)
    draw.rect(screen,BLACK, saveRect,2)
    draw.rect(screen,WHITE, polyRect,2)
    draw.rect(screen,(192,192,192), (549,595,266,173))
    screen.blit(assassins[pos],(820,80))
    draw.rect(screen,WHITE, dropperRect,2)    
    draw.rect(screen,WHITE,undoRect,2)
    draw.rect(screen,WHITE,redoRect,2)
    draw.rect(screen,WHITE,assassinRect,2)
    screen.blit(locations[posB],(140,596))
    draw.rect(screen,WHITE,fillPRect,2)
    draw.rect(screen,BLACK,sepiaRect,2)
    draw.rect(screen,BLACK,grayRect,2)
    draw.rect(screen,BLACK,rgbRect,2)
    #########for filters
    for x in range(10,130):##grayscale filter
        for y in range(540,640):
            r1,g1,b1,a1=screen.get_at((x,y))
            r2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
            g2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
            b2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
            screen.set_at((x,y), (r2,g2,b2))
        
    for x in range(10,130):##sepia filter
        for y in range(650,750):
            r1,g1,b1,a1=screen.get_at((x,y))
            r2=min(255,int(0.393*r1+0.769*g1+0.189*b1))
            g2=min(255,int(0.349*r1+0.686*g1+0.168*b1))
            b2=min(255,int(0.272*r1+0.534*g1+0.131*b1))
            screen.set_at((x,y), (r2,g2,b2))
        


    ############for text
    titlePic=timesFont.render(title,True,BLACK)
    w=pic.get_width()
    h=pic.get_height()
    screen.blit(titlePic,(407, 50))
    startPic=timeFont.render(text,True,BLACK)
    wt=pic.get_width()
    ht=pic.get_height()
    screen.blit(startPic,(558,600))
    subPic=subFont.render(subText,True,BLACK)
    screen.blit(subPic, (558,640))
    widthPic=subFont.render(widthText,True,BLACK)
    sepiaPic=timesFont.render(sepiafilt,True,WHITE)
    screen.blit(sepiaPic,(40,700))
    grayPic=timesFont.render(grayfilt,True,WHITE)
    screen.blit(grayPic,(10,590))
    rgbPic=timesFont.render(rgbfilt,True,WHITE)
    screen.blit(rgbPic,(40,485))
    ######selecting the tool
    if mb[0]==1 and click:
        if pencilRect.collidepoint(mx,my):
            tool="pencil"
        elif eraserRect.collidepoint(mx,my):
            tool="eraser"
        elif clearRect.collidepoint(mx,my):
            tool="clear"
        elif lineRect.collidepoint(mx,my):
            tool="line"
        elif brushRect.collidepoint(mx,my):
            tool="brush"
        elif highlightRect.collidepoint(mx,my):
            tool="highlighter"
        elif sprayRect.collidepoint(mx,my):
            tool="spray"
        elif rectangleRect.collidepoint(mx,my):
            tool="rect"
        elif assassinRect.collidepoint(mx,my):
            tool="assassin"
        elif circleRect.collidepoint(mx,my):
            tool="circle"
        elif fillRect.collidepoint(mx,my):
            fill=0
        elif unfillRect.collidepoint(mx,my):
            fill=1
        elif locateRect.collidepoint(mx,my):
            tool="background"
        elif saveRect.collidepoint(mx,my):
            action="save"
        elif loadRect.collidepoint(mx,my):
            action="load"
        elif fillPRect.collidepoint(mx,my):
            tool="bucket"
        elif dropperRect.collidepoint(mx,my):
            tool="dropper"
        elif polyRect.collidepoint(mx,my):
            tool="polygon"
        elif sepiaRect.collidepoint(mx,my):
            action="sepia"
        elif grayRect.collidepoint(mx,my):
            action="gray"
        elif rgbRect.collidepoint(mx,my):
            action="rgb"
        
        

    ############changing the text to specify what tool is currently selected
    if tool=="pencil":
        text="Pencil Tool"
        subText="Draw smooth lines"
    if tool=="eraser":
        text="Eraser Tool"
        subText="Erase things"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thickEraser)
        thickEraserPic=subFont.render(width,True,BLACK)
        screen.blit(thickEraserPic,(650,670))
    if tool=="line":
        text="Line Tool"
        subText="Draw your own lines"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thick)
        thickPic=subFont.render(width,True,BLACK)
        screen.blit(thickPic,(650,670))
    if tool=="brush":
        text="Brush Tool"
        subText="Draw thick lines"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thickBrush)
        thickBrushPic=subFont.render(width,True,BLACK)
        screen.blit(thickBrushPic,(650,670))
    if tool=="highlighter":
        text="Highlighter Tool"
        subText="Draw transparent lines"
        screen.blit(widthPic, (558,670))
        widthText="Transparency"
        width=str(alp)
        alphaPic=subFont.render(width,True,BLACK)
        screen.blit(alphaPic,(710,670))
    if tool=="spray":
        text="Spray Tool"
        subText="Spray your art"
        widthText="Radius"
        screen.blit(widthPic, (558,670))
        width=str(rad)
        thickSprayPic=subFont.render(width,True,BLACK)
        screen.blit(thickSprayPic,(650,670))
    if tool=="rect":
        text="Rectangle Tool"
        subText="Draw rectangles"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thickRect)
        thickRectPic=subFont.render(width,True,BLACK)
        screen.blit(thickRectPic,(650,670))
    if tool=="assassin":
        text="Assassin Stamps"
        subText="Stamp Assassins on"
    if tool=="circle":
        text="Circle Tool"
        subText="Draw circles"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thickCircle)
        thickCirclePic=subFont.render(width,True,BLACK)
        screen.blit(thickCirclePic,(650,670))
##    if action=="save":
##        text="Save"
##        subText="Save your work"
##    if action=="load":
##        text="Open/Load"
##        subText="Open/load files"
    if tool=="background":
        text="Change Backgrounds"
        subText="Select backgrounds"
    if tool=="bucket":
        text="Fill Tool"
        subText="Fill canvas with colour"
    if tool=="clear":
        text="Screen Cleared"
        subText="remove everything"
    if tool=="polygon":
        text="Polygon Tool"
        subText="Draw your own shapes"
        widthText="Width"
        screen.blit(widthPic, (558,670))
        width=str(thickPoly)
        thickPolyPic=subFont.render(width,True,BLACK)
        screen.blit(thickPolyPic,(650,670))
    if tool=="dropper":
        text="Dropper Tool"
        subText="Select colour anywhere"
    if action=="undo":
        text="Undo Work"
        subText="Undo a previous step"
    if action=="redo":
        text="Redo Work"
        subText="Redo a previous step"
    if action=="sepia":
        text="Filter"
        subText="Sepia"
        
    if action=="gray":
        text="Filter"
        subText="Grayscale"
    if action=="rgb":
        text="Filter"
        subText="RGB"
    

    ##############highlighting the tool if the mouse touches the tool icon
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,RED,pencilRect,2)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,RED,eraserRect,2)
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,RED,lineRect,2)
    if brushRect.collidepoint(mx,my):
        draw.rect(screen,RED,brushRect,2)
    if clearRect.collidepoint(mx,my):
        draw.rect(screen,RED,clearRect,2)
    if highlightRect.collidepoint(mx,my):
        draw.rect(screen,RED,highlightRect,2)
    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,RED,sprayRect,2)
    if rectangleRect.collidepoint(mx,my):
        draw.rect(screen,RED,rectangleRect,2)
    if assassinRect.collidepoint(mx,my):
        draw.rect(screen,RED,assassinRect,2)
    if circleRect.collidepoint(mx,my):
        draw.rect(screen,RED,circleRect,2)
    if locateRect.collidepoint(mx,my):
        draw.rect(screen,RED,locateRect,2)
    if unfillRect.collidepoint(mx,my):
        draw.rect(screen,RED,unfillRect,2)
    if fillRect.collidepoint(mx,my):
        draw.rect(screen,RED,fillRect,2)
    if dropperRect.collidepoint(mx,my):
        draw.rect(screen,RED,dropperRect,2)
    if polyRect.collidepoint(mx,my):
        draw.rect(screen,RED,polyRect,2)
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,RED,saveRect,2)
    if loadRect.collidepoint(mx,my):
        draw.rect(screen,RED,loadRect,2)
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,RED,redoRect,2)
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,RED,undoRect,2)
    if fillPRect.collidepoint(mx,my):
        draw.rect(screen,RED,fillPRect,2)
    if sepiaRect.collidepoint(mx,my):
        draw.rect(screen,RED,sepiaRect,2)
    if grayRect.collidepoint(mx,my):
        draw.rect(screen,RED,grayRect,2)
    if rgbRect.collidepoint(mx,my):
        draw.rect(screen,RED,rgbRect,2)

#########################once a tool is selected, that tool will stay highlighted 

    if tool=="pencil":
        draw.rect(screen,BLUE,pencilRect,2)
    elif tool=="eraser":
        draw.rect(screen,BLUE,eraserRect,2)
    elif tool=="line":
        draw.rect(screen,BLUE,lineRect,2)
    elif tool=="brush":
        draw.rect(screen,BLUE,brushRect,2)
    elif tool=="highlighter":
        draw.rect(screen,BLUE,highlightRect,2)
    elif tool=="spray":
        draw.rect(screen,BLUE,sprayRect,2)
    elif tool=="rect":
        draw.rect(screen,BLUE,rectangleRect,2)
    elif tool=="assassin":
        draw.rect(screen,BLUE,assassinRect,2)
    elif tool=="circle":
        draw.rect(screen,BLUE,circleRect,2)
    
    elif tool=="background":
        draw.rect(screen,BLUE,locateRect,2)
    elif tool=="bucket":
        draw.rect(screen,BLUE,fillPRect,2)
    
    elif tool=="polygon":
        draw.rect(screen,BLUE,polyRect,2)
    elif tool=="dropper":
        draw.rect(screen,BLUE,dropperRect,2)
    elif action=="undo":
        draw.rect(screen,BLUE,undoRect,2)
    elif action=="redo":
        draw.rect(screen,BLUE,redoRect,2)
    elif action=="clear":
        draw.rect(screen,BLUE,clearRect,2)
    elif action=="sepia":
        draw.rect(screen,BLUE,sepiaRect,2)
    elif action=="gray":
        draw.rect(screen,BLUE,grayRect,2)
    elif action=="rgb":
        draw.rect(screen,BLUE,rgbRect,2)


############once a fill option (1 or 0) is selected, that fill option will stay selected
    if fill==0:
        draw.rect(screen,(255,215,0),fillRect,2)
    elif fill==1:
        draw.rect(screen,(255,215,0),unfillRect,2)
    ######using the tool
    if mb[0]==1:
        
        if canvasRect.collidepoint(mx,my):
            screen.set_clip(canvasRect)#only the canvas can be used ("updated")
            
              
            if tool=="pencil":
                draw.line(screen,col,(omx,omy),(mx,my))
                
            elif tool=="eraser":
                dx=mx-omx #horiz. distance (run)
                dy=my-omy #vert. distance (rise)
                dist=int(sqrt(dx**2+dy**2))     
                for i in range(1,dist+1):#1,2,3,4,5,6,7,8,9,.....
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                    if drawn==True:
                        draw.circle(screen,col2,(dotX,dotY),thickEraser)
                    if drawn==False and posB==6:
                        
                        draw.circle(screen,WHITE,(dotX,dotY),thickEraser)

                    else:
                        try:
                            backEraser=big[posB].subsurface((int(omx+dx*i)-220-thickEraser,int(omy+dy*i)-5-thickEraser,thickEraser*2,thickEraser*2))
                            screen.blit(backEraser,(int(omx+bx*i)-thick,int(omy+by*i)-thick))
                        except:
                            pass

                        ##erase=big[posB].subsurface((mx,my,30,30))
                        ##screen.blit(erase,(dotX-15,dotY-15))
##                    if filt==2:
##                        r1,g1,b1,a1=screen.get_at((x,y))
##                        r2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
##                        g2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
##                        b2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
##                        draw.circle(screen,(r2,b2,g2),(dotX,dotY),thickEraser)
            elif tool=="line":
                screen.blit(screenShot,(0,0))
                draw.line(screen,col,(sx,sy),(mx,my),thick)
            elif tool=="polygon":
                
                if polyButton==2 and polyEnd!=0 and polyStart!=0 :
                    draw.line(screen,col,polyEnd,polyStart,2)
                    polyEnd=0
                    polyMid=0
                    polyStart=0
                    polyButton=0
                elif  polyButton==1 and polyStart==0:
                    polyStart=mx,my
                elif  polyButton==1 and polyMid==0 and polyStart !=(mx,my):
                   if polyEnd ==0:
                        polyMid=mx,my
                        draw.line(screen,col,polyStart,polyMid,2)
                        polyEnd=polyMid
                        polyMid=0
                        polyButton=0
                   else:
                        polyMid=mx,my
                        draw.line(screen,col,polyEnd,polyMid,2)
                        polyEnd=polyMid
                        polyMid=0
                        polyButton=0
                    
##                        if mb[2]==1:
##                            polyEnd=polyStart
##                            draw.line(screen,col,polyEnd,polyStart,2)
##                    
##                            polyMid=0
##                            polyButton=0
                    
            
            
            elif tool=="brush":
                dx=mx-omx #horiz. distance (run)
                dy=my-omy #vert. distance (rise)
                dist=int(sqrt(dx**2+dy**2))
                for i in range(1,dist+1):#1,2,3,4,5,6,7,8,9,.....
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                    draw.circle(screen,col,(dotX,dotY),thickBrush)
            elif tool=="highlighter":
                dx=mx-omx #horiz. distance (run)
                dy=my-omy #vert. distance (rise)
                dist=int(sqrt(dx**2+dy**2))
                for i in range(1,dist+1):#1,2,3,4,5,6,7,8,9,.....
                    dotX=int(omx+i*dx/dist)
                    dotY=int(omy+i*dy/dist)
                
                    highlight=Surface((30,30),SRCALPHA)#creating a blank surface
                    draw.circle(highlight,(r,g,b,alp),(15,15),15)
                    if mx!=omx or my!=omy:#there is movement
                        if mb[0]==1:
                            screen.blit(highlight,(dotX,dotY))
            elif tool=="spray":
                for i in range(0,50):
                    rx=randint(negRad,rad)
                    ry=randint(negRad,rad)
                    wx=mx+rx
                    wy=my+ry
                    if (wx-mx)**2 + (wy-my)**2<rad**2:
                        draw.circle(screen,col,(wx,wy),0)
            elif tool=="rect":
                if fill==1:
                    if thickRect%2==0:
                        thickRect=thickRect-1
                    screen.blit(screenShot,(0,0))
                    w=mx-sx
                    l=my-sy
                    draw.line(screen,col,(sx,sy-thickRect//2),(sx,my+thickRect//2),thickRect)
                    draw.line(screen,col,(sx-thickRect//2,sy),(mx+thickRect//2,sy),thickRect)
                    draw.line(screen,col,(mx,sy-thickRect//2),(mx,my+thickRect//2),thickRect)
                    draw.line(screen,col,(sx-thickRect//2,my),(mx+thickRect//2,my),thickRect)
                    if w<0 and l<0:
                        draw.line(screen,col,(sx,sy+thickRect//2),(sx,my-thickRect//2),thickRect)
                        draw.line(screen,col,(sx+thickRect//2,sy),(mx-thickRect//2,sy),thickRect)
                        draw.line(screen,col,(mx,sy+thickRect//2),(mx,my-thickRect//2),thickRect)
                        draw.line(screen,col,(sx+thickRect//2,my),(mx-thickRect//2,my),thickRect)
                    
                if fill==0:
                    screen.blit(screenShot,(0,0))
                    draw.rect(screen,col,(mx,my,sx-mx,sy-my),0)
            elif tool=="assassin":
                screen.blit(screenShot,(0,0))
                screen.blit(assassins[pos],(mx-100,my-100))
            elif tool=="dropper":
                col=screen.get_at((mx,my))
                
                r,g,b,a=screen.get_at((mx,my))



            
            elif tool=="circle":
                if fill==1:
                    if abs(sx-mx)>thick*2 and abs(sy-my)>thick*2:
                        x=min(sx,mx)
                        x2=max(sx,mx)
                        y=min(sy,my)
                        y2=max(sy,my)
                        
                        screen.blit(screenShot,(0,0))
                        for i in range(0,3,1):
                            ellipseRect=Rect(x+i,y-i,x2-x,y2-y)
                            ellipseRect.normalize()
                            draw.ellipse(screen,col,ellipseRect,thickCircle)
    ##                if mx>sx and my>sy:
    ##                    draw.ellipse(screen,col,[sx,sy,mx-sx,my-sy])
    ##                elif mx<sx and my<sy:
    ##                    draw.ellipse(screen,col,[mx,my,sx-mx,sy-my])
    ##                elif mx>sx and my<sy:
    ##                    draw.ellipse(screen,col,[sx,my,mx-sx,sy-my])
    ##                elif mx<sx and my>sy:
    ##                    draw.ellipse(screen,col,[mx,sy,sx-mx,my-sy])
                if fill==0:
                    if abs(sx-mx)>thick*2 and abs(sy-my)>thick*2:
                        x=min(sx,mx)
                        x2=max(sx,mx)
                        y=min(sy,my)
                        y2=max(sy,my)
                        screen.blit(screenShot,(0,0))
                        for i in range(0,3,1):
                            ellipseRect=Rect(x+i,y-i,x2-x,y2-y)
                            ellipseRect.normalize()
                            draw.ellipse(screen,col,ellipseRect,0)
        
        elif tool=="background":
            screen.blit(screenShot,(0,0))
            screen.blit(big[posB],(140,80))
            drawn=False
        elif tool=="bucket":
            if palRect.collidepoint(mx,my):
                
                col2=screen.get_at((mx,my))
                
                draw.rect(screen,col2,(140,80,675,515))
                drawn=True
###########################separate for the actions
        if saveRect.collidepoint(mx,my):
            saveFName=filedialog.asksaveasfilename(defaultextension=".jpg")
            if saveFName!="":
                image.save(screen.subsurface(canvasRect),saveFName)
        elif loadRect.collidepoint(mx,my):
            loadFName=filedialog.askopenfilename()
            if loadFName!="":
                Image=image.load(loadFName)
                screen.blit(Image,canvasRect)
    
        if undoRect.collidepoint(mx,my) and click:
            action="undo"
            if len(undoList)>1:
                redoList.append(undoList[-1])
                undoList.pop()
                screen.blit(undoList[-1],canvasRect)
                
               
        if redoRect.collidepoint(mx,my) and click:
            action="redo"
            if len(redoList)>0:
                crop=redoList.pop()
                screen.blit(crop,canvasRect)
                undoList.append(crop)
        if action=="sepia":
            filt=3
            for x in range(140,815):
                for y in range(80,595):
                    r1,g1,b1,a1=screen.get_at((x,y))
                    r2=min(255,int(0.393*r1+0.769*g1+0.189*b1))
                    g2=min(255,int(0.349*r1+0.686*g1+0.168*b1))
                    b2=min(255,int(0.272*r1+0.534*g1+0.131*b1))
                    screen.set_at((x,y), (r2,g2,b2))
                
        if action=="gray":
            filt=2
            for x in range(140,815):
                for y in range(80,595):
                    r1,g1,b1,a1=screen.get_at((x,y))
                    r2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
                    g2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
                    b2=min(255,int(0.2989*r1+0.5870*g1+0.1140*b1))
                    screen.set_at((x,y), (r2,g2,b2))
        if action=="rgb":
            for x in range(140,815):
                for y in range(80,595):
                    r1,g1,b1,a1=screen.get_at((x,y))
                    r2=min(255,int(0.9*r1+0*g1+0*b1))
                    g2=min(255,int(0*r1+0.9*g1+0*b1))
                    b2=min(255,int(0*r1+0*g1+0.9*b1))
                    screen.set_at((x,y), (r2,g2,b2))
                
            
            
            
    ##########draws the box of the selected colour as well as labelling the colour code      
    draw.rect(screen,col,(822,300,200,58),0)
    draw.rect(screen,BLACK,(822,300,200,58),1)           
    draw.rect(screen,WHITE,(822,260,200,38),0)
    draw.rect(screen,BLACK,(822,260,200,38),1) 
    colour=str(col)
    colourPic=timeColFont.render(colour,True,BLACK)
    screen.blit(colourPic,(850,270))
    #print(thickBrush,thickEraser,thick)
    
    
    #print(negRad,rad)
    screen.set_clip(canvasRect)#only the canvas can be used ("updated")
    #depending on the background selected, will the screen clear to that specific background
    if tool=="clear":
         if drawn==False:
             screen.blit(screenShot,(0,0))
             screen.blit(big[posB],(140,80))
         else:
             screen.blit(screenShot,(0,0))
             draw.rect(screen,col2,canvasRect,0)
    #######changing the colour
    
    screen.set_clip(None)
    ##########everytime the user selects a colour on the palette
    if mb[0]==1 and click:
        if palRect.collidepoint(mx,my):
            col=screen.get_at((mx,my))
            
            r,g,b,a=screen.get_at((mx,my))
                      
            draw.rect(screen,col,(822,300,200,58),0) 
            draw.rect(screen,BLACK,(822,300,200,58),1)
            
               
        
        
    

    omx=mx
    omy=my
    display.flip()
    

quit()




