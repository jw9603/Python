def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    ans = []
    letter = letter.split()
    for i in letter:
        if i in morse.keys():
            ans.append(morse.get(i))
    
    return ''.join(ans)

if __name__ =='__main__':
    print(solution(".--. -.-- - .... --- -."))