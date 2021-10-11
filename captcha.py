{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "captcha.py",
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyOKzT1hEOIqAkdZPGzTKwp1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/stierlpz/Captcha/blob/main/captcha.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cZ0moyJ072jy"
      },
      "source": [
        "pip install captcha\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J-bAO2_r8AWf"
      },
      "source": [
        "from captcha.image import ImageCaptcha"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YXup-4i18CzI"
      },
      "source": [
        "image = ImageCaptcha(width = 200, height = 200)   #<<Größe des Captcha in Pixel width=Breite  heigh=Höhe"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3TFElxXA8EEp"
      },
      "source": [
        "text=input(\"Text:  \") #<<Eingabe der Zeichen die im Captca erscheinen sollen\n",
        "captcha_text = text "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5fziloSJ8GOq"
      },
      "source": [
        "data = image.generate(captcha_text) #<<Umwandlung in Captcha\n",
        "image.write(captcha_text, 'images/captcha.jpg') #<<Ausgabe als jpg\n",
        "image.write(captcha_text, 'images/captcha.png') #<<Ausgabe als png\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}