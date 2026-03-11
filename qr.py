import qrcode 

img = qrcode.make("https://www.reddit.com/r/learnpython/comments/5lggna/is_there_a_big_difference_between_using_import_x/")
img.save("qr.png", "PNG")