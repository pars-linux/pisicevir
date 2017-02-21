#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pisicevir Pardus için bir paket çevirme aracıdır.
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
import debian

argumanlar = sys.argv[1:]
dargumanlar = ("--yardim", "--dbtemizle", "--listele", "--gecicitemizle")

yardim_metni = \
"""
Kullanım şekli: pisicevir [paketadi] {fonksiyon}
Desteklenen dağıtımlar: debian-deb

Fonksiyonlar:

--yardim         = bu yardım metnini görüntüler.
--dbtemizle      = veritabanını temizler.
--listele        = çevirdiğiniz paketleri bağımlılıklarıyla birlikte listeler.
--dbyoksay       = çevirdiğiniz paketi veritabanına eklemez.
--gecicitemizle  = hatalardan dolayı kalmış olabilecek geçici dizinleri siler.
"""

db = arc.db

def kontrolk():
	if os.environ["USER"] != "root":
		print 'Hata[0] - Yetki Hatası: Pisicevir root olarak çalıştırılmalıdır. Lütfen root olun veya "sudo" komutunu kullanın.'
		sys.exit()

def pisicevir(paket_adi):
	kontrolk()
	debian.deb_to_pisi(paket_adi, argumanlar)

try:
	arguman_paket = sys.argv[1]
	if "--yardim" in argumanlar:
		print yardim_metni
	if "--dbtemizle" in argumanlar:
		arc.dbtemizle(db)
	if "--listele" in argumanlar:
		arc.listele(db)
	if "--gecicitemizle" in argumanlar:
		arc.gecicitemizle()
	if arguman_paket[-4:] == ".deb":
		pisicevir(arguman_paket)
	if (arguman_paket not in dargumanlar) and (arguman_paket[-4:] != ".deb"):
		print "Hata[3]: Eksik yada yanlış arguman."
except(IndexError):
	print 'Hata[1] - Arguman Hatası: Lütfen komutunuzu kontrol edin ve pisicevir --yardim" komutuna bakın.'
	sys.exit()
except(IOError):
	print "Hata[2] - Okuma Hatası: Dosya bulunamadı."
	sys.exit()