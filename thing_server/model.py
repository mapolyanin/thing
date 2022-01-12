# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:39:44 2022

@author: polyanin-ma
"""

import secrets
import random
from typing import List



class Game():
    def __init___(self, state):
        pass
    
    def create_game(self):
        #Создаем игру
        pass
    
    def start_game(self):
        #Начинаем игру
        pass
    
    def get_card(self):
        #получаем карты из колоды
        pass
    
    def check_game_status(self):
        pass
    
    def connect_to_game(self):
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

        
    def create_deck(self, number_of_player:int):
        """Какие карты попадают в колоду, зависит от количества игроков"""
        pass

    def get_card(self) -> int:
        """Получить карту во время игры из колоды"""
        pass

    def fold_card(self, card: Card):
        """Сброс карты в сброшенную колоду"""
        pass

    def shuffle_cards(self, deck:List) -> List:
        """Перетасовать карты. Надо, чтобы он перетасовывал либо start_dec, либо game_dec
        Ну или сделать два разных метода"""
        pass


class Card():
    """
    Свойства:
    Тип карты:  событие или паника
    Подтип карты: инфекция, действия, защиты, препятсвия
    Действие карты: прописать через json
    Применимость карты: к соседу или к любому
    Карта закреплена: True False (для зараженных)
    Применимо для количества игроков: int
    """
    def __init__(self, card_type:str, card_subtype: str, 
    card_fix:bool, apply_to:str, max_players:int ) -> None:
        self.card_type =  card_type # event, panic
        self.card_subtype = card_subtype #infection, action, defense, barrier
        self.card_fix = card_fix #True - если владелец заражен, False, если нет
        self.apply_to = apply_to # neighbour, all
        self.max_players = max_players


    pass

class Player():
    """Свойства """
    pass


