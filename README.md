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
In this repository.



-ve Case: 
 
 
The decoding is not working properly  if the result (Encode) image was saved as jpg.
If you save the img file in jpg format , it wont save the img pixel as you intended, it compresses you data into smaller size .(It is called “lossy compression”).
So save it in png format.

Result:
 We were successfully able to encode and decode the message through the image with the technique LSB Encoding.
References:
Geeks For Geeks 
Stack Overflow

