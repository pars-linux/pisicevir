#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pisicevir kurulum aracı
"""
    Copyright (C) 2008 Oğuzhan Eroğlu
    http://pisicevir.googlecode.com/
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

import os
import sys
import araclar as arc
import glob

if os.environ["USER"] != "root":
	print "Kurulum root yetkileri ile yapılabilir."
	sys.exit()

dizin = "/usr/lib/python2.5/site-packages/pisicevir"

def kur():
	os.mkdir(dizin)
	print "Dizin olulşturuldu"
	dosyalar = glob.glob("*")
	dosyalar.remove("pisicevir")
	for i in dosyalar:
		arc.kopyala(i, dizin)
	arc.kopyala("pisicevir", "/usr/bin/")
	os.chmod("/usr/bin/pisicevir", 0777)
	print "Kurulum tamamlandı"

try:
	if sys.argv[1] == "--kaldir":
		arc.dizin_sil(dizin)
		os.remove("/usr/bin/pisicevir")
		print "Pisiçevir kaldırıldı."
		sys.exit()
except(IndexError):
	kur()
