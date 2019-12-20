# print ('Nama : Sely Fitriatun Wakhidah')
# print( 'Kelas : DS JKT 07')
# print ('Materi : Ujian Modul 1 / 20 Des 2019')

##NOMOR 1
# def Hastag(string):
#     if (len(string))==0 or (len(string))> 140:
#         return print(False)
#     else:
#         a1 =string.split(' ')
#         a2=[]
#         for i in a1:
#             a2.append(i)
#         z=''
#         for j in a2:
#             z+=j.capitalize()
#         print('#{}'.format(z))
# Hastag(" Hello there how are you doing")
# Hastag("")
# Hastag("  Hello  World")
# print('\n')

##NOMOR 2
# def create_phone_number(number):
#     # a = [1,2,3,4,5,6,7,8,9,0]
#     y = ('{}{}{}{}{}{}{}{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]))
#     # print(y)
#     print(' "({}) {}-{}"'.format(y[:3],y[3:6],y[6:]))
# create_phone_number([1,2,3,4,5,6,7,8,9,0])
# print('\n')


##NOMOR 3
def sort_odd_even(num):
    genap =[]
    ganjil =[]
    result=[]
    for i in num:
        if i%2==0:
            genap.append(i)
        else:
            ganjil.append(i)
    genap.sort(reverse=True)
    ganjil.sort()
    print('[{},{},{},{},{},{}]'.format(ganjil[0],ganjil[1],genap[0],genap[1],ganjil[2],genap[2]))
sort_odd_even([5,3,2,8,1,4])

##NOMOR 4
# def hollowTriangle(n):
#     if n==1:
#         print ('    #    ')
#     else:
#         z=''
#         for i in range (0,n,1):
#             for j in range (0, 2*n+1):
#                 if j >= n-i and j <= n+i:
#                     z += ' # '
#                 else: 
#                     z += '---'    
#             z += '\n'
#         print (z)       
#hollowTriangle(2) 