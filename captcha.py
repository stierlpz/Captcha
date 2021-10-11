#!/usr/bin/env python
# coding: utf-8

pip install captcha


from captcha.image import ImageCaptcha


image = ImageCaptcha(width = 280, height = 90)


text=input("Text:  ")
captcha_text = text 


data = image.generate(captcha_text)


image.write(captcha_text, 'CAPTCHA.jpg')
image.write(captcha_text, 'CAPTCHA.png')
