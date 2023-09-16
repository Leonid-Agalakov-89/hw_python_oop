class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type, duration, distance, speed, calories):
        self.trainin_type = training_type
        self.duration = duration
        self. distance = distance
        self.speed = speed
        self.calories = calories

    def show_training_info():
        pass

    def get_message():
        return f'Тип тренировки: {training_type}; Длительность: {duration:3f} ч.; Дистанция: {distance:3f} км; Ср. скорость: {speed:3f} км/ч; Потрачено ккал: {calories:3f}.'


class Training:
    """Базовый класс тренировки."""

    STEP_M = 0.65  # Длина шага в метрах.
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * STEP_M
        self.M_IN_KM = M_IN_KM

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return distance / duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return self


class Running(Training):
    """Тренировка: бег."""
    
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: float):
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * STEP_M
        self.M_IN_KM = M_IN_KM

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return distance / duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        (CALORIES_MEAN_SPEED_MULTIPLIER * mean_speed + CALORIES_MEAN_SPEED_SHIFT) * weight / M_IN_KM * duration 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return self


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_WEIGHT_SHIFT = 0.029
    
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 M_IN_KM: float,
                 height: float):
        self.action = action
        self.duration = duration
        self.weight = weight
        sself.LEN_STEP = action * STEP_M
        self.M_IN_KM = M_IN_KM
        self.height = height

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return distance / duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        ((CALORIES_WEIGHT_MULTIPLIER * вес + (mean_speed**2 / height) * CALORIES_WEIGHT_SHIFT * weight) * duration) 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return self

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
                 M_IN_KM: float,
                 length_pool: float,
                 count_pool:int
                 ):
        
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = action * STROKE_M
        self.M_IN_KM = M_IN_KM
        self.length_pool = length_pool
        self.count_pool = count_pool
 
    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return length_pool * count_pool / M_IN_KM / duration 

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return (mean_speed + CALORIES_MEAN_SPEED_MULTIPLIER) * CALORIES_WEIGHT_SHIFT * weight * duration 

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return self

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    associations = {'SWM': Swimming,
                    'RUN': Running,
                    'WLK': SportsWalking}
    return read_package(workout_type, data)


def main(training: Training) -> None:
    """Главная функция."""
    info = show_training_info()
    print(info)


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
