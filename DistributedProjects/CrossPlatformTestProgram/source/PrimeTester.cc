// This program is meant for use with the grid computing archetecture provided by
// The Computing Collective

#include<iostream>
#include<math.h>
#include<stdlib.h>

using namespace std;

bool isPrime(long inputNumber)
{
    if (inputNumber == 1)
    {
        return 1;
    }
    for(long i = 2; i <= sqrt(inputNumber);i++)
    {
        if (!(inputNumber % i))
        {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char* argv[])
{
    long startrange = atoi(argv[1]);
    long endrange = atoi(argv[2]);
    //This program will expect two values representing the range in which to test 
    //for primeness. The starting value is included, and the ending value is not.
    
    for (long i = startrange; i < endrange; i++)
    {
        if (isPrime(i))
        {
            cout<<i<<"\n";
        }
    }
    return 1;
}
