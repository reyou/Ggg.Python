class Foo:
    # Static: visible to all classes
    something: None
    def f(self,x):
        if not self.something:
            # New local version for this object
            self.something = []
        self.something.append(x)