al_Xorazmiy = {
    'ismi' : 'al-Xorazmiy',
    'yurti' : 'Xiva',
    'tugulgan_sanasi' : '783',
    'sohasi' : ['matematik','astronom','geograf'],
    'vafoti' : '850',
    'umri' : '67',
    'asarlari' : ['Arifmetika','Surat al-Arz']
}
Ibn_Sin0 = {
    'ismi' : 'Ibn Sino',
    'yurti' : 'Buxoro',
    'tugulgan_sanasi' : '980',
    'sohasi' : ['olim','tabib','faylasuf'],
    'vafoti' : '1037',
    'umri' : '57',
    'asarlari' : ['Tib qonunlari']
}
al_Fargoniy = {
    'ismi' : 'al-Farg\'oniy',
    'yurti' : 'Farg\'ona',
    'tugulgan_sanasi' : '798',
    'sohasi' : ['matematik','astronom','geograf'],
    'vafoti' : '865',
    'umri' : '67',
    'asarlari' : ['Kitob al-harakot as-samoviya va javomi','ilm an-nujum']
}
Termiziy = {
    'ismi' : 'Termiziy',
    'yurti' : 'Termiz',
    'tugulgan_sanasi' : '824',
    'sohasi' : 'muaddis',
    'vafoti' : '892',
    'umri' : '68',
    'asarlari' : ['atTaʼrix','alIlal filhadis']
}

ajdodlar = [al_Xorazmiy, Ibn_Sin0, al_Fargoniy, Termiziy]

for ajdod in ajdodlar :
    habar = f"{ajdod['ismi']}ning asarlari : "
    print(habar)

    for asar in ajdod['asarlari']:
        print(asar)

    print()
