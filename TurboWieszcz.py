﻿#! /usr/bin/env python

# Turbo Wieszcz ++ Python version, v1.0
# (c)2017 Noniewicz.com, Jakub Noniewicz
#///////////////////////////////////////////////////////////////////////////////
#// based directly on (translated from): previous version written for Windows in Delphi
#// which was based directly on: previous version written for Commodore C-64 sometime in 1993
#// by me (Jakub Noniewicz) and Freeak (Wojtek Kaczmarek)
#// which was based on:
#// idea presented in "Magazyn Amiga" magazine and implemented by Marek Pampuch.
#// also inspired by version written for iPhone by Tomek (Grych) Gryszkiewicz.
#// and versions written in C, JavaScript, Pascal, PHP and as CGI by Tomek (Grych) Gryszkiewicz.
#// note: there are also ZX Spectrum (ASM Z80) and Android (Java) versions
#///////////////////////////////////////////////////////////////////////////////
# created: 20171021 22:00-23:05
# updated: 20171021 23:40-23:59
# updated: 20171022 00:00-01:10


import string, sys, random


class TurboWieszcz:
    titles = [
        'Zagłada',
        'To już koniec',
        'Świat ginie',
        'Z wizytą w piekle',
        'Kataklizm',
        'Dzień z życia...',
        'Masakra',
        'Katastrofa',
        'Wszyscy zginiemy...',
        'Pokój?',
        'Koniec',
        'Koniec ludzkości',
        'Telefon do Boga',
        'Wieczne ciemności',
        'Mrok',
        'Mrok w środku dnia',
        'Ciemność',
        'Piorunem w łeb',
        'Marsz troli',
        'Szyderstwa Złego',
        'Okrponości świata',
        'Umrzeć po raz ostatni',
        'Potępienie',
        'Ból mózgu',
        'Wieczne wymioty',
        'Zatrute dusze',
        'Uciekaj',
        'Apokalipsa',
        'Złudzenie pryska',
        'Makabra',
        'Zagłada świata',
        'Śmierć',
        'Spokój']
    ENDINGS1 = ['.', '...', '.', '!', '.']
    ENDINGS2 = ['', '...', '', '!', '']
    TRYB2ORDER = [[0,1,2,3], [0,1,3,2], [0,2,1,3]] # ABAB, ABBA, AABB

    data = [[0 for x in range(32)] for y in range(4)] # note: lame const!

#///////////////////////////////////////////////
#//po 10
    data[0][0]  = 'Czy na te zbrodnie nie będzie kary?'
    data[0][1]  = 'Opustoszały bagna, moczary'
    data[0][2]  = 'Na nic się modły zdadzą ni czary'
    data[0][3]  = 'Z krwi mordowanych sączą puchary'
    data[0][4]  = 'To nietoperze, węże, kalmary'
    data[0][5]  = 'Próżno nieszczęśni sypią talary'
    data[0][6]  = 'Za co nam znosić takie ciężary'
    data[0][7]  = 'Złowrogo iskrzą kóbr okulary'
    data[0][8]  = 'Próżno swe modły wznosi wikary'
    data[0][9]  = 'Pustoszą sny twoje złe nocne mary'
    data[0][10] = 'Próżno nieszczęśnik sypie talary'
    data[0][11] = 'Przedziwnie tka się życia logarytm'
    data[0][12] = 'Już Strach wypuścił swoje ogary'
    data[0][13] = 'Niebawem zginiesz w szponach poczwary'
    data[0][14] = 'Wbijają pale złote kafary'
    data[0][15] = 'Życie odkrywa swoje przywary'
    data[0][16] = 'Na dnie ponurej, pustej pieczary'
    data[0][17] = 'Apokalipsy nadeszły czary'
    data[0][18] = 'Upadły anioł wspomina chwałę'
    data[0][19] = 'Życie ukrywa swoje przywary'
    data[0][20] = 'Dziwnych owadów wzlatują chmary'
    data[0][21] = 'Bombowce biorą nasze namiary'
    data[0][22] = 'Nie da się chwycić z czartem za bary'
    data[0][23] = 'Próżno frajerzy sypią talary'
    data[0][24] = 'Nie da sie wyrwać czartom towaru'
    data[0][25] = 'Po co nam sączyć podłe browary'
    data[0][26] = 'Diler już nie dostarczy towaru'
    data[0][27] = 'Lokomotywa nie ma już pary'
    data[0][28] = 'Gdy nie każdego stać na browary'
    data[0][29] = 'Pożarł Hilary swe okulary'
    data[0][30] = 'Spowiły nas trujące opary'
    data[0][31] = 'To nie jest calka ani logarytm'
#///////////////////////////////////////////////
#//po 8
    data[1][0]  = 'Już na arenę krew tryska'
    data[1][1]  = 'Już piana cieknie im z pyska'
    data[1][2]  = 'Już hen w oddali gdzieś błyska'
    data[1][3]  = 'Śmierć w kącie czai się bliska'
    data[1][4]  = 'Niesamowite duchów igrzyska'
    data[1][5]  = 'Już zaciskając łapiska'
    data[1][6]  = 'Zamiast pozostać w zamczyskach'
    data[1][7]  = 'Rzeka wylewa z łożyska'
    data[1][8]  = 'Nieszczęść wylała się miska'
    data[1][9]  = 'Już zaciskając zębiska'
    data[1][10] = 'Otwarta nieszczęść walizka'
    data[1][11] = 'Niczym na rzymskich boiskach'
    data[1][12] = 'Czart wznieca swe paleniska'
    data[1][13] = 'A w mroku świecą zębiska'
    data[1][14] = 'Zewsząd dochodzą wyzwiska'
    data[1][15] = 'Świętych głód wiary przyciska'
    data[1][16] = 'Ponuro patrzy z ich pyska'
    data[1][17] = 'Mgła stoi na uroczyskach'
    data[1][18] = 'Kości pogrzebią urwiska'
    data[1][19] = 'Głód wiary tak nas przyciska'
    data[1][20] = 'Runęły skalne zwaliska'
    data[1][21] = 'Czart rozpala paleniska'
    data[1][22] = 'A w mroku słychać wyzwiska'
    data[1][23] = 'Znów pusta żebraka miska'
    data[1][24] = 'Diabelskie to są igrzyska'
    data[1][25] = 'Nie powiedz diabłu nazwiska'
    data[1][26] = 'Najgłośniej słychać wyzwiska'
    data[1][27] = 'Diabelskie mają nazwiska'
    data[1][28] = 'Tam uciekają ludziska'
    data[1][29] = 'Tak rzecze stara hipiska'
    data[1][30] = 'Gdzie dawne ludzi siedliska'
    data[1][31] = 'Najgłośniej piszczy hipiska'
#///////////////////////////////////////////////
#//po 10
    data[2][0]  = 'Rwą pazurami swoje ofiary'
    data[2][1]  = 'Nic nie pomoże tu druid stary'
    data[2][2]  = 'To nocne zjawy i senne mary'
    data[2][3]  = 'Niegroźne przy nich lwowskie batiary'
    data[2][4]  = 'Pod wodzą księżnej diablic Tamary'
    data[2][5]  = 'Z dala straszliwe trąbia fanfary'
    data[2][6]  = 'Skąd ich przywiodły piekła bezmiary'
    data[2][7]  = 'Zaś dookoła łuny, pożary'
    data[2][8]  = 'A twoje ciało rozszarpie Wilk Szary'
    data[2][9]  = 'Tu nie pomoże już siła wiary'
    data[2][10] = 'Tak cudzych nieszczęść piją nektary'
    data[2][11] = 'Wszystko zalewa wrzący liparyt'
    data[2][12] = 'Zabójcze są ich niecne zamiary'
    data[2][13] = 'Zatrute dusze łączą się w pary'
    data[2][14] = 'Świat pokazuje swoje wymiary'
    data[2][15] = 'Z życiem się teraz weźmiesz za bary'
    data[2][16] = 'Brak uczuć, chęci, czasem brak wiary'
    data[2][17] = 'Wspomnij, co mówił Mickiewicz stary'
    data[2][18] = 'Spalonych lasów straszą hektary'
    data[2][19] = 'Z życiem się dzisiaj weźmiesz za bary'
    data[2][20] = 'Ksiądz pozostaje nagle bez wiary'
    data[2][21] = 'Papież zaczyna odprawiać czary'
    data[2][22] = 'Tu nie pomoże paciorek, stary'
    data[2][23] = 'Niegroźne przy nich nawet Atari'
    data[2][24] = 'Takie są oto piekła bezmiary'
    data[2][25] = 'A teraz nagle jesteś już stary'
    data[2][26] = 'Mordercy liczą swoje ofiary'
    data[2][27] = 'I bez wartości są już dolary'
    data[2][28] = 'Gdzie się podziały te nenufary'
    data[2][29] = 'Upada oto dąb ten prastary'
    data[2][30] = 'Bystro śmigają nawet niezdary'
    data[2][31] = 'Już nieruchome ich awatary'
#///////////////////////////////////////////////
#//po 8
    data[3][0]  = 'Wnet na nas też przyjdzie kryska'
    data[3][1]  = 'Znikąd żadnego schroniska'
    data[3][2]  = 'Powietrze tnie świst biczyska'
    data[3][3]  = 'Rodem z czarciego urwiska'
    data[3][4]  = 'I swąd nieznośny się wciska'
    data[3][5]  = 'Huk, jak z wielkiego lotniska'
    data[3][6]  = 'Złowroga brzmią ich nazwiska'
    data[3][7]  = 'W kącie nieśmiało ktoś piska'
    data[3][8]  = 'Ktoś obok morduje liska'
    data[3][9]  = 'Krwią ociekają zębiska'
    data[3][10] = 'Wokoło dzikie piarżyska'
    data[3][11] = 'I żądza czai się niska'
    data[3][12] = 'Diabeł cię dzisiaj wyzyska'
    data[3][13] = 'Płoną zagłady ogniska'
    data[3][14] = 'Gwałt niech się gwałtem odciska!'
    data[3][15] = 'Stoisz na skraju urwiska'
    data[3][16] = 'Tam szatan czarta wyiska'
    data[3][17] = 'Uciekaj, przyszłość jest mglista'
    data[3][18] = 'Nadziei złudzenie pryska'
    data[3][19] = 'Wydziobią oczy ptaszyska'
    data[3][20] = 'Padają łby na klepisko'
    data[3][21] = 'Śmierć zbiera żniwo w kołyskach'
    data[3][22] = 'Coś znowu zgrzyta w łożyskach'
    data[3][23] = 'Spadasz z wielkiego urwiska'
    data[3][24] = 'Lawa spod ziemi wytryska'
    data[3][25] = 'Wokoło grzmi albo błyska'
    data[3][26] = 'Fałszywe złoto połyska'
    data[3][27] = 'Najwięcej czart tu uzyska'
    data[3][28] = 'Owieczki Zły tu pozyska'
    data[3][29] = 'Owieczki spadły z urwiska'
    data[3][30] = 'Snują się dymy z ogniska'
    data[3][31] = 'To czarne lecą ptaszyska'

    zwrotek = 4
    powtorzeniaOk = False
    tryb = 0
    wiersz = ""
    title_id = 0
    numer = [[0 for x in range(4)] for y in range(4)]
    ending = [[0 for x in range(4)] for y in range(2)]

    def setcount(self, newzwrotek):
        self.zwrotek = newzwrotek
        self.numer = [[0 for x in range(self.zwrotek)] for y in range(4)]
        self.ending = [[0 for x in range(self.zwrotek)] for y in range(2)]

    def checkUniqOK(self, z, w, value):
        r = True
        if (not self.powtorzeniaOk):
            for i in range(z):
                if (self.numer[w][i] == value):
                    r = False
        return r

    def setrndrow(self, z, w):
        while True:
            self.numer[w][z] = random.randint(0, 32-1)  # note: lame const!
            if ((z == 0) or self.checkUniqOK(z, w, self.numer[w][z])):
                break

    def koniec(self, z, w, s):
        chk = True
        if (len(s) > 0):
            if s[-1] in ['?', '!']:
                chk = False
        result = ''
        if ((w == 1) and chk):
            result = self.ENDINGS2[self.ending[0][z]]
        if ((w == 3) and chk):
            result = self.ENDINGS1[self.ending[1][z]]
        return result

    def strofa(self, z, w, w0):
        s = self.data[w][self.numer[w][z]]
        return ' ' + s + self.koniec(z, w0, s) + "\n"

    def zwrotka(self, z):
        return(
          self.strofa(z, self.TRYB2ORDER[self.tryb][0], 0) + self.strofa(z, self.TRYB2ORDER[self.tryb][1], 1) +
          self.strofa(z, self.TRYB2ORDER[self.tryb][2], 2) + self.strofa(z, self.TRYB2ORDER[self.tryb][3], 3)
          )

    def generuj(self, newone):
        if (self.zwrotek < 1):
            exit
        if (newone):
            self.title_id = random.randint(0, len(self.titles)-1)
            for z in range(self.zwrotek):
                for w in range(4):
                    self.numer[w][z] = -1
                self.ending[0][z] = random.randint(0, len(self.ENDINGS2)-1)
                self.ending[1][z] = random.randint(0, len(self.ENDINGS1)-1)
        for z in range(self.zwrotek):
            self.setrndrow(z, 0)
            self.setrndrow(z, 1)
            self.setrndrow(z, 2)
            self.setrndrow(z, 3)
        self.wiersz = "\n " + self.titles[self.title_id]+ " \n\n"
        for z in range(self.zwrotek):
            self.wiersz += self.zwrotka(z) + "\n"

def main():
    random.seed()

    if (len(sys.argv) >= 2):
        zwr = int(sys.argv[1])
    else:
        zwr = 4
    if (len(sys.argv) >= 3):
        tr = int(sys.argv[2])
    else:
        tr = 0
    if (len(sys.argv) >= 4):
        if (int(sys.argv[3]) == 0):
            po = False
        else:
            po = True
    else:
        po = False

    twobj = TurboWieszcz()
    twobj.setcount(zwr)
    twobj.tryb = tr
    twobj.powtorzeniaOk = po
    twobj.generuj(True)
    print(twobj.wiersz)


if __name__ == '__main__':
    main()
