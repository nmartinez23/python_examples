def square(num):
    return num * num

def main():
    for i in range(10):
        print(f"{i} squared is {square(i)}")
        ## print("{} squared is {}".format(i, square(i)))    ## old school way

if __name__ == "__main__":
    main()
