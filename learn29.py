'''
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!
Examples:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:
def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty
Have fun coding it and please don't forget to vote and rank this kata! :-)
要构建加密的字符串：
从字符串中获取每个第二个字符，然后获取不是每个第二个字符的其他字符，并将它们合并为新的String。
这样做n次！
例子：
“这是一个测试！”，1->“ hsi etTi sats！”
“这是一个测试！”，2->“ hsi etTi sats！” ->“ eT ashi tist！”
编写两种方法：
def加密（文本，n）
def解密（encrypted_text，n）
对于这两种方法：
如果输入字符串为null或为空，则返回该值！
如果n <= 0，则返回输入文本。
此kata是简单加密系列的一部分：
简单加密＃1-交替分割
简单加密＃2-索引差异
简单加密＃3-扭转局面
简单加密＃4-Qwerty
编码很有趣，请不要忘了投票给这个kata排名！ :-)
'''
#高赞
def decrypt(encrypted_text, n):
    if encrypted_text in ("",None):
        return encrypted_text
    ndx = len(encrypted_text) // 2

    for i in range(n):
        a = encrypted_text[:ndx]
        b = encrypted_text[ndx:]
        encrypted_text = ''.join(b[i:i+1] + a[i:i+1] for i in range(ndx+1))
    return encrypted_text
    
def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

print(encrypt("This is a test!", 0))
print(encrypt("This is a test!", 1))
print(decrypt(" Tah itse sits!", 3))