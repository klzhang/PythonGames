def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]


def main():
    x = 1
    y = 0
    z = 0
    smallest = 10000
    for b in range(2,25,1):
        for c in range(2,50,1):
            clist = [1,b,c]
            total = 0
            for i in range(100):
                amnt = i
                coinsUsed = [0]*(amnt+1)
                coinCount = [0]*(amnt+1)
        
                total = total + dpMakeChange(clist,amnt,coinCount,coinsUsed)

            avg = total / 100
            if(avg < smallest):
                smallest = avg
                y = b
                z = c         
   
    print(smallest)
    print(x)
    print(y)
    print(z)


main()
