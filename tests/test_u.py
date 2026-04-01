from colorama import init, Fore, Back, Style

init()

def test_eqiual():
    assert 1 == 1, "Jijo"
    print('hello')
    print(Fore.RED + 'Этот текст красный')
    print(Back.GREEN + 'А у этого текста зеленый фон')
    print(Style.RESET_ALL + 'Стиль сброшен')