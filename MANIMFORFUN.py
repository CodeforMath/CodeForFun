from manim import *
import numpy as np
import pygments.styles as code_styles
code_style = code_styles.get_style_by_name("one-dark")

SCALE_FACTOR=0.8
tmp_pixel_height=config.pixel_height
config.pixel_height=config.pixel_width
config.pixel_width=tmp_pixel_height

config.frame_height=config.frame_height/SCALE_FACTOR
config.frame_width=config.frame_width*9/16
FRAME_HEIGHT=config.frame_height
FRAME_WIDTH=config.frame_width

class FORFUN0001(Scene):
    def setup(self,add_border=True):
        if add_border:
            self.border=Rectangle(
                width=FRAME_WIDTH,
                height=FRAME_HEIGHT,
                color=WHITE
                )
            self.add(self.border)
    def construct(self): 
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[utf8]{vietnam}")
        myTemplate.add_to_preamble(r"\usepackage{anysize}")
        myTemplate.add_to_preamble(r"\usepackage{tabvar}") 
        myTemplate.add_to_preamble(r"\usepackage{longtable}") 
        LoGo=VGroup(Circle(radius=1,color=BLUE,fill_opacity=0.7).move_to([-5.5,2.5,0]),
                    Circle(radius=0.9,color=PURPLE,fill_opacity=0.7).move_to([-5.8,2.8,0]),
                    Circle(radius=0.6,color=RED,fill_opacity=0.7).move_to([-5.1,2.1,0]),
                    Circle(radius=0.6,color=YELLOW,fill_opacity=0.7).move_to([-4.9,2.9,0]),
                    Circle(radius=0.13,color=BLUE,fill_opacity=1).move_to([-4.1,2.5,0]),
                    Circle(radius=0.06,color=RED,fill_opacity=1).move_to([-4.3,2.3,0]),
                    Circle(radius=0.1,color=RED,fill_opacity=1).move_to([-5.1,3.8,0]),
                    Circle(radius=0.06,color=YELLOW,fill_opacity=1).move_to([-6.5,1.8,0]))
        
        LoGoTam=LoGo.copy().scale(0.4).to_edge(DOWN+RIGHT)
        TenSeri=Text("VMaths",color=ORANGE,font="fuzzy bubbles",font_size=70,
                    stroke_width=2).scale(0.25).next_to(LoGoTam,DOWN*0.3)
        TenSeri.set_color_by_gradient("#7CFC00",YELLOW)
        LoGoSeri=VGroup(LoGoTam,TenSeri).shift(LEFT*0.1)
        self.add(LoGoSeri)

        FontMath=45
        FontTex=35
        #Mau=["#7CFC00",TEAL,YELLOW,ORANGE,RED]

        #FontMath=45
        #FontTex=40
        Mau=["#7CFC00",BLUE,YELLOW,ORANGE,RED]
        BK=0.1
                
        HT=VGroup(*[Dot(radius=BK,color=Mau[0],
                fill_opacity=1) for i in range(21)]).arrange_submobjects(RIGHT,buff=0.1).to_edge(UP)
        

        axes = Axes(
            x_range =[-4,4],
            y_range = [-4,4],
            tips=False,
            x_length = 8, y_length = 8,
            axis_config={"color":WHITE,
                        "stroke_width":4,
                        "include_ticks":False,
                         },
        )
        axes.to_edge(LEFT)
        fx=axes.plot(lambda x: x*x/4-4,x_range=[-3.7,3.7],color=YELLOW,stroke_width=10)
        TD=Circle(radius=0.2,stroke_width=7,color=ORANGE).move_to(axes.c2p(0,-2,0))
        Parabol=VGroup(fx,TD).move_to(ORIGIN).shift(DOWN*2)

        self.add(HT,Parabol)
        self.wait(1)
        DSTD=[]
        for i in range(21):
            Dau=HT[i].get_center()
            Cuoi=np.array([Dau[0],Dau[0]*Dau[0]/4-4+0.3,0])
            DSTD.append([Dau,Cuoi])
        QD=VGroup()
        for i in range(21):
            QD.add(
                VGroup(
                Line(DSTD[i][0],DSTD[i][1],stroke_width=3),
                Line(DSTD[i][1],TD.get_center(),stroke_width=3)
                )
            )
        for i in range(len(Mau)):
            HT.set_color(Mau[i])
            tracker=ValueTracker(0)
            DT1=VGroup(*[VMobject() for _ in range(21)])
            self.add(DT1)
            def outer_func(j):
                DT1[j].add_updater(lambda x: x.become(
                    Line(DSTD[j][0],DSTD[j][0]+tracker.get_value()*(DSTD[j][1]-DSTD[j][0]),stroke_width=3,color=Mau[i])))
                return DT1[j]
            for j in range(21):
                outer_func(j)
               
            Animations1=[MoveAlongPath(HT[j],QD[j][0]) for j in range(21)]
            self.play(AnimationGroup(
                        *Animations1,
                        tracker.animate.set_value(1),
                        ),run_time=5-i,rate_func=linear)
            DT2=VGroup(*[VMobject() for _ in range(21)])
            self.add(DT2)       
            for j in range(21):
                DT1[j].clear_updaters()
            tracker=ValueTracker(0)
            def outer_func(j):
                DT2[j].add_updater(lambda x: x.become(
                    Line(DSTD[j][1],DSTD[j][1]+tracker.get_value()*(TD.get_center()-DSTD[j][1]),stroke_width=3,color=Mau[i])))
                return DT2[j]
            for j in range(21):
                outer_func(j)
            Animations2=[MoveAlongPath(HT[j],QD[j][1]) for j in range(21)]
            self.play(AnimationGroup(
                    tracker.animate.set_value(1),
                    *Animations2,
                    ),run_time=5-i,rate_func=linear)
            for j in range(21):
                DT2[j].clear_updaters()
            self.wait(1)