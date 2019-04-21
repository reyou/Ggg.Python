https://docs.python.org/3/library/enum.html

The most interesting thing about Enum members is that they are singletons. 
EnumMeta creates them all while it is creating the Enum class itself, 
and then puts a custom __new__() in place to ensure that no new ones are 
ever instantiated by returning only the existing member instances.

