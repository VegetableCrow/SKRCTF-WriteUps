## XSS-GPT
![image](https://github.com/user-attachments/assets/8479e899-7598-44fc-b4e0-c80bac8e3c72)

# Description :
I built a chatgpt website using chatgpt. Feel free to try it! Remember to report to me if you found any bug

# Solution :

![image](https://github.com/user-attachments/assets/cd35f7db-48be-43b8-853f-879741ba8250) <br>
The challenge will bring us to a link that looks like chatgpt. I'm not allow to progress further as it says I do not have the API key but we can see that we have a lead that we can 
try to tamper with the API key value with other things

![image](https://github.com/user-attachments/assets/cc0c29db-0c5c-4645-bf5b-f5ed15d8480d) <br>
Since the challenge says XSS GPT, I try it rit away and a little changes is that the XSS payload needs to starts with the closing of </script> else it will not work because the API key part is wrap inside the JS script

![image](https://github.com/user-attachments/assets/08b40eda-e0a7-4b3d-9e32-d0166ff15083)


![image](https://github.com/user-attachments/assets/ce4526ba-a301-4ddc-900a-4b3a7e797624)


![image](https://github.com/user-attachments/assets/ca3034f4-b787-4524-9719-41c0d465c2fc)


![image](https://github.com/user-attachments/assets/66d95877-39ac-4c11-9f66-31f81b186f6d)


![image](https://github.com/user-attachments/assets/36963aa9-c499-49ef-b70f-9a50613182ea)


![image](https://github.com/user-attachments/assets/a1e70c8a-812d-482c-8ecf-d31576d5c866)


![image](https://github.com/user-attachments/assets/ef6afacc-a7d0-4610-945d-70113e584f18)
**FLAG**
```
SKR{R3flec73D_1n_API_k3y_e9bc37}
```
