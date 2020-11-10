zpráva = "MZONBZSJTAXKZHMENQLZBDSZHMENQLZBDAXKNTANGZSZHMENQLZBDAXKZATGSNAXKNMZONBZSJTTANGZURDBGMNONURSZKNRJQYDMHZADYMHMDONURSZKNMHBBNIDRSUMHAXKYHUNSZYHUNSAXKRUDSKNKHCHSNRUDSKNUDSLDRUHSHZSLZIDMDONGKSHKZNCANGZAXKONRKZMBKNUDJILDMDLIZMSDMOQHRDKOQNSNZAXUXCZKRUDCDBSUHNSNLRUDSKDZAXURHBGMHTUDQHKHRJQYDMDGNIZMRZLMDAXKSHLRUDSKDLZKDOQHRDKZAXNSNLRUDSKDUXCZKRUDCDBSUHAXKNSTOQZUDRUDSKNJSDQDNRUDBTIDJZYCDGNBKNUDJZSNOQHBGZYDKNCNRUDSZMZRUDSDAXKRUDSRJQYDMDIONURSZKZKDRUDSGNMDONYMZKOQHRDKCNRUDGNUKZRSMHGNZKDIDGNUKZRSMHGNMDOQHIZKHSDLOZJJSDQHGNOQHIZKHZUDQHUIDGNILDMNCZKLNBRSZSRDANYHLHCDSLH"

abeceda = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for klíč in range(len(abeceda)):
   přeložení = ''
   for symbol in zpráva:
      if symbol in abeceda:
         číslo = abeceda.find(symbol)
         číslo = číslo - klíč
         if číslo < 0:
            číslo = číslo + len(abeceda)
         přeložení = přeložení + abeceda[číslo]
      else:
         přeložení = přeložení + symbol
print(klíč, přeložení)
