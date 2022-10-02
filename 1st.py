import turtle
t = turtle.Turtle()
t.shape("turtle")

t.color("blue");
t.pensize(10);
t.up();
t.goto(-150, 0);
t.down(); 
t.circle(80);
t.color("yellow");
t.pensize(10);
t.up(); 
t.goto(-20, 0); 
t.down(); 
t.circle(80);
t.color("black");
t.pensize(10);
t.up(); 
t.goto(110, 0); 
t.down(); 
t.circle(80);
t.color("green");
t.pensize(10);
t.up(); 
t.goto(-80, -110); 
t.down(); 
t.circle(80)
t.color("red");
t.pensize(10);
t.up(); 
t.goto(50, -110); 
t.down(); 
t.circle(80);
t._screen.exitonclick();   # 화면을 마우스로 클릭해야 종료되게 하는 부분