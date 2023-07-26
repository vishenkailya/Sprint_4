import random
import faker


class OrderForm:

    def fill_form_name():
        fake = faker.Faker('ru_RU')
        name = fake.first_name()
        return name

    def fill_form_surname():
        fake = faker.Faker('ru_RU')
        surname = fake.last_name()
        return surname

    def fill_form_street():
        fake = faker.Faker('ru_RU')
        address = fake.street_name()
        return address

    def fill_form_phone():
        return random.randint(89000000000, 89999999999)
