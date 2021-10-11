#!/usr/bin/env python
# coding: utf-8

pip install captcha


from captcha.image import ImageCaptcha


image = ImageCaptcha(width = 1000, height = 200)   #<<Größe des Captcha in Pixel width=Breite  heigh=Höhe


text=input("Text:  ") #<<Eingabe der Zeichen die im Captca erscheinen sollen
captcha_text = text 


data = image.generate(captcha_text)


data = image.generate(captcha_text) #<<Umwandlung in Captcha
image.write(captcha_text, 'captcha.jpg') #<<Ausgabe als jpg
image.write(captcha_text, 'captcha.png') #<<Ausgabe als png
