The Abstract Factory pattern looks like the factory objects we’ve seen previously, 
with not one but several factory methods. Each of the factory methods creates a 
different kind of object. 
The idea is that at the point of creation of the factory object, you decide how all 
the objects created by that factory will be used. The example given in Design Patterns 
implements portability across various graphical user interfaces (GUIs):
you create a factory object appropriate to the GUI that you’re working with, and from 
then on when you ask it for a menu, button, slider, etc. it will automatically create 
the appropriate version of that item for the GUI. Thus you’re able to isolate, in one 
place, the effect of changing from one GUI to another.
As another example suppose you are creating a general-purpose gaming environment and 
you want to be able to support different types of games. Here’s how it might look using 
an abstract factory: