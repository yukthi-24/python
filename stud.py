from tabulate import tabulate

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


print("\n")
print("=" * 80)
print("STUDENT MARKS CARD".center(80))
print("=" * 80)

for name in M:

    print("\nStudent Name :", name)
    print()

    table = []

    for i in range(5):
        table.append([
            S[i],
            E[name][i],
            M[name][i][0],
            M[name][i][1],
            T[name][i],
            R[name][i],
            L[name][i],
            H[name][i]
        ])

    print(tabulate(
        table,
        headers=[
            "Subject",
            "Credit",
            "Internal",
            "External",
            "Total",
            "Remark",
            "Grade",
            "Honor Points"
        ],
        tablefmt="grid"
    ))

print()

print("Total Marks     :", sum(T[name]), "/ 500")
print("Percentage      : {:.2f}%".format(sum(T[name]) / 5))
print("Credits Earned  :", sum(E[name]), "/", sum(c))
print("SGPA            : {:.2f}".format(G[name]))

if "F" in R[name]:
    print("Overall Result  : FAIL")
else:
    print("Overall Result  : PASS")

print("=" * 80)

rank = sorted(G.items(), key=lambda x: x[1], reverse=True)

print("\n")
print("=" * 40)
print("COLLEGE RANK LIST".center(40))
print("=" * 40)

rank_table = []

for i, (name, sgpa) in enumerate(rank, start=1):
    rank_table.append([i, name, sgpa])

print(tabulate(
    rank_table,
    headers=["Rank", "Student Name", "SGPA"],
    tablefmt="grid"
))
