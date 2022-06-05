from operator import index

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_INDEX = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, 
    "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
    "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
    "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
    "y": 24, "z": 25
}

BABBINGTON_ALPHABET = {
    "a":"\N{COPTIC CAPITAL LETTER O}", "b":"\N{OLD HUNGARIAN CAPITAL LETTER EGY}",
    "c":"\N{OLD HUNGARIAN CAPITAL LETTER ES}", "d":"\N{COPTIC CAPITAL LETTER OLD COPTIC OOU}",
    "e":"\N{COPTIC CAPITAL LETTER ALFA}", "f":"\N{CAUCASIAN ALBANIAN LETTER EYN}",
    "g":"\N{COPTIC CAPITAL LETTER THETHE}", "h":"\N{COPTIC SMALL LETTER OOU}",
    "i":"\N{COPTIC CAPITAL LETTER IAUDA}", "j":" ", "k":"\N{GEORGIAN LETTER BAN}",
    "l":"\N{CAUCASIAN ALBANIAN LETTER SEYK}", "m":"\N{COPTIC OLD NUBIAN VERSE DIVIDER}",
    "n":"\N{CAUCASIAN ALBANIAN LETTER DZAY}", "o":"\N{OLD HUNGARIAN NUMBER FIVE}",
    "p":"\N{CAUCASIAN ALBANIAN LETTER GHEYS}", "q":"\N{GEORGIAN LETTER ON}", 
    "r":"\N{ARMENIAN CAPITAL LETTER BEN}", "s":"\N{COPTIC CAPITAL LETTER DALDA}",
    "t":"\N{CAUCASIAN ALBANIAN LETTER KAR}", "u":"\N{COPTIC SMALL LETTER SIMA}",
    "v":" ", "w":" ", "x":"\N{CAUCASIAN ALBANIAN LETTER YOWD}", 
    "y":"\N{CAUCASIAN ALBANIAN LETTER SHOY}", "z":"\N{COPTIC CAPITAL LETTER DIALECT-P HORI}", 
    "and":"\N{COPTIC SMALL LETTER DIALECT-P KAPA}", "for":"\N{GEORGIAN LETTER WE}", 
    "but":"\N{COPTIC CAPITAL LETTER AKHMIMIC KHEI}", "with":"\N{OLD HUNGARIAN CAPITAL LETTER A}", 
    "that":"\N{ARMENIAN CAPITAL LETTER KEN}", "if":"\N{ARMENIAN CAPITAL LETTER VEW}", 
    "as":"\N{GEORGIAN LETTER UN}", "of":"\N{GEORGIAN LETTER GHAN}", 
    "the":"\N{GEORGIAN LETTER TAR}", "by":"\N{GLAGOLITIC CAPITAL LETTER DOBRO}", 
    "so":"\N{GEORGIAN CAPITAL LETTER HOE}", "not":"\N{OLD HUNGARIAN CAPITAL LETTER EB}", 
    "when":"\N{COPTIC CAPITAL LETTER CRYPTOGRAMMIC GANGIA}", 
    "from":"\N{OLD HUNGARIAN CAPITAL LETTER ETY}", "this":"\N{GLAGOLITIC CAPITAL LETTER ONU}", 
    "is":"\N{GLAGOLITIC CAPITAL LETTER NASHI}", "in":"\N{COPTIC CAPITAL LETTER KHI}", 
    "say":"\N{GEORGIAN LETTER IN}", "me":"\N{GEORGIAN LETTER TAN}", 
    "my":"\N{GEORGIAN LETTER LAS}", "you":"\N{CAUCASIAN ALBANIAN LETTER QAY}", 
    "what":"\N{GEORGIAN LETTER DON}", "where":"\N{CAUCASIAN ALBANIAN LETTER TIWR}", 
    "which":"\N{CAUCASIAN ALBANIAN LETTER BET}", "there":"\N{GEORGIAN LETTER CHAR}", 
    "send":"\N{COPTIC CAPITAL LETTER OLD COPTIC HAT}", "receive":"\N{ARMENIAN SMALL LETTER FEH}", 
    "pray":"\N{GEORGIAN CAPITAL LETTER HE}"
    }
ATBASH_ALPHABET = {
    "a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u",
    "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o",
    "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i",
    "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", 
    "y":"b", "z":"a"
}
BACONIAN_ALPHABET = {
    "a":"aaaaa", "b":"aaaab", "c":"aaaba", "d":"aaabb", 
    "e":"aabaa", "f":"aabab", "g":"aabba", "h":"aabbb", 
    "i":"abaaa", "j":"abaaa", "k":"abaab", "l":"ababa",
    "m":"ababb", "n":"abbaa", "o":"abbab", "p":"abbba", 
    "q":"abbbb", "r":"baaaa", "s":"baaab", "t":"baaba", 
    "u":"baabb", "v":"baabb", "w":"babaa", "x":"babab",
    "y":"babba", "z":"babbb"
}

"""#TODO: finish these alphabets
PIGPEN_ALPHABET = {}
MUSIC_ALPHABET = {}
BILL_CIPHER_ALPHA = {}
THE_AUTHOR_ALPHA = {}
FUTURAMA_ALPHA = {}
TICK_TACK_TOE_ALPHA = {}
WINDOW_ALPHA = {}
LUNAR_ALPHABEET = {}"""

WHEELS = [
    "jfaebytdvlhgnpczxwqirsmuok", "wksrbqyzfeuanpvmcohigjdxtl", "tlaismyknxgrwbpfjeuozqhdcv", "tnwxryauzhpsfdoqvkcbielgmj", 
    "xycnwstfbzahopkruidqglvjem", "vcadtmpbuhigjswqxyznkfrole", "dxeufwhmaoqkvjscpgrynilbzt", "ryslugqfnmxzvpkabohdceijwt",
    "psrefaytjobuxilnmzgkdwcqhv", "hygftuwmevlzcdapxqroknisjb", "iwvcodsyjzngmltqrpubahxkef", "dmgyrzxwqalpeuvijfbnscohkt",
    "tnqzdojgbyivfwhxrlakeumscp", "dhxiavjnzklbgfecpwyroqumst", "pchuoelxkntfbgijzdswmavqyr", "exwqlvpgucthmjrzoifydskban",
    "kbnuxpljworyfqtszmveiacdgh", "uwbgjtkxncpvrsalzeqimyhdfo", "hopmxgibdftcqzslaurkejywnv", "xdymprevolqwaufctzjngibshk", 
    "epysugkifzhbnjqmoctxrwvlad", "exijtdmscogwzrlpyuqnafbhkv", "fclmajqzedyvuxnortkgpiwshb", "zkcmtevhfbixqlpywaojnrgsud", 
    "rcolguhfsjytpwxmneiavzqdkb", "aojifngptrxbeylcuskmzhvqwd", "ughltbjmdriqkeyawxfszvocpn", "xyqjdlikfzpgnrbhacemvtwuos", 
    "iqkjxyntfsreczmbdolgavuphw", "yughlqxrtozbdjmfkcnspveiaw", "bnymkioxjtucsvrqwpfhgledza", "oclypewxqriusvhgfnkbtjzadm", 
    "bespdlhjrnvoqmzkfawcxgutyi", "palmnjcdqibhugxektsfwzvryo", "tyfrgxbqpejiavmschuozlndkw", "bodvnumrfekysgqctwpxhiljza", 
    "xmkqarhifewgyobcljutvpsndz", "nzclivqrpaejsgkymfuhdobwxt", "vlpjhfrkgybcemzowiqdtunsax", "rydcushlnpwqgzaxktjeivmbof", 
    "chvqerxwjtasilnkobudfpgmzy", "hpbqifmarzjxtdecknlogswyvu", "pizovbrjxyncltawgmdqsfhkeu", "rykcjtlnquasxvzphdogwibmef", 
    "lwspuxvkrhzotnbfiymaqgdcej", "dnwypagbvkjzfmixceqsutrlho", "jdzvunaomgwbyfxrtekpiqhslc", "pbwkxgtcdnqfersmjoyhivazul", 
    "csxilzuekqfntdojygrbmpvahw", "nkytjbswumriazgdlechqvofxp", 
    ]
PLUGS = [
    'sf', 'ha', 'af', 'lt', 'bj', 'ma', 'ys', 'pq', 'jq', 'iy', 'pd', 'jm', 'oo', 'ia', 'gb', 'mb', 'rw', 'xt', 'yy', 'gh', 'kq', 
    'zi', 'po', 'dl', 'wy', 'ni', 'wj', 'hd', 'wl', 'eq', 'me', 'fd', 'ze', 'fh', 'vb', 'nk', 'xh', 'fp', 'ng', 'el', 'nf', 'xc', 
    'lv', 'kv', 'kb', 'rg', 'cm', 'mk', 'ed', 'ye', 'bg', 'ya', 'ao', 'ja', 'nu', 'kd', 'dj', 'im', 'fi', 'to', 'uf', 'ee', 'as', 
    'kl', 'st', 'bq', 'ew', 'hj', 'cz', 'gl', 'ts', 'cv', 'yh', 'bt', 'dm', 'ex', 'jy', 'ih', 'wk', 'yo', 'hn', 'rd', 'ud', 'bk', 
    'bb', 'gf', 'ay', 'uv', 'pp', 'ap', 'kz', 'zy', 'fr', 'kk', 'tr', 'kj', 'xb', 'fc', 'cd', 'ax', 'dv', 'ra', 'xj', 'jd', 'qx', 
    'yb', 'ir', 'it', 'zc', 'bx', 'uc', 'by', 'mr', 'xd', 'jf', 'yt', 'ch', 'mg', 'yj', 'cr', 'qp', 'xy', 'dt', 'dh', 'yq', 'ns', 
    'qv', 'ct', 'qe', 'fe', 'xi', 'cf', 'wv', 'zz', 'gg', 'ca', 'hr', 'ko', 'bm', 'px', 'qw', 'ur', 'lg', 'kr', 'ml', 'rt', 'pl', 
    'nz', 'mf', 'ut', 'xk', 'la', 'hi', 'hg', 'gt', 'rj', 'wf', 'xq', 'zw', 'mm', 'wc', 'vm', 'ym', 'em', 'mp', 'iw', 'pf', 'll', 
    'jp', 'sr', 'jb', 'ai', 'mo', 'vu', 'nn', 'cu', 'nj', 'jr', 'hl', 'bl', 'ev', 'vi', 'td', 'gy', 'ne', 'oq', 'lo', 'mq', 'hw',
    'je', 'xg', 'er', 'or', 'hy', 'sl', 'df', 'tc', 'pn', 'et', 'sg', 'us', 'xf', 'rq', 'tk', 'jx', 'zs', 'ta', 'am', 'ru', 'xe', 
    'ba', 'da', 'tx', 'au', 'pm', 'rn', 'dr', 'gx', 'rl', 'on', 'vt', 'hc', 'dn', 'vx', 'ar', 'nv', 'qg', 'uo', 'gm', 'lk', 'yr',
    'di', 'lz', 'he', 'ln', 'cj', 'pz', 'ij', 'eb', 'mj', 'pk', 'gw', 'ps', 'vr', 'jl', 'il', 'br', 'md', 'vz', 'jw', 'bs', 'du', 
    'nc', 'uq', 'zf', 'hk', 'tm', 'hz', 'qj', 'db', 'zq', 'en', 'ht', 'dw', 'lm', 'jk', 'zr', 'yf', 'ov', 'ho', 'rh', 'ua', 'pt', 
    'pa', 'wx', 'ig', 'dy', 'mu', 'pb', 'qt', 'dk', 'kc', 'wr', 'fx', 'kh', 'na', 'jv', 'hq', 'hu', 'fn', 'un', 'xx', 'lx', 'ki', 
    'xw', 'tp', 'vl', 'ji', 'tg', 'qa', 'zd', 'op', 'rc', 'wi', 'cc', 'uj', 'if', 'tt', 'vy', 'jj', 'qd', 'ak', 'up', 'za', 'av', 
    'fb', 'vg', 'rm', 'bi', 'gp', 'kp', 'bd', 'ub', 'sd', 'te', 'zv', 'ms', 'wd', 'yx', 'oc', 'oa', 'ws', 'fy', 'iu', 've', 'su', 
    'qu', 'sb', 'ic', 'dx', 're', 'ec', 'jn', 'wh', 'ka', 'qm', 'at', 'ls', 'fo', 'oh', 'ro', 'zh', 'is', 'rb', 'dc', 'pc', 'gq', 
    'fg', 'vh', 'jz', 'aq', 'yk', 'fa', 'ug', 'lc', 'ci', 'mx', 'ah', 'nb', 'ie', 'cq', 'ix', 'pj', 'ti', 'dp', 'lf', 'dd', 'np', 
    'id', 'le', 'ke', 'ii', 'qc', 'bc', 'nx', 'fz', 'dg', 'eo', 'ku', 'tw', 'lu', 'tn', 'hx', 'xr', 'kw', 'bn', 'sq', 'lb', 'cn', 
    'ga', 'qo', 'ae', 'qs', 'of', 'lq', 'xu', 'rv', 'qn', 'yw', 'ql', 'vo', 'fv', 'ww', 'wn', 'fq', 'vp', 'cb', 'eg', 'ei', 'tf',
    'ox', 'aj', 'ek', 'fm', 'ea', 'vq', 'ab', 'cs', 'pg', 'mz', 'pu', 'xn', 'ej', 'pe', 'uw', 'rs', 'tq', 'cw', 'nl', 'jh', 'zk', 
    'fl', 'ou', 'no', 'oy', 'bv', 'bh', 'mt', 'uz', 'pw', 'sv', 'zl', 'qy', 'yl', 'bp', 'lr', 'xa', 'ri', 'zo', 'de', 'cg', 'ot', 
    'mw', 'rz', 'nd', 'li', 'hv', 'ce', 'dq', 'sp', 'wq', 'zp', 'fu', 'nw', 'lp', 'tv', 'zx', 'cl', 'ue', 'zn', 'tu', 'xl', 'gr', 
    'nm', 'xp', 'ks', 'eu', 'gn', 'yp', 'yv', 'km', 'oz', 'zt', 'ly', 'ft', 'hs', 'qr', 'jc', 'xs', 'tl', 'eh', 'io', 'sx', 'fk', 
    'kn', 'pr', 'qz', 'gc', 'jo', 'ph', 'sw', 'rk', 'vc', 'es', 'qf', 'ag', 'an', 'fs', 'yn', 'xz', 'do', 'be', 'um', 'sa', 'qh', 
    'zm', 'ep', 'tz', 'zj', 'cp', 'ff', 'mh', 'wt', 'yd', 'zu', 'si', 'tb', 'jt', 'sy', 'vs', 'vn', 'vv', 'kt', 'al', 'jg', 'ac', 
    'rp', 'uk', 'sk', 'zg', 'wb', 'vk', 'wg', 'bf', 'uu', 'aa', 'ib', 'uh', 'in', 'zb', 'wp', 'ey', 'oe', 'ad', 'gv', 'hp', 'sz', 
    'ju', 'xm', 'ob', 'vd', 'ui', 'yu', 'co', 'hf', 'yz', 'oi', 'wo', 'vf', 'ef', 'az', 'hm', 'bz', 'pi', 'nt', 'oj', 'hb', 'lh', 
    'cy', 'mv', 'dz', 'qi', 'th', 'gd', 'nh', 'sj', 'iv', 'va', 'wu', 'om', 'bw', 'ny', 'yc', 'iq', 'js', 'iz', 'ol', 'gz', 'nr', 
    'od', 'xv', 'mn', 'kx', 'yg', 'se', 'gk', 'ds', 'we', 'sc', 'rf', 'fj', 'yi', 'my', 'rr', 'so', 'ss', 'gj', 'sm', 'kf', 'pv', 
    'ck', 'cx', 'ok', 'hh', 'ip', 'bu', 'vj', 'lw', 'uy', 'sn', 'nq', 'og', 'ul', 'qq', 'gu', 'ld', 'mc', 'bo', 'vw', 'os', 'mi', 
    'gs', 'ux', 'gi', 'kg', 'qk', 'fw', 'wm', 'rx', 'ow', 'aw', 'qb', 'ty', 'ik', 'tj', 'go', 'wz', 'py', 'ry', 'sh', 'ez', 'xo', 
    'ge', 'wa', 'ky', 'lj'
    ]


TEST_WHEELS = WHEELS[:3]
TEST_PLUGS = PLUGS[:6]
TEST_KEYS = ["key", "once upon a midnight dreary", "the quick brown fox jumps over the lazy dog"]
TEST_TEXT = """Hi my name is Ebony Dark'ness Dementia Raven Way 
and I have long ebony black hair -that's how I got my name- 
with purple streaks and red tips that reaches my mid-back 
and icy blue eyes like limpid tears 
and a lot of people tell me I look like Amy Lee 
-AN: if u don't know who she is get da hell out of here!-. 
I'm not related to Gerard Way but I wish I was because he's a major fucking hottie. 
I'm a vampire but my teeth are straight and white. I have pale white skin. 
I'm also a witch, and I go to a magic school called Hogwarts in England 
where I'm in the seventh year -I'm seventeen-. 
I'm a goth -in case you couldn't tell- and I wear mostly black. 
I love Hot Topic and I buy all my clothes from there. 
For example today I was wearing a black corset with matching lace around it 
and a black leather miniskirt, pink fishnets and black combat boots. 
I was wearing black lipstick, white foundation, black eyeliner and red eye shadow. 
I was walking outside Hogwarts. It was snowing and raining so there was no sun, 
which I was very happy about. A lot of preps stared at me. I put up my middle 
finger at them."""


def simplify_plaintext(plaintext):
    """removes spaces and punctuation from a plain text for better encryption
    
    >>> simplify_plaintext("`~!@#$%^&*()_+=-\|]}[{;:'<,>.?/Hello World")
    'helloworld'

    """

    punctuation = ",./?><;':[]\{}|=-)(*&^%$#@!~`_+\n \t"
    for punct in punctuation:
        plaintext = plaintext.replace(punct, "")
    
    plaintext = plaintext.replace('"','')

    return plaintext.lower()


def subsitution_cipher(plaintext, cipher_alphabet):
    """encodes a given plaintext with a cipher alphabet, returns a ciphertext string
    
    cipher_alphabets are dictionaries with letters and/or words as keys, cipher chars as values
    
    >>> subsitution_cipher("Hello world", BABBINGTON_ALPHABET)
    'ⲱⲀ𐕚𐕚𐳻 𐳻Բ𐕚Ⲿ'

    """

    ##first replace the full words in the plain text
    ciphertext = ""
    plain_words = plaintext.split()

    for word in plain_words:
        simple_word = simplify_plaintext(word)##remove punctuation AFTER splitting 

        if simple_word in cipher_alphabet:##check for full word in the cipher alphabet
            ciphertext += cipher_alphabet[simple_word]

        else:
            for char in simple_word:##if not a keyword replace each letter
                ciphertext += cipher_alphabet[char]

    return ciphertext


def shift_cipher(plaintext, shift):
    """encodes a given plaintext n-number of letters shifted down the alphabet
    
    >>> shift_cipher("Hello World", 6)
    'nkrrucuxrj'
    
    """

    ciphertext = ""

    plaintext = simplify_plaintext(plaintext) 

    for char in plaintext:
        char_idx = ALPHABET_INDEX[char]

        if char_idx + shift > 25:
            ciphertext += ALPHABET[char_idx + shift - 26]

        else:
            ciphertext += ALPHABET[char_idx + shift]            
    
    return ciphertext


def vigenere_cipher(plaintext, key):
    """encodes a given plaintext with a rotating shift cipher based on the alphabetIdx of a given key
    
    repeats the key over the length of the plaintext, giving each char in plaintext a coresponding key char
    shift each char using the index of the key char as the shift number

    >>> vigenere_cipher("Hello World", "test")
    'aidehagkeh'
    
    """

    plaintext = simplify_plaintext(plaintext)
    key = simplify_plaintext(key)

    key = key * len(plaintext)

    ciphertext = ""
    for idx, char in enumerate(plaintext):
        ciphertext += shift_cipher(char, ALPHABET_INDEX[key[idx]])
    
    return ciphertext


def enigma_machine(plaintext, swaps, wheels):
    """encodes a given plaintext via an enigma machine

    first letters from the swaps trade places in the plaintext
    second each character goes through a wheel, shifting according to the letter on it
        same for the second wheel
        same for the third wheel
    
    the first wheel rotates one degree for the next character
    when the first wheel rotates 26x
        the second wheel begins rotating
        the same for the third

    >>> enigma_machine("Hello World", TEST_PLUGS, TEST_WHEELS)
    'yyimejwjdd'

    TODO: something about a reflector so decoding is the same process as encoding

    """

    swapedtext = simplify_plaintext(plaintext)
    ciphertext = ""

    # Use .upper() to ensure the second swap won't reswap first
    for pair in swaps:
        swapedtext = swapedtext.replace(pair[0], pair[1].upper())
        swapedtext = swapedtext.replace(pair[1], pair[0].upper())

    swapedtext = swapedtext.lower()


    rotate1_num = 0 
    rotate2_num = 26
    rotate3_num = 26

    def rotate_wheel(wheel):
        extra = wheel[0]
        wheel = wheel[1:]

        return wheel + extra


    for char in swapedtext:
        wheel1 = wheels[0][0]
        wheel2 = wheels[1][0]
        wheel3 = wheels[2][0]

        cipher = shift_cipher(char, ALPHABET_INDEX[wheel1])
        if rotate1_num < 26:
            wheels[0] = rotate_wheel(wheels[0])
            rotate1_num += 1
        elif rotate1_num == 25:
            rotate1_num = 26
            rotate2_num = 0

        cipher = shift_cipher(cipher, ALPHABET_INDEX[wheel2])
        if rotate2_num < 26:
            wheels[1] = rotate_wheel(wheels[1])
            rotate2_num += 1
        elif rotate2_num == 25:
            rotate2_num = 26
            rotate3_num = 0

        cipher = shift_cipher(cipher, ALPHABET_INDEX[wheel3])
        if rotate3_num < 26:
            wheels[2] = rotate_wheel(wheels[2])
            rotate3_num += 1
        elif rotate3_num == 25:
            rotate3_num = 26
            rotate1_num = 0

        ciphertext += cipher

    return ciphertext


'''##TODO: encoders to implement
def binary_conversion(plaintext):
    """given a plaintext, convert the text to binary"""

def autokey_cipher(plaintext, key):
    """encodes a plaintext with the autokey cipher
    
    keys are placed over top the plaintext, then plaintext is repeated afterwards
    ciphertext is encoded using the alphabet index of the corresponding key(+plaintext) char"""

def beaufort_cipher(plaintext, key):
    """encodes a plainext with a beaufort cipher
    
    keys are repeated to the length of plaintext, 
    then each plaintext vchar is encoded using 
    the alphabet index of the corresponding key, but in reverse
    """

def zodiac_cipher(plaintext):'''


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED!\n")
    