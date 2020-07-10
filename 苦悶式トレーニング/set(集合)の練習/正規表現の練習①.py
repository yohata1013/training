import re #正規表現

#おきまり
r = re.compile('^https?://([^/]+).*$')

str = 'https://ibm.com/cras/in.jsp?justo=massa&sit=volutpat&amet=convallis&sapien=morbi&dignissim=odio&vestibulum=odio'
#正規表現利用時に使うもの（ドメインをうまく取り出す）
domain = r.search(str).group(1)

print(domain)
