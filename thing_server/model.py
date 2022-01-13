# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:39:44 2022

@author: polyanin-ma
"""

import secrets
import random
import time
import hashlib




class Game():
    """"""
    def __init__(self):
        self.game_hash = None #идентификатор игры. Надо кстати, покороче сделать
        self.players = list() #список игроков в порядке их расположения
        self.move_now:int = None #индекс игрока, который делает ход
        self.direction_move = 1 #направление хода. 1 = по часовой, -1 = против часовой

        
    
    def create_game(self, player_name:str) -> 'str':
        """Определяем идентификатор игры. Для этого используем серверное время,
         и делаем хэш из нее.
         Создаем первого игрока, определяем его токен, добавляем его в очередь
        """
        nowtime = time.time()
        game_hash = hashlib.md5(str(nowtime).encode()).hexdigest()
        self.game_hash = game_hash
        player = Player(player_name)
        self.players.append(player)
        return {'gameID': game_hash, 'playerID': player.token}
        
    
    def start_game(self):
        #Начинаем игру
        """"""
        pass
    
    def get_card(self):
        #получаем карты из колоды
        pass
    
    def check_game_status(self):
        pass
    
    def connect_to_game(self, gameID:str, playerName:str):
        
        #возвращаем токен, номер игрока и имя игрока
        pass

    
class CardDeck():
    """
    Класс колоды карт.
    Свойства:
        
        Всего карт в колоде
        Осталось карт в колоде
        Список карт в виде словаря:
    Методы:
        Создание колоды карт в начале игры - create_deck
        Создать колоду из оставшихся карт
        Получить свои карты в начале игры
        Получить карту из колоды во время игры
        Сбросить карту
        Создать колоду из сброшенных карт          
    """
    def __init__(self, count_of_player:int)-> None:
        self.start_deck = []
        self.game_deck = []
        self.cards_in_dec = 0
        self.folded_cards = []
        
    def read_card(self):
        pass

        
    def create_deck(self, number_of_player:int):
        """Какие карты попадают в колоду, зависит от количества игроков"""
        pass

    def get_card(self) -> int:
        """Получить карту во время игры из колоды"""
        pass

    def fold_card(self, card):
        """Сброс карты в сброшенную колоду"""
        pass

    def shuffle_cards(self, deck) -> list:
        """Перетасовать карты. Надо, чтобы он перетасовывал либо start_dec, либо game_dec
        Ну или сделать два разных метода"""
        pass


class Card():
    """
    Свойства:
    Идентификатор карты
    Тип карты:  событие или паника
    Подтип карты: инфекция, действия, защиты, препятсвия
    Действие карты: прописать через json
    Применимость карты: к соседу или к любому
    Карта закреплена: True False (для зараженных)
    Применимо для количества игроков: int
    """
    def __init__(self, cardID:int, card_type:str, card_subtype: str, 
    card_fix:bool, apply_to:str, max_players:int ) -> None:
        self.card_type =  card_type # event, panic
        self.card_subtype = card_subtype #infection, action, defense, barrier, 
        self.card_fix = card_fix #True - если владелец заражен и не может отдать карту, False, если нет
        self.apply_to = apply_to # neighbour, all
        self.max_players = max_players


    pass

class Player():
    """Свойства 
    name - имя
    hand - карты в руке
    token - идентификатор для транзакций
    thing:bool    
    """
    
    def __init__(self, name:str) -> None:
        self.name = name
        self.thing:bool = False #Играет ли игрок роль Чужого
        self.infected:bool = False #инфицирован ли игрок
        self.token:str = hashlib.md5(''.join([str(nowtime), self.name]).encode()).hexdigest()
        self.hand:list = []

        

if __name__ == '__main__':
    game = Game()
    answer = game.create_game('Mike_Pol')
    print(answer)
    


