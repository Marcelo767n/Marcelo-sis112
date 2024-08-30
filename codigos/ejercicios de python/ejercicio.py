n=int(input("ingrese un numero "))

for i in range(n):
    if i%2!=0:
        print(i)
sumatotal=0
sumatoria=(n*(n+1)//2)
print(sumatoria)
sumatotal=0
for j in range(n+1):
    sumatotal+=j
print(sumatotal)