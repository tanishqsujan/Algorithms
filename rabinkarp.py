d= 10
def searchpattern(pattern, text, q):
    m= len(pattern)
    n= len(text)
    p= 0
    t= 0
    h= 1
    i= 0
    j= 0
    
    for i in range(m-1):
        h = (h*d) % q
        
    #calculate the hash value for pattern and text
    for i in range(m):
        p= (d*p + ord(pattern[i])) % q
        t= (d*t + ord(text[i])) % q
        
    #find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break
            
            j += 1
            if j== m:
                print("Pattern is found at position: " + str(i+1))
                
        if i < n-m:
            t= (d*(t- ord(text[i])*h) + ord(text[i+m])) % q
            
            if t < 0:
                t = t+q
                
text = "ABCCDDJHGT"
pattern= "DJH"
q= 13
searchpattern(pattern, text, q)
                