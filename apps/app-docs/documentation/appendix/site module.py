import site

packages = site.getusersitepackages()
userbase = site.getuserbase()
print("packages:", packages)
print("userbase:", userbase)
