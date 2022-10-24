from selenium import webdriver

#abre o navegador
navegador = webdriver.Chrome(executable_path="C:\\Users\\renan\\AppData\\Local\\Programs\\Python\\Python38\\chromedriver.exe")
#coloca o endereço do site desejado
navegador.get("https://platform.senior.com.br/login/?redirectTo=https%3A%2F%2Fplatform.senior.com.br%2Fsenior-x%2F&tenant=supermercadosguanabara.com.br")

#procura o campo de loguin e preenche
navegador.find_element("xpath",'//*[@id="username-input-field"]').send_keys("106710")#novo codigo
#procura o campo de senha e preenche
navegador.find_element("xpath",'//*[@id="password-input-field"]').send_keys("975865")#novo codigo
#procura o campo de loguin e preenche
navegador.find_element("xpath",'//*[@id="loginbtn"]').click()
