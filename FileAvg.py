if __name__ == '__main__' :

     # Read images
    filename1 = '2.58'
    filename2 = '2.60'

    file = open('avg_' + filename1 + '_' + filename2 + '.txt','w+')
    
    with open(filename1 + ".txt") as bf1:
        with open(filename2 + ".txt") as bf2:
            for line1, line2 in zip(bf1, bf2):
                x1, y1 = line1.split()
                x2, y2 = line2.split()

                xavg = (int(x1) + int(x2))/2
                yavg = (int(y1) + int(y2))/2

                print(int(xavg) , int(yavg))
                file.write("%d %d\n" % (int(xavg) , int(yavg)))

    file.close()