emails_list = ['freirefellipe@gmail.com', 'lipefreioliv@gmail.com', 'freirefellipe@outlook.com', 'lipeoliv@mail.com']

## 1st way to go:

emails_gmail_1 = []

for email in emails_list:
    if '@gmail' in email:
        emails_gmail_1.append(email)

## 2nd, BEST, way to go, by not creating variable for the lambda function:

emails_gmail_2 = list(filter(lambda email: '@gmail' in email, emails_list)) # impressindível colocar em list(), senão vai retornar somente uma mensagem de espaço alocado na memória.


'-------------------------------'

print(emails_gmail_2)
