# Content of Project

* [Task 1: Software setup](#Task-1:-Software-setup)
* [Task 2: Selectors](Task-2:-Selectors)




## Task 1: Software setup
<details>
<summary>Click here to see general information about <b>Task</b>!</summary>
  
##   *"Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?"*

Zdecydowałam się wziąć udział w wyzwaniu bo chcę zmienić swoje życie-pracę, bo od dawna mnie to interesowało.
#### Napędza mnie możliwość rozwoju, ciekawość, dociekliwość, wytrwałość w dążeniu do celu. 
#### Uwielbiam wiedzieć "skąd"? i "dlaczego"?
Moim celem jest nauczyć się testowania, poznać tajniki tego zawodu by umieć z łatwością wspierać zespoły dweloperów a przy tym mieć frajdę z odnalezienia buga :smiley:.

##   **Zadanie dla chętnych. Nie samymi testami automatycznymi człowiek żyje.**

Udzielono odpowiedzi dobrze na 6 z 14
</details>

## Task 2: Selectors
<details>
<summary>Click here to see general information about <b>Task</b>!</summary>

##   **Subtask 2: Search for selectors on the login page. List all the elements that are on the login page.**
1. Login
  #### //*[@id="login"]
  #### //*[@id="__next"]/form/div/div[1]/div[1]/div
  #### #login
  #### $x('//*[@id="login"]')
2. Scouts Panel
  #### //*[@id="__next"]/form/div/div[1]/h5
  #### #__next > form > div > div.MuiCardContent-root > h5
  #### $x('//*[@id="__next"]/form/div/div[1]/h5')
  ####  //*[text()="Scouts Panel"]
3. English
  #### //*[@id="__next"]/form/div/div[2]/div/div
  #### #__next > form > div > div.MuiCardActions-root > div > div
  #### $x('//*[@id="__next"]/form/div/div[2]/div/div')
  ####  //*[text()="English"]
4. Sign in
  #### //*[@id="__next"]/form/div/div[2]/button/span[1]
  #### $x('//*[@id="__next"]/form/div/div[2]/div/div')
  #### 	//*[@class="MuiButton-label"]
5. Password
  #### //*[@id="password"]
  #### $x('//*[@id="password"]')
  #### //*[@id="password"]
6. Remind password
  #### //*[@id="__next"]/form/div/div[1]/a
  #### $x('//*[@id="__next"]/form/div/div[1]/a')
  #### //*[@class="MuiTypography-root MuiLink-root MuiLink-underlineHover jss4 MuiTypography-colorPrimary"] 
  ####  //*[contains(@class, "MuiTypography-root MuiLink-root")]  

  



