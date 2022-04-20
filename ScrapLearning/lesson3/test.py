url = "background-image:url(/upload/file/mp/brands/artellogo.jpg)"

url = url.split("background-image:url(")[-1].split(")")[-2]
print(url)
