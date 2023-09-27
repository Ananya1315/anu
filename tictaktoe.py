width=int(input("enter the width of the tic tac toe board"))
def tictactoe(width):
    for i in range(2*width-1):
        if i%2==0:
            for j in range(width-1):
                print("  |  ",end=" ")
            print("\n")
        else:
            for k in range(width):
                print(" __ ", end=" ")
            print("\n")
                    
print("tic tac toe board ready!!")
tictactoe(width)
















