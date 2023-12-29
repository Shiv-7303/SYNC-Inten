import random
import smtplib
import os

def send_mail(email):
    otp = random.randint(1000, 9999)
    print(otp)
    my_email = "pythontut23@gmail.com"
    password = os.environ.get("PYTHON_EMAIL_PASSWORD")
    print(password)
    subject = 'OTP VERIFICATION CODE'
    body = f'Your OTP is: {otp}'
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as conn:
        conn.starttls()
        conn.login(my_email, password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=message
        )
        return str(otp)


def verify_otp():
    email = input("Enter the valid email: ")
    generated_otp = send_mail(email)
    entered_otp = input("Enter the OTP you received: ")
    if entered_otp == generated_otp:
        print("Verified Successfully")
    else:
        print("Wrong OTP. Try again later")


verify_otp()