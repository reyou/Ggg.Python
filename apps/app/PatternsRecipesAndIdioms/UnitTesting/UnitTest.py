# UnitTesting/UnitTest.py
# The basic unit testing class
class UnitTest:
    testID = ""
    errors = []

    # Override cleanup() if test object creation allocates non-memory
    # resources that must be cleaned up:
    def cleanup(self): pass

    # Verify a condition is true:
    def affirm(self):
        if not self:
            UnitTest.errors.append("failed: " + UnitTest.testID)
