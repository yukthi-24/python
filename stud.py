n = int(input("Enter number of students: "))

M={}
T = {}
R = {}
L = {}
H = {}
E = {}
G = {}

c=[4, 3, 3, 4, 2]
S = ['Maths', 'Physics', 'Chemistry', 'Biology', 'Python']

print("\nTo enter student marks")

for i in range(n):
    name = input("\nEnter students name: ")
    
    Imat = int(input("\nEnter Maths internal marks out of 60: "))
    Emat = int(input("Enter Maths external marks out of 40: "))
    
    Iphy = int(input("\nEnter Physics internal marks out of 60: "))
    Ephy = int(input("Enter Physics external marks out of 40: "))
    
    Ichm = int(input("\nEnter Chemistry internal marks out of 60: "))
    Echm = int(input("Enter Chemistry external marks out of 40: "))
    
    Ibio = int(input("\nEnter Biology internal marks out of 60: "))
    Ebio = int(input("Enter Biology external marks out of 40: "))
    
    Ipyt = int(input("\nEnter Python internal marks out of 60: "))
    Epyt = int(input("Enter Python external marks out of 40: "))
    
    M[name] = [[Imat, Emat], [Iphy, Ephy], [Ichm, Echm], [Ibio, Ebio], [Ipyt, Epyt]]
    
for name in M:
    mat = M[name][0][0] + M[name][0][1]
    phy = M[name][1][0] + M[name][1][1]
    chm = M[name][2][0] + M[name][2][1]
    bio = M[name][3][0] + M[name][3][1]
    pyt = M[name][4][0] + M[name][4][1]
    T[name] = [mat, phy, chm, bio, pyt]

for name in M:
    li = []
    for i in range(5):
        if M[name][i][0] < 30 or M[name][i][1] <20:
            li.append('F')
        else:
            li.append('P')
    R[name] = li

for name in R:
    li2 = []
    h = []
    C=[]
    for i in range(5):
        if R[name][i] == 'F':
            li2.append('F')
            h.append(0)
            C.append(0)
        else:
            C.append(c[i])
                     
            if T[name][i] >= 90 and T[name][i] <= 100:
                li2.append('O')
                h.append(10)
            elif T[name][i] >= 80 and T[name][i] < 90:
                li2.append('A+')
                h.append(9)
            elif T[name][i] >= 70 and T[name][i] < 80:
                li2.append('A')
                h.append(8)
            elif T[name][i] >= 60 and T[name][i] < 70:
                li2.append('B')
                h.append(7)
            elif T[name][i] >= 50 and T[name][i] < 60:
                li2.append('C')
                h.append(6)
            elif T[name][i] >= 0 and T[name][i] < 50:
                li2.append('F')
                h.append(0)
    L[name] = li2
    H[name] = h
    E[name] = C

for name in H:
    tp = 0
    tc = 0

    for i in range(5):
        tp += H[name][i] * E[name][i]
        tc += E[name][i]

    if tc == 0:
        G[name] = 0
    else:
        G[name] = round(tp / tc, 2)


## 🎓 Student Marks Card

**Student Name:** Rahul

| Subject | Internal | External | Total | Result | Grade | Grade Point | Credit |
|:---------|---------:|---------:|------:|:------:|:-----:|------------:|-------:|
| Maths | 55 | 35 | 90 | Pass | O | 10 | 4 |
| Physics | 48 | 26 | 74 | Pass | A | 8 | 3 |
| Chemistry | 40 | 22 | 62 | Pass | B | 7 | 3 |
| Biology | 56 | 37 | 93 | Pass | O | 10 | 4 |
| Python | 51 | 35 | 86 | Pass | A+ | 9 | 2 |

| Summary | Value |
|:--------|:------|
| Total Marks | **405 / 500** |
| Percentage | **81.00%** |
| SGPA | **8.94** |
| Overall Result | **PASS ✅** |

print("Total Credits: ", sum(c))

print("\nSGPA")
for name in G:
    print(name, ":", G[name])

rank = sorted(G.items(), key=lambda x: x[1], reverse=True)
