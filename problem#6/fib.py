
def fibonacci(n):
    #write your code here
    fibonacciSequence = [0,1]
    if(n > 0):
        for i in range(n - 1):
            fibonacciSequence.append(fibonacciSequence[i + 1] + fibonacciSequence[i])
        return fibonacciSequence[len(fibonacciSequence) - 1]
    elif(n == 0):
        return(0)
    else:
        return(-1)

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')