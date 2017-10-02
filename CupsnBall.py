def a(pos):
    pos[0],pos[1] = pos[1],pos[0]
def b(pos):
    pos[1],pos[2] = pos[2],pos[1]
def c(pos):
    pos[0],pos[2] = pos[2],pos[0]
def main():
    pos = ["ball","2","3"]
    input1=input("Input: ")
    input1 = list(input1)
    for i in input1:
        if i == 'a':
            a(pos)
        if i == 'b':
            b(pos)
        if i == 'c':
            c(pos)
    final_position = pos.index("ball")
    print (final_position+1)
    print(pos)
main()
