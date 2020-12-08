from PIL import Image 
import numpy as np 

def Main():
    while True:
        print("Please choose one of the following-->")
        print("1.Encode")
        print("2.Decode")
        print("3.Quit")
        choice = int(input())
        if choice==1:
            Encode()
        elif choice==2:
            result = Decode()
            print(result)
        elif choice==3:
            break
        else:
            print("Invalid Input!!!")
            print("Logging Off!!!")
            break
        print(" ")
def Decode():
    file_location = input("Image location: ")
    # open method used to open different extension image file 
    im = Image.open(file_location)  
    px = im.load()
    m_store=[]
    motor=0
    binary_store=""
    flag=0
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixel = px[i,j]
            img_pixel_binary_value='{0:08b}'.format(pixel[0])
            binary_store+=img_pixel_binary_value[-1]
            motor+=1
            if motor==7:
                temp=int(binary_store, 2)
                m_store.append(chr(temp))
                motor=0
                binary_store=""
                #Checking if END has come
                if len(m_store)>=3:
                    if m_store[-3]=="E" and m_store[-2]=="N" and m_store[-1]=="D":
                        flag=1
                        break
        if flag==1:
            break
    result = ""
    for i in range(len(m_store)-3):
        result+=m_store[i]
    return result


def Encode():
    data = input("Enter the data:")
    file_location = input("Image location: ")
    file_destination = input("Name of the Image you want to save: ")
    data+="END"
    data_length = len(data)
    
    
    # open method used to open different extension image file 
    im = Image.open(file_location)  
    px = im.load()
   
    height = im.size[0]
    width = im.size[1]

    

    #i and j counts for the index reached for the image
    i=0
    j=0
    count=0


    #While all the characters are not encoded
    while count<data_length:
            temp = str(data[count])        

            # using join() + ord() + format() 
            # Converting char to binary 
            data_binary_value= ''.join(format(ord(i), 'b') for i in temp) 
            #Counting for the binary (7)
            temp_count=0
            while temp_count<len(data_binary_value):
                if j==width:
                    j=0
                    i+=1
                else:
                    #Getting binary value of the pixel (In 8 values)
                    img_pixel = px[i,j]
                    pixel_1 = img_pixel[0]
                    img_pixel_binary_value='{0:08b}'.format(pixel_1)
                    #Modifying the least significant bit, and saving it back
                    #As string are immutable , we need to copy the data
                    temp_img_pixel_binary_value = img_pixel_binary_value[0:7]
                    temp_last_pixel=int(data_binary_value[temp_count])
                    temp_img_pixel_binary_value+=str(temp_last_pixel)
                    modified_pixel=int(temp_img_pixel_binary_value, 2)
                    result_pixel = (modified_pixel,)+img_pixel[1:]
                    px[i,j]=result_pixel
                    j+=1
                    temp_count+=1
            count+=1
    im.save(file_destination)
    
   
    


    
Main()
