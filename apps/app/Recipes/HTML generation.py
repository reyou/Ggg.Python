from string import Template

greeting = 'Salutations'
name = 'Abdullah'
imgSrc = 'http://www.google.com/intl/en_ALL/images/logo.gif'
link = 'http://feihonghsu.blogspot.com'

html = """
<div>
    <h1>
        ${greeting}, ${name}!
    </h1>
    <p>
        This is an image <img src="${imgSrc}" />
    </p>
    <p>
        Try clicking on the <a href="${link}">link</a> right now.
    </p>
</div>"""

"""def locals()
Return a dictionary containing the current scope's local variables.
NOTE: Whether or not updates to this dictionary will affect name lookups in the local 
scope and vice-versa is *implementation dependent* and not covered by 
any backwards compatibility guarantees."""
local_variables = locals()
html = Template(html).substitute(**local_variables)
print(html)
