# ===============================
# PR-4 Functional Treatment Project
# ===============================

data = []
matrix = []

GLOBAL_TOTAL = 0
GLOBAL_AVG = 0

# ------------------
# Input Data
# ------------------------------
def input_data(*args, **kwargs):
    """Input 1D and 2D List"""

    global data, matrix

    print("\n1. Sample Data")
    print("2. Manual Data")
    ch = int(input("Enter Choice: "))

    if ch == 1:
        data = [34, 12, 56, 78, 43, 21, 90]
        matrix = [[10,20,30],[40,50,60],[70,80,90]]
    else:
        data = list(map(int, input("Enter 1D List: ").split()))

        r = int(input("Rows: "))
        c = int(input("Columns: "))

        matrix = []

        for i in range(r):
            row = list(map(int, input("Enter Row: ").split()))
            matrix.append(row)

    print("\nData Stored Successfully!")

    print("\nUsing *args")
    for i in args:
        print(i)

    print("\nUsing **kwargs")
    for k,v in kwargs.items():
        print(k,"=",v)

    print("\nDoc String:")
    print(input_data.__doc__)


# ------------------------------
# Built-in Functions
# ------------------------------
def calculate_built_in_summary():
    """Display Data Summary"""

    global GLOBAL_TOTAL, GLOBAL_AVG

    GLOBAL_TOTAL = len(data)
    GLOBAL_AVG = sum(data)/len(data)

    print("\nLength :",len(data))
    print("Minimum :",min(data))
    print("Maximum :",max(data))
    print("Sum :",sum(data))
    print("Average :",GLOBAL_AVG)


# ------------------------------
# Recursion
# ------------------------------
def calculate_factorial(n):
    """Factorial Using Recursion"""

    if n==0 or n==1:
        return 11

    return n*calculate_factorial(n-1)


# ------------------------------
# Return Multiple Values
# ------------------------------
def get_dataset_statistics():
    """Return Statistics"""

    mn=min(data)
    mx=max(data)
    sm=sum(data)
    avg=sm/len(data)

    return mn,mx,sm,avg


# ===============================
# Main Program
# ===============================

while True:

    print("\n========== MENU ==========")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data (Lambda)")
    print("5. Sort Data")
    print("6. Dataset Statistics")
    print("7. Exit")

    ch=int(input("Enter Choice : "))

    if ch==1:
        input_data("Hello","Python",Name="Vaidehi",Project="PR4")

    elif ch==2:
        calculate_built_in_summary()

    elif ch==3:
        n=int(input("Enter Number : "))
        print("Factorial =",calculate_factorial(n))

    elif ch==4:

        t=int(input("Enter Threshold : "))

        ans=list(filter(lambda x:x>=t,data))

        print("Filtered Data :",ans)

    elif ch==5:

        print("\n1. Ascending")
        print("2. Descending")

        s=int(input("Enter Choice : "))

        if s==1:
            data.sort()
            print("Sorted 1D :",data)

        else:
            data.sort(reverse=True)
            print("Sorted 1D :",data)

        print("\nSorted 2D")

        new_matrix=sorted(matrix)

        for i in new_matrix:
            print(i)

    elif ch==6:

        a,b,c,d=get_dataset_statistics()

        print("\nMinimum :",a)
        print("Maximum :",b)
        print("Sum :",c)
        print("Average :",d)

        print("\n2D List")

        for i in matrix:
            for j in i:
                print(j,end=" ")
            print()

    elif ch==7:
        print("Thank You...")
        break

    else:
        print("Invalid Choice")