#Captcha

import random
import time

time.sleep(1)
if __name__ == '__main__':
    verification_code = ""
    for i in range (4):
        index = random.randrange(0, 4)
        if index != i and index + 1 != i:
            verification_code += chr(random.randint(97, 122))
        elif index + 1 ==i:
            verification_code += chr(random.randint(65, 90))
        else:
            verification_code += str(random.randint(1, 9))
    print("验证码:(Captcha:)",verification_code)
    time.sleep(3)
    yzm = input("请输入验证码:(Please enter the verification code:)")
    if yzm == verification_code:
        print("验证码正确!(verification code is correct!) \n")
        time.sleep(3)
        pass
    else:
        print("验证码错误!(verification code error!) \n")
        time.sleep(3)
        print("")
        pass

        
        
                


           
            
            

    
