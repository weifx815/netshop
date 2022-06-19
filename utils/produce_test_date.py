from faker import Faker


class GetSysAdminInfo(object):
    fake = Faker("zh-CN")
    user_name = fake.name()
    user_account = fake.email()
    password = fake.password(special_chars=False)
    phone_number = fake.phone_number()
    recent_date = fake.date_this_month()

