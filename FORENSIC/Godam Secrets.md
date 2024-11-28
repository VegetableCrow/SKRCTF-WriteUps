Name               : Path_Finder <br>
Challenge category : Forensics <br>
Challenge name     : Godam Secrets <br><br>

Challenge required us to download a zip file AKA godam's hard drive, after download it, extract the zip file.
<br>
<br>

![image](https://github.com/user-attachments/assets/fa1899a5-9829-4ca4-ac3c-9d62e25ea9fb) <br>
When going thru the folder after extracted, first info is that you can know that we are mostly looking for a file named places.sqlite that stores browser history.
This can be confirm when the file path is identical of how Firefox browser store their user browsing history and with the keyword of the folder mozilla.
<br>
<br>

![image](https://github.com/user-attachments/assets/7256c453-12ee-4d34-973a-2026c391f949)
The places.sqlite is found, now we can see that inside the search history,after looking thru the links, most of the link looks normal except for this one (https://h4ck3r5club666.appspot.com/). 
<br>
<br>

![image](https://github.com/user-attachments/assets/979be962-e24a-4763-91d9-2442bb37d44d) <br>
Sus indeed, and it ask for a secret key. Likewise poking around the cookies and source code but found nothing so going back to godam's hard drive.
<br>
<br>

![image](https://github.com/user-attachments/assets/79b68244-7f20-4b29-bb8c-6041483deefe) <br>
Here is where things get confusing, picture says red herring which means something intended to distract attention from the real problem.
I fell right into the trap for steghide hint.jpg and going through key4.db file to extract the user id and password and decrypt it but nothing works.
<br>
<br>

![image](https://github.com/user-attachments/assets/a17866df-9335-42e2-8840-ba6f48b564e9) <br>
When poking around again at the sqlite files to find clues, this file (formhistory.sqlite) gives me the previus challenge flag. However it is put under the field name "key".
<br>
<br>

![image](https://github.com/user-attachments/assets/94f74e5f-edaa-40e9-b4c1-1113656ac6b7) <br>
Secret key is SKR{hidden_text_in_color_hex_code} confirmed.
<br>
<br>

![image](https://github.com/user-attachments/assets/a192c679-ad36-46c2-b729-23250d27161b) <br>
Inside the home page of this sus website, the content looks weird and is in reverse. After reversing it there is some weird capital letters and the flag format.
<br>
<br>

![image](https://github.com/user-attachments/assets/068fd731-43f7-4d69-a3e5-62bdabb0487f)<br>
![image](https://github.com/user-attachments/assets/7fd95df5-ad24-48e6-8041-71b1267eda00)<br>
Go to cyber chef reverse it and extract the capital letters and piece the words together to form the flag.

**FLAG**
SKR{SECRET_CLUB_IS_NOT_LONGER_SECRET}



