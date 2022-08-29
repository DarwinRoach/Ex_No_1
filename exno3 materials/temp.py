max = 99999999
nodes = int(input("Enter the number of nodes: "))
graph=[]
INF = float("inf")
for i in range(nodes):
    jk1 = []
    for j in range(nodes):
        print("Enter the distance between the path: ",str(i)+" to ",str(j))
        a=input()
        jk1.append(a)
        graph.append(jk1)
print(graph)

def floyd(graph):
    distance = list(map(lambda p: list(map((lambda q: q, p)), graph)))

    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
        sol(distance)
def sol(distance):
    for j in range(nodes):
        for k in range(nodes):
            if(distance[j][k] == "INF"):
                print("infinity")
            else:
                print(distance[j][k], end=" ")
        print(" ")
floyd(graph)
        
