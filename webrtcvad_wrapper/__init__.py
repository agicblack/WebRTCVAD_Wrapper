#!/usr/bin/python3
# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#       OS : GNU/Linux Ubuntu 16.04 or 18.04
# LANGUAGE : Python 3.5.2 or later
#   AUTHOR : Klim V. O.
#     DATE : 14.10.2019
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

'''
Предназначен для удаления тишины/извлечения фрагментов с речью (или другими звуками) из wav аудиозаписи.
Для работы используется py-webrtcvad (https://github.com/wiseman/py-webrtcvad).

Содержит класс VAD. Подробнее в https://github.com/Desklop/WebRTCVAD_Wrapper.

Зависимости: pydub, librosa, webrtcvad.
'''

from .webrtcvad_wrapper import VAD
