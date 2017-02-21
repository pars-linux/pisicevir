# -*- coding: utf-8 -*-
# Pisicevir Debian Modülü
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

import araclar as arc
from time import strftime
import os
import sha
import tempfile
import sys

bd = os.getcwd()
tarih = strftime("%Y-%m-%d")
workdir = ""
depends = ""
pisi_adi = ""

def deb_ac(paket_adi):
	global workdir
	workdir = tempfile.mktemp()
	workdir = workdir + "/"
	os.mkdir(workdir)
	arc.kopyala(paket_adi, workdir)
	os.chdir(workdir)
	arc.yap("ar xv %s > /dev/null" % (paket_adi))
	arc.tar_ac("control.tar.gz")
	print "\033[1;32mDosyalar açıldı...\033[0m"

def deb_pisi_yaz(paket_adi):
	global depends
	global pisi_adi
	deb_ac(paket_adi)
	control = open("control").read()
	package = arc.bul("Package: (.*)", control)
	homepage = arc.bul("Homepage: (.*)", control)
	depends = arc.bul("Depends: (.*)", control)
	if depends.__len__() == 0:
		depends = "(Bağımlılık Yok)"
	description = "Bağımlılıklar: %s" % depends
	pisi_adi = package
	pspec = arc.pspecd
	actions = arc.actionsd
	hash_dosya = open("%sdata.tar.gz" % workdir)
	shad = sha.new()
	shad.update(hash_dosya.read())
	sha1sum = shad.hexdigest()
	print "Sha1sum alındı...(%s)" % sha1sum
	pspec = pspec.replace("***PaketAdi***", package).replace("***Sha1Sum***", sha1sum).replace("***Dosya***", "%sdata.tar.gz" % workdir).replace("***Tarih***", tarih).replace("***HomePage***", homepage).replace("***Aciklama***", description)
	print "\033[1;36mBağımlılıklar Listeleniyor: \n" + depends + "\033[0m"
	pspecw = open("pspec.xml", "w")
	pspecw.write(pspec)
	actionsw = open("actions.py", "w")
	actionsw.write(actions)
	print "PiSi dosyaları yazıldı..."

def deb_to_pisi(paket_adi, argumanlar):
	deb_pisi_yaz(paket_adi)
	os.chdir(bd)
	arc.build(workdir)
	arc.gecici_sil(workdir)
	arc.dbyaz(paket_adi, depends, argumanlar, pisi_adi)