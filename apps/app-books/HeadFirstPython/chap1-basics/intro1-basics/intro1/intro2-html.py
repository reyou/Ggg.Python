import html
escaped = html.escape("This HTML fragment contains a <script>script</script> tag.")
print("escaped: ", escaped)
unescaped = html.unescape(escaped)
print("unescaped: ", unescaped)