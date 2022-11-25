from telegraph import Telegraph


def get_telegraph_token() -> str:
    try:
        telegraph = Telegraph()
        account = telegraph.create_account(short_name='main')
        return account.get('access_token')
    except Exception as e:
        print(e)
