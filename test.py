a = "блаблабла мы готовы машины люди паровоз с 01.02.1011 по 14.06.1115  и мы бы сделали что-то с 15.01.13 по 12.03.14 и каупкуц ваып с 11.11 по 12.11"




import regex

ba = regex.findall("с ([0-9]{2}[/.-][0-9]{2}[/.-][0-9]{2,4}) по ([0-9]{2}[/.-][0-9]{2}[/.-][0-9]{2,4})", a)
print(ba)

bv = regex.findall("с ([0-9]{2}[/.-][0-9]{2}) по ([0-9]{2}[/.-][0-9]{2})", a)
print(bv)

