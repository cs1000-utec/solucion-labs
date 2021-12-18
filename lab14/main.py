original_str = """Bgc-bfufb tegaedppqna ql aggv zge xof tegaedppfe'l lgjb.

Xof adpf vflqanfe logjbvn'x hf pdwqna d cgebv qn coqro xof tbdkfe ql mjlx d lpdbb tdex. Xof tbdkfe QL XOF HGLL; qx'l kgje vjxk xg fnxfexdqn oqp ge ofe.

Zgrjl ql d pdxxfe gz vfrqvqna codx xoqnal kgj def ngx agqna xg vg.

Xof rglx gz dvvqna d zfdxjef qln'x mjlx xof xqpf qx xdwfl xg rgvf qx. Xof rglx dblg qnrbjvfl xof dvvqxqgn gz dn ghlxdrbf xg zjxjef fstdnlqgn. Xof xeqrw ql xg tqrw xof zfdxjefl xodx vgn'x zqaox fdro gxofe. - Mgon Rdepdrw.

(ccc.adpdljxed.rgp/uqfc/nfcl/234346?utkjpvbjr)

(ccc.hedqnkijgxf.rgp/ijgxfl/djxogel/m/mgon_rdepdrw.oxpb)"""

freqLang = "TOEAIRSNCUPFLHMDYVGBW"

str = original_str.lower()

count = {}

for i in range(0, len(str)):
  c = str[i]
  
  if(c in count):
    count[c] += 1
  else:
    count[c] = 1

print(count)

sorted_repetitions = sorted(count, key=count.get)[::-1]

print("sorted")
print(sorted_repetitions)

clean_repetitions = []

for v in sorted_repetitions:
  if(v.isalpha()):
    clean_repetitions.append(v)

print(clean_repetitions)

map_replace = {}

for i in range(0,len(clean_repetitions)):
  c = clean_repetitions[i]
  map_replace[c] = freqLang[i]

print(map_replace)

for i in range(0, len(original_str)):
  c = original_str[i]

  if(c.lower() in map_replace):
    rep = map_replace[c.lower()]
    if(c.isupper()):
      print(rep, end="")
    else:
      print(rep.lower(), end="")
  else:
    print(c, end="")
