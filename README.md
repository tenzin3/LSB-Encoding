# LSB-Encoding
Steganography technique

Title:  LSB Encoding

Experiment: To encode a secret message into an image using LSB Encoding.
Theory:
Steganography:
Steganography is the method of hiding secret data inside any form of digital media. The main idea behind steganography is to hide the existence of data in any medium like audio, video, image, etc. When we talk about image steganography, the idea is quite simple. Images are made up of pixels which usually refer to the color of that particular pixel. 
In a greyscale (black and white) image, these pixel values range from 0-255, 0 being black and 255 being white.
In RGB(Red, Green and Blue) image, there are three pixel values ranging from 0-255 for corresponding concentration of these three Colours.

Steganography is used to send secret data, as its is much more less obvious for hackers than to sent a cipher text through internet. But for better protection,  encryption is done before encoding the message into the image. There are many different techniques to perform this data hiding under image. But this paper will explain only LSB Encoding.
LSB Encoding:
LSB stands for Least Significant Bit. The idea behind LSB embedding is that if we change the last bit value of a pixel, there won’t be much visible change in the color. For example, 0 is black. Changing the value to 1 won’t make much of a difference since it is still black, just a lighter shade.






Algorithm:
The program mainly does two things. 
1.	Encode(Hide) the secret message into the image
2.	Decode(Extract) the message from the image
       Encoding LSB:
1.	START
2.	insert message ,img_file and result_img_name
3.	append “END” as delimiter 
4.	for each char m in message
5.	        convert m into binary b_m
6.	        for each b in b_m
7.	             get the last modified pixel of img
8.	             modify the pixel with b
9.	             increment the pixel and b
10.	save the img
11.	END 
Decoding:
1.	START
2.	insert the img_file 
3.	while img_size
4.	      get the pixel of img
5.	      convert into binary and store it in a list
6.	      if list size becomes 7
7.	                convert 7 binary into char and store it in list m_store
8.	                if last 3 element of m_store is “END”
9.	                      return the string
10.	                
11.	END
imp: All the characters can be represented in 7 binary values, thats y 7 in step 6.




Program:
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



-ve Case: 
 
 
The decoding is not working properly  if the result (Encode) image was saved as jpg.
If you save the img file in jpg format , it wont save the img pixel as you intended, it compresses you data into smaller size .(It is called “lossy compression”).
So save it in png format.

Result:
 We were successfully able to encode and decode the message through the image with the technique LSB Encoding.
References:
Geeks For Geeks 
Stack Overflow

