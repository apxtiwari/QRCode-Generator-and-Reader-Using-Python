import pyqrcode
import png

s=" Hello World! This Is Anand"

url = pyqrcode.create(s)
url.svg("Anandsfirstqr.svg",scale = 8)
url.png('Anandsfirstqr.png',scale =6 )
