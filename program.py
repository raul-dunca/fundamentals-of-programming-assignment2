#
# Write the implementation for A2 in this file
#

# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values
# print('Hello A2'!) -> prints aren't allowed here!
def create_complex(real,imaginary):
    return [real,imaginary]
def add_complex(complex_list,c):
    complex_list.append(c)
def get_real(Z):
    return Z[0]
def get_imaginary(Z):
    return Z[1]
def init_complex():
    return [create_complex(2, 2), create_complex(1, 2), create_complex(2, 1), create_complex(1, 3), create_complex(2, 0), create_complex(2, 1), create_complex(1, 2),create_complex(2,2),create_complex(21,3),create_complex(-1,-2)]
   # return[create_complex(1,2),create_complex(3,-4),create_complex(5,0),create_complex(-2,7),create_complex(-3,-2),create_complex(0,9),create_complex(12,-6),create_complex(2,2),create_complex(21,3),create_complex(-1,-2)]
def f_real_part(complex_list):
    """

    :param complex_list: the list of complex numbers
    :return:the first and the last position of the sequence with numbers with a strictly increasing real part
    """
    k=int(1)
    maxi=int(0)
    p=int(0)
    for i in range (0,len(complex_list)-1):
        if(int(get_real(complex_list[i]))<int(get_real(complex_list[i+1]))):  #we compare the real part of 2 consecutive numbers
            if(k==1):                                                         #if k=1 thath means we can have a potentialy sequence so we save the first pos of it in p
                p=i
            k=k+1
        else:                                                                 #if we found a number with a lower real part that means our seqence is finished and we verifie if
            if maxi<k:                                                        # it has the most elements so far, if that is the case we save the first positoin of in in prim
                maxi=k                                                        # and the last position in last
                prim=p
                last=prim+k
            k=1
    if maxi < k:                                                              #after we go through all of the list we may not find a case which leads us
        prim = p
        last = prim + k                                                       #to the else aboce(ex: if we have only increasing real part numbers)
    return [prim,last]
def f_pair_sum(complex_list):
    """

    :param complex_list: the list of complex numbers
    :return:the first and the last position of the sequence with consecutive number pairs have equal sum.1
    """
    sum=[]
    k_p=int(1)
    k_i=int(1)
    maxi_p=int(0)
    maxi_i=int(0)
    p_p=int(0)
    p_i=int(1)
    for i in range(0,len(complex_list)-1):            # we make the sum of 2 by 2 complex numbers and put the sum in a list (sum)
        sum.append([get_real(complex_list[i])+get_real(complex_list[i+1]),get_imaginary(complex_list[i])+get_imaginary(complex_list[i+1])])
    #print(sum)
    for i in range(0,len(sum)-2):                     #we go on the sum list and we compare the sums 2 by 2 on the parity(ex: position 0 with position 2 then position 2 with position 4, etc)
        if i%2==0:                                    #we check if i is even or odd bcs our sequence can start from an even or odd postion
            if(get_real(sum[i])==get_real(sum[i+2]) and get_imaginary(sum[i])==get_imaginary(sum[i+2])):# here is the comparation
                if k_p==1:                            #if k is 1 that means and the we start a potentialy bigger sequence so we keep the first position of it in p
                    p_p=i
                k_p=k_p+1                             #we count the number of pairs in the sequence
            else:
                if maxi_p < k_p:                      #if maxi <k then that means we have a new higher sequence so we save the first and the last position of it
                    maxi_p = k_p
                    prim_p = p_p
                    last_p = prim_p + 2*k_p           #we multiply k by 2 bcs k is the number of pairs in the sequence
                k_p=1
        else:                                         #here is the same but for odd positions
            if (get_real(sum[i]) == get_real(sum[i+2]) and get_imaginary(sum[i]) == get_imaginary(sum[i+2])):
                if k_i == 1:
                    p_i = i
                k_i = k_i + 1
            else:
                if maxi_i < k_i:
                    maxi_i = k_i
                    prim_i = p_i
                    last_i = prim_i + 2 * k_i
                k_i = 1
    if maxi_p < k_p:                                #these ifs just verifies in case the sequence did not end until the last element
        maxi_p=k_p
        prim_p = p_p
        last_p = prim_p + 2*k_p
    if maxi_i < k_i:                                #same but for odd ones
        maxi_i=k_i
        prim_i = p_i
        last_i = prim_i + 2*k_i
    if(maxi_p>=maxi_i):                            #we see who the higher numbers of pairs in their sequence the odd positions or the even ones
        return[prim_p,last_p]
    else:
        return[prim_i,last_i]

# UI section
# (write all functions that have input or print statements here).
# Ideally, this section should not contain any calculations relevant to program functionalities
def sequence_display(complex_list,l):
    """

    :param complex_list: the list of complex numbers
    :param l: in l[0] we have the position of the first number in the sequence and in l[1] we have the the position of t
    he last number in the sequence this function just print out the sequence from l[0] to l[1]-1
    """
    index = 1
    for i in range(l[0],l[1]):
        if (int(get_real(complex_list[i])) == 0 and int(get_imaginary(complex_list[i])) == 0):
            print(str(index) + ") 0")
        elif (int(get_real(complex_list[i])) == 0 and int(get_imaginary(complex_list[i])) != 0):
            print(str(index) + ") " + str(get_imaginary(complex_list[i])) + "i")
        elif (int(get_real(complex_list[i])) != 0 and int(get_imaginary(complex_list[i])) == 0):
            print(str(index) + ") " + str(get_real(complex_list[i])))
        elif int(get_imaginary(complex_list[i])) < 0:
            print(str(index) + ") " + str(get_real(complex_list[i])) + str(get_imaginary(complex_list[i])) + "i")
        elif int(get_imaginary(complex_list[i])) > 0:
            print(str(index) + ") " + str(get_real(complex_list[i])) + "+" + str(get_imaginary(complex_list[i])) + "i")
        index += 1
def show_complex(complex_list):
    index = 1
    for Z in complex_list:
        if(int(get_real(Z))==0 and int(get_imaginary(Z))==0):
            print(str(index) + ") 0" )
        elif (int(get_real(Z))==0 and int(get_imaginary(Z))!=0):
            print(str(index) + ") " + str(get_imaginary(Z))+"i" )
        elif(int(get_real(Z))!=0 and int(get_imaginary(Z))==0):
            print(str(index) + ") " + str(get_real(Z)))
        elif int(get_imaginary(Z))<0:
            print(str(index) + ") " + str(get_real(Z)) + str(get_imaginary(Z))+"i")
        elif int(get_imaginary(Z))>0:
            print(str(index) + ") " + str(get_real(Z)) +"+" + str(get_imaginary(Z)) + "i")
        index += 1
def create_complex_nr_ui(complex_list):
    try:
        real_part=int(input("Enter real part: "))
        imaginary_part=int(input("Enter imaginary part: "))
        c = create_complex(real_part, imaginary_part)
        add_complex(complex_list, c)
    except ValueError as ve:
        print(ve)
def print_menu():
    print("\t1. Read a list of complex numbers (in z = a + bi form) from the console.")
    print("\t2. Display the entire list of numbers on the console.")
    print("\t3. Display the sequence (consists of) numbers with a strictly increasing real part.")
    print("\t4. Display the sequence (consists of)) consecutive number pairs have equal sum.")
    print("\t5. Exit the application.")


def start():
    # Don't use global vars
    complex_list=init_complex()

    while True:
        print_menu()
        option=input("Option: ")
        if option=="5":
            return
        elif option=="1":
            create_complex_nr_ui(complex_list)
        elif option=="2":
            show_complex(complex_list)
        elif option=="3":
            sequence_display(complex_list,f_real_part(complex_list))
        elif option=="4":
           sequence_display(complex_list,f_pair_sum(complex_list))
        else:
            print("Invalid input :( ")



start()

