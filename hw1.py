{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMtBP6B8CIYKQARUdlspiR8",
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
        "<a href=\"https://colab.research.google.com/github/sooloin/Subin-cho/blob/main/hw1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yjh6iUSym11f",
        "outputId": "c58fbef1-2b24-41fb-82de-39da9f04db10"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "넓이를 구하고자 하는 원의 반지름은? 4\n",
            "반지름이 4인 원의 넓이 = 3.14 x 4*4 =  50.24\n"
          ]
        }
      ],
      "source": [
        "# 사용자 정의 함수부\n",
        "def get_radius(prompt):\n",
        "  r=int(input(prompt))\n",
        "  return r ; #입력한 정수값을 반환\n",
        "\n",
        "def get_circle_area(r):\n",
        "  area=3.14*(r**2)\n",
        "  return area\n",
        "\n",
        "# 주 프로그램부\n",
        "r=get_radius(\"넓이를 구하고자 하는 원의 반지름은? \")\n",
        "print(f\"반지름이 {r}인 원의 넓이 = 3.14 x {r}*{r} =  {get_circle_area(r)}\")\n",
        "#출력형 f string 사용"
      ]
    }
  ]
}