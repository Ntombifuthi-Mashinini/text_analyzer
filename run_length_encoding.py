def encode(s):
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(str(count) + s[i - 1])
            count = 1
          
    result.append(str(count) + s[-1])
    
    return "".join(result)


def decode(s):
    result = []
    num = ""
    
    for char in s:
        if char.isdigit():
            num += char
        else:
            result.append(char * int(num))
            num = ""
            
    return "".join(result)
