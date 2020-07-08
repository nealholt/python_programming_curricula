'''
Students could see whose english essay has the highest entropy.

Twain source: i18nguy.com/twain.html

Source I used:
towardsdatascience.com/the-intuition-behind-shannons-entropy-e74820fe9800

'''

import math

def getEntropy(sentence):
    '''Equation 3.49 (Shannon's Entropy) is implemented.
    Source:
    https://towardsdatascience.com/the-intuition-behind-shannons-entropy-e74820fe9800

    It's important to note that you loop over the alphabet'''
    entropy = 0
    # There are 256 possible ASCII characters
    for character_i in range(256):
        Px = sentence.count(chr(character_i))/len(sentence)
        if Px > 0:
            entropy -= Px * math.log(Px, 2)
    return entropy


'''In the decision tree progam later on I use this better entropy function
that takes the alphabet as an argument:
def getEntropy(data_list, alphabet):
    entropy = 0
    for a in alphabet:
        Px = data_list.count(a) / len(data_list)
        if Px > 0:
            entropy -= Px * math.log(Px, 2)
    return entropy

'''

first_sentence = 'For example, in Year 1 that useless letter "c" would be dropped to be replased either by "k" or "s", and likewise "x" would no longer be part of the alphabet.'
last_sentence = 'Fainali, xen, aafte sam 20 iers ov orxogrefkl riform, wi wud hev a lojikl, kohirnt speling in ius xrewawt xe Ingliy-spiking werld.'

print('Comparison normalized by length')
print(getEntropy(first_sentence)/len(first_sentence))
print(getEntropy(last_sentence)/len(last_sentence))

print()
print('Same length comparison')
print(getEntropy(first_sentence[:len(last_sentence)]))
print(getEntropy(last_sentence))

first_paragraph = 'For example, in Year 1 that useless letter "c" would be dropped to be replased either by "k" or "s", and likewise "x" would no longer be part of the alphabet. The only kase in which "c" would be retained would be the "ch" formation, which will be dealt with later. Year 2 might reform "w" spelling, so that "which" and "one" would take the same konsonant, wile Year 3 might well abolish "y" replasing it with "i" and Iear 4 might fiks the "g/j" anomali wonse and for all.'
last_paragraphs = 'Jenerally, then, the improvement would kontinue iear bai iear with Iear 5 doing awai with useless double konsonants, and Iears 6-12 or so modifaiing vowlz and the rimeining voist and unvoist konsonants. Bai Iear 15 or sou, it wud fainali bi posibl tu meik ius ov thi ridandant letez "c", "y" and "x" -- bai now jast a memori in the maindz ov ould doderez -- tu riplais "ch", "sh", and "th" rispektivli. Fainali, xen, aafte sam 20 iers ov orxogrefkl riform, wi wud hev a lojikl, kohirnt speling in ius xrewawt xe Ingliy-spiking werld.'

print()
print('Comparison normalized by length')
print(getEntropy(first_paragraph)/len(first_paragraph))
print(getEntropy(last_paragraphs)/len(last_paragraphs))

print()
print('Same length comparison')
print(getEntropy(first_paragraph))
print(getEntropy(last_paragraphs[:len(first_paragraph)]))

print()
print('Test comparison')
print(getEntropy('11110000'))
print(getEntropy('11111110'))
print(getEntropy('11111111'))

gettysburg_original = 'four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal. now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. we are met on a great battle-field of that war. we have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. it is altogether fitting and proper that we should do this. but, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. the brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. the world will little note, nor long remember what we say here, but it can never forget what they did here. it is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. it is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under god, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'
gettysburg_improved = 'for skor and seven iers ago ower faxers brot forx on xis kontinent, a new naiyun, konsived in liberti, and dedicaited to the proposiyun xat all men ar kreeaited ekwal. now we ar engaijed in a grait sivil war, testin wexer xat naiyun, or ani naiyun so konseeved and so dedikaited, kan lon ender. we ar met on a grait batl-feeld of xat war. we hav kom to dedikait a poryun of xat feeld, as ai final restin plais for xos hoo heer gaiv xer lievs xat xat nayun miet liv. it is altugexer fiting and proper xat we yold du xis. but, in a larjer sens, we kan not dedikait -- we kan not konsekrait -- we kan not halow -- xis grownd. xi braiv men, living and ded, hu struhgled heer, hav konsekraited it, far abov ower por power to ad or detrakt. xi world wil litl not, nor lon remember wat we sai heer, but it kan never forget wat xai did heer. it is for us xi living, raxer, to be dedikated heer to xi unfiniyed work wic xai hu fot heer hav xus far so noblee advansed. it is raxer for us tu bee heer dedikated to the grait task remaining befor us -- xat from xees onored ded wee taik inkreesed devoyun tu xat caus for wic xai gaiv xi last ful meser of devoyun -- xat wee heer hylee resolv xat xees ded yal not hav died in vain -- xat xis nayun, under god, yal hav a nu berx of freedom -- and xat government of xi peepl, bai xi peepl, for xi peepl, yal not periy from xi erx.'

print()
print('gettysburg noralized by length')
print(getEntropy(gettysburg_original)/len(gettysburg_original))
print(getEntropy(gettysburg_improved)/len(gettysburg_improved))

print()
print('gettysburg')
print(getEntropy(gettysburg_original))
print(getEntropy(gettysburg_improved))

