import sys
import binascii
from Crypto.PublicKey import RSA
from base64 import b64decode



print "\n"

print "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "\t        RSA Hastad Attack         "
print "\t         JulesDT -- 2016          "
print "\t         License GNU/GPL          "
print "\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


def chinese_remainder(n, a):
	sum = 0
	prod = reduce(lambda a, b: a * b, n)

	for n_i, a_i in zip(n, a):
		p = prod / n_i
		sum += a_i * mul_inv(p, n_i) * p
	return sum % prod


def mul_inv(a, b):
	b0 = b
	x0, x1 = 0, 1
	if b == 1: return 1
	while a > 1:
		q = a / b
		a, b = b, a % b
		x0, x1 = x1 - q * x0, x0
	if x1 < 0: x1 += b0
	return x1


def find_invpow(x, n):
	high = 1
	while high**n < x:
		high *= 2
	low = high / 2
	while low < high:
		mid = (low + high) // 2
		if low < mid and mid**n < x:
			low = mid
		elif high > mid and mid**n > x:
			high = mid
		else:
			return mid
	return mid + 1


def parseC(argv, index, verbose):
	import string
	file = open(argv[index], 'r')
	cmd = ' '.join(argv)
	fileInput = ''.join(file.readlines()).strip()
	if '--decimal' in cmd:
		if verbose:
			print "##"
			print "##", fileInput
			print "## Considered as decimal input"
			print "##"
		return long(fileInput)
	elif '--hex' in cmd:
		if verbose:
			print "##"
			print "##", fileInput
			print "## Considered as hexadecimal input"
			print "##"
		return long(fileInput, 16)
	elif '--b64' in cmd:
		if verbose:
			print "##"
			print "##", fileInput
			print "## Considered as base64 input"
			print "##"
		return long(binascii.hexlify(binascii.a2b_base64(fileInput)), 16)
	else:
		try:
			fileInput = long(fileInput)
			if verbose:
				print "##"
				print "##", fileInput
				print "## Guessed as decimal input"
				print "##"
			return long(fileInput)
		except ValueError:
			if all(c in string.hexdigits for c in fileInput):
				if verbose:
					print "##"
					print "##", fileInput
					print "## Guessed as hexadecimal input"
					print "##"
				return long(fileInput, 16)
			else:
				if verbose:
					print "##"
					print "##", fileInput
					print "## Guessed as base64 input"
					print "##"
				return long(
				    binascii.hexlify(binascii.a2b_base64(fileInput)), 16)
			pass


def parseN(argv, index):
	file = open(argv[index], 'r')
	fileInput = ''.join(file.readlines()).strip()
	try:
		fileInput = long(fileInput)
		return fileInput
	except ValueError:
		from Crypto.PublicKey import RSA
		return long(RSA.importKey(fileInput).__getattr__('n'))
		pass


if __name__ == '__main__':
	e = 3
	cmd = ' '.join(sys.argv)
	if '-v' in cmd or '--verbose' in cmd:
		verbose = True
	else:
		verbose = False
	n0 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
	n1 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
	n2 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723

	c0 = 261345950255088824199206969589297492768083568554363001807292202086148198677263604958247638518239089545015544140878441375704999371548235205708718116265184277053405937898051706510050325657424248032017194168466912140157665066494528590260879287464030275170787644749401275343677539640347609231708327119700420050952
	c1 = 147535246350781145803699087910221608128508531245679654307942476916759248448374688671157343167317710093065456240596223287904483080800880319712443044372346198448258006286828355244986776657425121775659144630571637596283100201930037799979864768887420615134036083295810488407488056595808231221356565664602262179441
	c2 = 633230627388596886579908367739501184580838393691617645602928172655297372282390454586345936209841638502749645277206386289490247066959822668419069562380546618337543323956757811325946190976649051724173510367477564435069180291575386473277111391106753472257905377429144209593931226163885326581862398737742032667573
	n = [n0, n1, n2]
	a = [c0, c1, c2]

	result = (chinese_remainder(n, a))
	resultHex = str(hex(find_invpow(result, 3)))[2:-1]
	print ""
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "Decoded Hex :\n", resultHex
	print "---------------------------"
	print "As Ascii :\n", resultHex.decode('hex')
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
