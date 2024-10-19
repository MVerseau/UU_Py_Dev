from time import sleep


class User:
    ''' nickname(имя пользователя, строка)
    password(в хэшированном виде, число)
    age(возраст, число)'''

    # def __new__(cls, name: str, password: int, age: int):
    #     if type(password) == int:
    #         instance = object.__new__(cls)
    #         return instance
    #     else:
    #         raise TypeError(f'"{password}": формат данных не поддерживается')

    def __init__(self, name: str, password: int, age: int):
        self.nickname = str(name)
        # self.password = self.passw(int(password))
        self.password = hash(password)
        self.age = age

    def check(self, data):
        raise ValueError(
            f'"{data}": формат данных не поддерживается')

    def __str__(self):
        return self.nickname

    # def nickname(self, name):
    #     if type(name) != str:
    #         self.check(name)
    #     else:
    #         self._nickname = name

    # def age(self, age):
    #     if type(age) != int:
    #         self.check()
    #     else:
    #         self._age = age
    #
    # def passw(self, password):
    #     if type(password) == int:
    #         self.password = hash(password)
    #         return self.password
    #     else:
    #         self.check(password)


class Video:
    '''
    title(заголовок, строка)
    duration(продолжительность, секунды)
    time_now(секунда остановки (изначально 0))
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    '''

    def __init__(self, title: str, duration, time_now=0, adult_mode=False):
        self._title = str(title)
        self._duration = duration  # Возможные типы данных?
        self._time_now = time_now  # Возможные типы данных?
        self.adult_mode = adult_mode  # Реализовано без проверки


class UrTube:
    '''
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    Метод log_in, который принимает на вход аргументы: login, password и пытается найти пользователя в users с такмими же логином и паролем. Если такой пользователь суещствует, то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.
    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
    Метод log_out для сброса текущего пользователя на None.
    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится, если же находит ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
    '''

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.users = []  # список ОБЪЕКТОВ класса User
        self.videos = []  # список ОБЪЕКТОВ класса Video
        self.current_user = None


    def log_in(self, login, password):
        for i in self.users:
            if login == i.nickname and hash(password) == i.password:
                self.current_user = i
            # else:
            #     self.error()

    def log_out(self):
        self.current_user = None

    @staticmethod
    def error():
        print('Неверный логин или пароль')

    @staticmethod
    def user_exists(nickname):
        print(f'Пользователь {nickname} уже существует.')

    def register(self, nickname, password, age):
        if nickname in set(i.nickname for i in self.users):
            self.user_exists(nickname)
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def add(self, *args):
        if set([i._title for i in args]) <= set([i._title for i in self.videos]) and len(
                set([i._title for i in self.videos])) != 0:
            pass
        else:
            self.videos.extend(args)

    def get_videos(self, search):
        return [i._title for i in self.videos if str(search).lower() in i._title.lower()]

    def watch_video(self, requested_video_title):
        # found_video=self.get_videos(requested_video_title)
        found_video = [i for i in self.videos if str(requested_video_title) in i._title]
        if len(found_video) != 0:
            if self.current_user is None:
                # print(f"Найдено:{[i._title for i  in found_video]}.")
                print('Войдите в аккаунт, чтобы смотреть видео.')
            else:
                if found_video[-1].adult_mode is not False and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу.')
                else:
                    counter = 0
                    for i in range(found_video[-1]._duration):
                        counter += 1
                        print(counter, end=' ')
                        sleep(1)
                    print('Конец видео')


def watch_video(arg):
    ur.watch_video(arg)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')
