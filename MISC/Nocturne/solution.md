## Nocturne
![image](https://github.com/user-attachments/assets/8f99db1f-902c-470b-9896-1026ccf8c033)

# Description :
My friend send me this file, but it does not sound like nocturne at all..
I think there is something fishy, can you find it out?

# Attachment :
https://skrctf.me/challenges#Nocturne

# Solution :
![image](https://github.com/user-attachments/assets/917f976f-b1df-446c-abbe-3119fcc4848c)
The challenge only gave us a .mid file AKA MIDI file, easy understanding is known as audio file. Open it up and listen it, it resembles morse code but when open up with audacity and decode it with red unit pitch as dot and white space as underscore. It gives me nothing in when decrypt with morse code since there is no separator between each of the unit.

# Hint :
Notice the song is in 8 beats?

With the hint is very obvious that we will be looking at 8 bits which is something like 01110011, so with this 8 bits we will look for it and convert it into decimal value that ranges between the ASCII readable value.

# Reading the 8 bits :
![image](https://github.com/user-attachments/assets/929e1f69-ffe6-483d-b6c7-210d82c2c3b4)
![image](https://github.com/user-attachments/assets/b2edf650-0c4d-4881-b0a8-e487feb063d8)

This part I guess is where most people find it lost even though you are on the right track or maybe Im just dumb. The mistake here is firstly we did not understand the MSB (leftmost value of an 8 bits value) of an ASCII value which will be 0. An 8 bit with MSB of 1 will result of the value is out of the ASCII readbale range which is more than 128. 

Second is if we read it from the right to left, we need to add in a value 0 in the very front of the red bar in the nocturne.mid file right after we convert the red bar into 1 and spaces into 0. But even though manage to count it, reading from the right to left might cause some miscalcaulate of bits. So the safe way is to count from the left to right in this case, which you will be counting from the last character to the first character to avoid lefting out any bits.

Anyways lets get the flag now.
![image](https://github.com/user-attachments/assets/86852224-5118-4ff1-8524-8748ab776d8f)


