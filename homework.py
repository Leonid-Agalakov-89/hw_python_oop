class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type, duration, distance, speed, calories):
        self.training_type = training_type
        self.duration = duration
        self. distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return f'''Тип тренировки: {self.training_type}; Длительность: {self.duration:3f} ч.;
Дистанция: {self.distance:3f} км; Ср. скорость: {self.speed:3f} км/ч;
Потрачено ккал: {self.calories:3f}.'''


class Training:
    """Базовый класс тренировки."""

    STEP_M = 0.65  # Длина шага в метрах.
    M_IN_KM = 1000

    def __init__(self,
                 training_type,
                 action: int,
                 duration: float,
                 distance: float,
                 speed: float,
                 weight: float,
                 LEN_STEP: int,
                 M_IN_KM: int,
                 calories: int
                 ) -> None:
        self.training_type = training_type
        self.action = action
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.weight = weight
        self.LEN_STEP = action * Training.STEP_M
        self.M_IN_KM = M_IN_KM
        self.calories = calories

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.distance / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        Message = InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories)
        return Message


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER: float = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: int):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * Training.STEP_M
        self.M_IN_KM = M_IN_KM

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = self.distance / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = (Running.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed + Running.CALORIES_MEAN_SPEED_SHIFT) * self.weight / self.M_IN_KM * self.duration
        return calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        Message = InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories)
        return Message


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_WEIGHT_SHIFT = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: int,
                 height: float):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * Training.STEP_M
        self.M_IN_KM = M_IN_KM
        self.height = height

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.distance / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = ((SportsWalking.CALORIES_WEIGHT_MULTIPLIER * self.weight + (self.get_mean_speed**2 / self.height) * SportsWalking.CALORIES_WEIGHT_SHIFT * self.weight) * self.duration)
        return calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        Message = InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories)
        return Message


class Swimming(Training):
    """Тренировка: плавание."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 1.1
    CALORIES_WEIGHT_SHIFT = 2
    STROKE_M = 1.38  # Длина шага в метрах.

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: int,
                 length_pool: float,
                 count_pool: int):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * Swimming.STROKE_M
        self.M_IN_KM = M_IN_KM
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        calories = (self.get_mean_speed + Swimming.CALORIES_MEAN_SPEED_MULTIPLIER) * Swimming.CALORIES_WEIGHT_SHIFT * self.weight * self.duration
        return calories

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        Message = InfoMessage(self.__class__.__name__, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories)
        return Message


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workouts = {'SWM': Swimming,
                'RUN': Running,
                'WLK': SportsWalking}
    if workout_type == 'SWM':
        return Swimming
    elif workout_type == 'RUN':
        return Running
    else:
        return SportsWalking


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info
    rezult = InfoMessage.get_message(info)
    print(rezult)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

packages = [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180]),
]
