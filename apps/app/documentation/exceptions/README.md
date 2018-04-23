https://docs.python.org/3/library/exceptions.html
//=============================================================================
In Python, all exceptions must be instances of a class that derives from 
BaseException. In a try statement with an except clause that mentions a particular 
class, that clause also handles any exception classes derived from that class 
(but not exception classes from which it is derived). Two exception classes that 
are not related via subclassing are never equivalent, even if they have the same 
name.
//=============================================================================
Note It should not be used to indicate that an operator or method is not meant 
to be supported at all – in that case either leave the operator / method 
undefined or, if a subclass, set it to None.
//=============================================================================
Note NotImplementedError and NotImplemented are not interchangeable, even though 
they have similar names and purposes. See NotImplemented for details on when to 
use it.
//=============================================================================


