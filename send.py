import resend

resend.api_key = "re_arR3czPE_HmMB9QnVgWG5DRYh91unFhZ9"

params: resend.Emails.SendParams = {
    "from": "Yusif Aliyev <updates@blog.yusifaliyevpro.com>",
    "to": ["yusifaliyevpro@gmail.com"],
    "subject": "Test for Python",
    "html": "<p>Hello i am Yusif</p>"
}

email = resend.Emails.send(params)
print(email)