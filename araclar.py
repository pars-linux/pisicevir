# -*- coding: utf-8 -*-
# Pisicevir araçları
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
import re
import shutil
import shelve
import glob

dbyol = "%s/.pisicevir.db" % os.environ["HOME"]
if not os.path.exists(dbyol):
	db = shelve.open(dbyol)
try:
	db = shelve.open(dbyol)
except:
	pass

def kopyala(dosya, dizin):
	shutil.copy(dosya, dizin)

def tar_ac(dosya):
	os.system("tar xzvf %s > /dev/null" % dosya)

def tasi(dosya, dizin):
	shutil.move(dosya, dizin)

def yap(komut):
	os.system("%s > /dev/null" % komut)

def gecici_sil(dosya):
	shutil.rmtree(dosya)
	print "\033[1;32mGeçici Dosyalar Silindi\033[0m"

def dizin_sil(dosya):
	shutil.rmtree(dosya)

def bul(arama, yer):
	try:
		return re.compile(arama).findall(yer)[0]
	except:
		return "none"

def dbyaz(deb_paket, depends, argumanlar, pisi_adi):
	if "--dbyoksay" not in argumanlar:
		try:
			db[deb_paket] = (depends, pisi_adi)
		except:
			pass

def dbtemizle(db):
	for i in db.keys():
		db.__delitem__(i)
	print "Veritabanı temizlendi."

def listele(db):
	print "Çevirdiğiniz paketler:"
	for i in db.keys():
		print "\033[1;31m%s | %s-pisicevir:\033[1;33m Bağımlılıkları: \033[1;36m%s\033[0m\n" % (i, db[i][1], db[i])

def gecicitemizle():
	dizinsayisi = 0
	dizinler = glob.glob("/tmp/tmp*")
	for i in dizinler:
		dizinsayisi += 1
		shutil.rmtree(i)
	print "Kalan geçici dizinler silindi.(%s)" % dizinsayisi

def build(workdir):
	os.system("sudo pisi bi %spspec.xml > /dev/null" % workdir)
	print "\033[1;32mPaket oluşturuldu.\033[0m"

actionsd = \
"""
# Coded by PiSicevir

from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/", "*")
"""

pspecd = \
"""
<?xml version="1.0" ?>
<!DOCTYPE PISI SYSTEM "http://www.pardus.org.tr/projeler/pisi/pisi-spec.dtd">
<PISI>
	<Source>
		<Name>***PaketAdi***-pisicevir</Name>
		<Homepage>***HomePage***</Homepage>
		<Packager>
			<Name>pisicevir</Name>
			<Email>pisicevir@gmail.com</Email>
		</Packager>
		<License>As-Is</License>
		<PartOf>None</PartOf>
		<IsA>app:console</IsA>
		<Summary>pisicevir</Summary>
		<Description>***Aciklama***</Description>
		<Archive sha1sum="***Sha1Sum***" type="targz">***Dosya***</Archive>
	</Source>
	
	<Package>
		<Name>***PaketAdi***-pisicevir</Name>
		<Files>
			<Path fileType="all">/</Path>
		</Files>
	</Package>
	
	<History>
		<Update release="1">
			<Date>***Tarih***</Date>
			<Version>1.0</Version>
			<Comment>First release</Comment>
			<Name>pisicevir</Name>
			<Email>pisicevir@gmail.com</Email>
		</Update>
	</History>
</PISI>
"""