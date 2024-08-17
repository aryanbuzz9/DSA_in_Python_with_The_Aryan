def get_nice(s):
    return len(set(s.lower())) == (len(set(s)) // 2)
    
def longestNiceSubstring(s):
    window_size = len(s)
    
    while window_size:
        for i in range(len(s) - window_size + 1):
            substring = s[i:i + window_size]
            print(substring,window_size,i)
            
            if get_nice(substring):
                return substring
            
        window_size -= 1
        
    return ''
s = "YazaAay"
print(longestNiceSubstring(s))