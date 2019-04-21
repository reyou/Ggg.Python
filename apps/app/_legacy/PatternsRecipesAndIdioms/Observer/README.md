http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Observer.html
The observer pattern solves a fairly common problem: What if a group of objects 
needs to update themselves when some object changes state? This can be seen in the 
“model-view” aspect of Smalltalk’s MVC (model-view-controller), or the almost-equivalent 
“Document-View Architecture.” Suppose that you have some data (the “document”) and 
more than one view, say a plot and a textual view. When you change the data, the two 
views must know to update themselves, and that’s what the observer facilitates. 
It’s a common enough problem that its solution has been made a part of the standard 
java.util library. 

There are two types of objects used to implement the observer pattern in Python. 
The Observable class keeps track of everybody who wants to be informed when a change 
happens, whether the “state” has changed or not. When someone says “OK, everybody should 
check and potentially update themselves,” the Observable class performs this task by 
calling the notifyObservers( ) method for each one on the list. The notifyObservers( ) 
method is part of the base class Observable.

There are actually two “things that change” in the observer pattern: the quantity 
of observing objects and the way an update occurs. That is, the observer pattern allows 
you to modify both of these without affecting the surrounding code.

Observer is an “interface” class that only has one member function, update( ). 
This function is called by the object that’s being observed, when that object decides 
its time to update all its observers. The arguments are optional; you could have an update( ) 
with no arguments and that would still fit the observer pattern; however this is more 
general-it allows the observed object to pass the object that caused the update 
(since an Observer may be registered with more than one observed object) and any 
extra information if that’s helpful, rather than forcing the Observer object to 
hunt around to see who is updating and to fetch any other information it needs.

