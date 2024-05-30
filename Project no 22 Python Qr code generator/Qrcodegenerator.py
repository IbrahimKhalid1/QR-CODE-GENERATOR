import qrcode

img = qrcode.make('https://chat.openai.com/')
img.save('saved.png')
img.show('saved.png')