# For example, the format sequence “%d” means
# that the second operand should be
# formatted as an integer (d stands for “decimal”):

camels = 42
print('%d' % camels)
print('I have spotted %d camels.' % camels)

# The following example uses “%d” to format an integer, “%g” to format a floating-
# point number (don’t ask why), and “%s” to format a string:
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
